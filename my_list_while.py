
my_list = []

input_user = input("what do you need to buy? (whrite end, when you want to end):")

while input_user != "END":
    my_list.append(input_user)
    input_user = input("what do you need to buy? (whrite end, when you want to end): ")

largue_list = len(my_list)
indice_actual = 0

while indice_actual < largue_list:
    print("I have to buy {}".format(my_list[indice_actual]))
    indice_actual += 1

print("these is the list of the market")