#%%
def vigenere_encript(text="", key=""):
    if (text=="") & (key==""):
        text = input('Podaj tekst do zaszyfrowania: ')

        key = input('Podaj klucz: ')
        #Pobieraj klucz, dopoki nie jest z zakresu a-z
        for _ in range(len(key)):
            while ord(key[_]) < 97 or ord(key[_]) > 122:
                key = input('Wszystkie znaki klucza muszą być z zakresu a-z: ')
                break

    #Zmieniam stringi na listy, zeby ulatwic operacje w petli
    text = list(text)
    key = list(key)

    for _ in range(len(text)):
        #Aktualny znak tekstu
        char = text[_]
        #Aktualny znak klucza
        key_fragment = key[_%len(key)]

        #jesli od a do z
        if ord(char) >= 97 & ord(char) <= 122:
            #Aktualna pozycja w tekscie = aktualny znak + przesuniecie o wartosc klucza
            #Sprowadzamy klucz do wartosci z zakresu 1-26, dodajemy wartość z klucza,
            #robimy modulo zeby nie wyjsc poza alfabet i znow wracamy na zakres 97-122
            text[_] = chr((ord(char) + (ord(key_fragment)-96) - 97) % 26 + 97)

    #Wyświtlenie listy jako string
    text = ''.join(text)
    return text

#%%
def vigenere_decript(text="", key=""):
    if (text=="") & (key==""):
        text = input('Podaj tekst do zaszyfrowania: ')

        #Pobieraj klucz, dopoki nie jest z zakresu a-z
        key = input('Podaj klucz: ')
        for _ in range(len(key)):
            while ord(key[_]) < 97 or ord(key[_]) > 122:
                key = input('Wszystkie znaki klucza muszą być z zakresu a-z: ')
                break

    #Zmieniam stringi na listy, zeby ulatwic operacje w petli
    text = list(text)
    key = list(key)

    for _ in range(len(text)):
        #Aktualny znak
        char = text[_]
        #Aktualny znak klucza
        key_fragment = key[_%len(key)]

        #jesli od a do z
        if ord(char) >= 97 & ord(char) <= 122:
            #Aktualna pozycja w tekscie = aktualny znak + przesuniecie o wartosc klucza
            #Sprowadzamy klucz do wartosci z zakresu 1-26, usuwamy wartość z klucza,
            #robimy modulo zeby nie wyjsc poza alfabet i znow wracamy na zakres 97-122
            text[_] = chr((ord(char) - (ord(key_fragment)-96) - 97) % 26 + 97)

    #Wyświtlenie listy jako string
    text = ''.join(text)
    return text
