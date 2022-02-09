
namingConvention = {11:'Jack',12:'Queen',13:'King',14:'Ace'}
class Card():
    def __init__(self,value,kind,position=-1):
        self.value = value
        self.kind = kind
        self.position = position

    def getPosCard(self,position):
        c = Card(self.value,self.kind,position)
        return c

    def getName(self):
        if self.value<=10:
            return f"{self.value} of {self.kind}"
        else:
            return f"{namingConvention[self.value]} of {self.kind}"
        
class Deck():
    def __init__(self):
        self.cards = []
        i=1
        for kind in ["Clubs","Diamonds","Hearts","Spades"]:
            for value in range(2,15):
                self.cards.append(Card(value,kind,i))
                i+=1
        
        
    def get(self,position):
        lst = []
        for card in self.cards:
            lst.append(card.position)
            if card.position == position:
                return card
        
    
    def set(self,card,position):
        for i in range(len(self.cards)):
            if self.cards[i].position == position:
                self.cards[i] = card
                break

    def copy(self):
        d = Deck()
        d.cards = self.cards
        return d

testCases = int(input("Enter no of test cases : "))
for testCase in range(testCases):
    noOfShuffles = int(input("Enter no of shuffles : "))
    shuffles = []
    print(f"Enter {noOfShuffles} shuffle sequences")
    for i in range(noOfShuffles):
        shuffles.append(list(map(int,input().split())))
    sequences = []
    print("Enter sequence of shuffles")
    while True:
        ip = input()
        if ip == "":
            break
        sequences.append(int(ip))

    deck = Deck()
    
    for seq in sequences:
        shuffle = shuffles[seq-1]
        newDeck = Deck()
        for i in range(52):
            c=deck.get(shuffle[i])
            c = c.getPosCard(position=i+1)
            newDeck.set(c,i+1)
        deck = newDeck.copy()
    print("The final shuffle order is")
    for card in deck.cards:
        print(card.getName())
    print("\n")

