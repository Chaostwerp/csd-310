from glob import escape
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "whatabook",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)
    
cursor = db.cursor()

#define book viewing function
def show_books():
    try:

        cursor.execute("SELECT book_name, author, details FROM books")

        book_list = cursor.fetchall()
        print ("\n  -- DISPLAYING AVAILABLE BOOKS --")

        for book in book_list:
            print("\nName: ", book[0],
            "\nAuthor: ", book[1],
            "\nDetails: ", book[2])

    except:
        print("An error has occurred")

#define store location viewing function
def show_locations():
    try:

        cursor.execute("SELECT locale FROM stores")

        store_list = cursor.fetchall()
        print ("\n  -- DISPLAYING LIST OF STORES --")

        for store in store_list:
            print("\nLocation: ", store[0])

    except:
        print("An error has occurred")    

#define account viewing function, making sure to use try/catch block to check for valid user id
    #within account view, give options for viewing current wishlist, adding to wishlist, and returning to main menu
        #book adding function must list book_id, book_name, author, and details fields of books not already in the wishlist
        #insert statement for adding a book to a wishlist needs both book_id and user_id

#function for showing account menu
def show_account_menu(current_user):
    selection = None
    while selection != 3:

        try:

            print("\n1 - View your wishlist",
            "\n2 - Add a book to your wishlist",
            "\n3 - Return to main menu")

            selection = int(input("\nPlease enter the number by the action you would like to take. "))

            #section of account menu function that displays user's wishlist
            if selection == 1:
                
                cursor.execute("SELECT user_id, book_name, author, details FROM wishlists INNER JOIN books ON wishlists.book_id = books.book_id")

                user_wishlist = cursor.fetchall()

                for book in user_wishlist:

                    if book[0] == current_user:

                        print("\nBook name: ", book[1],
                        "\nAuthor: ", book[2],
                        "\nDetails: ", book[3])

            #Section of account menu function that allows for making additions to the wishlist
            elif selection == 2:

                cursor.execute("SELECT user_id, books.book_id, book_name, author, details FROM books LEFT JOIN wishlists ON books.book_id = wishlists.book_id")

                other_books = cursor.fetchall()

                print("\nThe following books are available for addition to your wishlist:")

                for book in other_books:
                    if book[0] != current_user:
                     print("\nBook ID: ", book[1],
                        "\nBook name: ", book[2],
                        "\nAuthor: ", book[3],
                        "\nDetails: ", book[4])
                
                new_book = int(input("Please enter the book ID of the book you would like to add to your wishlist. "))

                try:
                    for book in other_books:
                        if book[0] == current_user:
                            print("\nThat book is already on your wishlist!")

                        elif book[1] == new_book:
                            cursor.execute("INSERT INTO wishlists (user_id, book_id) VALUES(%s, %s)", (current_user, book[1]))
                            print("\n",book[2],"has successfully been added to your wishlist.")
                        
                
                except:
                    print("There was a problem adding the book to your wishlist.")




            elif selection == 3:
                print("\nReturning to main menu")

            else:
                print("\nI'm sorry, that's not a valid selection.")
        except:
            print("\nI'm sorry, that's not a valid selection.")



def validate_user():
    try:

        supplied_id = int(input("What is your user ID? "))

        cursor.execute("SELECT user_id, first_name, last_name FROM users")

        user_list = cursor.fetchall()

        for user in user_list:

            if user[0] == supplied_id:

                print("Hello,", user[1], user[2])

                current_user = user[0]

                show_account_menu(current_user)
    
    except:
        print("\nError: invalid user")


#Function for displaying the main menu

def show_main_menu():
    print("Welcome to the WhatABook app! What would you like to do?")

    selection = None

    while selection != 0:

        try:

            print("\n1 - View our list of available books"
            "\n2 - View a list of our store locations"
            "\n3 - Go to your account"
            "\n0 - Exit the app")

            selection = int(input("Please enter the number to the left of your selection. "))

            if selection == 1:
                show_books()

            elif selection == 2:
                show_locations()

            elif selection == 3:
                validate_user()

            elif selection == 0:
                escape

            else:
                print("I'm sorry, that's not a valid choice.")

        except:
            print("An error occurred, please try again.")



show_main_menu()

#Exit program block to close things off
input("Thank you for visiting WhatABook! Press the enter key to close the app.")