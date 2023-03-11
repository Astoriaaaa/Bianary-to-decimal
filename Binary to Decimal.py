#bianary to decimal
bianary_digit = (input( ))
bd = bianary_digit[::-1]
sum = 0 
for i in range(len(bd)):  
    if bd[i] == "0": 
        pass
    elif bd[i] == "1": 
        sum = sum + (2 ** i)
print(sum) 

#decimal to bianary
bianary = " "
number = int(input( ))
num = number
while num > 0.5: 
    num = number / 2
    if num % 1 == 0: 
        bianary += "0"
        number = num 
    elif num % 0.5 == 0: 
        bianary += "1"
        number = number // 2
print(bianary[::-1])





    



        


