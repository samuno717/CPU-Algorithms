import random
import pandas as pd

import FCFS
import LCFS
import SJF

# Seed służący do powtarzalności eksperymentu
random.seed(42)


# Funkcja generująca ciągi procesów, które mają losowe czasy przybycia i czas obliczeń. Zwraca listę zawierającą
# listy procesów. Jej parametry to liczba ciągów i liczba procesów.
def generate_processes(sequence_count=100, processes_count=100):
    sequences = []  # lista zawierająca ciągi

    for _ in range(sequence_count):
        processes = []
        for _ in range(processes_count):
            at = random.randint(0, 100)  # czas przybycia procesu - arrival time - w przedziale (0, 100)
            T = random.randint(1, 20)  # pozostały czas obliczeń - burst time - w przedziale (1, 20)
            processes.append((at, T))
        sequences.append(processes)  # dodawanie listy procesów do listy ciągów
    return sequences


# Funcja określa rezultaty danego algorytmu. Jej parametrem jest dany algorytm, którego ma ocenić.
# Dalej określone są ilości ciągów i procesów.
def evaluate_algorithm(algorithm, num_sequences=100, num_processes=100):
    sequences = generate_processes(num_sequences, num_processes)  # uzupełnienie listy wygenerowanymi procesami

    total_avg_waiting_time = 0  # średni czas oczekiwania na przydzielenie procesora dla wszystkich ciągów
    total_avg_turnaround_time = 0  # średni czas cyklu przetwarzania dla wszystkich ciągów
    results = []  # lista zawierająca wyniki w postaci krotek

    for processes in sequences:
        avg_waiting_time, avg_turnaround_time = algorithm(processes)  # wywołanie danego algorytmu
        results.append((avg_waiting_time, avg_turnaround_time))  # dodanie rezultatów do listy
        total_avg_waiting_time += avg_waiting_time  # uzupełnienie czasów całkowitych
        total_avg_turnaround_time += avg_turnaround_time

    avg_waiting_time = total_avg_waiting_time / num_sequences
    avg_turnaround_time = total_avg_turnaround_time / num_sequences

    return avg_waiting_time, avg_turnaround_time, results


# Funkcja zapisywania danych do trzech plików Excel
def save_to_excels(test_data, fcfs_results, lcfs_results, sjf_results, summary_data):
    # Zapis surowych danych testowych do 'test_data.xlsx'
    test_data.to_excel('test_data.xlsx', index=False)

    # Zapis wyników do 'results.xlsx'
    fcfs_df = pd.DataFrame(fcfs_results, columns=['FCFS_Średni_Czas_Oczekiwania', 'FCFS_Średni_Czas_Cyklu_Przetwarzania'])
    lcfs_df = pd.DataFrame(lcfs_results, columns=['LCFS_Średni_Czas_Oczekiwania', 'LCFS_Średni_Czas_Cyklu_Przetwarzania'])
    sjf_df = pd.DataFrame(sjf_results, columns=['SJF_Średni_Czas_Oczekiwania', 'SJF_Średni_Czas_Cyklu_Przetwarzania'])
    combined_results = pd.concat([fcfs_df, lcfs_df, sjf_df], axis=1)  # łączenie DataFrame'ów wzdłuż osi kolumn
    combined_results.to_excel('results.xlsx', index=False)

    # Zapis podsumowania do 'average_results.xlsx'
    summary_df = pd.DataFrame(summary_data)
    summary_df.to_excel('average_results.xlsx', index=False)


# Generowanie danych testowych (ciągów procesów) i ocena algorytmu na podstawie średnich
sequences = generate_processes()
avg_waiting_time_fcfs, avg_turnaround_time_fcfs, fcfs_results = evaluate_algorithm(FCFS.fcfs_algorithm)
avg_waiting_time_lcfs, avg_turnaround_time_lcfs, lcfs_results = evaluate_algorithm(LCFS.lcfs_algorithm)
avg_waiting_time_sjf, avg_turnaround_time_sjf, sjf_results = evaluate_algorithm(SJF.sjf_algorithm)

# Tworzenie DataFrame dla surowych danych testowych
test_data = pd.concat(
    [pd.DataFrame(seq, columns=[f'Ciąg_{i + 1}_Czas_Oczekiwania', f'Ciąg_{i + 1}_Czas_Wykonania']) for i, seq in
     enumerate(sequences)],
    axis=1
)

# Tworzenie podsumowania wyników
summary_data = {
    'Algorytm': ['FCFS', 'LCFS', 'SJF'],
    'Średni czas oczekiwania na przydzielenie procesora': [avg_waiting_time_fcfs, avg_waiting_time_lcfs,
                                                           avg_waiting_time_sjf],
    'Średni czas cyklu przetwarzania': [avg_turnaround_time_fcfs, avg_turnaround_time_lcfs, avg_turnaround_time_sjf]
}

# Zapis danych do plików Excel
save_to_excels(test_data, fcfs_results, lcfs_results, sjf_results, summary_data)

# Wyświetlanie wyników w konsoli
print(f"Średni czas oczekiwania na przydzielenie procesora (FCFS): {avg_waiting_time_fcfs:.2f} s")
print(f"Średni czas cyklu przetwarzania (FCFS): {avg_turnaround_time_fcfs:.2f} s")
print(f"Średni czas oczekiwania na przydzielenie procesora (LCFS): {avg_waiting_time_lcfs:.2f} s")
print(f"Średni czas cyklu przetwarzania (LCFS): {avg_turnaround_time_lcfs:.2f} s")
print(f"Średni czas oczekiwania na przydzielenie procesora (SJF): {avg_waiting_time_sjf:.2f} s")
print(f"Średni czas cyklu przetwarzania (SJF): {avg_turnaround_time_sjf:.2f} s")
