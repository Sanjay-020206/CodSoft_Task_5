class Contact:
    def __init__(self, store_name, phone_number, email, address):
        self.store_name = store_name
        self.phone_number = phone_number
        self.email = email
        self.address = address

contact_list = []

def add_contact(store_name, phone_number, email, address):
    contact = Contact(store_name, phone_number, email, address)
    contact_list.append(contact)
    print("Contact added successfully.")

def view_contacts():
    if not contact_list:
        print("No contacts found.")
    for contact in contact_list:
        print(f"Store Name: {contact.store_name}, Phone Number: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")

def search_contact(query):
    results = [contact for contact in contact_list if query.lower() in contact.store_name.lower() or query in contact.phone_number]
    if results:
        for contact in results:
            print(f"Store Name: {contact.store_name}, Phone Number: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
    else:
        print("No matching contacts found.")

def update_contact(old_phone_number, new_store_name=None, new_phone_number=None, new_email=None, new_address=None):
    for contact in contact_list:
        if contact.phone_number == old_phone_number:
            if new_store_name:
                contact.store_name = new_store_name
            if new_phone_number:
                contact.phone_number = new_phone_number
            if new_email:
                contact.email = new_email
            if new_address:
                contact.address = new_address
            print("Contact updated successfully.")
            return True
    print("Contact not found.")
    return False

def delete_contact(phone_number):
    global contact_list
    contact_list = [contact for contact in contact_list if contact.phone_number != phone_number]
    print("Contact deleted successfully.")

def display_menu():
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            store_name = input("Enter store name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(store_name, phone_number, email, address)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            search_contact(query)
        elif choice == '4':
            old_phone_number = input("Enter the phone number of the contact to update: ")
            new_store_name = input("Enter new store name (leave blank to keep current): ")
            new_phone_number = input("Enter new phone number (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")
            new_address = input("Enter new address (leave blank to keep current): ")
            update_contact(old_phone_number, new_store_name, new_phone_number, new_email, new_address)
        elif choice == '5':
            phone_number = input("Enter the phone number of the contact to delete: ")
            delete_contact(phone_number)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
