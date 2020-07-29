# PROGRAMMING ASSIGNMENT 05
# Filename: 'exercise2.py'
#
# Write the code for function valid_password.
# The function valid_password:
#   • takes 1 parameter pwd -> type str: password
#   • displays a message (depending on password rules (see the pdf))
#   • returns if the password is valid -> type bool
#
# see the rules in the pdf file
#

def main():
    #try to check some passords
    print('Calling: valid_password(\'qwertyuiop\')')
    r = valid_password('qwertyuiop') #also catch the returned value
    print(r) #print the returned value
    
    #empty line
    print()
    
    print('Calling: valid_password(\'ICPSpring2019\')')
    r = valid_password('ICPSpring2019') #also catch the returned value
    print(r) #print the returned value
    
    #empty line
    print()
    
    print('Calling: valid_password(\'pwd!!!\')')
    r = valid_password('pwd!!!') #also catch the returned value
    print(r) #print the returned value
    
    #empty line
    print()
    
    print('Calling: valid_password(\'PWD01_#PWD01\')')
    r = valid_password('PWD01_#PWD01') #also catch the returned value
    print(r) #print the returned value


def valid_password(pwd):
    #WRITE YOUR CODE HERE
    
    


#Call the main() function
main()
