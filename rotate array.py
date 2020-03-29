def rotateArray(array, n, d): 
    
    for i in range(0, d): 
        x = array[0]
        for j in range(0, n-1): 
            array[j] = array[j+1]
        array[n-1]= x
def printarray(array): 
    for i in range(0, n): 
        print(array[i])
array= [12,10,5,6,52,36]
n= len(array)
rotateArray(array, n, 2)
printarray(array)