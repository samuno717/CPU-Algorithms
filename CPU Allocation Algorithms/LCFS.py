# Funkcja implementująca algorytm LCFS. Jej parametrem jest lista krotek procesów.
def lcfs_algorithm(processes):
    # Sortowanie procesów po czasie przybycia, ale w odwrotnej kolejności
    processes.sort(key=lambda x: x[0], reverse=True)

    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    process_num = len(processes)  # liczba procesów

    while processes:
        arrival_time, burst_time = processes.pop(0) # aktualizacja listy - usuwanie pierwszego elementu, przesunięcie reszty
        if current_time < arrival_time:
            current_time = arrival_time
        waiting_time = current_time - arrival_time
        turnaround_time = waiting_time + burst_time

        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time

        current_time += burst_time

    avg_waiting_time = total_waiting_time / process_num
    avg_turnaround_time = total_turnaround_time / process_num

    return avg_waiting_time, avg_turnaround_time
