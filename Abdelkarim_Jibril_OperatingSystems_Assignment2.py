
#Abdelkarim Jibril
#Assignment 2 Using First Come First Served processing algorithm

import random

#This class will define the process 
class Process:
    def __init__(self, processIdentifier, tickets):
        #This will act as a process identifier
        self.pid = processIdentifier
        #How many tickets are assigned to he processes
        self.tickets = tickets

#This class will define the scheduler
class Scheduler:
    #This will store the processes
    def __init__(self):
        self.processes = []
    #Function to ass processes to scheduler
    def add_process(self, process):
        self.processes.append(process)
    #Function that will choose the nect process using FCFS
    def select_next_process(self):
        if self.processes:
            #Because we are using a FCFS approach, the first process will always be returned resulting in process 1 always being chosen
            return self.processes.pop(0)
        #Incase there are no processes
        else:
            return None
#Creates a instance of Scheduler when we make sure that the script os being run directly
if __name__ == "__main__":
    scheduler = Scheduler()

    #Adding processes with their tickets
    #Because we are using FCFS the number of tickets does not really matter at all.
    scheduler.add_process(Process(1, 100))
    scheduler.add_process(Process(2, 100))
    scheduler.add_process(Process(3, 22))

    #Selecting the next process using FCFS
    next_process = scheduler.select_next_process()
    #Which ever processis selected wins (This will always be the first one)
    if next_process:
        print(f"Process {next_process.pid} wins the lottery!!!")
    else:
        #If there are none we prin that nothing is there
        print("No process available")
