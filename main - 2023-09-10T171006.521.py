# Initialize an empty dictionary to store mooring information
moorings = {}

# Function to add a new mooring
def add_mooring():
    mooring_number = input("Enter mooring number: ")
    boat_name = input("Enter boat name: ")
    owner_name = input("Enter owner name: ")
    contact_number = input("Enter contact number: ")

    # Create a mooring entry in the dictionary
    moorings[mooring_number] = {
        'Boat Name': boat_name,
        'Owner Name': owner_name,
        'Contact Number': contact_number
    }
    print(f"Mooring {mooring_number} added successfully!")

# Function to view mooring information
def view_mooring():
    mooring_number = input("Enter mooring number to view details: ")
    mooring = moorings.get(mooring_number)

    if mooring:
        print(f"Mooring Number: {mooring_number}")
        print(f"Boat Name: {mooring['Boat Name']}")
        print(f"Owner Name: {mooring['Owner Name']}")
        print(f"Contact Number: {mooring['Contact Number']}")
    else:
        print(f"Mooring {mooring_number} not found.")

# Function to list all moorings
def list_moorings():
    if moorings:
        print("List of Moorings:")
        for mooring_number, mooring_info in moorings.items():
            print(f"Mooring Number: {mooring_number}")
            print(f"Boat Name: {mooring_info['Boat Name']}")
            print(f"Owner Name: {mooring_info['Owner Name']}")
            print(f"Contact Number: {mooring_info['Contact Number']}")
            print()
    else:
        print("No moorings found in the harbor.")

# Main menu
def main_menu():
    while True:
        print("\nHarbor Master Menu:")
        print("1. Add Mooring")
        print("2. View Mooring")
        print("3. List Moorings")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_mooring()
        elif choice == '2':
            view_mooring()
        elif choice == '3':
            list_moorings()
        elif choice == '4':
            print("Exiting Harbor Master application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
