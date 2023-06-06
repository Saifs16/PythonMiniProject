pwd = input("What is the master password? ")

def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:",user,"Password:",passw)


view()

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    # the command below open a file and closes it on it's own
    #modes w write, r read, a append
    with open('passwords.txt','a') as f:
        f.write(name + "|" + pwd + "\n")

while True:

    mode = input("Would you like to add a password or view exisiting one(view, add), press q to quit\n").lower()
    if mode =="q":
        pass
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. ")