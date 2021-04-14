#%%
import hashlib
import timeit
message = input("Podaj tekst do szyfrowania:").encode()

# Metadata 
LENGTH_IN_BITS = 8

# Setup prepared for measuring algorithms time
setup = """
import hashlib
message = {}
LENGTH_IN_BITS = {}
""".format(message, LENGTH_IN_BITS)

algorithms_available = list(hashlib.algorithms_available)

mismatches = []
for _ in range(len(algorithms_available)):
    try:
        print(algorithms_available[_],": ",getattr(hashlib,algorithms_available[_])(message).hexdigest(), sep="")
        t = timeit.timeit(stmt='hashlib.{}(message).hexdigest()'.format(algorithms_available[_]), setup=setup)
        print("Czas trwania:",t,end="\n\n")
    except AttributeError:
        # algorithms_available has more attributes than module hashlib.
        # Ignore additional attributes.
        mismatches.append(algorithms_available[_])
    except TypeError:
        # A few of algorythms need length argument in hexdigest()
        print(algorithms_available[_],": ",getattr(hashlib,algorithms_available[_])(message).hexdigest(LENGTH_IN_BITS), sep="")
        t = timeit.timeit(stmt='hashlib.{}(message).hexdigest(LENGTH_IN_BITS)'.format(algorithms_available[_]), setup=setup)
        print("Czas trwania:",t,end="\n\n")

print("\nPoniższe funkcje nie są obługiwane przez bibliotekę hashlib:")

for _ in mismatches:
    print(_)
