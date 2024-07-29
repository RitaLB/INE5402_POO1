'''Faça um programa que leia algo pelo teclado
e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele'''
info1= input("digite algo")
print("info1 é: {}".format(info1))
print("A classe da info 1 é", type(info1))
print("info1 é um número inteiro?", info1 .isnumeric() )
print ("info1 é compostosó de letras?",info1 .isalpha())

