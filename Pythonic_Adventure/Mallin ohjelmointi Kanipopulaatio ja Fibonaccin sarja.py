######################################################################
# Ohjelmoinnin perusteet
# Tekijä: Leena Pasanen
# Opiskelijanumero:001053344
# Päivämäärä:23.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
# COPY RIGHT
# Mallin ohjelmointi: Kanipopulaatio ja Fibonaccin sarja
######################################################################

numeroKuukaudet = int(input("Anna kuukausien lukumäärä: "))

def kani_populaatio(kuukaudet):
  if kuukaudet == 0:
    return 0
  elif kuukaudet == 1: 
    return 1

  eka = 0
  toka = 1

  for i in range(1, kuukaudet + 1):
    next = eka + toka
    eka = toka
    toka = next

  return toka

print(f"Kanipariskuntia on {numeroKuukaudet} kuukauden kuluttua {kani_populaatio(numeroKuukaudet)}")  
print("Kiitos ohjelman käytöstä.")
