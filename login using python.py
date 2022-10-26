def register():
    db = open("access_register.txt", "r")
    a = input("Create your username in format __@__.__: ")
    d = []
    for line in db:
        x = line.split(",")
        d.append(x[0])

    if a in d:
        print("Try Again with different username")
        register()

    elif a.count('@') != 1 and a.count('.') != 1:
        print("Please enter the username in proper format")
        register()

    elif ((a.index('@')) - (a.index('.'))) == 1:
        print("Please enter the username in proper format")
        register()

    elif a[0] in range(0, 9):
        print("Start with characters only")
        register()

    elif (a[0] == '@' or a[0] == '$' or a[0] == '_' or a[0] == '%' or a[0] == '!' or a[0] == '#' or a[0] == '*' or a[
        0] == '&'):
        print("Username must start with characters not numbers")
        register()

    else:
        print("Username created")

    b = input("Enter your password with at least one capital letter, one number and one special character: ")
    s = False

    if len(b) < 5 and len(b) > 16:
        print("Password length should be between 5 and 16 characters, So please Try Again")
        register()

    if len(b) > 5 and len(b) < 16:
        l, u, p, d = 0, 0, 0, 0
        for i in b:
            if i.isdigit():
                d += 1
            if i.islower():
                l += 1
            if i.isupper():
                u += 1
            if (i == '@' or i == '$' or i == '_' or i == '%' or i == '!' or i == '#' or i == '*' or i == '&'):
                p += 1
            if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(b)):
                s = True

    if s:
        c = input("Confirm Password: ")
        while (c != b):
            print("Password not match, Try Again")
            c = input("Try Again: ")

    else:
        print("Try again")
        register()

    file = open("access_register.txt", "a")
    file.write(a + "," + b + "\n")
    file.close()
    login()

def login():
    X=input("Enter your username to login: ")
    X = X.strip()
    db = open("access_register.txt", "r")
    d = []
    for line in db:
        x = line.split(",")
        d.append(x[0])

    if X in d:
        Y=input("Please Enter your password: ")
        Y=Y.strip()
        file1=open("access_register.txt","r").readlines()
        for x in file1:
            x=x.strip()
            info=x.split(",")
            if X==info[0] and Y==info[1]:
                print("Login successful, Welcome")
            else:
                F = input("Forgot Password [Y/N] : ")

                if F == "N":
                    print("try")
                    login()

                if F == "Y":
                    b = input("Enter your password with at least one capital letter, one number and one special character: ")
                    s = False

                    if len(b) < 5 and len(b) > 16:
                        print("Password length should be between 5 and 16 characters, So please Try Again")
                        register()

                    if len(b) > 5 and len(b) < 16:
                        l, u, p, d = 0, 0, 0, 0
                        for i in b:
                            if i.isdigit():
                                d += 1
                            if i.islower():
                                l += 1
                            if i.isupper():
                                u += 1
                            if (
                                    i == '@' or i == '$' or i == '_' or i == '%' or i == '!' or i == '#' or i == '*' or i == '&'):
                                p += 1
                            if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(b)):
                                s = True

                    if s:
                        c = input("Confirm Password: ")
                        while (c != b):
                            print("Password not match, Try Again")
                            c = input("Try Again: ")

                    else:
                        print("Sorry,Try again to login")
                        login()

                    file = open("access_register.txt", "w")
                    file.write(X + "," + b + "\n")
                    file.close()

    else:
        print("User information not registered. So please register")
        register()

def welcome():
    print("WELCOME TO THE DIGITAL WORLD")
    print("Existing users should login and new users need to register before entering further")
    W=input("Login|Register[L/R]: ")
    if W=="L":
        login()
    elif W=="R":
        register()
    else:
        print("Enter L to login and R to register")
        welcome()
welcome()