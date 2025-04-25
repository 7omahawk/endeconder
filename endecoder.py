import argparse

parser = argparse.ArgumentParser(description="This is the symmetric encryption and decryption system where you can encrypt or decrypt the text or file's content.")

parser.add_argument("-f", "--filename", help="Enter the file name with extension.")
parser.add_argument("-m", "--message", help="Enter the message.")
parser.add_argument("-a", "--algorithm", help="Choose the algorithm.", choices=["vigenere", "transposition", "affine", "autokey"])
parser.add_argument("-k", "--key", help="Use the key for encryption or decryption.")
parser.add_argument("-o","--operation", help="Choose the operation encrypt or decrypt.", choices=["encrypt", "decrypt"])

args = parser.parse_args()



print(args)