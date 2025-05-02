
# this is the encryption part
def encryption(userInput, key, domain, string):
    
    # using the value of key making the cipher
    cipher = ""
    for i in range(len(userInput)):
        for j in range(len(string)):
            if string[j] == userInput[i]:
                text = (string[(j+key)%domain])
                cipher = cipher + text
                key = j    # store next letters key
                
    print(f"The encrypted message is: {cipher}")
    print('\n')

# the decryption part will be added here
def decryption(userInput, key, domain, string):
    
    # using the value of key making the cipher
    plaintext = ""
    for i in range(len(userInput)):
        for j in range(len(string)):
            if string[j] == userInput[i]:
                text = (string[(j-key)%domain])
                plaintext = plaintext + text
                key = (j-key)%domain   # store next letters key
                
    print(f"The decrypted message is: {plaintext}")
    print('\n')