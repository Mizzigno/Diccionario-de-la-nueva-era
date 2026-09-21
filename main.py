meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            }
word = input("Ingresa la palabra que deseas conocer")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Esa palabra no está en el diccionario")
