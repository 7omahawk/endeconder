import argparse
from algorithm import vigenere, transposition, affine, autokey

domain = 26
string = "abcdefghijklmnopqrstuvwxyz"

def main():
    parser = argparse.ArgumentParser(description="This is the symmetric encryption and decryption system where you can encrypt or decrypt the text or file's content.")

    parser.add_argument("-f", "--filename", help="Enter the file name with extension.")
    parser.add_argument("-m", "--message", help="Enter the message.")
    parser.add_argument("-a", "--algorithm", help="Choose the algorithm.", choices=["vigenere", "transposition", "affine", "autokey"])
    parser.add_argument("-k", "--key", help="Use the key for encryption or decryption.")
    parser.add_argument("-o","--operation", help="Choose the operation encrypt or decrypt.", choices=["encrypt", "decrypt"])

    args = parser.parse_args()

    if args.algorithm == "vigenere":
        pass
    elif args.algorithm == "transposition":
        args.message = args.message.lower()
        if args.operation == "encrypt":
            transposition.encryption(args.key, args.message)
        elif args.operation == "decrypt":
            transposition.decryption(args.key, args.message)
    elif args.algorithm == "affine":
        pass
    elif args.algorithm == "autokey":
        args.message = args.message.lower()
        if args.operation == "encrypt":
            autokey.encryption(args.message, args.key, domain, string)
        elif args.operation == "decrypt":
            autokey.decryption(args.message, args.key, domain, string) 
    else:
        print("Choose the right algorithm.")

if __name__ == '__main__':
    main()