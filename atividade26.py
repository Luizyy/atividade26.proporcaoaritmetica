# Exercício Python 26: Desenvolva um programa que leia o primeiro termo e a razão de uma Pogreçao Aritimetica.
# No final, mostre os 10 primeiros termos dessa progressão.

PT= int(input('Digite o primeiro termo da progreção aritimetica:'))
razao = int(input("Insira a razão da progreção aritimetica"))
for PA in range(10):
    print(PA)
    termo = PT + PA * razao
    print(f'Termo {PA+1}: {termo}')