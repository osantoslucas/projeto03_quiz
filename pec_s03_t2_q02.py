print('''QUE PAÍS FOI DESCOBERTO EM 1500 PELOS PORTUGUESES?
[1] ALEMANHA
[2] PORTUGAL
[3] ESTADOS UNIDOS
[4] BRASIL''')
ano = int(input())
score = 0
if ano == 4:
    score += 1
    print(f'Parabéns!!! Você acertou. Sua pontuação é de {score} ponto(s).')
elif ano == 1:
    print(f'Nessa época Martinho Lutero já estudava na Universidade Alemã de Erfurt. Sua pontuação é de {score} ponto(s).')
elif ano == 2:
    print(f'Portugal já era um país bem evoluído e poderoso então ele não poderia se descobrir, não é? Sua pontuação '
          f'é de {score} ponto(s).')
elif ano == 3:
    print(f'O país norte americano foi descoberto em 12 de outubro de 1492. Sua pontuação é de {score} ponto(s).')
else:
    print(f'Você não escolheu nenhuma das opções. tente novamente. Sua pontuação é de {score} ponto(s).')
