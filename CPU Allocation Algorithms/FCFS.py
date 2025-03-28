# Funkcja implementująca algorytm FCFS. Jej parametrem jest krotka procesów. Zwraca krotkę zawierającą średni czas
# oczekiwania i cyklu przetwarzania (arrival time, burst time)

def fcfs_algorithm(processes):
    processes.sort(key=lambda x: x[0])  # Sortowanie po czasie przybycia procesu

    present_time = 0  # czas bieżący
    total_waiting_time = 0  # czas oczekiwania wszystkich procesów
    total_turnaround_time = 0  # czas cyklu przetwarzania wszystkich procesów

    for arrival_time, burst_time in processes:
        if present_time < arrival_time:  # aktualizacja bierzącego czasu
            present_time = arrival_time  # procesor jest bezczynny do momentu przybycia procesu)
        waiting_time = present_time - arrival_time  # czas oczekiwania jako różnica między czasem obecnym a czasem przybycia
        turnaround_time = waiting_time + burst_time  # suma czasu oczekiwania i czasu wykonywania procesu

        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time

        present_time += burst_time  # zwiększenie obecnego czasu o czas wykonywania danego procesu przez procesor

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    return avg_waiting_time, avg_turnaround_time
