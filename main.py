from address_book import AddressBook, Record


if __name__ == "__main__":
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("7777777777")

    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for record in book.data.values():
        print(record)

    john = book.find("John")
    if john is not None:
        john.edit_phone("1234567890", "1112223333")
        print(john)

        # повертає None
        #found_phone = john.find_phone("1")
        found_phone = john.find_phone("7777777777")
        print(f"{john.name}: {found_phone}")

    book.delete("Jane")
