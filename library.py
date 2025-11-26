import os

class Library:
    def __init__(self):
        self.books = []               
        self.issued_books = set()       
        self.student_map = {}           
        self.file = "issued.txt"

        self.load_data()

  

    def save_data(self):
        with open(self.file, "w") as f:
            for student, book_list in self.student_map.items():
                for book in book_list:
                    f.write(f"{student},{book}\n")

    def load_data(self):
        if not os.path.exists(self.file):
            return
        with open(self.file, "r") as f:
            for line in f:
                student, book = line.strip().split(",")
                self.issued_books.add(book)
                if student in self.student_map:
                    self.student_map[student].append(book)
                else:
                    self.student_map[student] = [book]

   

    def add_book(self, book):
        self.books.append(book)
        print(f"✔ Book '{book}' added.")

    def show_books(self):
        print("\n📚 Available Books:")
        if not self.books:
            print("❌ No books available.")
        else:
            for b in self.books:
                print(" -", b)

    def issue_book(self, student, book):
        if book not in self.books:
            print(f"❌ Error: '{book}' is not available.")
            return

        self.books.remove(book)
        self.issued_books.add(book)

        if student in self.student_map:
            self.student_map[student].append(book)
        else:
            self.student_map[student] = [book]

        self.save_data()
        print(f"✔ '{book}' issued to {student}.")

    def return_book(self, student, book):
        if student not in self.student_map or book not in self.student_map[student]:
            print("❌ Error: This book was not issued to this student.")
            return

        self.student_map[student].remove(book)
        self.issued_books.remove(book)
        self.books.append(book)

        self.save_data()
        print(f"✔ '{book}' returned by {student}.")



def menu():
    library = Library()

    while True:
        print("\n========== LIBRARY MENU ==========")
        print("1. Add Book")
        print("2. Show Available Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        print("==================================")

        choice = input("Enter choice: ")

        if choice == "1":
            book = input("Enter book name: ")
            library.add_book(book)

        elif choice == "2":
            library.show_books()

        elif choice == "3":
            student = input("Enter student name: ")
            book = input("Enter book to issue: ")
            library.issue_book(student, book)

        elif choice == "4":
            student = input("Enter student name: ")
            book = input("Enter book to return: ")
            library.return_book(student, book)

        elif choice == "5":
            print("✔ Exiting system...")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
