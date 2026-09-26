numbers = [10, 25, 30, 45, 50]
target = 30

for x in numbers:
    found = False
    if  x == target:
        found = True
        break

if found == True:
    print("Found")
else:
    print("not found")