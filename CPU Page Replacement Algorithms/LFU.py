# Funkcja implementująca algorytm LFU. Jako argumenty przyjmuje ciąg stron i liczbę ramek.
def lfu_algorithm(sequence, num_frames):
    frames = []  # lista ramek
    page_faults = 0  # ilość brakujących stron
    page_hits = 0  # ilość trafionych stron
    frequency = {}  # słownik częstotliwości

    for page in sequence:
        if page in frames:
            # Trafienie strony (page hit)
            frequency[page] += 1  # zwiększenie częstotliwości użycia strony w słowniku
            page_hits += 1
        else:
            # Brak strony (page fault)
            if len(frames) < num_frames:  # sprawdzenie czy jest miejsce na liście ramek (liczba ramek mniejsza niż całkowita liczba ramek)
                frames.append(page)  # dodawanie strony do listy ramek
                frequency[page] = 1  # ustawienie częstotliwości strony w słowniku na 1
            else:
                # Nie ma miejsca - znalezienie strony o najmniejszej częstotliwości
                lfu_page = min(frames, key=lambda x: frequency[x])  #jeśli jest kilka stron o tej samej częstotliwości, wybiera tę, która pojawiła się najwcześniej
                frames.remove(lfu_page)  # usuwanie strony z listy ramek
                del frequency[lfu_page]  # usuwanie wpisu w słowniku
                frames.append(page)  # dodawanie nowej strony do listy ramek
                frequency[page] = 1  # ustawienie częstotliwości nowej strony na 1
            page_faults += 1

    return page_faults, page_hits
