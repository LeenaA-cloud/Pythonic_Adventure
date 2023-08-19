######################################################################
# Ohjelmoinnin perusteet
# Tekijä: Leena Pasanen
# Päivämäärä:3.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:

# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
# Valikkopohjainen ohjelma ostoslistan käsittelyyn
# COPY RIGHTS
######################################################################
def paaohjelma():
    ostoslista=[]
    valinta = '1'
    while(valinta !='0'):
        valinta = valikko(ostoslista)
        if(valinta== '1'):
            tuote =input("Anna lisättävä tuote: ")
            ostoslista.append(tuote)
            print()
        elif(valinta == '2'):
            print("Ostoslistassasi on", len(ostoslista), "tuotetta.")
            poistaNumero =int(input("Anna poistettavan tuotteen järjestysnumero: "))
            del ostoslista[poistaNumero -1]
            print()
        elif (valinta == '0'):
            print ("Sinulta jäi ostamatta seuraavat tuotteet:\n", ostoslista, sep="")
    return None

def valikko(ostoslista):
    print ("Ostoslistasi sisältää seuraavat tuotteet:\n", ostoslista, sep="")
    print ("Voit valita alla olevista toiminnoista:\n1) Lisää\n2) Poista\n0) Lopeta")
    valinta = input("Valintasi: ")
    if(valinta == '1' or valinta == '2' or valinta == '0'):
        return valinta
    else:
        print("Tunnistamaton valinta.\n")
        return valinta

paaohjelma()

print("Kiitos ohjelman käytöstä.")
       
             

    
