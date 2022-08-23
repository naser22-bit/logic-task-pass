# Initialize function to remove character from string
def rem_chaar(x,y):
    # initialize an empty string
    new_s = "" 
    for i  in x:
        if i != y:
            new_s = new_s + i
        
    return new_s


s = list(input("Enter your String: "))
print('*********************')
print('Enter The Character That You Want to Remove:')
ch = input()
# Calling the function to given string and character
result_str = rem_chaar(s,ch)
print(result_str)






    
   







