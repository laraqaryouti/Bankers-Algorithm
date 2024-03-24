#*Note: To ensure the program functions correctly, please make sure that each process's instance resources are separated by a comma
# and the processes are followed by a space. 
#For example, allocated resources: 1,2,3 4,5,6 

import tkinter as tk

def Bankers_Algorithm():
    available = Available.get().split(',')
    resources = int(m.get())
    processes = int(n.get())
    splittingAllocation = Allocated.get().split()
    allocation = []
    splittingMax = Max.get().split()
    maxResources = []
    sequence = ''
    need = []
    work = []
    unvisited = []
    seq = 0
    finished = [False] * processes

    for i in available:
        work.append(int(i))

    for x in splittingAllocation:
        allocation.append(list(map(int, x.split(','))))

    for x in splittingMax:
        maxResources.append(list(map(int, x.split(','))))

    for i in range(processes):
        row = []
        for j in range(resources):
            row.append(maxResources[i][j] - allocation[i][j])
        need.append(row)

    for i in range(processes):
        count = 0
        for j in range(resources):
            if need[i][j] <= int(work[j]):
                count += 1
                if count == resources:
                    for x in range(resources):
                        work[x] += allocation[i][x]
                    sequence += f'P{i} '
                    seq += 1
                    finished[i] = True
            else:
                if i not in unvisited:
                    unvisited.append(i)

    count = 0
    for i in unvisited:
        count = 0
        for j in range(resources):
            if need[i][j] <= int(work[j]):
                count += 1
                if count == resources:
                    for x in range(resources):
                        work[x] += allocation[i][x]
                    sequence += f'P{i} '
                    seq += 1
                    finished[i] = True

    if seq == processes:
        result_label.config(text="The system is in a safe state, no deadlocks, the safe sequence:")
        sequence_label.config(text=sequence)
    else:
        result_label.config(text="The system is in an unsafe state, possible deadlock, the partial sequence:")
        sequence_label.config(text=sequence)
    work_label.config(text=f"Work: {work}")


window = tk.Tk()
window.title("Banker Algorithm")

label = tk.Label(window, text="Number of Processes")
label.grid(row=0, column=0, padx=10, pady=10)
n = tk.Entry(window)
n.grid(row=0, column=1, padx=10, pady=10)

label1 = tk.Label(window, text="Number of Resources")
label1.grid(row=1, column=0, padx=10, pady=10)
m = tk.Entry(window)
m.grid(row=1, column=1, padx=10, pady=10)

label2 = tk.Label(window, text="Instances for each resource")
label2.grid(row=2, column=0, padx=10, pady=10)
Instances = tk.Entry(window)
Instances.grid(row=2, column=1, padx=10, pady=10)

label3 = tk.Label(window, text="Currently allocated resources to a process")
label3.grid(row=3, column=0, padx=10, pady=10)
Allocated = tk.Entry(window)
Allocated.grid(row=3, column=1, padx=10, pady=10)

label4 = tk.Label(window, text="Max number of resources for each process")
label4.grid(row=4, column=0, padx=10, pady=10)
Max = tk.Entry(window)
Max.grid(row=4, column=1, padx=10, pady=10)

label5 = tk.Label(window, text="Available Instances of each resource")
label5.grid(row=5, column=0, padx=10, pady=10)
Available = tk.Entry(window)
Available.grid(row=5, column=1, padx=10, pady=10)

button = tk.Button(window, text="Calculate", command=Bankers_Algorithm)
button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(window, text="")
result_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
sequence_label = tk.Label(window, text="")
sequence_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
work_label = tk.Label(window, text="")
work_label.grid(row=9, column=0, columnspan=2, padx=10, pady=10)
finished_label = tk.Label(window, text="")
finished_label.grid(row=10, column=0, columnspan=2, padx=10, pady=10)
window.mainloop()
