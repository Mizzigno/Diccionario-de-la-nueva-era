meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "67": "no tiene un significado fijo y suele usarse para decir «más o menos» o como broma",
            "ROFL": "una respuesta a una broma"
            "SHEESH" - "ligera desaprobación"
            "CREEPY" - "aterrador, siniestro"
            "AGGRO" - "ponerse agresivo/enojado"
            }
word = input("Ingresa la palabra que deseas conocer")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Esa palabra no está en el diccionario")
