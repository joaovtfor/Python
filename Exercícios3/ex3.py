nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
par = 0
imp = 0

for num in nums:
    if num % 2 == 0:
        par += 1
    else:
        imp += 1

print(f"A lista contém {par} números pares e {imp} números ímpares")