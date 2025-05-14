import argparse
from algorithm import vigenere, transposition, affine, autokey

domain = 26
string = "abcdefghijklmnopqrstuvwxyz"


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    parser = argparse.ArgumentParser(description="This is the symmetric encryption and decryption system where you can encrypt or decrypt the text or file's content.")

    parser.add_argument("-f", "--filename", help="Enter the file name with extension.")
    parser.add_argument("-m", "--message", help="Enter the message.")
    parser.add_argument("-a", "--algorithm", help="Choose the algorithm.", choices=["vigenere", "transposition", "affine", "autokey"])
    parser.add_argument("-k", "--key", help="Use the key for encryption or decryption.", type=str)
    parser.add_argument("-k2", "--key2", help="Use the key specifically for affine cipher encryption or decryption.", type=str)
    parser.add_argument("-o","--operation", help="Choose the operation encrypt or decrypt.", choices=["encrypt", "decrypt"])

    args = parser.parse_args()

    
    if args.algorithm == "vigenere":
        try:
            if args.key.isdigit():
                raise ValueError("Integer input is not allowed!")
            else:
                args.message = args.message.lower()

                if args.operation == "encrypt":
                    vigenere.encryption(args.message, args.key, domain, string)
                elif args.operation == "decrypt":
                    vigenere.decryption(args.message, args.key, domain, string)
        except ValueError:
            print("Invalid input! Please enter the string value.")
            
    elif args.algorithm == "transposition":
        try:
            args.key = int(args.key)
            args.message = args.message.lower()

            if args.operation == "encrypt":
                transposition.encryption(args.key, args.message)
            elif args.operation == "decrypt":
                transposition.decryption(args.key, args.message)
        except ValueError:
            print("Invalid input! Please enter the integer value.")   
         
    elif args.algorithm == "affine":
        try:
            args.key =int(args.key)
            args.key2 = int(args.key2)
            args.message = args.message.lower()
        
            if is_prime(args.key) and is_prime(args.key2):
                if args.operation == "encrypt":
                    affine.encryption(args.message, args.key, args.key2, domain, string)
                elif args.operation == "decrypt":
                    t1 = affine.multiplicativeInverse(args.key, domain)
                    affine.decryption(args.message, args.key, args.key2, t1, domain, string)
            else:
                print("Invalid input! Please enter the prime number.")
        except ValueError:
            print("Invalid input! Please enter the prime number.")
        
    elif args.algorithm == "autokey":
        try:
            args.message = args.message.lower()
            args.key = int(args.key)
            
            if args.operation == "encrypt":
                autokey.encryption(args.message, args.key, domain, string)
            elif args.operation == "decrypt":
                autokey.decryption(args.message, args.key, domain, string) 
        except ValueError:
            print("Invalid input! Please enter the integer value.")      

    else:
        print("Type in terminal: 'python endecoder.py --help'.")

if __name__ == '__main__':
    main()
    
    
    
    
    
    
"""have to solve several problem
   1. text file input and out adding problem
   2. proper comment out every where"""