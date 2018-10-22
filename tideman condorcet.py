import numpy as np
import random


# voters = criteria with their weight
alpha  = 3.0 # voting token (default value = 3)
beta = 6.0 # Age of the last block (default value = 6)
gamma = 1.0 # reputation (default value = 1)


# ballots
def makeballot(maxValue):
    # This will create a set of candidates
    i={}
    for x in range (maxValue):
        i[chr(250+x)]=random.randint(1,maxValue)
    return (i)


# define function to create M matrix
def fillMatrix(ballot):        # square array of arrays
    dim = len(ballot)
    new_square = np.zeros(shape=(dim,dim))
    # fill upper and lower triangles symmetrically by replicating diagonally
    
    for v in range(1,dim):
        iterations = dim - v
        x =  v
        y = 0
        while iterations > 0:
            g=ballot[x][1]
            h=ballot [y][1]
            if h-g > 0:
                new_square[x][y] = -1
                new_square[y][x] =  1
            elif h-g < 0:
                new_square[x][y] = 1
                new_square[y][x] =  -1 
            else :
                new_square[x][y] = 0
                new_square[y][x] =  0   
            x += 1
            y += 1
            iterations -= 1
    return new_square

# create a loop to make m voting rounds with n candidates
n = int(input("Please enter the number of candidates to simulate:"))
m = int(input("Please enter the number simulations of voting round you want:"))
for i in range (m):
    # for each candidates, creation of the corresponding ballot Age, Reputation and Voting
    ballotAge=makeballot(100)
    ballotReputation=makeballot(100)
    ballotVoting=makeballot(100)

    # sorting ballot is important (dict has no sequence)
    ballotAgeSort = list(ballotAge.items())
    ballotAgeSort.sort
    print(ballotAgeSort)
    
    ballotRepSort = list(ballotReputation.items())
    ballotRepSort.sort
    #print(ballotRepSort)

    ballotVoteSort = list(ballotVoting.items())
    ballotVoteSort.sort
    #print(ballotVoteSort)

    # creation of M matrix
    MA=MR=ME=0

    MA=fillMatrix(ballotAgeSort)
    #print(MA)

    MR= fillMatrix(ballotRepSort)
    #print(MR)

    ME = fillMatrix(ballotVoteSort)
    #print(ME)

    Mtot = alpha*ME+ beta*MA + gamma*MR
    #print(Mtot)

    #check immediate concorcet winner
    w=np.where(np.all(Mtot>=0, axis=1)) #number of row with all value > or equal to 0

    if len(w[0])==1: # if the number of rows with all value > or equal to 0 is =1 then it is the winner
        print ("There is an immediate Condorcet Winner :" ,ballotAgeSort [np.where(np.all(Mtot>=0, axis=1))[0][0]][0])
        #print(Mtot)
    else :
        print ("No immediate Condorcet Winner !!!!")
        print('Age',ballotAgeSort)
        print('Rep',ballotRepSort)
        print('Vote',ballotVoteSort)
        print('Mtot',Mtot)
         #create a new matrix with only tie candidates and their scores in A, R, E
        Tie_ballot=[]
        for t in range (0,len(w[0])):
            Tie_ballot.append([ballotAgeSort [w [0][t]][0],ballotRepSort [w [0][t]][1], ballotAgeSort [w [0][t]][1], ballotVoteSort [w [0][t]][1]])
            Max_R_tie=max(Tie_ballot, key=lambda x:x[1])
        print(Tie_ballot)  
        print (Max_R_tie)
    


