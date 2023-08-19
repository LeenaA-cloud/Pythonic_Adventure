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
#Oman kirjaston tekeminen ja käyttö
######################################################################
##kirjasto: Fahrenheit, Kelvin, Celsius 
## vaihtoehdot:
##Fahrenheit	Celsius	°C = (°F − 32) / 1,8
##Celsius	Fahrenheit	°F = (°C) · 1,8 + 32
##Fahrenheit	Kelvin	K = (°F + 459,67) / 1,8
##Kelvin	Fahrenheit	°F = K · 1,8 − 459,67
##Kelvin	Celsius	°C = K − 273,15
##Celsius	Kelvin	K = °C + 273,15
## 
Versio = 1.0

def CelsiusFahrenheit(kerroin):
    vastaus = float(kerroin * 1.8 + 32)
    return vastaus

def FahrenheitCelsius(kerroin):
    vastaus = float((kerroin -32)/1.8)
    return vastaus

def CelsiusKelvin(kerroin):
    vastaus = float(kerroin + 273.15)
    return vastaus

def KelvinCelsius(kerroin):
    vastaus = float(kerroin - 273.15)
    return vastaus

def KelvinFahrenheit(kerroin):
    vastaus = float(1.8 * kerroin - 459.67)
    return vastaus

def FahrenheitKelvin(kerroin):
    vastaus = float((5 / 9) * (kerroin -32) + 273.15)
    return vastaus



