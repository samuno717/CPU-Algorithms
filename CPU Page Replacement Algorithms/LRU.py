# Funkcja implementująca algorytm LRU. Jako argumenty przyjmuje ciąg stron i liczbę ramek.
def lru_algorithm(sequence, num_frames):
    frames = []  # lista ramek
    page_faults = 0  # liczba brakujących stron
    page_hits = 0  # liczba trafionych stron

    for page in sequence:
        if page in frames:
            # Trafienie strony (page hit)
            frames.remove(page)  # usuwa stronę z jej obecnej pozycji na liście ramek
            frames.append(page)  # dodaje stronę na koniec listy ramek: oznacza to, że była przed chwilą użyta
            page_hits += 1
        else:
            # Brak strony (page fault)
            if len(frames) < num_frames:  # sprawdza, czy jest miejsce na liście ramek (liczba ramek mniejsza niż liczba wszystkich dostępnych ramek)
                frames.append(page)  # dodaje stronę na koniec listy ramek
            else:
                frames.pop(0)  # usuwa pierwszą stronę z listy ramek (ostatnio użytą)
                frames.append(page)  # dodaje stronę na koniec listy ramek
            page_faults += 1
    return page_faults, page_hits  # funkcja zwraca liczbę trafionych i brakujących ramek
