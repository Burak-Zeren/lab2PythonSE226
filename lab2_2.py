number=int(input("Please enter between 3 and 9 (inclusive) : "))
for i in range(1, number+1):
    if i == number:
        print('*' * i + f" {number} stars")
        break
    print('*' * i)

for j in range(number - 1, 0,-1):
            print('*' * j)