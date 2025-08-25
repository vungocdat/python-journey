# ask for age
print('How old are you?')
age = input()

if age:
    if int(age) >= 18 and int(age) < 21:
        # 18-21 wristbrand
        print('You can enter, but you need a wristbrand!')
    elif int(age) >= 21:
        # 21+ drink, normal entry
        print('You are good to enter and can drink!')
    else:
        # too you, sorry
        print('You cannot enter. You are too young.')
else:
    print('Please enter an age!')
