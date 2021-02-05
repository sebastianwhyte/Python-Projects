# Contact Book

A program that acts like the contact app on a cell phone. This program makes a text file, named "contacts.txt", which stores contacts the user creates. Upon running, the user is 
given a menu of options. If they haven't entered any contacts, they will be asked to do so once they choose an option from the main menu.

If given invalid responses from user, the program will go back to the main menu. 


## Contacts Option

In the Contacts menu, the program will tell give the user options of making a new contact or viewing current contacts. The program will check the file to see if the user has made any contacts. If they haven't, the program will tell them they have no contacts and ask if they'd like to make one. The new contact will be saved into the text file. Any contacts afterwards will be appended onto the file.

<img width="800" alt="Screen Shot 2021-02-04 at 11 50 24 PM" src="https://user-images.githubusercontent.com/62267311/106991215-c6295780-6743-11eb-8910-498ae5c6a41f.png">


## Call Option

If the user chooses to call someone, the program will ask for who they'd like to call. After reading what the user typed in, the program will read the text file and
check if the desired name is inside. If the name is in the file, the output will say "Calling {name}..." 

However, if the name is not in the file, the program will tell the user there is no such contact and give them the option to add that person into their contacts.

<img width="800" alt="Screen Shot 2021-02-04 at 11 54 48 PM" src="https://user-images.githubusercontent.com/62267311/106991516-62ebf500-6744-11eb-8288-589621e44daf.png">


## Text Option

If the user would like to text, the program asks who they'd like to text with. After reading what the user typed in, the program will read the text file and
check if the desired name is inside. If the name is in the file, the program will ask user to type a message. If the user types a message, they will get an automated text back. 

But if the user presses Enter without typing anything, the program will tell user that they can't send an empty text message and ask for them to type a message. 

<img width="800" alt="Screen Shot 2021-02-04 at 11 59 53 PM" src="https://user-images.githubusercontent.com/62267311/106991844-17861680-6745-11eb-8938-2f5482042b0e.png">


## Power Off Option

Once this option is chosen, the program will give an output that tells the user that its shutting down.

<img width="824" alt="Screen Shot 2021-02-05 at 12 03 31 AM" src="https://user-images.githubusercontent.com/62267311/106992112-b4e14a80-6745-11eb-8958-b98fd419a2b0.png">
