# -*- coding: utf-8 -*-

produit = {
    '1': {'id': 1, 'nom': 'Banane', 'prix': 4, 'quantite': 2},
    '2': {'id': 2, 'nom': 'Pomme', 'prix': 2, 'quantite': 1},
    '3': {'id': 3, 'nom': 'Orange', 'prix': 1.5, 'quantite': 0},
    '4': {'id': 4, 'nom': 'Poire', 'prix': 3, 'quantite': 80}}

TotalBanane = produit['1']['prix'] * produit['1']['quantite']
TotalPomme = produit['2']['prix'] * produit['2']['quantite']
TotalOrange = produit['3']['prix'] * produit['3']['quantite']
TotalPoire = produit['4']['prix'] * produit['4']['quantite']

def calcultva(TotalHT):
    prixTva = TotalHT * 1.20
    return prixTva
def calculremise(prixTva):
    remise = prixTva * 0.05 - prixTva
    return remise


TotalHT = TotalBanane + TotalPoire + TotalPomme + TotalOrange

prixTva = calcultva(TotalHT)

if prixTva >= 200:
    remise = calculremise(prixTva)
    TotalTTC = prixTva - remise

print('+----------------------------------+---------+------------------------+----------------+\n'
      '|                Nom               |  Prix   |       Quantité         |    Total HT    |\n'
      '|                {}                |   {}    |            {}          |       {}       |\n'.format(
          produit['1']['nom'], produit['1']['prix'], produit['1']['quantite'], TotalBanane),
      '|                {}                |   {}    |            {}          |       {}       |\n'.format(
          produit['2']['nom'], produit['2']['prix'], produit['2']['quantite'], TotalPomme),
      '|                {}                |   {}    |            {}          |       {}       |\n'.format(
          produit['3']['nom'], produit['3']['prix'], produit['3']['quantite'], TotalOrange),
      '|                {}                |   {}    |            {}          |       {}       |\n'.format(
          produit['4']['nom'], produit['4']['prix'], produit['4']['quantite'], TotalPoire))

print("prix HT", TotalHT, '\n', "prix TVA", prixTva)



