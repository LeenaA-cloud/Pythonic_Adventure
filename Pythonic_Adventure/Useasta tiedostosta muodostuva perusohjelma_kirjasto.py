######################################################################
# Ohjelmoinnin perusteet
# Tekijä: Leena Pasanen
# 
# Päivämäärä: 24.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
# COPY RIGHT
# Useasta tiedostosta muodostuva perusohjelma
######################################################################
class TietoLuokka:
    tuotekoodi = ""
    tuoteLkm = 0
    tuoteHinta = 0.0


def LueTiedosto(luettavaTiedostoNimi):
    # avataan tiedosto luettavaksi
    luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")
    # tuotelista
    tuoteLista = []
    # silmukka tiedoston lukua varten
    while(True):
        # objekti
        tuoteRivi = TietoLuokka()
        # luetaan rivi
        rivi = luettavaTiedosto.readline()
        
        # jos rivi on tyhja
        if (len(rivi) == 0):
            # poistutaan silmukasta
            break
        # poistetaan rivinvaihto
        rivi = rivi[:-1]
        # kaytetaan split funktiota hyodyksi joka tekee
        # luetusta rivista listan
        rivi = rivi.split(';')
        # for element in rivi:
        #     print(element)
        # asetetaan tiedot objektiin
        tuoteRivi.tuotekoodi = rivi[0]
        tuoteRivi.tuoteLkm = int(rivi[1])
        tuoteRivi.tuoteHinta = float(rivi[2])
        # lisataan objekti listaan
        tuoteLista.append(tuoteRivi)
    # suljetaan tiedosto
    luettavaTiedosto.close()
    # aliohjelman lopetusviesti
    print("Tiedosto '", luettavaTiedostoNimi, "' luettu, ", len(tuoteLista), " riviä.", sep="")
    print()
    # palautetaan lista
    return tuoteLista


def AnalysoiTiedot(tuoteLista):
    tulosLista = []
    summa = 0
    for element in tuoteLista:
        tulos = round(element.tuoteLkm * element.tuoteHinta, 2)
        summa += tulos
        tulos = '{:.2f}'.format(tulos) + "\n"
        tulosLista.append(tulos)
    # aliohjelman lopetusviesti
    print("Tiedot analysoitu, varaston arvo on", '{:.2f}'.format(summa), "EUR.")
    print()
    # palautetaan lista
    return tulosLista


def TallennaTiedot(kirjoitettavaTiedostoNimi, tulosLista):
    # avataan tiedosto kirjoitettavaksi
    kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")
    for element in tulosLista:
        # kirjoitetaan tiedot tiedostoon
        kirjoitettavaTiedosto.write(element)
    # suljetaan tiedosto
    kirjoitettavaTiedosto.close()
    # tulostetaan aliohjelman lopetusviesti
    print("Tulokset tallennettu tiedostoon '" + kirjoitettavaTiedostoNimi + "'.")
    print()
    return None
