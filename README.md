# CPU Algorithms

## CPU allocation algorithms

### Summary
FCFS, LCFS and SJF algorithms were tested on generated sequences of processes.
Each sequence contains 100 processes with randomly generated arrival and burst times. 
Test data and results are saved to .xlsx files.

### Results overview
The algorithms were evaluated in terms of two measurement criteria:
* Waiting time (amount of time each process has to wait)
    * Total amount of time that a process has to wait in the queue before getting the CPU time
* Turnaround time
    * Total amount of time taken from the initiation of a process to the completion time of the process
The results were averaged out. 

## CPU page replacement algorithms

### Summary
LRU and LFU algorithms were again tested on 100 sequences. Each sequence contains randomly generated page numbers. 
The parameters used are as follows:
* The number of pages taken by processes S = 20. The number of memory pages occupied by processes S = 20. This number means that the algorithms under test will have to handle processes that can refer to up to 20 different pages of logical memory.
* Number of physical memory frames available for R processes: {3, 5, 7}. They affect the performance and efficiency of memory management.

For each reference string and each R value, the number of missing pages was recorded. The results were then averaged to evaluate the performance of each algorithm.
