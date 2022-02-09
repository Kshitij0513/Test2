import re

global HighCard, black, white, Rank, INDEX

n = input().split()
HighCard = {}
Rank = {}
Rank[1] = 0
Rank[2] = 0
white = n[5:]
black = n[:5]

def convert(Set):
    for i in range(0,5):
        temp = re.split('(\d+)',Set[i])
        try:
            temp[1]
        except:
            temp = ['',temp[0][0],temp[0][1]]
        print(temp)

        if(temp[1]=='J'):
            temp[1]='11'
        elif(temp[1]=='Q'):
            temp[1]='12'
        elif(temp[1]=='K'):
            temp[1]='13'
        elif(temp[1]=='A'):
            temp[1]='14'

        Set[i] = [temp[1], temp[2]]

    return Set

def Straight(Set):
    for i in range(0,4):
        if(Set[i][0]<Set[i+1][0]):
            continue
        else:
            return 0
    else:
        return 1

def Flush(Set):
    for i in range(0,4):
        if(Set[i][1]==Set[i+1][1]):
            continue
        else:
            return 0
    else:
        return 1

def Straight_Flush(Set):
    if(Straight(Set) == 1 and Flush(Set) == 1):
        Rank[INDEX] = 1
        print('black 1')
    else:
        Of_Kind(Set, 4)

def Of_Kind(Set, value):
    for i in range(0, 5):
        count = 0
        for j in range(i,5):
            if(Set[i][0]==Set[j][0]):
                count+=1
        if(count==value):
            if(value==4):
                Rank[INDEX]=2
                print('four of kind ')
            if(value==3):
                Rank[INDEX]=6
                print('three of kind ')
            if(value==2):
                Rank[INDEX]=8
                print('one pair')
            break
    else:
        if(value==4):
            Full_House(Set)
        if(value==3):
            Two_Pairs(Set)
        if(value==2):
            High_card(Set)

def Full_House(Set):
    for i in range(0,5):
        acount = 0
        temp = []
        bcount = 1
        for j in range(i,5):
            if(Set[i][0]==Set[j][0]):
                acount+=1
            else:
                if(Set[j][0]==Set[j][0]):
                    bcount+=1
                else:
                    temp.append(Set[j][0])
        if((acount==3 and bcount==2) or (acount==2 and bcount==3)):
            Rank[INDEX]=3
            #print('full house')
            break
    else:
        x = Flush(Set)
        if(x == 1):
            Rank[INDEX]=4
            print('flush')
        else:
            x = Straight(Set)
            if(x == 1):
                Rank[INDEX]=5
                print('straight')
            else:
                Of_Kind(Set, 3)

def Two_Pairs(Set):
    for i in range(0,5):
        acount = 0
        temp = []
        bcount = 1
        for j in range(i,5):
            if(Set[i][0] == Set[j][0]):
                acount+=1
            else:
                if(Set[j][0] in temp):
                    bcount+=1
                else:
                    temp.append(Set[j][0])
        if(acount==2 and bcount==2):
            Rank[INDEX]=7
            print('Two pairs')
    else:
        Of_Kind(Set, 2)

def High_card(Set):
    max = 0
    for j in range(0,4):
        for i in range(0,4):
            if(Set[i][0]<Set[i+1][0]):
                max = Set[i+1][0]
    Rank[INDEX] = 9
    print(max)
    HighCard[INDEX] = max


black = convert(black)
white = convert(white)
INDEX = 1
Straight_Flush(black)
INDEX = 2
Straight_Flush(white)

if(Rank[1] > Rank[2]):
    print('black wins')
elif(Rank[2] > Rank[1]):
    print('white wins')
elif(Rank[2]==Rank[1] and HighCard[1]==HighCard[2]):
    print('Tie')
else:
    if(HighCard[1]>HighCard[2]):
        print('Black wins')
    else:
        print('White wins')
