'''
Faça um programa que pergunte o valor da conta a ser paga no restaurante. O programa deve apresentar como resposta o valor da conta com o acréscimo de 10% do garçom.
'''

valorbruto = float(input("Quanto que foi a conta do restaurante?"))
valortotal = valorbruto + valorbruto * (10/100)

print("O valor total com o acréscimo do garçom é:",valortotal,"Reais")