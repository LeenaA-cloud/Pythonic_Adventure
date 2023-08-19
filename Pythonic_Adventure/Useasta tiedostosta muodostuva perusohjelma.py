######################################################################
# Ohjelmoinnin perusteet
# Tekijä: Leena Pasanen
# Päivämäärä:24.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
# COPY RIGHT
# Useasta tiedostosta muodostuva perusohjelma
######################################################################
import L08T5Kirjasto


def main():
    # kysytaan syotteena luettavan tiedoston nimi
    luettavaTiedostoNimi = input("Anna luettavan tiedoston nimi: ")
    # lisataan tiedoston eteen sen polku
    # luettavaTiedostoNimi = "./L08-tehtavat/files/" + luettavaTiedostoNimi
    # maaritetaan kirjoitettavan tiedoston nimi
    kirjoitettavaTiedostoNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    # lisataan tiedoston eteen sen polku
    # kirjoitettavaTiedostoNimi = "./L08-tehtavat/files/" + kirjoitettavaTiedostoNimi
    # listat lukemista ja tallenntamista varten
    tuoteLista = []
    tulosLista = []

    while (True):
        valinta = Valikko()

        # jos valinta on 1
        if (valinta == 1):
            # kutsutaan aliohjelmaa
            tuoteLista = L08T5Kirjasto.LueTiedosto(luettavaTiedostoNimi)
        # jos valinta on 2
        elif (valinta == 2):
            # kutsutaan aliohjelmaa
            tulosLista = L08T5Kirjasto.AnalysoiTiedot(tuoteLista)
        # jos valinta on 3
        elif (valinta == 3):
            # kutsutaan aliohjelmaa
            L08T5Kirjasto.TallennaTiedot(kirjoitettavaTiedostoNimi, tulosLista)
        # jos valinta on 0
        elif (valinta == 0):
            # tulostetaan lopetusviesti
            break
        # jos valinta ei ole 1, 2, 3 tai 0
        else:
            print("Tuntematon valinta, yritä uudestaan.")
    # poistutaan paaohjelmasta
    return None

def Valikko():

    # tulostetaan valinnat    
    print("Mitä haluat tehdä:\n1) Lue tiedosto\n2) Analysoi tiedot\n3) Tallenna Tulokset\n0) Lopeta")
    # kysytaan kayttajalta syote
    valikko = int(input("Valintasi: "))
    # palautetaan kayttajan valinta
    return valikko

# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
