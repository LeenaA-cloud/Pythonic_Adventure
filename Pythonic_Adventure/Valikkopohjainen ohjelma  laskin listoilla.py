######################################################################
# Ohjelmoinnin perusteet
# Tekijä: Leena Pasanen
# Päivämäärä:19.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
#COPY RIGHT
#Valikkopohjainen ohjelma / laskin listoilla
######################################################################
def paaohjelma():

    luettavaTiedostoNimi = input("Anna luettavan tiedoston nimi: ")
    kirjoitettavaTiedostoNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    lukuTulos = []
    tulosTaulu = []
    valinta = 1
    lukuLaskuri = 0

    while (valinta != 0):
        valinta = Valikko()
     
        if (valinta == 1):
            if (lukuLaskuri == 0):
                lukuTulos = LueLuku(luettavaTiedostoNimi)
                print("Luettu tiedosto '" + luettavaTiedostoNimi + "'.")
                ekaLuku = lukuTulos[lukuLaskuri]
                tokaLuku = lukuTulos[lukuLaskuri + 1]
                print("Luettiin luvut", ekaLuku, "ja", tokaLuku)
                lukuLaskuri += 2
            elif (lukuLaskuri + 1 > len(lukuTulos)):
                print("Luvut loppuivat, lopeta ohjelma.")
            else:
                ekaLuku = lukuTulos[lukuLaskuri]
                tokaLuku = lukuTulos[lukuLaskuri + 1]
                print("Luettiin luvut", ekaLuku, "ja", tokaLuku)
                lukuLaskuri += 2
        elif (valinta == 2):
            kirjoitettavaTeksti = Summa(ekaLuku, tokaLuku)
            tulosTaulu.append(kirjoitettavaTeksti)
            print("Tulos lisätty listaan.")
        elif (valinta == 3):
            kirjoitettavaTeksti = Osamaara(ekaLuku, tokaLuku)
            tulosTaulu.append(kirjoitettavaTeksti)
            print("Tulos lisätty listaan.")
        elif (valinta == 0):
            KirjoitaTiedostoon(kirjoitettavaTiedostoNimi, tulosTaulu)
            print("Tallennettu tiedosto '" + kirjoitettavaTiedostoNimi + "'.")
        else:
            print("Tuntematon valinta, yritä uudestaan.")
    
    return None

def Valikko():
    print("Tämä laskin osaa seuraavat toiminnot:\n1) Anna luvut\n2) Summa\n3) Osamäärä\n0) Lopeta")
    valikko = int(input("Valitse toiminto (0-3): "))
    
    return valikko

def LueLuku(luettavaTiedostoNimi):
    
    luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")
    luettavatLuvut = []
       
    while (True):
        rivi = luettavaTiedosto.readline()
        rivi = rivi[:-1]
        if (not(rivi.isdigit())):
            luettavaTiedosto.close()
            return luettavatLuvut    
        else:
            luettavatLuvut.append(int(rivi))
  
    return None    
    
def Summa(ekaLuku, tokaLuku):
   
    SummaLause = f"Summa {ekaLuku} + {tokaLuku} = {ekaLuku + tokaLuku}\n"
    return SummaLause

def Osamaara(ekaLuku, tokaLuku):
    OsamaaraLause = f"Osamäärä {ekaLuku} / {tokaLuku} = {round((ekaLuku / tokaLuku), 2)}\n"
    
    return OsamaaraLause


def KirjoitaTiedostoon(kirjoitettavaTiedostoNimi, tulosLista):
    kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")
   
    for element in tulosLista:
       
        kirjoitettavaTiedosto.write(element)
       
    kirjoitettavaTiedosto.close()
    
    return None

paaohjelma()
print("Kiitos ohjelman käytöstä.")
