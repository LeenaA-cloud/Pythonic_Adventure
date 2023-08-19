######################################################################
# Ohjelmoinnin perusteet
# Tekijä: Leena Pasanen
# Päivämäärä:12.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
# COPY RIGHT
#Poikkeustenkäsittely käyttäjäsyötteiden yhteydessä
######################################################################

def paaohjelma():
    naytaValikko = True
    while (True):
        if (naytaValikko):
            
            print("Mitä haluat tehdä:\n1) Testaa ValueError\n2) Testaa IndexError\n3) Testaa ZeroDivisionError\n4) Testaa TypeError\n0) Lopeta")
        
        try:
            
            valinta = int(input("Valintasi: "))
            naytaValikko = True
            
            if (valinta == 1):
                print("Valikko-ohjelma testaa ValueError'n.")
           
            elif (valinta == 2):
                
                TestaaIndexError()
            
            elif (valinta == 3):
                
                TestaaZeroDivisionError()
          
            elif (valinta == 4):
                
                TestaaTypeError()
            
            elif (valinta == 0):
                break
            
            else:
                print("Valintaa ei tunnistettu, yritä uudestaan.")
        except ValueError:
            print("Anna valinta kokonaislukuna.")
            naytaValikko = False
    
    return None


def TestaaIndexError():
    lista = [11, 22, 33, 44, 55]
    kysely = int(input("Anna indeksi 0-4: "))
    try:
        print("Listan arvo on ", lista[kysely], " indeksillä ", kysely, ".", sep="")
    except IndexError:
        print("Tuli IndexError, indeksi ", kysely, ".", sep="")
    return None


def TestaaZeroDivisionError():
    kysely = int(input("Anna jakaja: "))
    try:
        print("4/2 on ", '{:.2f}'.format(4/kysely), ".", sep="")
    except ZeroDivisionError:
        print("Tuli ZeroDivisionError, jakaja ", kysely, ".", sep="")
    return None

   
def TestaaTypeError():
    numero = input("Anna numero: ")
    try:
        print(numero*numero)
    except TypeError:
        print("Tuli TypeError, ", numero, "*", numero, " merkkijonoilla ei onnistunut.", sep="")
    return None

paaohjelma()
print("Kiitos ohjelman käytöstä.")
