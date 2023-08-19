######################################################################
# Ohjelmoinnin perusteet
# Tekijä: Leena Pasanen
# 
# Päivämäärä:11.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
# COPY RIGHT
# Oman kirjaston tekeminen ja käyttö
######################################################################

import L08T2Kirjasto

def paaohjelma():
    print("Käytetään lämpötilamuunnoskirjaston versiota", L08T2Kirjasto.Versio)

    while(True):
        print("Minkä lämpötilamuunnoksen haluat tehdä?\n1) Celsius->Fahrenheit\n2) Celsius->Kelvin\n3) Fahrenheit->Kelvin\n4) Fahrenheit->Celsius\n5) Kelvin->Celsius\n6) Kelvin->Fahrenheit\n0) Lopeta")
        valikko = input("Valintasi: ")

        if(valikko == "1"):
            kerroin = int(input("Anna lähtölämpötila: "))
            vastaus = L08T2Kirjasto.CelsiusFahrenheit(kerroin)
            print("Lämpötila Fahrenheit asteina: ", round(vastaus, 2), "\n", sep="")

        elif(valikko == "2"):
            kerroin = int(input("Anna lähtölämpötila: "))
            vastaus = L08T2Kirjasto.CelsiusKelvin(kerroin)
            print("Lämpötila Kelvin asteina: ", round(vastaus, 2), "\n", sep="")

        elif (valikko == "3"):
            kerroin = int(input("Anna lähtölämpötila: "))
            vastaus = L08T2Kirjasto.FahrenheitKelvin(kerroin)
            print("Lämpötila Kelvin asteina: ", round(vastaus, 2), "\n", sep="")
        elif (valikko == "4"):
            kerroin = int(input("Anna lähtölämpötila: "))
            vastaus = L08T2Kirjasto.FahrenheitCelsius(kerroin)
            print("Lämpötila Celsius asteina: ", round(vastaus, 2), "\n", sep="")
        elif (valikko == "5"):
            kerroin = int(input("Anna lähtölämpötila: "))
            vastaus = L08T2Kirjasto.KelvinCelsius(kerroin)
            print("Lämpötila Celsius asteina: ", round(vastaus, 2), "\n", sep="")
        elif (valikko == "6"):
            
            kerroin = int(input("Anna lähtölämpötila: "))
            vastaus = L08T2Kirjasto.KelvinFahrenheit(kerroin)
            print("Lämpötila Fahrenheit asteina: ", round(vastaus, 2), "\n", sep="")
        elif (valikko == "0"):
            break
   
        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.\n")
    return None
    
paaohjelma()
print("Kiitos ohjelman käytöstä.")
