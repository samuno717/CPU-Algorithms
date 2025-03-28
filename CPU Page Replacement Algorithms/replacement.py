import numpy as np
import pandas as pd

import LFU
import LRU

# Parametry
S = 20  # Liczba stron pamięci zajmowanych przez procesy
R_values = [3, 5, 7]  # Liczba ramek pamięci fizycznej dostępnych dla procesów
num_sequences = 100  # Liczba testowanych ciągów
sequence_length = 100  # Liczba losowych numerów stron w ciągu

# Ustawienie seeda, aby eksperyment był powtarzalny (wygenerowane dane nie zmieniają się)
np.random.seed(42)


# Funkcja generująca losowe dane testowe. Parametrami są: liczba ciągów, długość ciągu i liczba stron pamięci)
def generate_test_data(num_sequences, sequence_length, S):
    test_data = []  # lista przechowująca generowane ciągi

    for seq_num in range(1, num_sequences + 1):
        sequence = np.random.randint(1, S + 1, sequence_length).tolist()  # Generowanie losowego ciągu stron i zmiana tablicy numpy na listę.
        test_data.append([seq_num] + sequence)  # Dodanie ciągu do listy danych testowych

    columns = ['Ciąg'] + [f'Strona_{i}' for i in range(1, sequence_length + 1)]  # Tworzenie kolumn dla DataFrame'u z danymi
    return pd.DataFrame(test_data, columns=columns)


# Funkcja zapisująca dane do Excela
def save_to_excel(df, file_path):
    df.to_excel(file_path, index=False)


# Funkcja przetwarzająca ciągi stron. Jej parametrami są: DataFrame zawierający ciągi stron do przetworzenia oraz lista wartości ramek
def process_sequences(df, R_values):
    results = []  # lista na wyniki każdego algorytmu

    for i, row in df.iterrows():  # pętla iterująca po wierszach DataFrame'u: i to indeks wiersza, a row to zawartość wiersza
        sequence = row.iloc[1:].tolist()  # zmienna zawiera listę numerów stron dla danego wiersza. iloc[1:] omija pierwszą kolumnę
        seq_results = {'Sequence': row.iloc[0]}  # słownik zawierający numer ciągu

        for R in R_values:
            page_faults_lru, page_hits_lru = LRU.lru_algorithm(sequence, R)  # wywołanie algorytmów
            page_faults_lfu, page_hits_lfu = LFU.lfu_algorithm(sequence, R)
            seq_results[f'LRU_Page_Faults_R={R}'] = page_faults_lru  # zapisanie wyników do słownika
            seq_results[f'LRU_Page_Hits_R={R}'] = page_hits_lru
            seq_results[f'LFU_Page_Faults_R={R}'] = page_faults_lfu
            seq_results[f'LFU_Page_Hits_R={R}'] = page_hits_lfu

        results.append(seq_results)  # dodanie wyników do listy

    return pd.DataFrame(results)  # tworzenie DataFrame'u z wynikami - wypisuje brakujące strony dla 100 ciągów


# Funkcja obliczająca średnią ilość brakujących stron. Jej parametrami są: df - DataFrame oraz R-Values - lista wartości ramek
def calculate_averages(df, R_values):
    average_results = {'R': [], 'Average_LRU_Page_Faults': [], 'Average_LFU_Page_Faults': []}  # słownik przechowujący wyniki

    for R in R_values:
        avg_lru_faults = df[f'LRU_Page_Faults_R={R}'].mean()  # obliczanie średniej z listy brakujących stron dla każdego algorytmu
        avg_lfu_faults = df[f'LFU_Page_Faults_R={R}'].mean()
        average_results['R'].append(R)  # dodanie danej wartości R do listy wartości ramek w słowniku
        average_results['Average_LRU_Page_Faults'].append(avg_lru_faults)  # dodanie średnią liczbę brakujących stron do listy w słowniku
        average_results['Average_LFU_Page_Faults'].append(avg_lfu_faults)

    return pd.DataFrame(average_results)  # tworzenie DataFrame'u


# Generowanie i zapisywanie danych testowych
df = generate_test_data(num_sequences, sequence_length, S)
save_to_excel(df, 'test_data_2.xlsx')

# Przetwarzanie sekwencji i zapis ilości brakujących stron dla każdego ciągu
results_df = process_sequences(df, R_values)
save_to_excel(results_df, 'results_2.xlsx')

# Obliczanie i zapisywanie średnich wyników algorytmów
average_results_2_df = calculate_averages(results_df, R_values)
save_to_excel(average_results_2_df, 'average_results_2.xlsx')

print(average_results_2_df)
