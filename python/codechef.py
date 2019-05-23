# varible p1
# varible p2
# varible  X
# variable t
#
# input(x)



alien = {'color': 'green', 'points': 5}

print("The alien's color is " + alien['color'])
fav_numbers = {'eric': 17, 'ever': 4}
for name, number in fav_numbers.items():
        print(name + ' loves ' + str(number))
print(fav_numbers.items())
for name,number in fav_numbers.items():
    print(name)
# fav_numbers = {'eric': 17, 'ever': 4}
for name in fav_numbers.keys():
    print(name + 'loves a number')
for num in fav_numbers.values():
    print(num)


t=input()
for test_i in range t:                 #test_i is the test input
    p1=input()
    p2=input()
    x=input()

for test_o in range test_i:
    if ((p1+p2)%4==0 or (p1+p2)%4==1):
        print("CHEFF")
    else:
        prnt("COOK")
