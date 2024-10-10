import argparse

parser = argparse.ArgumentParser(description="A simple interactive CLI")
args = parser.parse_args()

def char_to_index(char):
    if char.isalpha():
        return ord(char.lower()) - ord('a')
    else:
        raise ValueError("Input character is not a letter")
    
def index_to_char(index):
    if 0 <= index < 26:
        return chr(index + ord('A'))
    else:
        raise ValueError("Index out of range")    

def main():
    print("Do you want to encrypt (E) or decrypt (D)? Or type 'exit' to quit")
    while True:
        text = input("")
        if text.lower() == 'e':
            encrypt()
        elif text.lower() == 'd':
            decrypt()
        elif text.lower() == "exit":
            print("Closing Encryption Software...")
            break
        else:
            print("Please pick either 'E' or 'D' or type 'exit' to quit")

def encrypt():
    plaintext = input("Please enter the text to encrypt:\n")
    plaintext = plaintext.replace(" ", "")    
    cyphertext = ''
    plaintext_length = len(plaintext)
    for pos in range(plaintext_length):
        c = plaintext[pos]
        k = pos % len(KEY)
        cyphertext += index_to_char((char_to_index(c) + char_to_index(KEY[k])) % 26)
    print('--------------------------')
    print(cyphertext)
    print('--------------------------')
    print("Do you want to encrypt (E) or decrypt (D)? Or type 'exit' to quit")
    
def decrypt():
    cyphertext = input("Please enter the text to decrypt:\n")
    plaintext = ''
    cyphertext_length = len(cyphertext)
    for pos in range(cyphertext_length):
        c = cyphertext[pos]
        k = pos % len(KEY)
        plaintext += index_to_char((char_to_index(c) - char_to_index(KEY[k])) % 26)
    print('--------------------------')
    print(plaintext)
    print('--------------------------')
    print("Do you want to encrypt (E) or decrypt (D)? Or type 'exit' to quit")

if __name__ == "__main__":
    main()