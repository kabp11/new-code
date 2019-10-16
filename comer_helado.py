apetece_helado_input = input("te apetece un helado? (si/no): ").upper()
tiene_dinero_input = input("tienes dinero para un helado? (si/no): ").upper()

if apetece_helado_input  == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
    print("que aburrido")
else:
    print("solo quiero saber si o no")

apetece_helado = apetece_helado_input =="SI"
tiene_dinero = tiene_dinero_input =="SI"

if tiene_dinero_input  == "SI":
    tiene_dinero = True
elif tiene_dinero_input == "NO":
    tiene_dinero = False
    print("que triste")
else:
    print("solo quiero saber si o no")


if apetece_helado and tiene_dinero :
    print("pues comete un helado")
elif apetece_helado == False and tiene_dinero == True:
    print("comprate otra cosa")