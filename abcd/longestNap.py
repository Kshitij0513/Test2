from datetime import datetime, time

class OccupiedTimeSlot():
    def __init__(self,text):
        t = text.split()
        self.startTime = Time(text=t[0])
        self.endTime = Time(text=t[1])
        self.duration = self.endTime.minus(self.startTime)

class FreeTimeSlot():
    def __init__(self,start,duration):
        self.startTime = start
        self.duration = duration


class Time():
    def __init__(self,minutes=None,text=''):
        if minutes == None:
            t = text.split(':')
            self.minutes = int(t[0])*60 + int(t[1])
        else:
            self.minutes = minutes


    def isGreaterThan(self,otherTime):
        if self.minutes > otherTime.minutes:
            return True
        return False

    def minus(self,otherTime):
        return Time(self.minutes - otherTime.minutes)

    def getTime(self):
        if self.minutes>=60:
             return f"{self.minutes//60}:{str(self.minutes%60).rjust(2,'0')}"
        else:
            return self.minutes

    def display(self):
        if self.minutes >= 60:
            return f"{self.minutes//60} hours and {self.minutes%60} minutes"
        else:
            return f"{self.minutes} minutes"

class Day():
    def __init__(self,no):
        self.no = no
        self.schedule = []
        self.freeTimes = []
        self.schedule.append(OccupiedTimeSlot('10:00 10:00 startTime'))

    def getAllFreeTimes(self):
        for i in range(1,len(self.schedule)):
            end = self.schedule[i].startTime
            start = self.schedule[i-1].endTime
            diff = end.minus(start)
            self.freeTimes.append(FreeTimeSlot(start,diff))
            

    def getMaxFreeTimeSlot(self):
        maxFreeTimeSlot = self.freeTimes[0]
        for time_slot in self.freeTimes[1:]:
            if time_slot.duration.isGreaterThan(maxFreeTimeSlot.duration):
                maxFreeTimeSlot = time_slot
        return maxFreeTimeSlot
    
    def addTimeSlot(self,time_slot):
        self.schedule.append(time_slot)

    def addEndSchedule(self):
        self.schedule.append(OccupiedTimeSlot('18:00 18:00 endTime'))

    def answer(self):
        self.getAllFreeTimes()
        longestNap = self.getMaxFreeTimeSlot()
        print(f"Day #{self.no}: the longest nap starts at {longestNap.startTime.getTime()} and will last for {longestNap.duration.display()}.")

        
        
'''
day = Day()

noOfLectures = 4
day.addTimeSlot(OccupiedTimeSlot('10:00 12:00 A'))
day.addTimeSlot(OccupiedTimeSlot('12:00 13:00 B'))
day.addTimeSlot(OccupiedTimeSlot('13:00 15:00 C'))
day.addTimeSlot(OccupiedTimeSlot('15:30 17:45 D'))

day.addEndSchedule()

day.answer()
'''
noOfDay = 1
while True:
    ip = input()
    if ip == "":
        break
    day = Day(noOfDay)
    noOfDay+=1
    noOfApps = int(ip)
    for i in range(noOfApps):
        day.addTimeSlot(OccupiedTimeSlot(input()))
    day.addEndSchedule()
    day.answer()
