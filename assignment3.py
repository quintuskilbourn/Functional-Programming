
#name: Quintus Kilbourn
#SID: 54871935


#############################################################
#############################################################
###################     QUESTION 1    #######################
#############################################################
#############################################################

tlist = [                     ##list for testing
             [
                  [[[],18,[]],20,[]],
                  21,
                  []
             ],
             33,
             [
                     [[],34,[[],18,[]]],
                     35,
                     [[[],52,[]],54,[]]
             ]
        ]


 #############################################################
def swap(aTree):
    if not aTree:       #base case
        return []

    return [swap(aTree[2]),aTree[1],swap(aTree[0])]   #switch left and right and do recursive calls

 #############################################################

def height(aTree):
    if not aTree:               #base case
        return 0

    return 1+max(height(aTree[0]),height(aTree[2]))  #max because tree is not necessarily perfect

 #############################################################

def maxNode(aTree):                 #function to find largest node in given tree

    if not aTree[0] and not aTree[2]:   # base case - leaf
        return aTree[1]

    return max(maxNode(aTree[0]),aTree[1],maxNode(aTree[2])) # recursive call



def minNode(aTree):                 #function to find smallest node in given tree

    if not aTree[0] and not aTree[2]:  # base case -  leaf
        return aTree[1]

    if not aTree[0]:                   #case only one child node
        return min(aTree[1],minNode(aTree[2]))

    if not aTree[2]:
        return min(aTree[1],minNode(aTree[0]))

    return min(minNode(aTree[2]),aTree[1],minNode(aTree[0])) #recursive call



def isBST(aTree):

    if len(aTree) >3:       #must be binary tree
        return False

    if not aTree:       #base case - no more nodes
        return True

    if aTree[0] and minNode(aTree[0])>=aTree[1]:    #case Left node larger
        return False

    if aTree[2] and minNode(aTree[2])<=aTree[1]:    #case right node larger
        return False

    return isBST(aTree[0])*isBST(aTree[2]) #only need one false to set return to false



#############################################################

def count(aTree):
    if not aTree:           #base case - no more nodes left
        return 0

    return 1+count(aTree[0])+count(aTree[2])        #increment by one for each node



#############################################################
#############################################################
###################     QUESTION 2    #######################
#############################################################
#############################################################

from functools import reduce

myList = [1,2,34,5,2,3,12,34,0] #list for testing

#################################################

def count(aList):
    return reduce(lambda cnt,x:1+cnt,aList)     #add one for each element

#################################################

def sortFilt(aList, y):
    aList = list(aList)     #appends if non decreasing
    if not (y < aList[-1]):
        aList.append(y)
    return aList

def isSorted(myList):
    if not myList:      #if no elements then they cannot be decreasing
        return True
    testListA = list(map(lambda x:[x], myList))     #list of lists
    testListB = list(reduce(sortFilt, testListA[1:],[testListA[0]]))#appends only non decreasing
    if testListA == testListB:  #will be different if there were non decreasing instances
        return True
    return False

#################################################
def remDup(aList):
    aList = list(map(lambda x: [x],aList))  #list of lists
    aList = list(reduce(reList, aList,[]))  #remove duplicates
    return list(map(lambda x: x[0],aList)) #convert back to list of numbers

def reList(aList, y):
    aList = list(aList) #cast as list object
    if y not in aList:  #only append if there will not be a duplicate
        aList.append(y)
    return aList

#################################################

def sumUp(aList):
    aList = list(map(lambda x: [x], aList))     #list of lists
    aList = list(reduce(remConDup, aList,[[0]]))    #remove consecutive duplicates
    aList = list(map(lambda x: x[0], aList))    #back to list of numbers
    aList = list(filter(lambda x: x>0, aList))  #remove negatives
    return reduce(lambda x,y:x+y,aList,0)       #sum

def remConDup(aList, y):
    aList = list(aList) #cast as list
    if y != aList[-1]:  #only append if it is not the same as the previous element
        aList.append(y)
    return aList

print(tlist)
print(count(tli))
