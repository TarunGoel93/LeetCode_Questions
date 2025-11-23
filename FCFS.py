process = int(input("Enter the total Processes: "))
print(process)

print("Enter the Arrival time: ")
arrival_time = []
for i in range(0,process,1):
  arrival_time.append(int(input()))
print(arrival_time)

print("Enter the Burst time: ")
burst_time = []
for i in range(0,process,1):
  burst_time.append(int(input()))
print(burst_time)

print("Intals Inputs of the Table:")
for i in range(process):
  print(f"P{i+1}\t{arrival_time[i]}\t{burst_time[i]}")

print("Step1: Sort whole table wrt arrival time: ")
table = []
for i in range(process):
  table.append([i+1,arrival_time[i],burst_time[i]])
table.sort(key=lambda x: x[1])
for i in table:
  print(f"P{i[0]}\t{i[1]}\t{i[2]}")

print("Step2: Calculate the Completion time: ")
CT = []
ST = []
WT = []
TAT = []

for i , j in enumerate(table):
  if i==0:
    ST = j[1]
  else:
    ST = max(CT[i-1],j[1])
  CT = ST+j[2]
  WT = ST-j[1]
  TAT = CT-j[1]

  