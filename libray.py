# working on a projject of library managemnet systemm
class Libray_Management_System:
    books=[]
    computer=[]
    math=[]
    Issued_books_with_reference=[]
    def __init__(self):
        self.student=[]
        self.my_library_record={}
    def Book_Record(self):
        print("Stock of Book is given ,put some you want in Library so that Student can Avail these Books")
        self.lst=["Database", "Computer Archetecture","Analysis of Algo","Caclulas","Probability","Differential equation","Linear Algebta"]
        for i in self.lst:
            if i not in Libray_Management_System.books:
                Libray_Management_System.books.append(i)
        print("Books That Are Available in Library At The Moment")
        print(Libray_Management_System.books)
    def Computer_books(self):
        self.cs_books=["Database", "Computer Archetecture","Analysis of Algo","Operating System"]
        for i in self.cs_books:
            if i in Libray_Management_System.books:
                if i not in Libray_Management_System.computer:
                    Libray_Management_System.computer.append(i)
        print("Computer Books that are available in Library")
        print(Libray_Management_System.computer)
    def Math_books(self):
        self.math_books=["Probability","Differential equation","Linear Algebta","Statistic"]
        for i in self.math_books:
            if i in Libray_Management_System.books:
                if i not in Libray_Management_System.math:
                    Libray_Management_System.math.append(i)
        print("Math Books that are available in Library")
        print(Libray_Management_System.math)
    def Issue_Books(self):
        student_name=input("Enter Your Name to Issue a Book")
        # self.student.append(self.student_name)
        print("Name of Department where exists and You want To Issue")
        self.enter=int(input("Enter 1 for computer books and ||  2 for math books"))
        book_name=input("Enter Book name to Issue")
        Libray_Management_System.Issued_books_with_reference.append((student_name,book_name))
        # for i in Libray_Management_System.books:
        if book_name in Libray_Management_System.books:
            if self.enter==1:
                if book_name in Libray_Management_System.computer:
                    # Libray_Management_System.Issued_books.append(self.book_name)
                    print("Books You Issued")
                    print(Libray_Management_System.Issued_books_with_reference)
                    Libray_Management_System.computer.remove(book_name)
                    Libray_Management_System.books.remove(book_name)
                    print("Remaining Computer Books in Library are")
                    print(Libray_Management_System.computer)
                    print("Remaining other all books in Library are")
                    print(Libray_Management_System.books)
            elif self.enter==2:
                if book_name in Libray_Management_System.math:
                    # Libray_Management_System.Issued_books_with_reference.append(book_name)
                    print("Books You Issued")
                    print(Libray_Management_System.Issued_books_with_reference)
                    Libray_Management_System.math.remove(book_name)
                    Libray_Management_System.books.remove(book_name)
                    print("Remaining Math Books are")
                    print(Libray_Management_System.math)
                    print("Remaining other all books in Library are")
                    print(Libray_Management_System.books)
        else:
            print("We are Really Sorry,thiss Book doesnot exist in our Library😥")
        # if book_name in Libray_Management_System.books:
        for student_name,book_name in Libray_Management_System.Issued_books_with_reference:
            if student_name not in self.my_library_record:
                self.my_library_record[student_name]=[]
            self.my_library_record[student_name].append(book_name)
        print("Student Name and Which book he issued")
        print(self.my_library_record)
    def Function_allow_keeping_Issueing_Book(self):
        while True:
            self.Book_Record()
            self.Computer_books()
            self.Math_books()
            self.Issue_Books()
obj1=Libray_Management_System()
obj1.Function_allow_keeping_Issueing_Book()