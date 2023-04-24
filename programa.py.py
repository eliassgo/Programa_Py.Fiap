#Nome: Elias Gomes De Oliveira Junior
#RM: 552381

#solicitar ao usuário o tempo, em anos, que ele fuma
tempo = float(input("Quanto tempo, em anos, você fuma? "))
#valor do maço de cigarro
valorM = float(input("Qual o valor do maço de cigarro que você fuma? "))
#Quantidade média de maços de cigarros que ele fuma por dia
quantM = float(input("Qual a média de cigarros que você fuma por dia? "))
#efetuar o cáculo do montante gasto em cigarros
montante = tempo * valorM * quantM * 360

if montante > 50000:
    print(f"Com o valor R$ {montante:.2f}, você poderia ter comprado um carro zero")
elif 20000 <= montante <= 50000:
    print(f"Com o valor R$ {montante:.2f}, você poderia ter comprado um carro popular usado")
else:
    print(f"Com o valor R$ {montante:.2f}, você poderia ter dado entrada em um carro")

