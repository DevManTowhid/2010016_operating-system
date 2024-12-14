import random 
class ProcessTowhid:
    #constructor
    def __init__(self, ID, name,arrival_time, burst_time):
        self.process_id = ID
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = 0
        self.completion_time = 0
        self.waiting_time = 0
        self.response_time = 0
        self.remaining_burst = burst_time
# Create a list to hold the processes
process_list = []       
for i in range(5):
    process = ProcessTowhid(i, f"Process{i}", random.randint(0,15), random.randint(3,20))
    process_list.append(process)

# Print the table header
print(f"{'Process Name':<20}{'Arrival Time':<20} {'Burst Time':<20}")
print("-" * 60)

# Print each process's name and burst time
for process in process_list:
    print(f"{process.name:<20}{process.arrival_time:<20}{process.burst_time:20}")

clocks = [process.burst_time for process in process_list]
total_clock = sum(clocks)
print(f"Clocks: {clocks} total clocks needed:{total_clock}")
print(f"{'Process Name':<20}{'Arrival Time':<20} {'Remaining Burst Time':<20}")
print("-" * 60)
for i in range(total_clock):
    arrived_processes = [(process.process_id,process.arrival_time,process.remaining_burst) for process in (process_list) if process.arrival_time <= i and process.remaining_burst > 0]

    print(arrived_processes) 
    running = sorted(arrived_processes, key=lambda x: (x[2], x[1]))[0][0] if arrived_processes != [] else None
    print("Running Id:" ,running)
    if running != None:
        print("running a process")
        process_list[running].remaining_burst -= 1
        print("Its remaining burst:",process_list[running].remaining_burst)

