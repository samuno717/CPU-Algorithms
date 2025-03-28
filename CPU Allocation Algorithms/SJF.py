# Funkcja implementująca algorytm SJF. Jej parametrem jest lista krotek procesów.
def sjf_algorithm(processes):
    processes.sort(key=lambda x: x[0])  # Sortowanie po czasie przybycia (arrival time)

    present_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    process_num = len(processes)

    while processes:
        # Lista zawierająca procesy, które przybyły do bieżącego czasu
        available_processes = [p for p in processes if p[0] <= present_time]

        if available_processes:
            # Jeśli lista nie jest pusta, wybiera proces o najkrótszym czasie wykonania
            next_process = min(available_processes, key=lambda x: x[1])  # x[1] to czas obliczeń procesu
            processes.remove(next_process)  # usuwanie procesu z listy
        else:
            # Jeśli lista jest pusta, przesuwa czas obecny do czasu przybycia następnego procesu na liście processes
            next_process = min(processes, key=lambda x: x[0])  # znajdowanie proces z najwcześniejszym czasem przybycia
            processes.remove(next_process)  # usuwanie procesu z listy
            present_time = next_process[0]  # aktualizowanie bieżącego czasu do czasu przybycia

        arrival_time, burst_time = next_process
        if present_time < arrival_time:
            present_time = arrival_time
        waiting_time = present_time - arrival_time
        turnaround_time = waiting_time + burst_time

        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time

        present_time += burst_time

    avg_waiting_time = total_waiting_time / process_num
    avg_turnaround_time = total_turnaround_time / process_num

    return avg_waiting_time, avg_turnaround_time
