#take the input from the keyboard and split the words into a list and store in user_input variable
user_input = input().split()
#intialize the acrynom to a empty string 
acrynom=""
#now iterate to the list of user_input
for i in user_input:
    #now concatinate the first letter of each word in a string
    #convert the string to uppercase
    acrynom += str(i[0]).upper()
#print the acrynom
print(acrynom)
