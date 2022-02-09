

class Author():
    def __init__(self,name):
        self.name = name
        self.no = "infinity"


class Journal():
    def __init__(self,name,authors):
        self.name = name
        self.authors = authors


def isIncluded(authorList,name):
    for author in authorList:
        if author.name == name:
            return True
        
        
def getAuthor(authorList,name):
    for author in authorList:
        if author.name == name:
            return author
        
def getMin(authorList):
    try:
        return min([author.no for author in authorList if author.no != "infinity"])
    except:
        return "infinity"


T = int(input("Enter no of test cases : "))
for testCase in range(T):
    allAuthors = []
    allJournals = []
    P, N = list(map(int,input("Enter P and N saperated by space : ").split()))
    print(f"\nEnter journal database for {P} Journals\n")
    for i in range(P):
        authorNames, journalName = input().split(': ')
        authorNames+=', '
        authorList = []
        for name in authorNames.split('., ')[:-1]:
            name+='.'
            if not isIncluded(allAuthors, name):
                allAuthors.append(Author(name))
            authorList.append(getAuthor(allAuthors,name))
        allJournals.append(Journal(journalName,authorList))
    
    erdos = getAuthor(allAuthors,'Erdos, P.')
    erdos.no = 0
    
    for journal in allJournals:
        minNo = getMin(journal.authors)
        if minNo != "infinity":
            for author in journal.authors:
                if author != erdos:
                    if author.no == "infinity" or author.no > minNo+1:
                        author.no = minNo + 1
                    else:
                        author.no == minNo
        else:
            for author in journal.authors:
                    author.no = "infinity"
        
    for journal in allJournals:
        minNo = getMin(journal.authors)
        if minNo != "infinity":
            for author in journal.authors:
                if author != erdos:
                    if author.no == "infinity" or author.no > minNo+1:
                        author.no = minNo + 1
                    else:
                        author.no == minNo
        else:
            for author in journal.authors:
                    author.no = "infinity"
        
    askedNames = []
    print(f"\nEnter names of {N} mathematicians\n")
    for i in range(N):
        askedNames.append(input())
    print(f"\nScenario {testCase+1}")
    for name in askedNames:
        author = getAuthor(allAuthors,name)
        print(f"{author.name} {author.no}")

