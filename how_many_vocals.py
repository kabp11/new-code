insert_phrase= input("INSERT THE TEXT THAT YOU WHANT TO NOW HOW MUCH VOCALS HAVE")

dot_n = 0
comas_n = 0
spaces_n = 0

list_dots_and_comas = [["."], [","], [" "]]

for letter in insert_phrase:
    if letter in list_dots_and_comas[0]:
        dot_n += 1
    elif letter in list_dots_and_comas[1]:
        comas_n += 1
    elif letter in list_dots_and_comas[2]:
        spaces_n += 1

print("your phrase have {} dots".format(dot_n))
print("your phrase have {} comas".format(comas_n))
print("your phrase have {} spaces".format(spaces_n))