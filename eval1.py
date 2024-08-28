def add_book(my_dict):
    title =input("enter book title: ")
    author =input("enter book author: " )
    isbn =int(input("enter book ISBN: " ))
    gener =input("enter book genre: ")
    avail =input("enter book status: ")
    book_id= len(my_dict)
    my_dict[book_id +1]=[title,author,isbn,gener,avail]
    print (my_dict)
    
def update_book_details(my_dict):
    print_dict(my_dict)

    
def search_by_isbn(my_dict):
    book_isbn= input("enter book ISBN : ")

    
def generate_genre_report(my_dict):
    print(" Title "," Author "," ISBN "," Genre "," Availability Status ")
    book_genre= input("enter book genre : ")
    

my_dict={1:["Twisted hate","Ana huang",1,"Romance","available"]}
print("what do you want to do?")
da = 1
while da==1:
    print("1. Add a new book")
    print("2. Update book details")
    print("3. Search for book")
    print("4. Report of all  available books in each genre")
    print("5. Exit")
    choice=int(input("enter a number: "))
    if choice == 1:
       add_book(my_dict)
    else:
       da=0




