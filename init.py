
from contextlib import nullcontext

#Initializing Truthtable
#TODO add support for enables from states
def init_ttable(num_of_signals, num_of_states):
    rows = 2**num_of_signals * num_of_states
    cols = num_of_signals +num_of_states*2
    #init table with all zeros
    ttable=[ [0]*cols for i in range(rows)]
    #fill the signals columns
    j=0
    while(j<num_of_signals):
        i = 0
        counter=-1
        flag=0
        while(i < rows):
            counter=counter+1
            if(counter == 2**j):
                if(flag):
                    flag=0
                else:
                    flag=1
                counter=0
            ttable[i][j] = flag
            i=i+1
        j=j+1
    #fill the state columns (THIS IS FOR ONE HOT ENCODING)
    j=0 ; h = 0
    counter = num_of_signals + num_of_states - 1
    while(j<rows):
        i=num_of_signals
        while(i<(cols - num_of_states)):
            if(i==counter):
                ttable[j][i]=1
            else:
                ttable[j][i]=0
            i=i+1
        h=h+1
        j=j+1
        if(h==2**num_of_signals):
            counter=counter-1
            h=0
    return (ttable)

#Initialize Karnaugh Maps
def init_karnaugh_map():
    nullcontext



