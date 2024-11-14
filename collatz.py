num = 2
steps = 0

if num > 0:
    while num != 1:
        steps +=1
        if num%2 == 0:
            num //=2
            print(num)
        else:
             num = 3 * num + 1
             print(num)
    else:
        num+=1
else:
    print("Error")
print("Steps:",steps)
