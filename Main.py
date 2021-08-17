class Book:
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year
        self.next = None
        self.prev = None

    def __str__(self):
        return "Title: " + self.title + "\t Author: " + self.author + "\t Published Year: " + str(self.year)


class ReadingList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_book(self, new_book):
        if self.head is None:
            self.head = new_book
            self.tail = new_book
        else:
            self.tail.next = new_book
            new_book.prev = self.tail
            self.tail = new_book

    def display(self):
        current = self.head
        while current is not None:
            print(current)
            current = current.next
        print()

    def remove_duplicates(self):
        head = self.head
        while head is not None:
            next_node = head.next
            if next_node is not None:
                while next_node is not None:
                    if next_node.title == head.title:
                        if next_node.next is not None:
                            next_node.next.prev = next_node.prev
                        if next_node.prev is not None:
                            next_node.prev.next = next_node.next
                    next_node = next_node.next
            head = head.next


if __name__ == "__main__":
    book_list = [
        ('Cassie Ng', 'Artificial Intelligence Applications', 2000),
        ('Jack Chan', 'Python 3', 2016),
        ('Cassie Ng', 'Artificial Intelligence Applications', 2000),
        ('Cassie Chun', 'Zoo', 2000),
        ('Cassie Chun', 'Zoo', 2000)]

    rl = ReadingList()
    for book in book_list:
        rl.add_book(Book(book[0], book[1], book[2]))

    print("Reading List BEFORE removing duplicates")
    rl.display()

    rl.remove_duplicates()

    print("Reading List AFTER removing duplicates")
    rl.display()
