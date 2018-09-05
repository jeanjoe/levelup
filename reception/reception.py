#Read files
vip_file = open("./reception/vip_list.txt", "r")
ordinary_file = open("./reception/ordinary_list.txt", "r")

vip_names = []
ordinary_names = []

#Store names to Lists
for line in vip_file:
    vip_names.append(line)

for line in ordinary_file:
    ordinary_names.append(line)

#Search name from list and return fullname
def registration_checker(name, data):

    #Default fullname is None if no Match
    full_name = None

    #Search name and return fullname else do nothing
    for fname in data:
        if fname.lower().find(name.lower()) != -1:
            full_name = fname.rstrip("\n")
    
    #return fullname variable
    return full_name

#make app run continiously
while True:

    #Prompt for user single name
    input_name = input("Enter your name: ")

    #search name in VIP if no match search in Oridary 
    if registration_checker(input_name, vip_names) == None:
        if registration_checker(input_name, ordinary_names) == None:
            #If no Match visitor is not registered
            print("Not Registered")
        else:
            #Visitor is Ordinary
            print(registration_checker(input_name, ordinary_names) + " - ORDINARY")
    else:
        #visitor is VIP
        print(registration_checker(input_name, vip_names) + " - VIP")
    
