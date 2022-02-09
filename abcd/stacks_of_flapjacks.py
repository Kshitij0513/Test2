# 1, 2, 3, 4, 5
# 3, 2, 1, 4, 5
#stack = [2,1,4,3,5]
#stack = [4,1,2,3,5]
stack = [5,1,2,3,4]
#stack = [1,5,3,4,2]

def getMaxNotDone(l,done):
    lst=l[:]
    for no in done:
        lst.remove(no)
    return max(lst),lst.index(max(lst))



def flip(lst,n=None):
    global done, indexes
    if n == None:
        n = len(done)+1
    indexes.append(n)
    l = len(lst)+1
    return lst[:l-n][::-1] + lst[l-n:]

def getStartDone(lst):
    newlst = sorted(lst)
    done = []
    #print(lst,newlst)
    for i in range(len(lst)-1,-1,-1):
        #print(i)
        if lst[i] == newlst[i]:
            #print('yes')
            done.append(newlst[i])
        else:
            break
    return done
while True:
    stack = input()
    if stack == "":
        break
    stack = list(map(int,stack.split()))    
    #print(stack)
    done = getStartDone(stack)
    #print(f"done = {done}")
    b = stack[:] 
    #print(f"maxnoindex = {no}")
    indexes = []
    l = len(b)
    while b != sorted(stack):
        no,index = getMaxNotDone(b,done)
        if index == 0:
            b = flip(b)
            done.append(no)
        else:
            b = flip(b,l-index)
        #print(f"final is {b}")
        #print(f"done is {done}")
    indexes.append(0)
    print(*indexes)

