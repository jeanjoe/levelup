vip_file = open("files/vip_list.txt", "r")
ordinary_file = open("files/ordinary_list.txt", "r")

name = input("Enter your name: \t")

vip_names = []
ordinary_names = []

for line in vip_file:
    vip_names.append(line)
    if line.find(name) != -1:
        print(line)

for line in ordinary_file:
    ordinary_names.append(line)
    if line.find(name) != -1:
        print(line)
