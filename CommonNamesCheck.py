with open('PatientNames.txt') as f:
    line = f.readline()

names = eval(line)
seenNames = set()
digits = '0987654321'

for name in names:
    print(name[-2])

