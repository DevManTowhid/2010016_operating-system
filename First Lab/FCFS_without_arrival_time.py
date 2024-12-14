import random 
class ProcessTowhid:
    #constructor
    def __init__(self, name,burst_time):
        self.name = name
        self.burst_time = burst_time
        self.start_time = 0
        self.completion_time = 0
        self.waiting_time = 0
        self.response_time = 0
        self.remaining_burst = burst_time
# Create a list to hold the processes
process_list = []       
for i in range(8):
    process = ProcessTowhid(f"Process{i}", random.randint(2,6))
    process_list.append(process)

# Print the table header
print(f"{'Process Name':<15} {'Burst Time':<15}")
print("-" * 30)

# Print each process's name and burst time
for process in process_list:
    print(f"{process.name:<15} {process.burst_time}")

clocks = [process.burst_time for process in process_list]
total_clock = sum(clocks)
print(f"Clocks: {clocks} total clocks needed:{total_clock}")

running_id = 0

print(f"{'Iteration':<20}{'Running Process':<20} {'Remaining Burst Time':<20}")
print("-" * 60)



for i in range(total_clock):
    
    running = process_list[running_id]
    running.remaining_burst -= 1
    print(f"{i:<20}{running.name:<20} {running.remaining_burst:<20}")
    
    if running.remaining_burst == 0:
        running_id += 1
    if running_id > len(process_list) - 1:
        break



