#%%
def ceazar_encript(text="", key=""):
    if (text=="") & (key==""):
        text = input('Podaj tekst do zaszyfrowania: ')

        key = input('Podaj klucz: ')
        #Pobieraj klucz, dopoki nie jest znakiem z zakresu a-z
        while len(key) != 1 or (ord(key) < 97 or ord(key) > 122):
            key = input('Klucz musi zawierać tylko jeden znak z zakresu a-z: ')

    #Zmieniam string na liste, zeby ulatwic operacje w petli
    text = list(text)

    for _ in range(len(text)):
        #char = aktualny znak
        char = text[_]

        #jesli od a do z
        if ord(char) >= 97 and ord(char) <= 122:
            #Aktualna pozycja w tekscie = aktualny znak + przesuniecie o wartosc klucza
            #Sprowadzamy klucz do wartosci z zakresu 1-26, dodajemy wartość z klucza, robimy modulo zeby nie wyjsc poza alfabet i znow wracamy na zakres 97-122
            text[_] = chr((ord(char) + (ord(key)-96) - 97) % 26 + 97)

    #Wyświtlenie listy jako string
    text = ''.join(text)
    return text
#%%
def ceazar_decript(text="", key=""):
    if (text=="") & (key==""):
        text = input('Podaj tekst do zaszyfrowania: ')

        key = input('Podaj klucz: ')
        while len(key) != 1 or (ord(key) < 97 or ord(key) > 122):
            key = input('Klucz musi zawierać tylko jeden znak z zakresu a-z: ')


    #Zmieniam string na liste, zeby ulatwic operacje w petli
    text = list(text)

    for _ in range(len(text)):
        #char = aktualny znak
        char = text[_]

        #jesli od a do z
        if ord(char) >= 97 and ord(char) <= 122:
            #Aktualna pozycja w tekscie = aktualny znak + przesuniecie o wartosc klucza
            #Sprowadzamy klucz do wartosci z zakresu 1-26, odejmujemy wartość z klucza, robimy modulo zeby nie wyjsc poza alfabet i znow wracamy na zakres 97-122
            text[_] = chr((ord(char) - (ord(key)-96) - 97) % 26 + 97)

    #Wyświtlenie listy jako string
    text = ''.join(text)
    return text