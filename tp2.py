# -*- coding: utf-8 -*-
#i = int(input('indiquer le n° du produit :'))
produit = {
    '1': {'id': 1, 'nom': 'Banane', 'prix': 4, 'quantite': 2},
    '2': {'id': 2, 'nom': 'Pomme', 'prix': 2, 'quantite': 1},
    '3': {'id': 3, 'nom': 'Orange', 'prix': 1.5, 'quantite': 0},
    '4': {'id': 4, 'nom': 'Poire', 'prix': 3, 'quantite': 800}}

for key in produit:
    nom = produit[str(key)]['nom']
    prix = produit[str(key)]['prix']
    quantity = produit[str(key)]['quantite']
    TotalHT = prix * quantity

    Tva = 1.20

    prixTva = TotalHT * Tva
    if prixTva >= 200:
        remise = 0.05
        discount = prixTva - (prixTva * remise)
        prixTva = discount

    print("nom", nom, "prix HT", TotalHT, " prix TVA", prixTva)