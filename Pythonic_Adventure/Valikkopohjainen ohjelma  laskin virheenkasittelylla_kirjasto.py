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
import sys
def Valikko():
    print("Tämä laskin osaa seuraavat toiminnot:\n1) Anna luvut\n2) Summa\n3) Osamäärä\n0) Lopeta")
    valikko = int(input("Valitse toiminto (0-3): "))
    return valikko

def LueLuku(luettavaTiedostoNimi):
    luettavatLuvut = []
    try:
        luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")
        while (True):
            rivi = luettavaTiedosto.readline()
            rivi = rivi[:-1]
            if (not(rivi.isdigit())):
                luettavaTiedosto.close()
                return luettavatLuvut    
            else:
               luettavatLuvut.append(int(rivi))
    except:
        print("Tiedoston '" + luettavaTiedostoNimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit()
    return None    
    
    
def Summa(ekaLuku, tokaLuku):

    SummaLasku = f"Summa {ekaLuku} + {tokaLuku} = {ekaLuku + tokaLuku}\n"
    return SummaLasku


def Osamaara(ekaLuku, tokaLuku):

    OsamaaraLasku = f"Osamäärä {ekaLuku} / {tokaLuku} = {round((ekaLuku / tokaLuku), 2)}\n"
    return OsamaaraLasku


def KirjoitaTiedostoon(kirjoitettavaTiedostoNimi, tulosLista):
    try:
        kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")
        for element in tulosLista:
            kirjoitettavaTiedosto.write(element)
        kirjoitettavaTiedosto.close()
    except:
        print("Tiedoston '" + kirjoitettavaTiedostoNimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit()
    return None
