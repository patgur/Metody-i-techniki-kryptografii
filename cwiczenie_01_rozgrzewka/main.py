
#%%
#pip install english-words
from caesar import ceazar_encript, ceazar_decript
from vigenere import vigenere_encript, vigenere_decript
from manual_descriptor import manual_descriptor
from automatic_descriptor import automatic_descriptor

print(ceazar_encript('siema','p'), end = "\n\n")
print(ceazar_decript('tjfnb','a'), end = "\n\n")
print(vigenere_encript('siema', 'not'), end = "\n\n")
print(vigenere_decript('gxyap', 'not'), end = "\n\n")
manual_descriptor('gxyap')
print()
automatic_descriptor('ikk')


