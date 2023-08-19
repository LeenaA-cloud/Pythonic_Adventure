######################################################################
# Ohjelmoinnin perusteet
# Tekijä: Leena Pasanen
# Päivämäärä:3.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
# COPY RIGHT
# Luokan määrittely ja olion käyttö
######################################################################

class auto:
    autonMerkki = ""
    autojenLukumaara = 0

def paaohjelma():
    autoA = auto()
    autoA = syote(autoA)
    tulostus(autoA)
    return None

def tulostus(autoA):
    print("Varastossa on nyt " + autoA.autoMerkki + "-merkkisiä autoja", autoA.autojenLukumaara, "kpl.")
    return None

def syote(autoA):
    autoA.autoMerkki = input("Anna automerkki: ")
    autoA.autojenLukumaara = int(input("Anna automerkin lukumäärä varastossa: "))
    return autoA

paaohjelma()
print("Kiitos ohjelman käytöstä.")
