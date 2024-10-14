import re

dokumenty = [
    "In a small town, an elderly artist painted a single leaf on the canvas of an old oak tree.\nEvery autumn, as the leaf turned gold and crimson, she whispered her hopes to the last leaf,\nbelieving it to be a guardian of her dreams. One winter morning, the leaf clung stubbornly to the branch,\n despite the icy winds. She made a photograph each time. Inspired by its resilience, she created her best work yet,\n a masterpiece that spoke of hope and perseverance, among others in the library. She'll keep the photograph to herself.",

    "After searching her cluttered drawers for hours, Mia stumbled upon an ornate key hidden beneath an old photograph.\nCuriosity piqued, she wondered what door it might unlock and what secrets lay behind it.\nFollowing a hunch, she ventured to the abandoned house at the end of the street, where whispers of lost treasure lingered.",

    "In a dusty corner of the only working library in the town, Oliver discovered an ancient book bound in cracked leather, its pages yellowed\nwith age. As he opened it, the words began to shimmer and dance, revealing stories of distant lands and enchanted creatures.\nIt was about the town and had a photograph attached, though no photograph should be there."
]


slowo_w_dokumentach = []
zapytanie = input("Wpisz słowo.\n").strip().lower()

for dokument in dokumenty:
    dokument_strip = dokument.strip()
    oczyszczony_dokument = dokument_strip.lower()

    znalezione_slowa = re.findall(rf'\b{zapytanie}\b', oczyszczony_dokument)
    slowo_w_dokumentach.append(len(znalezione_slowa))

print(
    f"Szukane słowo: {zapytanie}"
)

indeks = 1
for slowo_w_dokumencie in slowo_w_dokumentach:
    print(f"Dokument nr {indeks}: {slowo_w_dokumencie}")
    indeks += 1
