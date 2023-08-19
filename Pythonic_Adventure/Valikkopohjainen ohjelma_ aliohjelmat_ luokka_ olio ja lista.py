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
# Valikkopohjainen ohjelma, aliohjelmat, luokka, olio ja lista
######################################################################
class AUTO():
    merkki =""
    hinta = 0

def paaohjelma():
    autot =[]
    print ("Tämä ohjelma lisää autojen tietoja listaan ja tulostaa ne.")
    while(True):
        valinta =valikko()
        if(valinta== 1):
            autot = kysy(autot)
        elif(valinta == 2):
            tulostus(autot)
        else:
            autot.clear()
            break
    return None
def valikko():
    while(True):
        print("Käytettävissä olevat toiminnot:\n1) Anna auton tiedot\n2) Tulosta autojen tiedot\n0) Lopeta")
        valinta =int(input("Valintasi: "))
        if (not(valinta >= 0 and valinta <=2)):
            print ("Tuntematon valinta, yritä uudestaan.")
            print()
        else:
            break
    return valinta
def kysy(autot):
    auto= AUTO()
    auto.merkki = input("Anna auton merkki: ")
    auto.hinta =int(input("Anna auton hinta: "))
    autot.append(auto)
    print()
    return autot
def tulostus(autot):
    print("Listalta löytyy seuraavat automerkit ja hinnat:")
    for auto in autot:
        print (auto.merkki, auto.hinta)
    print()
    return None
paaohjelma()
print("Kiitos ohjelman käytöstä.")
        
