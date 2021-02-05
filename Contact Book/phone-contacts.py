# Phone Contact Book Project by Sebastian Whyte

import os

# Open file
f = open( r"contacts.txt", "a+" )

# Checks to see if there is text in the text file
get_size = os.path.getsize( "contacts.txt" )

flag = True


print("\nHello. Welcome to myPhone 12. What would you like to do?")


class Menu:

    # Main Menu
    def user_choice(self):

        print( "\nCONTACTS\n" + "CALL\n" + "TEXT\n" + "POWER OFF\n" )


        while flag:
            self.choice = input("Please type your choice: ").lower()

            if self.choice == 'contacts':
                menu.contacts()
                break

            if self.choice == 'call':
                menu.call()
                break

            if self.choice == 'text':
                menu.text()
                break

            if self.choice == 'power off':
                menu.power_off()
                break

            else:
                print("Invalid choice.")


    # Contacts Function
    def contacts(self):

        global get_size

        self.make_or_view_contact = input("Would you like to make a new contact or view contacts? Type make or view: ").lower()

        if self.make_or_view_contact == "make":
            if get_size == 0:
                print( "This file is empty.\n" + "You have no contacts." )
            menu.make_contact()


        if self.make_or_view_contact == "view":
            menu.view_contact()


    # Make Contact Function
    def make_contact( self ):

        print("Creating new contact....")

        self.name = input( "\nEnter Name: " ).title()
        self.phone_num = input( "Enter phone number: " )

        print( "Contact created." )
        print( self.name, self.phone_num[ :3 ] + "-" + self.phone_num[ 3:6 ] + "-" + self.phone_num[ 6: ] )

        f.write(self.name + ' ' + self.phone_num + '\n' )

        print( "\nTaking you back to home screen..." )
        menu.user_choice()


    # View Contact Fuction
    def view_contact( self ):

        print( "Viewing Contacts..." )

        with open( 'contacts.txt', 'r' ) as f:
            if get_size == 0:
                print("No contacts found")

            else:
                for contacts in f:
                    print(contacts, end ='')


    # Call Function
    def call(self):

        if self.choice == "call":
            self.call_person = input("\nWho would you like to call? ").title()

            if self.call_person.isalpha():
                with open( 'contacts.txt', 'r' ) as f:

                    if self.call_person in f.read():
                        print(f"Calling {self.call_person}...")

                    else:
                        print(f"{self.call_person} is not in your contacts. " + "Would you like to add them? If yes, type y. If no, type n.")

                        self.call_choice = input()

                        if self.call_choice == "y" or self.call_choice == "yes":
                            menu.contacts()

                        else:
                            #if self.call_choice == "n" or self.call_choice == "no":
                            print("Taking you back to home screen...")
                            menu.user_choice()

            else:
                print("Invalid choice. Taking you back to home screen...")
                menu.user_choice()


    # Text Function
    def text(self):

        global flag

        if self.choice == "text":
            self.text_person = input("\nWho would you like to text? ").title()

            if self.text_person.isalpha():
                with open( 'contacts.txt', 'r' ) as f:
                    if self.text_person in f.read():

                        while flag:
                            self.txt_message = input("Type in your message... ")


                            if len(self.txt_message) > 0:
                                print(f"\nHello! This is {self.text_person}. It's nice to hear from you!")
                                break


                            if len(self.txt_message) == 0:
                                print("\nYou can't send an empty text.")


                    else:
                        print(f"{self.text_person} is not in your contacts. " + "Would you like to add them? If yes, type y. If no, type n.")

                        self.text_choice = input()

                        if self.text_choice == "y" or self.text_choice == "yes":
                            menu.contacts()

                        else:
                            print("Taking you back to home screen...")
                            menu.user_choice()

            else:
                print( "Invalid choice. Taking you back to home screen..." )
                menu.user_choice()


    # Power Off Function
    def power_off(self):
        print("Shutting Down...zzz...")
        f.close()


# Creates object for Menu class
menu = Menu()
menu.user_choice()


