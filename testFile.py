# testFile.py

from BookCollectionNode import BookCollectionNode
from BookCollection import BookCollection
from Book import Book

# pytests for Book.py
def test_Book():
    b = Book("Jane Eyre", "Bronte, Charlotte", 1847)
    b2 = Book("Animal Farm", "Orwell, George", 1945)
    b3 = Book("Frankenstein", "Shelley, Mary", 1818)
    b4 = Book("Frankenstein", "Shelley, Mary", 2023)
    b5 = Book("Hunger Games", "Shelley, Mary", 2023)

    
    assert b.getTitle() == "Jane Eyre"
    assert b.getAuthor() == "Bronte, Charlotte"
    assert b.getYear() == 1847
    assert b.getBookDetails() == f"Title: Jane Eyre, Author: Bronte, Charlotte, Year: 1847"

    assert b2.getTitle() == "Animal Farm"
    assert b2.getAuthor() == "Orwell, George"
    assert b2.getYear() == 1945
    assert b2.getBookDetails() == f"Title: Animal Farm, Author: Orwell, George, Year: 1945"

    assert b3.getTitle() == "Frankenstein"
    assert b3.getAuthor() == "Shelley, Mary"
    assert b3.getYear() == 1818
    assert b3.getBookDetails() == f"Title: Frankenstein, Author: Shelley, Mary, Year: 1818"

    assert (b < b2) == True
    assert (b2 > b) == True
    assert (b3 > b2) == True
    assert (b3 < b2) == False
    assert (b4 > b3) == True
    assert (b5 > b4) == True
    assert (b5 < b4) == False


# pytests for BookCollectionNode.py
def test_BookCollectionNode():
    n = BookCollectionNode(4)
    assert n.getData() == 4

    n.setData(600)
    n.setNext(800)
    assert n.getData() == 600
    assert n.getNext() == 800

    n.setData(1)
    n.setNext(2)
    assert n.getData() == 1
    assert n.getNext() == 2

    n.setData(0)
    n.setNext(10)
    assert n.getData() == 0
    assert n.getNext() == 10



# pytests for BookCollection.py

def test_BookCollection():
    a = BookCollection()

    assert a.isEmpty() == True
    assert a.getNumberOfBooks() == 0
    assert a.getAllBooksInCollection() == ""

    b = Book("Jane Eyre", "Bronte, Charlotte", 1847)
    b2 = Book("Animal Farm", "Orwell, George", 1945)
    b3 = Book("Frankenstein", "Shelley, Mary", 1818)
    b4 = Book("Hunger Games", "Shelley, Mary", 2023)
    b5 = Book("Dracula", "Stoker, Bram", 1897)


    a.insertBook(b)
    a.insertBook(b2)
    a.insertBook(b3)
    

    assert a.isEmpty() == False
    assert a.getNumberOfBooks() == 3
    assert a.getBooksByAuthor("Bronte, Charlotte") == "Title: Jane Eyre, Author: Bronte, Charlotte, Year: 1847\n"
    assert a.getAllBooksInCollection() == "Title: Jane Eyre, Author: Bronte, Charlotte, Year: 1847\n\
Title: Animal Farm, Author: Orwell, George, Year: 1945\n\
Title: Frankenstein, Author: Shelley, Mary, Year: 1818\n"

    a.insertBook(b4)
    assert a.isEmpty() == False
    assert a.getNumberOfBooks() == 4
    assert a.getBooksByAuthor("Shelley, Mary") == "Title: Frankenstein, Author: Shelley, Mary, Year: 1818\n\
Title: Hunger Games, Author: Shelley, Mary, Year: 2023\n"
    assert a.getAllBooksInCollection() == "Title: Jane Eyre, Author: Bronte, Charlotte, Year: 1847\n\
Title: Animal Farm, Author: Orwell, George, Year: 1945\n\
Title: Frankenstein, Author: Shelley, Mary, Year: 1818\n\
Title: Hunger Games, Author: Shelley, Mary, Year: 2023\n"

    a.removeAuthor("Bronte, Charlotte")
    assert a.getAllBooksInCollection() == "Title: Animal Farm, Author: Orwell, George, Year: 1945\n\
Title: Frankenstein, Author: Shelley, Mary, Year: 1818\n\
Title: Hunger Games, Author: Shelley, Mary, Year: 2023\n"
    assert a.getBooksByAuthor("Bronte, Charlotte") == ""

    a.removeAuthor("Shelley, Mary")
    assert a.getAllBooksInCollection() == "Title: Animal Farm, Author: Orwell, George, Year: 1945\n"
    assert a.getBooksByAuthor("Shelley, Mary") == ""    

    a.insertBook(b5)
    assert a.getAllBooksInCollection() == "Title: Animal Farm, Author: Orwell, George, Year: 1945\n\
Title: Dracula, Author: Stoker, Bram, Year: 1897\n"

    a.removeAuthor("Orwell, George")
    assert a.getAllBooksInCollection() == "Title: Dracula, Author: Stoker, Bram, Year: 1897\n"

    assert a.recursiveSearchTitle("Ready Player One", a.head) == False
    assert a.recursiveSearchTitle("Dracula", a.head) == True
    assert a.recursiveSearchTitle("Aniaml Farm", a.head) == False
    

    

