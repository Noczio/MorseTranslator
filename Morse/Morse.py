# -*- coding: utf-8 -*-
#region Importanciones
import tkinter # Libreria para messageboxes
import tkinter.messagebox as MessageBox # Libreria messagebox de tkinter con un alias
import json #gracias a esta libreria podemos utilizar regiones en python
#endregion Importaciones

#region dictionario morse
dicMorse={"a":".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "ñ":"--.--",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--..",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"-----",
    ":":"---...",
    ",":"--..--",
    ";":"-.-.-.",
    "?":"..--..",
    "-":"-....-",
    "_":"..--.-",
    "+":".-.-.",
    "=":"-...-",
    "@":".--.-.",
    ".":".-.-.-"
    }
#endregion dictionario morse

#region funciones
def insertInput():
    try:
        strSentence=str(input("\nIngrese la oración: ")) # pedimos la cadena al usuario
        aVowels,uVowels = 'áéíóúü','aeiouu' # declaracionde dos variables. vocales con acentos y vocales sin los acentos
        trans = str.maketrans(aVowels,uVowels) # retorna una tabla de traduccion
        strFixedSentence=strSentence.translate(trans) # reemplaza cada caracter en la cadena con la tabla de traduccion dada
        return strFixedSentence.lower() # retornamos la cadena en minusculas
    except:
        MessageBox.showerror(title="Error de inicialización", message="Error al ingresar por teclado la cadena") #msgbox si hay errores
        return False

def translateToMorseCode(_strSentence): 
    lst = list(_strSentence.split())
    strSentenceTranslated=""
    for word in lst:       
        for letter in word:
            if(letter!=" " and letter in dicMorse.keys()):          
                strSentenceTranslated=str(strSentenceTranslated+dicMorse[letter]+"   ") # concatenamos y dejamos 3 espacios entre letra y letra             
            else:
                continue
        strSentenceTranslated+="   " # deja 6 espacios entre palabra y palabra. Esto debido a que anteriormente ya se habia dejado 3 espacios
    return strSentenceTranslated    
#endregion funciones

#region main
if __name__== "__main__": 

    """
    1. Pediremos un mensaje por teclado
    2. Se transformara cada letra de cada palabra del mensaje a morse
    3. Entre cada letra habra 3 espacios, mientras que entre cada palabra habrá 6 espacios
    5. Se imprimira en pantalla el mensaje en código morse
    """

    window = tkinter.Tk()  # Requirido
    window.wm_withdraw()  # Para ocultar window una ves usado

    print("---- Traductor de lenguaje español/inglés a código morse ----")
    try:       
        strSentence=insertInput() # pedimos que se ingrese por teclado la oración  
        if(strSentence==False): # ocurrio una exepcioón al ingresar la cadena
            print("No se ingreso una cadena valida")                     
        else: # la cadena si es valida para ser transformada a morse
            strSentenceTranslated=translateToMorseCode(strSentence)
            print(strSentenceTranslated)               
    except:
        MessageBox.showerror(title="Error de ejecución", message="Error al ejectuar el programa") #msgbox si hay errores

    input("\nPresione cualquier tecla para terminar ... ")      
#endregion main