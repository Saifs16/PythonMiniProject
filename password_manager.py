from cryptography.fernet import Fernet

'''
#Generating an encryption key
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

#Running the encryption key, only run once!
write_key()'''

def  load_key():# Below is loading the encyption 
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key
#master password doesn't really do anything at the moment
#manster_pwd = input("What is the master password? ")
key = load_key() #+ manster_pwd.encode()
fer = Fernet(key)

def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            #print(line.rstrip()) rstrip removes \n from string
            #inserting the values without the new line (\n) into an object
            data = line.rstrip()
            #spliting the vaules from data(which is the text from the file) and dividing the vaules where ever there is a |
            user, passw = data.split("|")
            # printing the text in organized fashion
            print("User:",user,"\nPassword:",fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    # the command below open a file and closes it on it's own
    #modes w write overrides, r read, a append adds text at the end (plus creates a file if it doesn't exist)
    with open('passwords.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

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