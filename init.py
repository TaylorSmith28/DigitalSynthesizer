
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

#Header for truth table
def init_header(ttable, signals, states):
    i=0
    full_states=[]
    next_states=[]
    while(i<len(states)):
        full_states.append('q'+states[i])
        next_states.append('d'+states[i])
    full_states=full_states+next_states
    return (signals + full_states)

#for one hot
#TODO:Implement logic change
def update_ttable(state_machine, ttable, signals):
    j=0
    while(j<len(state_machine):
        flag=0
        dowhile(flag=0):
            current_state = state_machine[j][0]
            
            #interpret next states
            i=0
            while(i<len(state_machine[j]):
                if(state_machine[j][i].islower()):
                    current_command = state_machine[j][i]
                if(state_machine[j][i].isupper() & i!=0):
                    current_end_state = state_machine[j][i]
                if(state_machine[j][i]==','):
                    #we have reached the end of a command, time to update ttable
                    #need to find location of signal, current state, and next state
                    #TODO: replaces ttable with header
                    k=0
                    while(k<len(header[0])):
                        if(header[0][k]==current_command):
                            com_locx=k
                        elif(header[0][k]==current_state):
                            cur_sta_locx=k
                        elif(header[0][k]==current_end_state):
                            cur_end_locx=k
                    k=0
                    #iterate over the entire current state
                    while(k<2**len(signals)):
                        
            
            if(state_machine[j][i]==';'):
                #Go to next state
                flag=1
        j=j+1


