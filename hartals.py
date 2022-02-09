class Day():
    def __init__(self,date,name):
        self.date = date
        if name == "Fr" or name == "Sa":
            self.countable = False
        else:
            self.countable = True
        self.hartals = 0
        
    def add(self):
        self.hartals+=1
        
class Calendar():
    def __init__(self,duration):
        dayNames = ["Su","Mo","Tu","We","Th","Fr","Sa"]
        self.days = []
        for i in range(duration):
            self.days.append(Day(i+1,dayNames[i%7]))
            
    def addHartal(self,p):
        for day in self.days:
            if day.date % p == 0:
                day.add()
                
    def getEffective(self):
        effective = 0
        for day in self.days:
            if day.countable:
                if day.hartals > 0:
                    effective+=1
        return effective

T = int(input("Enter no of test cases : "))
for testCase in range(T):
    N = int(input("Enter span of days : "))
    P = int(input("Enter no of parties : "))
    H = []
    print(f"Enter party parameter for {P} parties")
    for i in range(P):
        H.append(int(input()))
    cal = Calendar(N)
    for party in H:
        cal.addHartal(party)
    print("No of working days lost is ",cal.getEffective())
    

