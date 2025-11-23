soma=0
for pares in range(1,7):
    num=int(input('Digite aqui um número inteiro:'))
    if num%2==0:
        soma+=num
print(f'A soma dos números que são só pares são {soma}')


'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
pares.Se o valor digitado for ímpar, desconsidere-o'''