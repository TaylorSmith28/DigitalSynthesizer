from ctypes import sizeof
from read import *
from init import *

#Main Driver for Simplified Boolean Expressions
#Currently implemented for one-hot encoding

#User input to determine input/output (i.e. statediagram, truth_table, karnaugh_map, boolean equation)
#Current implementation is to read state_diagram_file and then reprint
input = read_state_diagram('myfile.txt')
num_of_states = len(input)
num_of_signals = read_num_signals(input)

#Initializing Truthtable
truth_table = init_ttable(num_of_signals, num_of_states)

#Some outputs for fun XD
#print(input)
#print(len(input))
#print(num_of_signals)
i=0
while(i<len(truth_table)):
    print(truth_table[i])
    i=i+1



