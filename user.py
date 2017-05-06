class User:
    def __init__(self, name, surname, email, number):
        self.name = name
        self.surname = surname
        self.email = email
        self.number = number


class Book:
    def __init__(self):
        self.users = []
    def add_user(self, name, surname, email, number):
        self.users.append(User(name, surname, email, number))

    def save(self):
        f = open("Phonebook.txt", "w")
        print(len(self.users), file=f)
        for user in self.users:
            print(*[len(user.email), len(user.number)], file=f)
            print(*[user.name, user.surname], file=f)

            for email in user.email:
                print(email, file=f)

            for number in user.number:
                print(number, file=f)

        f.close()

    def load(self):
        f = open("Phonebook.txt", "r")
        for user_index in range(int(f.readline())):
            email_count, phone_count = [int(i) for i in f.readline().split(" ")]
            *name, surname = f.readline().split()
            emails = []
            for email_index in range(email_count):
                emails.append(f.readline().split("\n")[0])

            phones = []
            for phone_index in range(phone_count):
                phones.append(f.readline().split("\n")[0])

            self.add_user(name, surname, emails, phones)
        f.close()

class Menu:

    def __init__(self, book):
        book.load()
        while(True):
            print('1. Print Phone Numbers')
            print('2. Add a Phone Number')
            print('3. Remove a Phone Number')
            print('4. Lookup a Phone Number')
            print('5. Quit')
            menu_choice = int(input("Enter type in a number (1-5):"))

            print()
            if menu_choice == 1:

                print("Telephone Numbers:")
                print(*[user.name for user in book.users])

            elif menu_choice == 2:
                print("Add Name,Surname,Number and Email")
                name = input("Name: ")
                surname = input("Surname: ")
                email = input("Email: ")
                phone = int(input("Number: "))
                book.add_user(name, surname, [email], [phone])

            elif menu_choice == 3:
                print("Remove Name and Number")
                name = input("Name: ")
                for user in book.users:
                    if name in user.name:
                        book.users.remove(user)
                    else:
                        print(name, "was not found")

            elif menu_choice == 4:

                print("Lookup Number")
                name = input("Name: ")
                for user in book.users:


                    if name in user.name:




                        print("The name is", user.name)
                        print("The number is",*user.number)

            elif menu_choice == 5:
                book.save()
                return




book = Book()
menu = Menu(book)
