class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter contact name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        self.contacts[name] = Contact(name, phone_number, email, address)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for name, contact in self.contacts.items():
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    def search_contact(self):
        name_or_phone_number = input("Enter name or phone number to search: ")
        for contact in self.contacts.values():
            if contact.name == name_or_phone_number or contact.phone_number == name_or_phone_number:
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
                return
        print("Contact not found.")

    def update_contact(self):
        name = input("Enter contact name to update: ")
        if name in self.contacts:
            contact = self.contacts[name]
            print("Enter new details (press Enter to skip):")
            contact.name = input(f"Name ({contact.name}): ") or contact.name
            contact.phone_number = input(f"Phone Number ({contact.phone_number}): ") or contact.phone_number
            contact.email = input(f"Email ({contact.email}): ") or contact.email
            contact.address = input(f"Address ({contact.address}): ") or contact.address
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self):
        name = input("Enter contact name to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("-------------------------------")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            contact_manager.add_contact()
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            contact_manager.search_contact()
        elif choice == "4":
            contact_manager.update_contact()
        elif choice == "5":
            contact_manager.delete_contact()
        elif choice == "6":
            print("Exiting the contact management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
