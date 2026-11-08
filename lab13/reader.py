class Reader:
    def __init__(self, name, number, birth_date):
        self.name = name
        self.number = number
        self.birth_date = birth_date
        self.read_books = []
        self.current_books = []

    def add_book(self, title):
        self.current_books.append(title)
        print(self.name, "отримав книгу:", title)

    def return_book(self, title):
        if title in self.current_books:
            self.current_books.remove(title)
            self.read_books.append(title)
            print(self.name, "повернув книгу:", title)
        else:
            print("У читача", self.name, "немає такої книги на руках")

    def show_current_books(self):
        print("Книги на руках у", self.name, ":", self.current_books)

    def show_read_books(self):
        print("Прочитані книги", self.name, ":", self.read_books)