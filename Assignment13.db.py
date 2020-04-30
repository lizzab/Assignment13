# Ben Lizza
import sqlite3
from sqlite3 import Error


def create_connection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return conn


connection = create_connection("Assignment13.db")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

# String holds the query to create a table


create_customers_table = """
CREATE TABLE IF NOT EXISTS Customers (
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
  first_name        TEXT        NOT NULL,
  last_name         TEXT        NOT NULL,
  street_address    TEXT        NOT NULL,
  city              TEXT        NOT NULL,
  state             VARCHAR(2)  NOT NULL,
  zip               INTEGER
);
"""
create_books_table = """
CREATE TABLE IF NOT EXISTS Books (
  book_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
  title         TEXT    NOT NULL,
  author        TEXT    NOT NULL,
  ISBN          INTEGER NOT NULL,
  edition       TEXT    NOT NULL,
  price         INTEGER,
  publisher     TEXT    NOT NULL
);
"""

# Execute two queries to create the tables of the database
execute_query(connection, create_customers_table)
execute_query(connection, create_books_table)

# This is a main menu
option = None
while option != 3:
    menu_choice = int(input("Main Menu:\n"
                     "1.Customers\n"
                     "2.Books\n"
                     "3.Exit\n>>>"))

    if menu_choice == 1:
        # tem is a temporary value to terminate menu when asked
        tem = None
        while tem != 5:
            customers_menu_choice = input("Customers menu:\n"
                                              "1.Add a new customer\n"
                                              "2.Modify an existing customer\n"
                                              "3.Print a list of all customers\n"
                                              "4.Delete a customer\n"
                                              "5.Return to main menu\n>>>")
            if int(customers_menu_choice) == 1:
                # We start by receiving values for a new record
                name = str(input("Name:\n>>>"))
                last_name = str(input("Last Name:\n>>>"))
                address = str(input("Address:\n>>>"))
                city = str(input("City:\n>>>"))
                state = str(input("State:\n>>>"))
                zip = int(input("ZIP:\n>>>"))
                # Process of adding into database:
                add_customer = f"""
                INSERT INTO
                  Customers (first_name, last_name, street_address, city, state, zip)
                VALUES
                  ('{name}', '{last_name}', '{address}', '{city}', '{state}', '{zip}');
                """
                execute_query(connection,  add_customer)

            if int(customers_menu_choice) == 2:
                # We can change whatever we want in a record
                print("You can change:\ncustomer_id, first_name, last_name, street_address, city, state, zip")
                change = str(input("Be careful with your spelling (CASE SENSITIVE)\nType what you want to change:\n>>>"))
                # We need to specify a person to change
                print(f"Provide reference (Point out) from {change}")
                which_customer = input('>>>')
                value = input("Type new value:\n>>>")
                update_customer = f"""
                UPDATE
                  Customers
                SET
                  {change} = '{value}'
                WHERE
                  {change} = '{which_customer}'
                """
                execute_query(connection, update_customer)
                print("Remember changes will not work if you misspelled words.")

            if int(customers_menu_choice) == 3:
                # Create a query to return data from the users table
                select_customers = "SELECT * from Customers"
                people = execute_read_query(connection, select_customers)
                for person in people:
                    print(person)

            if int(customers_menu_choice) == 4:
                # We will delete by id
                delete_what = int(input("Be careful  with your spelling (CASE SENSITIVE)\nSpecify id:\n>>>"))
                delete_customer = f"""
                            DELETE FROM
                              Customers
                            WHERE
                              customer_id = '{delete_what}'
                            """
                execute_query(connection, delete_customer)
                print("Remember changes will not work if you misspelled words.")
            # Exiting a program
            if int(customers_menu_choice) == 5:
                tem = 5

    if menu_choice == 2:
        # tem is a temporary value to terminate menu when asked
        ten = None
        while ten != 5:
            books_menu = int(input("Books menu:\n"
                                   "1.Add a new book\n"
                                   "2.Modify an existing book\n"
                                   "3.Print a list of all books\n"
                                   "4.Delete a book\n"
                                   "5.Return to main menu\n>>>"))

            if int(books_menu) == 1:
                # We start by receiving values for a new record
                title = str(input("Title:\n>>>"))
                author = str(input("Author:\n>>>"))
                ISBN = int(input("ISBN number:\n>>>"))
                edition = input("Edition:\n>>>")
                price = int(input("Price:\n>>>"))
                publisher = input("Publisher:\n>>>")
                # Process of adding into database:
                add_book = f"""
                INSERT INTO
                  Books (title, author, ISBN, edition, price, publisher)
                VALUES
                  ('{title}', '{author}', '{ISBN}', '{edition}', '{price}', '{publisher}');
                """
                execute_query(connection,  add_book)

            if int(books_menu) == 2:
                # We can change whatever we want in a record
                print("You can change:\nbook_id, title, author, ISBN, edition, price, publisher")
                change_what = str(input("Be careful with your spelling (CASE SENSITIVE)\nType what you want to change:\n>>>"))
                # We need to specif a book
                print(f"Provide reference (Point out) from {change_what}")
                which_book = input('>>>')
                new_value = input("Type new value:\n>>>")
                update_book = f"""
                UPDATE
                  Books
                SET
                  {change_what} = '{new_value}'
                WHERE
                  {change_what} = '{which_book}'
                """
                execute_query(connection, update_book)
                print("Remember changes will not work if you misspelled words.")

            if int(books_menu) == 3:
                # Create a query to return data from the users table
                select_books = "SELECT * from Books"
                books = execute_read_query(connection, select_books)
                for book in books:
                    print(book)

            if int(books_menu) == 4:
                # Deletion by id
                book_id = int(input("Be careful with your spelling. (CASE SENSITIVE)\nSpecify id:\n>>>"))
                delete_book = f"""
                            DELETE FROM
                              Books
                            WHERE
                              book_id = '{book_id}'
                            """
                execute_query(connection, delete_book)
                print("Remember changes will not work if you misspelled words.")
            # Exiting
            if int(books_menu) == 5:
                ten = 5
    # Exiting a whole program
    if menu_choice >= 3:
        option = 3
        print("Have a nice day!")
