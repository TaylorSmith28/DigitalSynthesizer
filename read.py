

#file should be the file that is being read in as the state machine
from contextlib import nullcontext

def read_state_diagram(file):
    #does not strip '/n'
    file1 = open(file,'r')
    lines=file.readlines()
    return lines

def read_truth_table(file):
    nullcontext

def read_karnaugh_map(file):
    nullcontext

def read_boolean_statements(file):
    nullcontext

