import requests
import sys
from os import path

def main():
    if path.exists("1.txt"):
        file = open("1.txt", 'r', encoding="utf-8")
        file = file.read().split("\n")
        lista = []

        url = "http://seglass.ec/"

        for plugin in file:
            url_final = url + "/"+plugin
            peticion = requests.get(url = url_final )
            print ("(-) Trying: "+ url_final )
            if peticion.status_code ==200:
                print("(+) Succede:" + url_final)
                url_final = url_final.split('/')
                posicion = url_final.index('plugins')
                plugin_encontrado = url_final[posicion+1]
                lista.append(plugin_encontrado )

        print("-"*50)
        for i in lista:
            print("(*) Se encontro el plugin: {}".format(i))

    else:
        print("El archivo wp-plugins.txt no existe")


if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit
