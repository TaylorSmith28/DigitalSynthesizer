#file should be the file that is being read in as the state machine
from contextlib import nullcontext

def read_state_diagram(input):
    #does not strip '/n'
    with open(input) as file:
        lines=file.readlines()
    return lines

#input is lines of state diagram
def read_num_signals(input):
    #Counters
    i = 0; j=0
    #List of signals
    signals = []
    while(input[j][i]!='\n'):
        if(input[j][i].islower() & (input[j][i] not in signals)):
            signals.append(input[j][i])
        i=i+1
        #Move to next line to search for more signals
        if(input[j][i]=='\n'):
            j=j+1
            i=0
        if(j==len(input)):
            break
    return len(signals)

def read_truth_table(file):
    nullcontext

def read_karnaugh_map(file):
    nullcontext

def read_boolean_statements(file):
    nullcontext

