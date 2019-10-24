apetece_helado_input = input("te apetece un helado? (si/no): ").upper()
tiene_dinero_input = input("tienes dinero para un helado? (si/no): ").upper()
incorrecto = False
incorrecto2 = False
apetece_helado = None
tiene_dinero = None

if apetece_helado_input  == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    incorrecto = True

if tiene_dinero_input == "SI":
    tiene_dinero = True
elif tiene_dinero_input == "NO":
    tiene_dinero = False
else:
    incorrecto2 = True

while incorrecto == True and incorrecto2 == True:
    print("solamente si o no")
    apetece_helado_input = input("te apetece un helado? (si/no): ").upper()
    tiene_dinero_input = input("tienes dinero para un helado? (si/no): ").upper()
    if apetece_helado_input == "SI":
        apetece_helado = True
        incorrecto = False
    elif apetece_helado_input == "NO":
        apetece_helado = False
        incorrecto = False
    else:
        incorrecto = True
    if tiene_dinero_input == "SI":
        tiene_dinero = True
        incorrecto = False
    elif tiene_dinero_input == "NO":
        tiene_dinero = False
        incorrecto = False
    else:
        incorrecto2 = True

if apetece_helado and tiene_dinero:
    print("pues comete un helado")
elif apetece_helado == False and tiene_dinero == True:
    print("comprate otra cosa")
elif apetece_helado == True and tiene_dinero == False:
    print("Que triste")
elif apetece_helado == False and tiene_dinero == False:
    print("pues llegale")