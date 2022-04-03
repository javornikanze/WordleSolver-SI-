from _operator import itemgetter

besede = []
file = open("file.txt", "r", encoding="utf-8")
for line in file:
    besede.append(line.replace('",\n', '').replace('"', ''))

zelene = "_____"
oranzne = "_____"
sive = ""

ustrezne = []
predlagane = []

def ustreza(beseda, zelene, oranzne):
    for crka in zelene.replace("_", "") + oranzne.replace("_", ""):
        if crka not in beseda:
            return False
    for i in range(5):
        if beseda[i] in sive:
            return False
        if zelene[i] != "_":
            if zelene[i] != beseda[i]:
                return False
        if oranzne[i] != "_":
            if oranzne[i] == beseda[i]:
                return False
    return True


for beseda in besede:
    if ustreza(beseda, zelene, oranzne):
        ustrezne.append(beseda)

print("Opozorilo: vse besede v seznamu niso smiselne")
print("Ustrezne besede:\n\t", ustrezne)

for beseda in ustrezne:
    i = 0
    crke_beseda = dict()
    for crka in beseda:
        if crka not in zelene and crka not in oranzne:
            crke_beseda[crka] = ":-)"
    for beseda2 in ustrezne:
        for crka in crke_beseda:
            if crka in beseda2:
                i += 1
                break
    predlagane.append((beseda, i))

print("Število najdenih ustreznih besed:", len(ustrezne))
print("Predlagane besede (številka zraven pomeni koliko besed bi bilo izločenih iz ustreznih v najslabšem primeru):\n\t", sorted(predlagane, key=itemgetter(1), reverse=True))