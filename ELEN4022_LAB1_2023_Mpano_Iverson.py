import numpy as np
import math
#this function was made with the help of GPT 3.5
def generate_bit_patterns(n):
    # Total number of bit patterns possible for n bits is 2^n
    num_patterns = 2 ** n
    
    # Generate every bit pattern by iterating from 0 to num_patterns and converting each number to binary
    bit_patterns = [bin(i)[2:].zfill(n) for i in range(num_patterns)]
    
    return bit_patterns

def find_bit_trfms(bytes_list,n,c,t):

    modByteslist = bytes_list

    for i in range(2**n):
        bit = bytes_list[i]
        bit = list(bit)
        #if the control bit is toggled, toggle the target
        if(bit[n-c-1] == '1'):
            if(bit[n-t-1] == '1'):
                bit[n-t-1] = '0'
            else:
                bit[n-t-1] = '1'
        bit = "".join(bit)
        modByteslist[i] = bit

    return modByteslist
def find_CNOT(n,c,t):

    #generate all bit patters given a number of qbits.
    
    #print(bytes_list)
    #get how all the "bytes" change
    trfm_pairs = find_bit_trfms(generate_bit_patterns(n),n,c,t) 
    int_list =[]
    #turn that into a list that tells us which vector must be where in the matrix
    for i in range(2**n):
        int_list.append(int(trfm_pairs[i],2))

    #print(generate_bit_patterns(n))      
    #print(trfm_pairs)
    #print(int_list)
    
    CNOT = []

    for i in range(2**n):
        row = "0"*(2**n)
        row = list(row)
        row[int_list[i]] = '1'
        row = [int(x) for x in row]
        CNOT.append(row)

    return(CNOT)

n=3
CNOTs_list =[]
#getting all the CNOT "state" matrices along the circuit
for c in range(n):
    for t in range(c+1,n):
        CNOTs_list.append(find_CNOT(n,c,t))
        
#multiplying them together
U = np.identity(2**n)
for S in reversed(CNOTs_list):
    U = np.dot(U,S)
    
print(U)