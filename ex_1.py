import matplotlib.pyplot as plt

temperatures = [
    ("Janvier", 2.5),
    ("Février", 3.0),
    ("Mars", 6.2),
    ("Avril", 10.5),
    ("Mai", 15.3),
    ("Juin", 19.1),
    ("Juillet", 22.4),
    ("Août", 21.9),
    ("Septembre", 17.0),
    ("Octobre", 12.1),
    ("Novembre", 6.8),
    ("Décembre", 3.4)
]

mois = []
temp = []

for name, temperature in temperatures:
    mois.append(name)
    temp.append(temperature)
    plt.plot(mois, temp, color='green')
    plt.plot(mois, temp, 'o', color='green')

plt.grid(True, linestyle='--')
plt.title("temperature moyenne mensuelle dans la réserve naturelle")
plt.xlabel("Mois")
plt.ylabel("Température moyenne (C)")
plt.show()



