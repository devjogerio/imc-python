peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura * altura)

if imc < 22:
    print('Você está abaixo do peso')

if imc > 22:
    print('Você esta acima do peso')

print('Seu IMC é {}'.format(imc))
