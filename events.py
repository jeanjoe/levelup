vip_file = open("files/vip_list.txt", "r")
ordinary_file = open("files/ordinary_list.txt", "r")

vip_names = []
ordinary_names = []

for line in vip_file:
    vip_names.append(line)

for line in ordinary_file:
    ordinary_names.append(line)

print(vip_names[2])
print(ordinary_names[0])