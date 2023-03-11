#bianary to decimal
decision = int(input("Type '1' if you want to convert decimal to binary. Type '2' if you want to convert binary to decimal ")) 
if decision == 2:
    bianary_digit = (input("Input bianary number "))
    bd = bianary_digit[::-1]
    sum = 0 
    for i in range(len(bd)):  
        if bd[i] == "0": 
            pass
        elif bd[i] == "1": 
            sum = sum + (2 ** i)
    print("Your decimal digit is", sum) 

elif decision == 1:
    bianary = " "
    number = int(input("input decimal number " ))
    num = number
    while num > 0.5: 
        num = number / 2
        if num % 1 == 0: 
            bianary += "0"
            number = num 
        elif num % 0.5 == 0: 
            bianary += "1"
            number = number // 2
    print("Your bianary digit it", bianary[::-1])





    



        


