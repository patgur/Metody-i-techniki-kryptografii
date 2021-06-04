import cv2
from random import randint

#Alphabet list
alpha = "ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~`!@#$%^&*()_+-=.,'*/ "

# Steganography-encrypt function
def encrypt(mes, img):
    img_data = cv2.imread(img, 1)
    num = []
    locs = []

    for i in mes:
        num.append(alpha.index(i))
    for i in range(len(num)):
        locs.append((randint(0, len(img_data) - 1), randint(0, len(img_data[0]) -1), randint(0, 2)))
    for i,j in zip(locs, num):
        img_data[i[0]][i[1]][i[2]] = j

    return cv2.imwrite('encrypted.png', img_data), locs

#  Steganography-decrypt function
def decrypt(img, locs):
    img_data = cv2.imread(img, 1)
    str_ = ""
    for i in locs:
        str_ += alpha[img_data[i[0]][i[1]][i[2]]]

    return str_

img_new, locs = encrypt('Siemano', 'bite.png')

print(decrypt('encrypted.png', locs))

# Random (1-7) number addded to numbered text
MAX_MISLEADER_VALUE = 7


def clearText(text: str):
    """ Get rid of unnecessary characters such as new-line """
    #Function result
    character_proper_text = ''

    for _ in text:
        if (ord(_) >= 32) and (ord(_) <= 126):
            character_proper_text += _

    # Return cleared text
    return character_proper_text


def convertAndEncryptAsNumberText(text: str):
    """ Convert the text to number-text type """
    # Function result
    ciphertext = ''

    for _ in text:
        # Draw a random number between 1 and (MAX_MISLEADER_VALUE)
        randomInt = randint(1,MAX_MISLEADER_VALUE-1)
        # To the number-type letter add drawn number
        bench = ord(_) * MAX_MISLEADER_VALUE + randomInt

        # Add ciphered letter to ciphertext
        ciphertext += str(bench)

    # Return numbered text
    return ciphertext


def decryptAndConvertToText(text: str):
    """ Convert encrypted numbered-text to the normal one """
    # Function result
    newText = ''
    # Length of original text
    textLength = int(len(text) / 3)

    for _ in range(textLength):
        # Take first 3 numbers of ciphertext so they can be converted
        bench = int(text[:3])
        # Delete first 3 numbers from ciphertext
        text = text[3:]

        # Transform numbered-letter to ASCII code.
        bench = int(bench/MAX_MISLEADER_VALUE)

        # Add decrypted letter to the message
        newText += chr(bench)

    # Return the text
    return newText


def shuffleText(text: str):
    """ Shuffle letters in the text """
    # Function result
    newText = ''
    # Length of original text
    textLength = len(text)

    # Swap every neighbouring numbers
    for _ in range(0, textLength-1, 2):
        newText += text[_+1] + text[_]

    # Add last number if text's length is odd
    if textLength % 2:
        newText += text[-1]

    # Return shuffled text
    return newText


def encryptText(text: str):
    """ Encrypt given text """
    # Prepare the text so it'll be able to be encrypted
    text = clearText(text)
    
    # Convert the text to number-type text
    text = convertAndEncryptAsNumberText(text)

    # Shuffle numbers in the text
    text = shuffleText(text)

    # Return encrypted text
    return text


def decryptText(text: str):
    """ Decrypt given text """
    # Prepare the text so it'll be able to be encrypted
    text = clearText(text)

    # Unshuffle numbers in the text
    text = shuffleText(text)
    
    # Convert numbers to ASCII
    text = decryptAndConvertToText(text)

    # Return decrypted text
    return text