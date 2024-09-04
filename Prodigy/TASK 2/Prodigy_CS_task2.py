from PIL import Image
import numpy as np

print("------------- Image Encryption Tool With Pixel Manipulation****************** ")

def encrypt_image(image_path, key):
    
    original_image = Image.open(image_path)

    image_array = np.array(original_image)

    encrypted_image_array = (image_array * key) // (key + 1)

    encrypted_image = Image.fromarray(np.uint8(encrypted_image_array))

    encrypted_image_path = "encrypted_image.png"
    encrypted_image.save(encrypted_image_path)

    print(f"Image encrypted successfully. Encrypted image saved at: {encrypted_image_path}")

    exit()

def decrypt_image(encrypted_image_path, key):
  
    encrypted_image = Image.open(encrypted_image_path)

    encrypted_image_array = np.array(encrypted_image)

    decrypted_image_array = (encrypted_image_array * (key + 1)) // key

    decrypted_image_array = np.clip(decrypted_image_array, 0, 255)

    decrypted_image = Image.fromarray(np.uint8(decrypted_image_array))

    decrypted_image_path = "decrypted_image.png"
    decrypted_image.save(decrypted_image_path)\
    
    print(f"Image decrypted successfully. Decrypted image saved at: {decrypted_image_path}")

    exit()

def main():
    while True:
        print("Select an option:")
        print("1 - Encrypt image")
        print("2 - Decrypt image")
        print("x - Quit")
        choice = input("Your choice: ")

        if choice == '1':
            encrypt_choice()
        elif choice == '2':
            decrypt_choice()
        elif choice == 'x':
            print("Exitting the program.")
            exit()
        else:
            print("Invalid choice. Please choose '1' for encryption, '2' for decryption, or 'x' to quit.")

def encrypt_choice():
    key = int(input("Enter encryption key: "))
    image_location = input("Enter the location or URL of the image: ")

    try:
        encrypt_image(image_location, key)
    except FileNotFoundError:
        print("Invalid location. Image not found. Please try again.")
        encrypt_choice()

def decrypt_choice():
    key = int(input("Enter decryption key: "))
    encrypted_image_location = input("Enter the location of the encrypted image: ")

    try:
        decrypt_image(encrypted_image_location, key)
    except FileNotFoundError:
        print("Invalid location. Encrypted image not found. Please try again.")
        decrypt_choice()


if __name__ == "__main__":
    main()
