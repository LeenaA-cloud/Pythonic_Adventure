######################################################################
# Ohjelmoinnin perusteet
# Tekijä: Leena Pasanen
# Päivämäärä:3.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
# COPY RIGHT
# Tiedoston rivillä olevien tietojen käsittely
######################################################################
def paaohjelma():
    tiedostonNimi =input("Anna tiedoston nimi: ")
    tiedosto = open(tiedostonNimi, 'r', encoding="utf-8")
    rivi=tiedosto.readline()

    while(True):
        rivi = tiedosto.readline()
        if(len(rivi) == 0):
            break
        rivi = rivi[:-1]
        rivi = rivi.split(';')
        print("Kello oli " + rivi[2] + ", kun punnittiin marjoja " + rivi[0] + ".")
    tiedosto.close()
    return None
paaohjelma()
print("Kiitos ohjelman käytöstä.")


