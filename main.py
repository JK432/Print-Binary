number = int(input())

result = "" 
while number != 0:
    remainder = number % 2 
    number = number // 2
    result = str(remainder) + result
print(result)
    
