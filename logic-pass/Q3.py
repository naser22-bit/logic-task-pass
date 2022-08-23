# Function to calculate the number of character that repeated in string
def get_num(Sttr, ch):
    count = 0     # Counter to calculate the repeated characters
    for i in range(len(Sttr)):
        if Sttr[i] == ch:
            count = count +1        # increase the counter
    return count

st = input("Enter the String:")
x = input("Enter the character that count the time of repeated in string: ")
result = print(get_num(st, x))


