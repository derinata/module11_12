class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        print("Publication Type: Book")
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print("Publication Type: Magazine")
        print(f"Name: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")

if __name__ == "__main__":
    magazine = Magazine("Donald Duck", "Aki Hyyppä")
    book = Book("Compartment No. 6", "Rosa Liksom", 192)

    magazine.print_information()
    print()
    book.print_information()