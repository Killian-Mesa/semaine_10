populations = {
    "Cerfs": [32, 45, 50, 41],
    "Renards": [12, 15, 13, 10],
    "Lapins": [85, 102, 98, 76],
    "Aigles": [5, 7, 6, 5]
}
saisons = ["Printemps", "Été", "Automne", "Hiver"]

print("")
print(f'Recensement pour les {len(populations)} espèces :')
print("")

moys = []
nom = []

for espece, pop in populations.items():
    nombre = list(pop)
    moy = sum(nombre) / len(nombre)
    print(f'{espece} : moyenne par saison = {moy} individus')
    moys.append(moy)
    nom.append(espece)

print("")
max = max(moys)
position = moys.index(max)

print(f'Espèce la plus nombreuse : {nom[position]} ({max} individus en moyenne.)')

import matplotlib.pyplot as plt

cerfs = populations["Cerfs"]
renards = populations["Renards"]
lapins = populations["Lapins"]
aigles = populations["Aigles"]

plt.title("Évolution des populations selon les saisons")
plt.xlabel("Saison")
plt.ylabel("Nombre d'individus")

plt.plot(saisons,cerfs, '-o', color='blue')

plt.plot(saisons, renards, '-o', color='yellow')

plt.plot(saisons, lapins, '-o', color='green')

plt.plot(saisons, aigles, '-o', color='red')
plt.grid(True)
plt.legend(['Cerfs', 'Renards', 'Lapins', 'Aigles'])
plt.show()