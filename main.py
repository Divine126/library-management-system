import library, validators

def ask_valid(prompt, validator, error_message):
    while True:
        text = input(prompt).strip()
        if validator(text):
            return text
        print(error_message)

def main():
    lib = library.Library()       
    lib.load_all()               

    while True:
        print(f"\n{'='*40}")
        print("\tLibrary Management System")
        print(f"{'='*40}")
        print("\nMenu:\n")
        print("1. Add book")
        print("2. View all books")
        print("3. Search books")
        print("4. Register member")
        print("5. Borrow book")
        print("6. Return book")
        print("7. Get AI recommendation")
        print("8. Check overdue books")
        print("9. Save and exit")
        choice = input("\nChoose: ")

        try:
            if choice == "1":
                isbn = ask_valid("\nISBN: ", validators.validate_isbn, "Invalid ISBN")
                copies = int(input("Copies available: "))
                lib.add_book(isbn, copies)                      
                print("Book added\n")

            elif choice == "2":
                for book in lib.list_books():                  
                    print(book)

            elif choice == "3":
                keyword = input("Search (by keyword): ")
                for book in lib.search_book(keyword):         
                    print(book)

            elif choice == "4":
                name = input("\nName: ")
                email = ask_valid("Email: ", validators.validate_email, "Invalid email")
                phone = ask_valid("Phone: ", validators.validate_phone, "Invalid phone")
                lib.register_member(name, email, phone)          
                print("Member registered")

            elif choice == "5":
                isbn = ask_valid("\nISBN: ", validators.validate_isbn, "Invalid ISBN")
                email = ask_valid("Member email: ", validators.validate_email, "Invalid email")
                due_date = lib.borrow_book(isbn, email)           
                print("Borrowed. Due back: " + str(due_date))     

            elif choice == "6":
                isbn = ask_valid("\nISBN: ", validators.validate_isbn, "Invalid ISBN")
                email = ask_valid("Member email: ", validators.validate_email, "Invalid email")
                lib.return_book(isbn, email)                     
                print("Returned")

            elif choice == "7":
                taste = input("\nWhat do you like? ")
                print(lib.get_recommendation(taste))             

            elif choice == "8":
                overdue = lib.check_overdue_books()                
                if not overdue:                                   
                    print("No overdue books")
                else:
                    for record in overdue:
                        print(record["name"] + " (" + record["phone"] + ", " + record["email"] + ") - "
                              + record["title"] + " was due " + str(record["due_date"]))

            elif choice == "9":
                lib.save_all()                                    
                print("Goodbye")
                break

            else:
                print("Choose a number from 1 to 9")

        except Exception as e:
            print("Error: " + str(e))

        lib.save_all()                                          

if __name__ == "__main__":
    main()