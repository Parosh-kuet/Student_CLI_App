import math


def valid_name(name):
    # name = name.strip()
    return name != "" and not any(char.isdigit() for char in name)


while True:
    s_name = input("Enter Student Name: ").lower().title().strip()
    if valid_name(s_name):
        break
    else:
        print("Enter a valid name.")


def valid_roll(roll):
    return roll.isdigit() and int(roll) > 0


while True:
    s_roll = input("Enter student roll:").strip()
    if valid_roll(s_roll):
        s_roll = int(s_roll)
        break
    else:
        print("Enter a non zero ,positive and valid roll.")


def valid_sn(sn):
    return sn.isdigit() and int(sn) > 0


while True:
    sn = input("How many subjects:").strip()
    if valid_sn(sn):
        sn = int(sn)
        break
    else:
        print("Enter a valid sbuject number.")


def valid_sub_num(n):
    return n.isdigit() and 100 >= int(n) > 0


sub = {}
for i in range(sn):
    while True:
        num = input(f"Enter subject {i+1} number:")
        if valid_sub_num(num):
            num = int(num)
            sub[f"Subject{i+1}"] = num
            break
        else:
            print("Enter a valid sub number:")
max = sn*100
total = 0
for key in sub:
    total += sub[key]
avg = round(total/sn, 2)
Percentage = round((total/max)*100, 2)
print(total)
print(Percentage)


def grade(av):
    if av >= 80:
        return "A"
    elif av >= 70:
        return "B"
    elif av >= 60:
        return "C"
    elif av >= 50:
        return "D"
    elif av >= 0:
        return "F"


GPA = grade(avg)

Student_info = {
    s_name: {
        'Name': s_name,
        'Roll': s_roll,
        'Grade': GPA,
        'Total Marks': total,
        'Percentage': Percentage


    }
}
print(Student_info)
