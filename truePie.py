


def calculation(n):
#The range function is used to calculate the ongoing example of 1/3, 1/5, 1/6 example
    pi,numerator = 0,4.0
    for i in range(n):
        denominator = (2*i+1)
        term = numerator/denominator
        if i%2: # the modulus operator divides and rounds to the nearest whole number
            pi -= term
        else:
            pi += term
    return(pi)
    

print("Hello, what is your name?")
name = input() 
print('\n')
print('\n')
print("Hello" + '  ' + name + '\n' + '\n'+ "That is a nice name.")
print('\n')
print("Would you like to solve a math problem by" + ' ' + name +"?")
print('\n')
print('\n')

number = input ("Enter number to solve for pie:" + '  ') 
 



print(calculation(int(number)))