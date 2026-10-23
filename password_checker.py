# Password Strength Checker
# Author: Girdhar
# Internship Task 1
# This program checks if a password is strong or weak
# and tells the user how to make it better.

special_chars = "!@#$%^&*()-_=+[]{};:,.<>/?"

common_words = ["password", "admin", "welcome", "login", "letmein",
                "qwerty", "iloveyou", "monkey", "dragon", "hello",
                "india", "secret", "root", "test", "guest"]

bad_patterns = ["1234", "4321", "abcd", "dcba"]   # easy sequences

# common names that hackers try first
common_names = ["rahul", "rohit", "amit", "priya", "rohan", "ankit", "neha",
                "pooja", "sachin", "virat", "suresh", "ramesh", "mohit",
                "vikas", "deepak", "sunil", "manoj", "anil", "arjun", "ajay",
                "vijay", "sanjay", "shubham", "aman", "nikhil", "karan",
                "sonu", "monu", "golu", "john", "david", "michael", "james",
                "robert", "mary", "alex", "chris", "sarah", "emma"]

# keyboard clusters (keys that are next to each other)
keyboard_clusters = ["qwerty", "qwer", "asdf", "zxcv", "1qaz", "qazwsx",
                     "poiuy", "lkjhg", "mnbvc", "wasd"]

# common number clusters
common_numbers = ["123456", "654321", "111111", "000000", "222222",
                  "112233", "121212", "123123", "696969", "786",
                  "007", "1337", "9876", "2580", "0123"]

old_passwords = []   # stores passwords checked in this run


def has_repeats(password):
    # checks for 3 same characters in a row like aaa or 111
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True
    return False


def has_pattern(password):
    # checks for easy patterns like 1234 or qwerty
    p = password.lower()
    for pattern in bad_patterns:
        if pattern in p:
            return True
    return False


def find_common_word(password):
    # change tricks like p@ssw0rd back to password
    p = password.lower()
    p = p.replace("@", "a").replace("0", "o").replace("3", "e")
    p = p.replace("$", "s").replace("1", "i").replace("5", "s")
    for word in common_words:
        if word in p:
            return word
    return ""


def find_common_name(password):
    # checks if a common name like rahul or john is in the password
    p = password.lower()
    p = p.replace("@", "a").replace("0", "o").replace("3", "e")
    p = p.replace("$", "s").replace("1", "i").replace("5", "s")
    for name in common_names:
        if name in p:
            return name
    return ""


def find_keyboard_cluster(password):
    # checks for keys next to each other like qwerty or asdf
    p = password.lower()
    for cluster in keyboard_clusters:
        if cluster in p:
            return cluster
    return ""


def find_common_number(password):
    # checks for common number clusters like 123456 or 000000
    for number in common_numbers:
        if number in password:
            return number
    return ""


def has_year(password):
    # checks for a year like 1999 or 2005 (easy to guess, like a birth year)
    for i in range(len(password) - 3):
        chunk = password[i:i + 4]
        if chunk.isdigit() and (chunk.startswith("19") or chunk.startswith("20")):
            return chunk
    return ""


def is_passphrase(password):
    # passphrase = 4 or more words joined by space, - or _
    p = password.replace("-", " ").replace("_", " ")
    words = p.split()
    if len(words) >= 4 and len(password) >= 16:
        return True
    return False


def find_personal_info(password, personal_info):
    # checks if name, birth year, pet name etc. is inside the password
    p = password.lower()
    personal_info = personal_info.replace("/", ",").replace("-", ",").replace(".", ",")
    for item in personal_info.split(","):
        item = item.strip().lower()
        if len(item) >= 3 and item in p:
            return item
    return ""


