# BookCollection.py
from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getNumberOfBooks(self):
        temp = self.head
        count = 0
        
        while temp != None:
            count += 1
            temp = temp.getNext()

        return count
            
    def insertBook(self, book):

        current = self.head
        previous = None
        last = False

        while current != None and not last:
            if current.getData() > book:
                last = True
            else:
                previous = current
                current = current.getNext()

        temp = BookCollectionNode(book)

        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
            
        '''
        if self.head == None: # list isn't empty 
            b = BookCollectionNode(book)
            self.head = b
            return 

        current = self.head
        previous= None

        if previous == None:
            temp.setNext(self.head)
            self.head = temp

        while temp != None:
            if book > temp.getData():
                previous = temp
                temp = temp.getNext()
            
        if temp == self.head: # ensures correct positioning
            b = BookCollectionNode(book)
            b.setNext(temp)
            self.head = b
            return

        b = BookCollectionNode(book)
        previous.setNext(b)
        b.setNext(previous)
        return
        '''

    def getBooksByAuthor(self, author):
        curr = self.head
        all_books = ""

        while curr != None:
            if curr.getData().getAuthor().upper() == author.upper():
                all_books += curr.getData().getBookDetails() + "\n"

            curr = curr.getNext()

        return all_books

        
    def getAllBooksInCollection(self):
        curr = self.head
        all_books = ""
    

        while curr != None:
            all_books += curr.getData().getBookDetails() + "\n" 
            curr = curr.getNext()

        return all_books



    

    def removeAuthor(self, author):
        current = self.head
        previous = None
        found = False

        if current == None:
            return
        
        while not found: # find the element and move current and previous
            if current == None:
                return
            
            if current.getData().getAuthor().upper() == author.upper():
                found = True
                
            else:
                previous = current
                current = current.getNext()

        while current != None and current.getData().getAuthor().upper() == author.upper():
            current = current.getNext()

            
        # Case 1: Remove 1st element
        if found == True and previous == None:
            self.head = current

        # Case 2: Remove not 1st element
        if found == True and previous != None:
            previous.setNext(current)

    def recursiveSearchTitle(self, title, bookNode):
        
        if bookNode == None:
            return False

        if bookNode.getData().getTitle().upper() == title.upper():
           # current = current.getNext()
            return True
        else:
            return self.recursiveSearchTitle(title, bookNode.next)

