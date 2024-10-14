import re

ile_sdan = int(input("Ile zdań? "))

zdania = []
for j in range(ile_sdan):
    zdania.append(input("Wprowadź zdanie " + str(j + 1) + ": "))

slowa_zdania = [[slowo.strip() for slowo in re.split(r'[,\.\?!: ]+', zdanie.lower()) if slowo] for zdanie in zdania]

ile_slow = int(input("Ile słów do wyszukania? "))
slowa_do_wyszukania = []
for j in range(ile_slow):
    slowa_do_wyszukania.append(input("Wprowadź słowo " + str(j + 1) + ": ").lower())

output = {slowo: [0] * ile_sdan for slowo in slowa_do_wyszukania}

for i, slowa in enumerate(slowa_zdania):
    for slowo in slowa:
        if slowo in output:
            output[slowo][i] += 1

sort_output = {}

for slowo, wystapienia in output.items():
    indeksy_zdan = [i for i in range(len(wystapienia)) if wystapienia[i] > 0]
    indeksy_zdan.sort(key=lambda i: (-wystapienia[i], i))
    sort_output[slowo] = indeksy_zdan

for slowo, indeksy in sort_output.items():
    print(f"Posortowane indeksy dla słowa '{slowo}': {indeksy}")
