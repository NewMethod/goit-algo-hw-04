import re
#split arguments from command line
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
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
def add_contact(args, contacts):
    #delete empty spaces from phone number
    if len(args) > 2:
        print(args)
        final_values = [args[0]]
        values = args
        del values[0]
        values = ' '.join(values)
        final_values.append(values)
    name, phone = final_values
    #delete incorrect symbols from phone
    phone_norm = normalize_phone(phone)
    if phone_norm == None:
        return 'Incorrect phone number'
    else:
        contacts[name] = phone_norm
        return "Contact added."
#change contact im dictionary by name
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        #use command line
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
#for exit script
        if command in ["close", "exit"]:
            print("Good bye!")
            break
#main commands
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":            
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone" and len(args) == 1:
            print(contacts[args])
        elif command == 'all':
            for names in contacts:
                print(f"{names} - {contacts[names]}")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
