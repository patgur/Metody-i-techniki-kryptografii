#%%
def automatic_descriptor(text=""):
    #pip install english-words
    from english_words import english_words_set
    dictionary = list(english_words_set)
    
    not_found = True
    if text == "":
        text = input('Podaj tekst do deszyfracji:')

    #Przejscie po wszystkich literach alfabetu
    for i in range(25):
        text =  list(text)

        #Przechodze przez cały tekst
        for _ in range(len(text)):
            #Zwiekszenie o jeden dany znak w tekscie
            text[_] = chr(ord(text[_]) + 1)

            #Jesli znak wychodzi poza alfabet, to wracam na początek alfabetu
            if ord(text[_]) > 122:
                text[_] = chr(ord(text[_]) - 26)

        #Scalenie listy na typ string
        text = ''.join(text)

        #Przejscie po calym slowniku w celu porownania ze stworzonym stringiem
        for _ in dictionary:
            if _ == text:
                print('Rezszyfrowane słowo:',text)
                not_found = False

    if not_found:
        print('Nie znaleziono żadnego słowa.')
