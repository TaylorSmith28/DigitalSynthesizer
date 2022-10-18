
#Initializing Truthtable
#TODO add support for enables from states
def init_ttable(num_of_signals, num_of_states):
    rows = 2**num_of_signals * num_of_states
    cols = num_of_signals +num_of_states*2
    #init table
    ttable=[ [0]*cols for i in range(rows)]
    #fill table with default values
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
    return (ttable)

        


