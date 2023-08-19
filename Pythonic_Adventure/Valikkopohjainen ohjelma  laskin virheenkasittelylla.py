######################################################################
# Ohjelmoinnin perusteet
# Tekijä: Leena Pasanen
# Päivämäärä:23.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
# COPY RIGHT
# Valikkopohjainen ohjelma / laskin virheenkäsittelyllä
######################################################################
import L09T4Kirjasto

def paaohjelma():
    luettavaTiedostoNimi = input("Anna luettavan tiedoston nimi: ")
    kirjoitettavaTiedostoNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    lukuLista = []
    tulosLista = []
    valinta = 1
    lukuLaskuri = 0

    while (valinta != 0):
    
        valinta = L09T4Kirjasto.Valikko()
      
        if (valinta == 1):
            if (lukuLaskuri == 0):
                lukuLista = L09T4Kirjasto.LueLuku(luettavaTiedostoNimi)
                print("Luettu tiedosto '" + luettavaTiedostoNimi + "'.")
                ekaLuku = lukuLista[lukuLaskuri]
                tokaLuku = lukuLista[lukuLaskuri + 1]
                print("Luettiin luvut", ekaLuku, "ja", tokaLuku)
                lukuLaskuri += 2
            elif (lukuLaskuri + 1 > len(lukuLista)):
                print("Luvut loppuivat, lopeta ohjelma.")
            else:
                ekaLuku = lukuLista[lukuLaskuri]
                tokaLuku = lukuLista[lukuLaskuri + 1]
                print("Luettiin luvut", ekaLuku, "ja", tokaLuku)
                lukuLaskuri += 2

        elif (valinta == 2):
            kirjoitettavaTeksti = L09T4Kirjasto.Summa(ekaLuku, tokaLuku)
            tulosLista.append(kirjoitettavaTeksti)
            print("Tulos lisätty listaan.")

        elif (valinta == 3):
            kirjoitettavaTeksti = L09T4Kirjasto.Osamaara(ekaLuku, tokaLuku)
            
            tulosLista.append(kirjoitettavaTeksti)
            print("Tulos lisätty listaan.")
       
        elif (valinta == 0):
            if (len(tulosLista) == 0):
                print("Ei tallennettavia tietoja, tiedostoa ei tallennettu.")
            else:
                L09T4Kirjasto.KirjoitaTiedostoon(kirjoitettavaTiedostoNimi, tulosLista)
                
                print("Tallennettu tiedosto '" + kirjoitettavaTiedostoNimi + "'.")

        else:
            print("Tuntematon valinta, yritä uudestaan.")
  
    return None

paaohjelma()
print("Kiitos ohjelman käytöstä.")
