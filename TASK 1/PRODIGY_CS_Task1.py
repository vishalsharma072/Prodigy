
letters = 'abcdefghijklmnopqrstuvwzyz'
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1: 
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters 
                ciphertext += letters[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1: 
                ciphertext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += num_letters
                ciphertext += letters[new_index]
    return ciphertext



print()
print('****PRODIGY CS1 ** CAESAR CIPHER PROGRAM****')
print()

print('Do you want to Encrypt(1) or Decrypt(2) ?')
user_input = input('1/2: ').lower()
print()

if user_input == '1':
    print('ENCRYPTION MODE SELECTED')
    print()
    Key = int(input('Enter the key ( 1 through 26): '))
    text = input('Enter the text to Encrypt: ')
    ciphertext = encrypt(text, Key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input == '2':
    print('DECRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to Decrypt: ')
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')