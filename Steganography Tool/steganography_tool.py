from PIL import Image
import stepic

def encode_message(image_path, message, output_path):
    """Menyisipkan pesan ke dalam gambar."""
    img = Image.open(image_path)
    encoded_img = stepic.encode(img, message.encode())
    encoded_img.save(output_path, format='PNG')
    print(f'Pesan berhasil disisipkan ke dalam {output_path}')

def decode_message(image_path):
    """Mengambil pesan tersembunyi dari gambar."""
    img = Image.open(image_path)
    decoded_message = stepic.decode(img)
    print(f'Pesan tersembunyi: {decoded_message}')

if __name__ == "__main__":
    choice = input("Pilih mode: (1) Encode (2) Decode: ")
    if choice == '1':
        image_path = input("Masukkan path gambar: ")
        message = input("Masukkan pesan yang akan disisipkan: ")
        output_path = input("Masukkan nama file output: ")
        encode_message(image_path, message, output_path)
    elif choice == '2':
        image_path = input("Masukkan path gambar yang mengandung pesan: ")
        decode_message(image_path)
    else:
        print("Pilihan tidak valid!")
