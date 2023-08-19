######################################################################
# Ohjelmoinnin perusteet
# Tekijä: Leena Pasanen
# Päivämäärä:10.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
# Valikkopohjainen ohjelma  laskin kirjastolla
# COPY RIGHT
######################################################################
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
    
    
def Summa(ekaNumero, tokaNumero):
 
    SummaLause = f"Summa {ekaNumero} + {tokaNumero} = {ekaNumero + tokaNumero}\n"
 
    return SummaLause


def Osamaara(ekaNumero, tokaNumero):
    
       
    OsamaaraLause = f"Osamäärä {ekaNumero} / {tokaNumero} = {round((ekaNumero / tokaNumero), 2)}\n"
    
    return OsamaaraLause


def KirjoitaTiedostoon(kirjoitettavaTiedostoNimi, tulosLista):
   
    kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")
    
    for element in tulosLista:
        
        kirjoitettavaTiedosto.write(element)
      
    kirjoitettavaTiedosto.close()
    return None
