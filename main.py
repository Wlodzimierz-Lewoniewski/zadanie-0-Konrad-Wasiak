import re

liczba_dokumentow = int(input("Ile dokumentów chcesz dodać? "))
liczba_slow = int(input("Ile słów chcesz dodać? "))

dokumenty = []
for i in range(liczba_dokumentow):
    dokumenty.append(input(f"Podaj treść dokumentu {i + 1}: "))

for i in range(liczba_slow):
    czestosci = []
    zapytanie = input(f"Wpisz szukane słowo {i + 1}: ").strip().lower()

    for index, dokument in enumerate(dokumenty):
        oczyszczony_dokument = dokument.strip().lower()
        znalezione_slowa = re.findall(rf'\b{zapytanie}\b', oczyszczony_dokument)
        czestosci.append((index, len(znalezione_slowa)))

    czestosci.sort(key=lambda x: x[1], reverse=True)
    posortowane_indeksy = [index for index, _ in czestosci]
    print(posortowane_indeksy)
