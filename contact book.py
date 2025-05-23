import os

CONTACTS_FILE = "contacts.txt"

# Load existing contacts from file (if it exists)
def load_contacts():
    contacts = {}
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            for line in f:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    return contacts

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        for name, phone in contacts.items():
            f.write(f"{name},{phone}\n")

# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact added.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

# Search for a contact by name
def search_contact(contacts):
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

# Main menu loop
def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Quit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                add_contact(contacts)
            elif choice == "2":
                view_contacts(contacts)
            elif choice == "3":
                search_contact(contacts)
            elif choice == "4":
                save_contacts(contacts)
                print("Contacts saved. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
