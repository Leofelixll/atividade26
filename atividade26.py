# Exercício Python 26: Desenvolva um programa que leia o primeiro termo e a razão de uma Pogreçao Aritimetica.
# No final, mostre os 10 primeiros termos dessa progressão.

A1 = int(input("Digite o primero termo da PA: "))
R = int(input("Digite a razão da PA: "))

for n in range(10):
    print(n)
    termo = A1 + n * R
    print(f"termo {n+1}: {termo}")
    