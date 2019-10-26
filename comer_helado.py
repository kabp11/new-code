apetece_helado_input = input("te apetece un helado? (si/no): ").upper()

if apetece_helado_input  == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
    print("que aburrido")
else:
    print("solo quiero saber si o no")

tiene_dinero_input = input("tienes dinero para un helado? (si/no): ").upper()

apetece_helado = apetece_helado_input =="SI"
tiene_dinero = tiene_dinero_input =="SI"

if apetece_helado and tiene_dinero :
    print("pues comete un helado")
if apetece_helado == "NO" and tiene_dinero == "SI":
    print("comprate otra cosa")
