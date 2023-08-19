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
# COPY RIGHT
# Python-kirjastojen käyttö, datetime
######################################################################
import datetime

def paaohjelma():
    print("Tämä ohjelma käyttää datetime-kirjastoa tehtävien ratkaisemiseen.")
    while (True):
        print("Mitä haluat tehdä:\n1) Tunnistaa aika-olion komponentit\n2) Laskea iän päivinä\n3) Tulostaa viikonpäivät\n4) Tulostaa kuukaudet\n0) Lopeta")
        valikko = input("Valintasi: ")
        if (valikko == "1"):
           
            AikaOhjelma()
        elif (valikko == "2"):
            
            IkaEro()
        elif (valikko == "3"):
            ViikonPvm()
        
        elif (valikko == "4"):
            Kuukaudet()
        elif (valikko == "0"):
            
            break
        else:
           
           print("Valintaa ei tunnistettu, yritä uudestaan.\n")
    
    return None
    

def AikaOhjelma():
    
    pvmStr = input("Anna päivämäärä ja kello muodossa 'pp.kk.vvvv hh:mm': ")
    pvmObj = datetime.datetime.strptime(pvmStr, "%d.%m.%Y %H:%M")
            
    print("Annoit vuoden ", pvmObj.year, "\nAnnoit kuukauden ", pvmObj.month, "\nAnnoit päivän ", pvmObj.day, "\nAnnoit tunnin ", pvmObj.hour, "\nAnnoit minuutin ", pvmObj.minute, "\n", sep="")
    
    return None


def IkaEro():
    syntymaPaiva = datetime.datetime.strptime(input("Anna syntymäpäiväsi muodossa pp.kk.vvvv: "), "%d.%m.%Y")
    laskettavaSyntymaPaiva = datetime.date(syntymaPaiva.year, syntymaPaiva.month, syntymaPaiva.day)
    kaksTuhatta = datetime.date(2000, 1, 1)
    ika = abs(laskettavaSyntymaPaiva - kaksTuhatta)
    print(kaksTuhatta.day, ".", kaksTuhatta.month, ".", kaksTuhatta.year, " sinä olit ", ika.days, " päivää vanha.", "\n", sep="")
    return None

def ViikonPvm():
    viikonPvmObj = datetime.datetime(2023, 2, 13)
    for index in range(0, 7):
        print(viikonPvmObj.strftime("%A"))
        viikonPvmObj = viikonPvmObj + datetime.timedelta(days=+1)
    print()
 
    return None
def Kuukaudet():
    kuukaudetObj = datetime.datetime(2023, 1, 1)
    for index in range(0, 12):
        print(kuukaudetObj.strftime("%b"))
        kuukaudetObj = kuukaudetObj + datetime.timedelta(days=+31)
    print()
    return None
paaohjelma()
print("Kiitos ohjelman käytöstä.")
