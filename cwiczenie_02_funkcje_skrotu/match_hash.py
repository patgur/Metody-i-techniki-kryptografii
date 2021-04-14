#%%
import hashlib
def cipher_sha256(file_name=r"C:\Users\HARDPC\Desktop\Studia_6\MetodyITechnikiKryptografii\funkcjeSkrotu\plik.iso"):
    with open(file_name,"rb") as f:
        bytes = f.read()
        readable_hash = hashlib.sha256(bytes).hexdigest()
        print(readable_hash)
        #return readable_hash
cipher_sha256()

# Nie wysyłam pliku, ze względu na jego wagę.
# Ss'y z wykonania zadania są w paczce.