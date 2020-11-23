# -*- coding: utf-8 -*-
i = int(input('indiquer le nb de produit :'))
produit = [i]
for i in range(i):
    priceHT = float(input('indiquer une valeur :'))
    if priceHT <=0:
        priceHT = float(input('indiquer une nouvelle valeur :'))
    quantity = int(input('indiquer une nouvelle quantité :'))
    if quantity <=0:
        quantity = int(input('indiquer une quantité :'))

    priceQ = priceHT * quantity
    Tva = 0.20
    remise = 0.05
    priceTva = priceQ * Tva + priceQ

    if priceTva >= 200:
        discount = priceTva - (priceTva * remise)
        priceTva = discount

    print(priceTva)

