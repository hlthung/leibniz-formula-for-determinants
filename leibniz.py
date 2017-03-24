f = open("output.txt", "w")
new = []

for line in open ('matrix.txt').readlines():
    for a in line.splitlines():
        a = a.strip()
        if not a:
            continue
        #split by ','
        b = a.split(",")
        #convert to number
        v = [int(i) for i in b]
        new.append(v)#append to new list

def bubble_sort(alist):
    """
    Pre: take an argument alist
    Post: return either + or -
    Bestcase: O(N)
    Worstcase: O(N^2)
    N is the length of list
    """
    step = 0
    n = len(alist)
    for i in range(n-1,0,-1):#count from backward
        swapped = False
        for j in range(i):
            if alist[j] > alist[j+1]:
                swap(alist,j,j+1)
                step += 1#step +=1 whenever swapped is true
                swapped = True
                    
        if not swapped:
            break#break earlier
    #if number of steps is even, add
    if step == 0 or step%2 == 0:
        return '+'
    else:#else minus
        return '-'
    
def swap(a,i,j):
    """
    Pre:alist and two position
    Post: swapped
    """
    a[i],a[j] = a[j], a[i]
    
def checkDimension(a):
    """
    Pre: Take in a matrix
    Post: return True or Error
    Bestcase: O(N)
    Worstcase: O(N)
    N is the length of parameter a
    """
    for i in range (len(a)):
        #check column and row
        if len(a[i]) != len(a):
            print("Incorrect dimensions")
            return "Error"
    return True

tmp2=[]
array=[]

#OPTIMIZED-Decision explanation:
####################################################################################################################
#Reference1:    Below code refers to heap pseudo-algorithm from wikipedia
#               https://en.wikipedia.org/wiki/Heap%27s_algorithm#Details_of_the_algorithm
#Reference2:    Research paper on analysis at all the permutations algorithm
#               http://homepage.divms.uiowa.edu/~goodman/22m150.dir/2007/Permutation%20Generation%20Methods.pdf
#               Where in conclusion, it stated that Heap's algorithm is slightly more effecient and can code faster
#Reference3:    Books Electircal Engineering and Intelligent Systems Chapter6.1
#               stated"The heap method runs faster and is simpler than other methods as presented"
#Reference4:    Where I got a better understanding:
#               https://www.youtube.com/watch?v=YMMNgn6qZVA            
######################################################################################################################

#Implementation of Heap's algorithm
def det(b,alist):
    """
    pre: b and alist is define
    post:perform operation of aux_det, return tmp2,array2,array
    Bestcase: O(1)
    Worstcase: O(1)
    """
    array2 = []
    aux_det(b,alist,len(alist),array2,tmp2,array)
    return tmp2,array2,array

def aux_det(b,a,n,array2,tmp2,array):
    """
    pre: b,a,n,array2,tmp2,array are define
    post:perform operation
    Bestcase: O(N!), N is length of row/column of matrix(eg. 3x3)
    Worstcase: O(N!)
    """
    if n == 1:
        array2.append(a[:])
        for j in range(n):
            tmp = []
            for k in range(len(b)):
                tmp.append(b[k][a[k]-1])
            #init as 1
            mult=1
            for i in range(len(tmp)):
                mult *= tmp[i]
            #append to an array to check its sign later
            array.append(mult)
            tmp2.append(tmp)
            
    else:
        #perform the algorithm stated
        for i in range(n):
            #produce all of the permutations that end with the element that
            #has just been moved to the last position
            aux_det(b,a,n-1,array2,tmp2,array)
            if(n%2==1):#when n is odd switch the first element and the last one
                swap(a,0,n-1)  
            else:#when n is even, switch ith element and the last one
                swap(a,i,n-1)
def main():
    """
    Pre: take a matrix and its all possible permutation
    Post: either return result or error message
    (Part1)Bestcase: O(N^2), N is length of row/column of matrix(eg. 3x3)
           Worstcase: O(N^2)
    (Part2)Bestcase: O(N!), N is length of row/column of matrix(eg. 3x3)
           Worstcase: O(N!)
    (Part3)Bestcase: O(N), N is the length of row/column of matrix(eg. 3x3)
           Worstcase: O(N)
    """
    #process if dimension all right
    if checkDimension(new) == True:
            final = 0
            f.write("N = "+str(len(new))+"\n")
            f.write("Input Matrix: \n")
            
            #Part1:Print as required format
            for i in range (len(new)):
                for j in range (len(new)):
                    f.write(str(new[i][j]))
                f.write("\n")

            #Part2:Calculate Determination
            plist = [i+1 for i in range(len(new))]
            a,b,array = det(new,plist)
            
            #Part3: Sign
            for i in range(len(b)):    
                if ((bubble_sort(b[i])) == '+'):
                    final += array[i]#sgn(+1)
                else:
                    final -= array[i]#sgn(-1)

            f.write("\nDeterminant = "+str(final))
            return
    else:
        return 'Error'
print(main())
f.close()


