import json
import os

# Function to save contacts to a JSON file
def save_contacts_to_file():
    with open("contacts_data.json", "w") as file:
        json.dump(contacts_data, file, indent=4)

# Function to load contacts from a JSON file
def load_contacts_from_file():
    if os.path.exists("contacts_data.json"):
        with open("contacts_data.json", "r") as file:
            return json.load(file)
    return {}

# Initialize contacts data by loading from the file
contacts_data = load_contacts_from_file()

# Function to display the menu
def menu_display():
    print("Contact Organizer: Digital Contact Hub")
    print("1. Add New Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Show Stored Contacts")
    print("5. Exit")

# Main program loop
contact_id_counter = 1

while True:
    menu_display()
    choice = input("Select an option: ")

    if choice == "1":
        print("Enter Contact Information\n")
        name = input("Enter the contact name: ")
        email = input("Enter the contact email: ")
        phone = input("Enter the mobile number: ")

        # Generate a unique ID for the contact
        contact_id = contact_id_counter
        contact_id_counter += 1

        # Add contact to the contact list
        contacts_data[contact_id] = {"Name": name, "Email": email, "Phone": phone}
        save_contacts_to_file()
        print(f"Contact '{name}' has been added to your digital contact hub.")

    elif choice == "2":
        print("View Contact Information:")
        for contact_id, contact_details in contacts_data.items():
            print("Contact ID:", contact_id)
            print("Name:", contact_details["Name"])
            print("Email:", contact_details["Email"])
            print("Phone:", contact_details["Phone"])
            print()

    elif choice == "3":
        name_to_search = input("Enter the name to search for: ")
        found_contact = None
        for contact_id, contact_details in contacts_data.items():
            if contact_details["Name"] == name_to_search:
                found_contact = contact_details
                break
        if found_contact:
            print(f"Name: {name_to_search}")
            print(f"Phone: {found_contact['Phone']}")
            print(f"Email: {found_contact['Email']}")
        else:
            print(f"Contact '{name_to_search}' not found in the contact hub.")

    elif choice == "4":
        print("Stored Contacts:")
        for contact_id, contact_details in contacts_data.items():
            print("Contact ID:", contact_id)
            print("Name:", contact_details["Name"])
            print("Email:", contact_details["Email"])
            print("Phone:", contact_details["Phone"])
            print()

    elif choice == "5":
        print("Exiting the program")
        break

    else:
        print("The selected option is not available right now. Please choose a valid option from the menu.")
