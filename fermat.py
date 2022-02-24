import random


def prime_test(N, k):
	# This is main function, that is connected to the Test button. You don't need to touch it.
	return fermat(N,k), miller_rabin(N,k)

#returns x^y mod N
#complexity of O(n^3) because of the multiplications and bitshifts (complexity O(n^2)) that
#recurse n times.
def mod_exp(x, y, N):
    if y == 0:      #any value to the power 0 is one
        return 1
	
    z = mod_exp(x, int(y/2), N) #calculate the value of x^(y/2) mod N

    if y & 1:                   #if y is odd
        return (x * z**2) % N   #the return value is (x * z^2) mod N

    else:                       #otherwise if y is even
        return z**2 % N         #the return value is z^2 mod N
	

def fprobability(k):
    chance = 0.5                #the probability that the fermat algorithm is incorrect for a single value a
    return 1 - (chance ** k)    #the probability decreases for the number of values a (k) tested


def mprobability(k):
    chance = 0.25               #probablitiy that the miller-rabin test is incorrect for a single value a
    return 1 - (chance ** k)    #the probablity decreases for the number of values a (k) tested

#this function creates a list of k unique integers between 1 and N-1. It then proceeds to
#calculate the value a^(N-1) mod N (complexity of O(n^3)) for each value a. If the modular exponent
#is ever not one, then N is composite. Otherwise, we assume N is prime.
def fermat(N,k):
    vals = []                       #create an empty list
    i = 0                           #index counter
    while i != k:                   #while we haven't filled our list a with k values
        a = random.randint(1, N-1)  #generate a random integer between 1 and N-1
        if a not in vals:           #if it's not already in the list
            vals.append(a)          #add it to the list
            i += 1                  #increment the index counter

    for a in vals:                  #for each integer in our list
        test = mod_exp(a, N-1, N)   #calculate a^(N-1) mod N
        if test != 1:               #if it's not one
            return 'composite'      #the number is composite

    return 'prime'                  #if none of the a values tested confirmed composite, assume prime

#this function creates a list of k uniqe integers between 1 and N-1. It tests these values first by
#performing a Fermat test (complexity of O(n^3)) and if it passes, proceeeds to recursively half
#the exponent value and run the test again. The recursion of the helper function func results in a 
#complexity of O(n^4)
def miller_rabin(N,k):
    vals = []                       #create an empty list
    i = 0                           #index counter
    while i != k:                   #while we haven't filled our list a with k values
        a = random.randint(1, N-1)  #generate a random integer between 1 and N-1
        if a not in vals:           #if it's not already in the list
            vals.append(a)          #add it to the list
            i += 1                  #increment the index counter

    for a in vals:                  #for each value in our list
        test = mod_exp(a, N-1, N)   #calculate a^(N-1) mod N
        if test != 1:               #if it's not one
            return 'composite'      #N is composite
        
        test = func(a, int((N-1)/2), N) #perform the rest of the miller_rabin test
        if not test:                    #if it returns false
            return 'composite'          #then it's composite
    
    return 'prime'                      #if none of the a values tested composite, we assume prime

#recursively calculates a^exp mod N and halves the exp value. Performing modular exponentiation (O(n^3))
#for n recursions results in a complexity of O(n^4)
def func(a, exp, N):
    if exp & 1:                 #if the exp value is add
        return True             #exit assuming prime

    test = mod_exp(a, exp, N)   #calculate a^exp mod N

    if test-N == -1:            #if the result is negative 1
        return True             #exit assuming prime
    elif test != 1:             #otherwize if the result was not one
        return False            #N is composite

    return func(a, int(exp/2), N)   #perform these tests again but now exp = exp/2
    

