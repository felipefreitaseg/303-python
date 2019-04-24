print('Detetive')
print('Responda as perguntas abaixo com S(sim) ou N(nao): ')

perguntas = ('Voce telefonou para a vitima?',
             'Voce esteve no local do crime?',
             'Voce era vizinha da vitima?',
             'Voce tinha crush na vitima?',
             'Voce devia dinheiros para vitima?')

respostas = []

for pergunta in perguntas:
    respostas.append(input(pergunta).upper())

tipo = 0
for resposta in respostas:
    if resposta == 'S':
        tipo += 1
if tipo < 2:
    print ('inocente')
elif tipo == 2:
    print ('acho que voce matou')
elif tipo <= 4:
    print ('voce deve ter participado do assassinato')
else:
    print ('voce é o mordomo entao voce matou')