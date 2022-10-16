with open('PatientNames.txt') as f:
    line = f.readline()

names = eval(line)
seenNames = set()
digits = '0987654321'

names = []
for name in names:
    names.append(name[-2])

def name_check(name_list):
    lst = set()
    for n in name_list:
        if name_list[n] in lst:
            return False
        lst.add(name_list[n])
    return True
print(name_check(names))