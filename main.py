import sys
import datetime
x =(datetime.datetime.now())
day = x.strftime("%d %B %Y")
books=[]
orderBook=0
class book:
    id:int
    name:str
    writer:str
    addedIn:str
    available:bool=True

def addBook(id,bookName,bookWriter):
    myBook=book()
    myBook.id=id
    myBook.name=bookName
    myBook.writer=bookWriter
    myBook.addedIn=day
    books.append(myBook)
    
def showBook():
    print("There are " + str(len(books))  + " books!" )
    print("************************" )
    for b in books:
        bookOrder=1
        if(b.available==True):
            print("Book Id: "+str(b.id)+"\nBook Name: "+b.name+"\nWriter: "+ b.writer+"\nAdded in: "+ b.addedIn)
            print("************************" )
        bookOrder+=1
    
def removeBook(id):
    print("Remove Book")
    for b in books:
        if(str(b.id)==str(id)):
            b.available=False
            print(b.name)
run=True
while (run):
    sys.argv=input("Yapacağınız işlemi girin:")
    if "add" in sys.argv:
        orderBook+=1
        addBook(orderBook,input("Book Name:\n"),input("Book Writer:\n"))
    elif "show book" in sys.argv:
        showBook()
    elif "remove" in sys.argv:
        removeBook(input("Enter Book ID:\n"))
    else:
        print("Wrong Input")
