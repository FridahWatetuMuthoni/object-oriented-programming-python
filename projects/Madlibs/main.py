your_name = input('Enter Your name?')

try:
    if(your_name):
        print(f"Your name is {your_name}")
    else:
        print('Name can not be empty')

except:
    print('Something went wrong')