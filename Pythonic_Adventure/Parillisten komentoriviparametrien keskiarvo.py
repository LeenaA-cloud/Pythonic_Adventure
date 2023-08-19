######################################################################
# Ohjelmoinnin perusteet
# Tekijä: Leena Pasanen
# Päivämäärä:25.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
# COPY RIGHT
#Parillisten komentoriviparametrien keskiarvo
######################################################################
#  
import sys
print("Syötteen parilliset luvut ovat seuraavat:")
# hankitaan komentorivin argumentit
for numbers in sys.argv:

# muutetaan numeroiksi ja suoraan listalle
##numbers = [int(x) for x in numbers]

#alustetaan listaa sekä summausta
even_numbers = []
even_sum = 0

# käydään kaikki numerot läpi ja löydetään halutut
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
    even_sum += number

# lasketaan halutuista keskiarvo
if len(even_numbers) > 0:
  average = even_sum / len(even_numbers)
else:
  average = 0

# printataan numerot ja niiden keskiarvo
##print("Syötteen parilliset luvut ovat seuraavat:")
print(*even_numbers,"")
print(f"Lukujen keskiarvo on {average:.2f}.")
print("Kiitos ohjelman käytöstä.")
