print ("\nBenvenuti nel programma di calcolo del perimetro delle figure geometriche! \n\nDI quale figura hai bisogno?\n")
print ("1 - Quadrato ")
print ("2 - Cerchio ")
print ("3 - Rettangolo ")
print ("4 - Triangolo equilatero")
print ("5 - Uscita dal programma")
print ("\nInserire il numero scelto: ")

numero =int (input ("\n"))

if numero == 1:
    
    print ("\nComplimenti!\nHai scelto di calcolare il perimetro del quadrato!\ninserisci il valore del suo lato in centimetri!")
    l = float (input("\n"))
    print ("\nIl suo perimetro è di ", l * 4 ,"cm\n")

elif numero == 2:

    print ("\nComplimenti!\nHai scelto di calcolare la circonferenza del cerchio!\ninserisci il valore del suo raggio in centimetri!")
    r = float(input("\n"))
    print ("\nLa sua circonferenza è di ", r * 2 * 3.14, "cm\n")

elif numero == 3:
    
    print ("\nComplimenti!\nHai scelto di calcolare il perimetro del rettangolo!\ninserisci il valore della sua base in centimetri!")
    b = float (input("\n"))
    print ("\nOra inserisci il valore dell'altezza, sempre in centimetri!")
    h = float (input("\n"))
    print ("\nIl suo perimetro è di ", b * 2 + h * 2, "cm\n")

elif numero == 4:

    print ("\nComplimenti!\nHai scelto di calcolare il perimetro del triangolo!\ninserisci il valore del suo lato in centimetri!")
    l = float (input("\n"))
    print ("\nIl suo perimetro è di ", l * 3, "cm\n")

elif numero == 5:

    print("\nUscita in corso! Grazie per aver utilizzato questo programma!\n")
    exit()

else:
    print ("\nValore errato, si prega di riavviare il programma e di inserire un valore tra quelli citati precedentemente!\n")

