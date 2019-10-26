<<<<<<< HEAD
what_number_input = int(input("what number do you want to someone guess?"))
what_number_input2 = what_number_input
user_number_input = int(input("what number is that your body try to hide?"))

if user_number_input == what_number_input:
    user_number_input = True
else:
    user_number_input = False

while user_number_input == False:
    print("try again")
    try_again = int(input("what number is that your body try to hide?"))
    if try_again == what_number_input2:
        user_number_input = True

=======
what_number_input = int(input("what number do you want to someone guess?"))
what_number_input2 = what_number_input
user_number_input = int(input("what number is that your body try to hide?"))

if user_number_input == what_number_input:
    user_number_input = True
else:
    user_number_input = False

while user_number_input == False:
    print("try again")
    try_again = int(input("what number is that your body try to hide?"))
    if try_again == what_number_input2:
        user_number_input = True

>>>>>>> poniendo el archivo test
print("you win")