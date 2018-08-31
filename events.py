vip_file = open("files/vip_list.txt", "r")
ordinary_file = open("files/ordinary_list.txt", "r")

vip_names = []
ordinary_names = []

for line in vip_file:
    vip_names.append(line)

for line in ordinary_file:
    ordinary_names.append(line)

def registration_checker(name, data):
    full_name = None
    for fname in data:
        if fname.lower().find(name.lower()) != -1:
            full_name = fname
    
    return full_name

while True:
    input_name = input("Enter your name: \t")

    if registration_checker(input_name, vip_names) == None:
        if registration_checker(input_name, ordinary_names) == None:
            print("No Name match")
        else:
            print(registration_checker(input_name, ordinary_names))
    else:
        print(registration_checker(input_name, vip_names))
    
