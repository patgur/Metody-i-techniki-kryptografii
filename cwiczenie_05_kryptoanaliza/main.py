#%%
if __name__ == '__main__':
    import cryptanalysis

    with open('cipherMe.txt', 'r') as file:
        data = file.read()

    # Message from the file
    print(data)

    # Encrypting
    ciphertext = cryptanalysis.encryptText(data)

    # Encrypted data
    print(ciphertext)

    # Decrypted data
    print(cryptanalysis.decryptText(ciphertext))