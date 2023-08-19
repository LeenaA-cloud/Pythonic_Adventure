######################################################################
# Tekijä: Leena Pasanen
# Päivämäärä:10.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.

#Valikkopohjainen ohjelma / laskin kirjastolla
#COPY RIGHT
######################################################################
import L08T4Kirjasto


def paaohjelma():

    luettavaTiedostoNimi = input("Anna luettavan tiedoston nimi: ")
    kirjoitettavaTiedostoNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    lukuLista = []
    tulosLista = []
    valinta = 1
    lukuLaskuri = 0
   
    while (valinta != 0):
        valinta = L08T4Kirjasto.Valikko()
         
        
        if (valinta == 1):
            if (lukuLaskuri == 0):
                lukuLista = L08T4Kirjasto.LueLuku(luettavaTiedostoNimi)
                print("Luettu tiedosto '" + luettavaTiedostoNimi + "'.")
                ekaNumero = lukuLista[lukuLaskuri]
                tokaNumero = lukuLista[lukuLaskuri + 1]
                print("Luettiin luvut", ekaNumero, "ja", tokaNumero)
                lukuLaskuri += 2
            elif (lukuLaskuri + 1 > len(lukuLista)):
                print("Luvut loppuivat, lopeta ohjelma.")
            else:
                ekaNumero = lukuLista[lukuLaskuri]
                tokaNumero = lukuLista[lukuLaskuri + 1]
                print("Luettiin luvut", ekaNumero, "ja", tokaNumero)
                lukuLaskuri += 2
        
        elif (valinta == 2):
            kirjoitettavaTeksti = L08T4Kirjasto.Summa(ekaNumero, tokaNumero)
         
            tulosLista.append(kirjoitettavaTeksti)
            print("Tulos lisätty listaan.")
        
        elif (valinta == 3):
            kirjoitettavaTeksti = L08T4Kirjasto.Osamaara(ekaNumero, tokaNumero)
            tulosLista.append(kirjoitettavaTeksti)
            print("Tulos lisätty listaan.")

        elif (valinta == 0):
            L08T4Kirjasto.KirjoitaTiedostoon(kirjoitettavaTiedostoNimi, tulosLista)
            print("Tallennettu tiedosto '" + kirjoitettavaTiedostoNimi + "'.")
       
        else:
            print("Tuntematon valinta, yritä uudestaan.")

    return None
paaohjelma()
print("Kiitos ohjelman käytöstä.")
