#Prova input e concatenazione stringhe

quantity = int(input('quantity '))
price = float(input('price '))

total = quantity*price
print('total ', total)



#Print hello user

name = input("Digita il tuo nome: ")
print("Ciao %s" % (name))



name = "Francesco"
name2 = "Attilio"
quant = 6.998
print("Benvenuti %s e %s, entrate pure se avete mangiato %.2f biscotti" % (name, name2, quant))