class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {
            'Phone': phone,
            'Email': email,
            'Address': address
        }
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for name, details in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {details['Phone']}")
                print(f"Email: {details['Email']}")
                print(f"Address: {details['Address']}")
                print('-' * 20)
        else:
            print("No contacts found.")

    def search_contact(self, keyword):
        results = []
        for name, details in self.contacts.items():
            if keyword in name or keyword in details['Phone']:
                results.append((name, details))
        return results

    def update_contact(self, name, phone, email, address):
        if name in self.contacts:
            self.contacts[name] = {
                'Phone': phone,
                'Email': email,
                'Address': address
            }
            print(f"Contact {name} updated successfully!")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print(f"Contact {name} not found.")


def main():
    contact_manager = ContactManager()
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            results = contact_manager.search_contact(keyword)
            if results:
                print("Search Results:")
                for name, details in results:
                    print(f"Name: {name}")
                    print(f"Phone: {details['Phone']}")
                    print(f"Email: {details['Email']}")
                    print(f"Address: {details['Address']}")
                    print('-' * 20)
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            address = input("Enter new address: ")
            contact_manager.update_contact(name, phone, email, address)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
