import re
def password_size(password_to_check):
    for word in password_to_check:
        if len(word) <6:
            print(word,"-","\033[31mPassword must contain at least 6 characters!")
            print("\033[0m")
        else:
            print(word,"-","\033[32mCorrect!")
            print("\033[0m")
    return "Next Step\n"
def capital_letter(password_to_check):
    for word in password_to_check:
        match = re.findall(r'[A-Z]', word)
        if len(match) >=1:
            print(word,"-","\033[32mCorrect!")
            print("\033[0m")
        else:
            print(word,"-","\033[31mPassword must contain at least one capital letter!")
            print("\033[0m")
    return "Next Step\n"
def numbers(password_to_check):
    for word in password_to_check:
        match = re.findall(r'[0-9]',word)
        if len(match) >=2:
            print(word,"-","\033[32mCorrect!")
            print("\033[0m")
        else:
            print(word,"-","\033[31mPassword must contain at least two numbers!")
            print("\033[0m")
    return "Nest Step\n"



def symbol(password_to_check, symbols):
    for word in password_to_check:
        if any(char in word for char in symbols):
            print(word,"-", "\033[31mPassword must not iclude any characters! ")
            print("\033[0m")
        else:
            print(word,"-","\033[32mCorrect!")
            print("\033[0m")
    return "All passwords are checked!"

def main():

    password = input("Tell me your password: ")
    password_to_check = []
    symbols = "~!@#$%^&*()-+=}{|[]\?/:;'<>,."
    try:
        file = open(password + ".txt", "r")
        for i in file:
            password_to_check.append(i)

    except:
        if "," in password:
            password_to_check = password.split(",")
        else:
            password_to_check.append(password)


    print(password_size(password_to_check))
    print(capital_letter(password_to_check))
    print(numbers(password_to_check))
    print(symbol(password_to_check, symbols))


if __name__ == "__main__":
    main()

