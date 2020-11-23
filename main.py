# -*- coding: utf-8 -*-
priceHT = int(input('indiquer une valeur :'))
quantity = int(input('indiquer une quantiter :'))
if priceHT <=0:
    priceHT = int(input('indiquer une valeur :'))
elif quantity <=0:
    quantity = int(input('indiquer une quantiter :'))
else:
    print("valeur correcte")


priceQ = priceHT * quantity
Tva = 0.20
remise = 0.05
priceTva = priceQ*Tva + priceQ

if priceTva >= 200:
    discount = priceTva - (priceTva*remise)
    priceTva = discount

print(priceTva)
