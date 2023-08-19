######################################################################
# Ohjelmoinnin perusteet
# Tekijä: Leena Pasanen
# Päivämäärä:24.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
# COPY RIGHT
# Kalenterikuukauden tulostaminen
######################################################################

import datetime
yy = int(input("Anna vuosi: "))
mm = int(input("Anna kuukausi: "))

ekaPaiva = datetime.date(yy, mm, 1)

if mm == 12:
    seuraavaVuosi = yy + 1
    seuraavaKuukausi = 1
else:
    seuraavaVuosi = yy
    seuraavaKuukausi = mm + 1

viikonEkaPaiva = ekaPaiva.weekday()

vikaPaiva = datetime.date(seuraavaVuosi, seuraavaKuukausi, 1) - datetime.timedelta(days=1)
paiviaKuukaudessa = vikaPaiva.day

print("Kalenteri näyttää seuraavalle:")

print(' Ma', 'Ti', 'Ke', 'To', 'Pe', 'La', 'Su')

paiva = 1

for i in range(7):
    if i < viikonEkaPaiva:
        print('  ', end=' ')
    else:
        print(" {:>2d}".format(paiva), end='')
        paiva += 1
print('',end='\n')

while paiva <= paiviaKuukaudessa:
    print('', end='')
    for i in range(7):
        print(" {:>2d}".format(paiva), end='')
        paiva += 1
        if paiva > paiviaKuukaudessa:
            break
    if paiva <= paiviaKuukaudessa:
        print()
