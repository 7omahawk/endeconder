
# this is the encryption part
def encryption(userInput, key, domain, string):
    
    # making the value of key 
    for i in range(len(key)):
        for j in range(len(string)):
            if string[j] == key[i]:
                k = j   # the value of the key
    
    # using the value of key making the cipher
    cipher = ""
    for i in range(len(userInput)):
        for j in range(len(string)):
            if string[j] == userInput[i]:
                text = (string[(j+k)%domain])
                cipher = cipher + text
                k = j    # store next letters key
                
    print(f"The encrypted message is: {cipher}")
    print('\n')

# the decryption part will be added here
def decryption(userInput, key, domain, string):
    
    plaintext = ""
    # making the value of key 
    for i in range(len(key)):
        for j in range(len(string)):
            if string[j] == key[i]:
                k = j      # the value of the key

    # using the value of key making the cipher
    for i in range(len(userInput)):
        for j in range(len(string)):
            if string[j] == userInput[i]:
                text = (string[(j-k)%domain])
                plaintext = plaintext + text
                k = (j-k)%domain   # store next letters key
                
    print(f"The decrypted message is: {plaintext}")
    print('\n')