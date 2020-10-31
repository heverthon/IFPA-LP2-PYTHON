destino = input('Onde você deseja ir?')
dias= input("Quantos dias")
money = int( input("Quanto você tem?"))

interior= "Itupiranga"
capital ="Brasilia"
top="Paris"

if money < 100:
    print("Vixe! com esse dinheiro não dá pra chegar em/na {}, no máximo você chega em {} e talvez nem dê pra voltar ".format(destino,interior))

elif money >500:
    print ("Bem ainda não está TOP TOP!! Você não poderá ir para {} mas pode ir até {}!!! Tô indo embora to pra {} Neste país lugar melhor não há...".format(top,capital,capital))
