######################################################################
# Ohjelmoinnin perusteet
# Tekijä: Leena Pasanen
# Päivämäärä:24.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
# COPY RIGHT
# Poikkeustenkäsittely tiedostojenkäsittelyn yhteydessä
######################################################################
def paaohjelma():
    luettuLuettelo = []
    luettavaTiedostoNimi = input("Anna luettavan tiedoston nimi: ")
    
    try:
        luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")
        while(True):
            rivi = luettavaTiedosto.readline()
            if (len(rivi) == 0):
    
                break
           
            luettuLuettelo.append(rivi)
        luettavaTiedosto.close()
        
        print("Tiedoston '", luettavaTiedostoNimi, "' lukeminen onnistui, ", len(luettuLuettelo), " riviä.", sep="")
    except:
        print("Tiedoston '", luettavaTiedostoNimi, "' käsittelyssä virhe, lopetetaan.", sep="")
        return None
    
    kirjoitettavaTiedostoNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    
    try:
       
        kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")
        for element in luettuLuettelo:
           
            kirjoitettavaTiedosto.write(element)
        kirjoitettavaTiedosto.close()
       
        print("Tiedoston '" + kirjoitettavaTiedostoNimi + "' kirjoittaminen onnistui.", sep="")
    except:
        print("Tiedoston '", kirjoitettavaTiedostoNimi, "' käsittelyssä virhe, lopetetaan.", sep="")
        return None
    
    print("Kiitos ohjelman käytöstä.")
   
    return None

paaohjelma()
