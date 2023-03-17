import Bil 

looping = true #för att avsluta programmet
volvo_svart = bil.Bil("Volvo", "Svart", 5)
volvo_vit = bil.Bil("Volvo", "vit", 2)


while looping:
    print("-------------------------------------------------------------------")
    print("\n-:BilAutomat:- \n")

    #avsluta Programmet
    go = input("\n vill du avsluta programmet? j\n")

    if (go == "j"):
        break