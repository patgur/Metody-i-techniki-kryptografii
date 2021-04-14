#%%
def manual_descriptor(text=""):
    if text == "":
        text = input('Podaj tekst do deszyfracji:')
    
    #Przejscie po wszystkich możliwościach kodowania
    for i in range(25):
        text =  list(text)

        #Przetłumaczenia całego tekstu
        for _ in range(len(text)):

            #Zwiekszenie o jeden dany znak w tekscie
            text[_] = chr(ord(text[_]) + 1)

            #Jesli znak wychodzi poza alfabet, to wracam na początek alfabetu
            if ord(text[_]) > 122:
                text[_] = chr(ord(text[_]) - 26)

        #Scalenie listy w string
        text = ''.join(text)
        print(text)