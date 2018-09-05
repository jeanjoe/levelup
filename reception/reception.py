
#Search name from list and return fullname
def registration_checker(name, data):
    #Search name and return fullname else do nothing
    for fname in data:
        if fname.lower().find(name.lower()) != -1:
            return fname.rstrip("\n")
    #return fullname variable
    return None

if __name__ == "__main__":
    #Read files
    vip_file = open("./reception/vip_list.txt", "r")
    ordinary_file = open("./reception/ordinary_list.txt", "r")

    #Store names to Lists List comprehension
    vip_names = [line for line in vip_file]
    ordinary_names = [line for line in ordinary_file]

    #make app run continiously
    while True:
        #Prompt for user single name
        input_name = input("Enter your name: ")

        #search name in VIP if no match search in Oridary 
        vip_checker = registration_checker(input_name, vip_names)
        if  vip_checker == None:

            #Search in Ordinary
            ordinary_checker = registration_checker(input_name, ordinary_names)
            if ordinary_checker == None:
                #If no Match visitor is not registered
                print("Not Registered")
            else:
                #Visitor is Ordinary
                print(ordinary_checker + " - ORDINARY")
        else:
            #visitor is VIP
            print(vip_checker + " - VIP")