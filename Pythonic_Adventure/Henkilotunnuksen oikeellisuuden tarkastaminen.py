# Ohjelmoinnin perusteet
# Tekijä: Leena Pasanen
# Päivämäärä:11.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
# COPY RIGHT
# Henkilötunnuksen oikeellisuuden tarkastaminen
######################################################################

def tarkistaId(idStr):

  if len(idStr) != 11:
    return False
 
  try:
    paiva = int(idStr[0:2])
    kuukausi = int(idStr[2:4])
    vuosi = int(idStr[4:6])
    if not (1 <= paiva <= 31) or not (1 <= kuukausi <= 12) or not (0 <= vuosi <= 99):
      return False
  except ValueError:
    return False
  
  # tarkistaa onko vuosisata symbooli oikein
  if idStr[6] not in ['+', '-', 'A']:
    return False
  
  # tarkistaa onko (nnn) numerot aidot
  try:
    individualNumber = int(idStr[7:10])
    if not (2 <= individualNumber <= 999):
      return False
  except ValueError:
    return False
  
  # tarkistaa meneekö t merkintä läpi
  checkMarkTable = {
  0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
  10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'H', 17: 'J', 18: 'K',
  19: 'L', 20: 'M', 21: 'N', 22: 'P', 23: 'R', 24: 'S', 25: 'T', 26: 'U', 27: 'V',
  28: 'W', 29: 'X', 30: 'Y'
}
  dateAndNumber = int(idStr[0:6] + idStr[7:10])
  checkMark = checkMarkTable[dateAndNumber % 31]
  if idStr[10] != checkMark:
    return False
  
  return True

id = input("Anna henkilötunnus: ")

if tarkistaId(id):
  print("Henkilötunnus hyväksytty.")
else:
  print("Henkilötunnusta ei hyväksytä.")

print("Kiitos ohjelman käytöstä.")
