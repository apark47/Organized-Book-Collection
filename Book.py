# Book.py

class Book:
    def __init__(self, title="", author="", year=None):
        self.title = title
        self.author = author
        self.year = year

    def getTitle(self):
        return self.title
    
    def getAuthor(self):
        return self.author
    
    def getYear(self):
        return self.year
        
    def getBookDetails(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

    def __gt__(self, other):
        # Compares the authors
        if self.author > other.author:
            return True

        if self.author < other.author:
            return False

        # Authors must be the same, compares years
        if self.year > other.year:
            return True

        if self.year < other.year:
            return False

        # Authors and years must be the same, compares title
        if self.title > other.title:
            return True

        if self.title < other.title:
            return False            
 