def check_password(password, personal_info):
    score = 0
    total = 12
    tips = []
    bad_choice = False   # becomes True for common word or personal info

    phrase = is_passphrase(password)

    # check each character of the password
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True

    # 1. length
    if len(password) >= 12:
        score += 1
    else:
        tips.append("Use at least 12 characters (16 or more is best).")

    # 2. lowercase
    if has_lower:
        score += 1
    else:
        tips.append("Add a lowercase letter (a-z).")

    # 3. uppercase (passphrase does not need it)
    if has_upper or phrase:
        score += 1
    else:
        tips.append("Add an uppercase letter (A-Z).")

    # 4. number
    if has_digit or phrase:
        score += 1
    else:
        tips.append("Add a number (0-9).")

    # 5. special character
    if has_special or phrase:
        score += 1
    else:
        tips.append("Add a special character like ! @ # $ %.")

    # 6. patterns and repeats
    if has_pattern(password) or has_repeats(password):
        tips.append("Avoid patterns like 1234, abcd, qwerty or aaa.")
    else:
        score += 1

    # 7. common words
    word = find_common_word(password)
    if word != "":
        tips.append("Do not use common words (found '" + word + "').")
        bad_choice = True
    else:
        score += 1

    # 8. personal info
    info = find_personal_info(password, personal_info)
    if info != "":
        tips.append("Do not use personal info like name, DOB or pet name (found '" + info + "'). Hackers try these first!")
        bad_choice = True
    else:
        score += 1

    # 9. common names
    name = find_common_name(password)
    if name != "":
        tips.append("Do not use common names (found '" + name + "').")
        bad_choice = True
    else:
        score += 1

    # 10. keyboard clusters
    cluster = find_keyboard_cluster(password)
    if cluster != "":
        tips.append("Avoid keyboard clusters like qwerty or asdf (found '" + cluster + "').")
    else:
        score += 1

    # 11. common numbers and years
    number = find_common_number(password)
    year = has_year(password)
    if number != "":
        tips.append("Avoid common number clusters like 123456 or 000000 (found '" + number + "').")
    elif year != "":
        tips.append("Avoid years like birth years (found '" + year + "').")
    else:
        score += 1

    # 12. unique password
    if password in old_passwords:
        tips.append("You already used this password here. Use a different one for each account.")
    else:
        score += 1
        old_passwords.append(password)

    # decide the rating
    if bad_choice or score <= 6:
        rating = "WEAK"
    elif score == total:
        rating = "STRONG"
    else:
        rating = "MEDIUM"

    return rating, score, total, tips, phrase


def line(char="-", size=56):
    print(char * size)


def show_banner():
    line("=")
    print("*" * 56)
    print("*" + "PASSWORD STRENGTH CHECKER".center(54) + "*")
    print("*" + "Made by Girdhar".center(54) + "*")
    print("*" * 56)
    line("=")


def show_safety_rules():
    print("\n+" + "-" * 54 + "+")
    print("|" + "  [!] SECURITY RULES - READ BEFORE YOU START".ljust(54) + "|")
    print("+" + "-" * 54 + "+")
    print("|" + "  DO NOT put these in your password:".ljust(54) + "|")
    print("|" + "    x Your name or nickname".ljust(54) + "|")
    print("|" + "    x Date of birth (DOB) or birth year".ljust(54) + "|")
    print("|" + "    x Address, phone number or city".ljust(54) + "|")
    print("|" + "    x Pet name or family names".ljust(54) + "|")
    print("|" + "    x Social media details".ljust(54) + "|")
    print("|" + "  Hackers try this personal info FIRST!".ljust(54) + "|")
    print("+" + "-" * 54 + "+")


def show_result(rating, score, total, tips, phrase):
    print()
    line("=")
    print("  RESULT  >>  " + rating + "   (" + str(score) + "/" + str(total) + " checks passed)")
    line("=")

    if phrase:
        print("  [+] Nice! This is a passphrase, easy to remember and strong.")

    if len(tips) > 0:
        print("  How to improve your password:")
        line("-")
        for tip in tips:
            print("   [!]", tip)
        line("-")
    else:
        print("  [+] Great! Your password is strong.")

    print("  Reminder: never use your name, DOB or other personal")
    print("  details, and use a different password for each account.")
    line("=")


def main():
    show_banner()
    show_safety_rules()
    print("\n  Tip: 4 to 7 random words together make a strong passphrase.")

    print()
    line("-")
    personal_info = input("Enter your name, DOB, pet name etc. (separate with commas)\n"
                          "so I can check they are NOT in your password\n"
                          "(or press Enter to skip): ")
    line("-")

    while True:
        password = input("\n>> Enter a password (or type q to quit): ")

        if password == "q":
            print("\n  Goodbye! Stay safe online.")
            line("=")
            break
        if password == "":
            print("  Password cannot be empty.")
            continue

        rating, score, total, tips, phrase = check_password(password, personal_info)
        show_result(rating, score, total, tips, phrase)


main()
