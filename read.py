
#file should be the file that is being read in as the state machine
def read_line(file):
    current_state=[]
    commands=[]
    next_states=[]
    # i, j index variables, d=temporary dummy variable 
    i=0 ; j=0 ; d=0
    while(file[i].isupper()):
        current_state.append(file[i])
        i=i+1
    if(file[i]=='!'):
        commands[j].append(file[i])
        i=i+1
    while(file[i].islower()):
        commands[j].append(file[i])
        i=i+1
    if(file[i]=='='):
        #good do nothing
        i=i+1
    else:
        #Throw an error
        d=d+1
    while(file[i].isupper()):
        next_states[j].append(file[i])
        i=i+1
    if(file[i]==','):
        #repeat
        i=i+1
    elif(file[i]==';'):
        #go to next line
        #TODO implement loop for this functionality
        d=d+1
    else:
        #throw error
        d=d+1
    
    

