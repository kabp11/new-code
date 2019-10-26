number_user = []
number_of_user = ""


while len(number_user) <5:
    while not number_of_user.isdigit():
        number_of_user = input("say a number")
    number_user.append(int(number_of_user))
    number_of_user = ""
    print("number added")

number_the_most_bigger = number_user[0]

for number in number_user:
    if number > number_the_most_bigger:
        number_the_most_bigger = number

print("the number most bigger is {}".format(number_the_most_bigger))