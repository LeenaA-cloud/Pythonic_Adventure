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
# Binaarilukujen erotus
######################################################################
def binaryToDecimal(num):
	b = list(num)
	n = len(list(num))
	decimal = 0
	hold = 0
	i = 0
	exp = n-1
	while (i < n):
		x = int(b[i])
		quit= 2**exp
		hold = x*quit
		i += 1
		exp -= 1
		decimal = decimal + hold
	return(decimal)

ekaBinary = input("Anna ensimmäinen binaariluku: ")
tokaBinary = input("Anna toinen binaariluku: ")

ekaDecimal = binaryToDecimal(ekaBinary)
tokaDecimal = binaryToDecimal(tokaBinary)

print(f"Bittijonosi {ekaBinary} on kymmenkantaisena kokonaislukuna {ekaDecimal}")
print(f"Bittijonosi {tokaBinary} on kymmenkantaisena kokonaislukuna {tokaDecimal}")

erotus = ekaDecimal - tokaDecimal
print(f"Lukujen {ekaDecimal} ja {tokaDecimal} erotus on {erotus}")
print("Kiitos ohjelman käytöstä.")
