

        # RGLAB 385.3.1 - Text File processing

## Application Features
# - Add Contacts - add a phone number and name to our contact list
# - View Contacts - view all contacts previously saved
# - Quit out of the application

## Program Constraints
# - User friendly messages to assist user
# - use `main function` to ensure program only runs when called directly
# - organize it modularly into functions (not class based)

# Python facts:
# - Used for both Funtional Programming Paradigm AND OOP (Object oriented programming)

# Paths:
# - absolute path - starts at the root of the computer
# - relative is the relative path from one folder/file to another.
# - `/` - represents inbetween directories
# - `.`  - represents current directory
# - `..` - represents one directory above current directory

# This variable contains path for my file
contact_file = 'data/contact.txt'

#
def add_contact():
    # Get user input
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")

    # Open file as f and write to it
    # using a - append mode (To add)
    # opening files with 'with' means it autocloses file for us at end of code block
    with open(contact_file, 'a') as f:
        f.write(f'{name}: {phone}\n')
    
    # Print statement to let user know task was successful
    print(f'🎉 {name} has been added to your contacts!')

def view_contact():
    try:
        with open(contact_file, 'r') as f:
            contacts = f.readlines()
            
            # If contacts file exists but empty
            if not contacts:
                print('Your contact list is empty')
            else:
                print('🌟 Your Contact List 🌟:')

                for contact in contacts:
                    print(contact, end='')


    # is if file does not exist            
    except FileNotFoundError:
        raise FileNotFoundError('Your Contact List is empty')

# Def = define a function
# the parens of fucnctions contain passed in information
def main():
    # While loop will run until condition runs false
    # condition 'True', so loop will run forever until we say stop
    while True:
        print('\nContact List Application:')
        print('1. Add Contact')
        print('2. View Contacts')
        print('3. Quit')
        choice = input('Enter your choice: ')

        # If choice 1 add contact, else if choice 2 - view contact, elif choice 3 quit
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact()
        elif choice == '3':
            print('Goodbye')
            break # break out of while loop
        else:
            print('Invalid Choice. Please try again')
# To run a function: invoking, executing, running

# This sepcific line of code makes sure the function is NOT run upon import
# Only run upon calling, not run upon import within another page
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Error: {e}")