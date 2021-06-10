# Create a list consisting of first 10 even numbers.
num= int(input("Please enter a number : "))
even_list = []
print (num)
i=1
while i<num+1:
    if i % 2 == 0:
        
        even_list.append(i)
        
    i += 1
    
print (even_list)
