import re
#split arguments from command line
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    result = [cmd, *args]
    return result
#normalize number of phone
def normalize_phone(phone_number):
    # generate right format numbers
    pattern_number = r"[+\(\)\w\s\\-]*(0\d{2})[\(\)\w\s\\-]*(\d{3})[\(\)\w\s\\-]*(\d{2})[\(\)\w\s\\-]*(\d{2})[\(\)\w\s\\-]*"
    match = re.search(pattern_number, phone_number)
    if match:
        replacement = r"\1\2\3\4"
        norm_phone = re.sub(pattern_number, replacement, phone_number)
        return norm_phone
#add new contact to the dictionary
def add_contact(contacts, arguments):
    #delete empty spaces from phone number
    if len(arguments) == 2 and len(arguments[0]) > 1:
        final_values = [arguments[0]]
        values = arguments
        del values[0]
        values = ' '.join(values)
        final_values.append(values)
    else:
        return "Incorrect name or all line"
    name, phone = final_values
    #delete incorrect symbols from phone
    phone_norm = normalize_phone(phone)
    if phone_norm == None:
        return 'Incorrect phone number'
    else:
        contacts[name.capitalize()] = phone_norm
        return "Contact added."
#change contact im dictionary by name
def change_contact(contacts, arguments):
    name, phone = arguments
    if name in contacts:
        phone_norm = normalize_phone(phone)
        contacts[name.capitalize()] = phone_norm
        return "Contact updated."
    else:
        return "Contact isn`t found"
#print all contacts
def show_all(contacts):
    for names in contacts:
        print(f"{names.capitalize()} - {contacts[names]}")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        #use command line
        user_input = input("Enter a command: ")
        program_output = parse_input(user_input)
        part_input = program_output[1:]
#for exit script
        if program_output[0].lower() in ["close", "exit", "quit"]:
            print("Good bye!")
            break
#main commands
        elif program_output[0] == "hello":
            print("How can I help you?")
        elif program_output[0] == "add":            
            print(add_contact(contacts, part_input))
        elif program_output[0] == "change":
            print(change_contact(contacts, part_input))
        elif program_output[0] == "phone" and len(part_input) == 1:
            print(contacts[part_input[0]])
        elif program_output[0] == 'all':
            show_all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
