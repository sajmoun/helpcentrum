
name = "Alice"
tel_num = 775665334

with open ('contacts.txt', "w") as f:
    f.write(f"{name}, {tel_num}\n")


s_name = "Alice"
with open ('contacts.txt', "r") as f:
    if s_name in f.read():
        print(f"{name} is in contacts!" )
    f.seek(0)
    print(f.read())