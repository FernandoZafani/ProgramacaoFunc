a=10

while a>10 :
    print(a)
    a=a-1

for x in range(1,11):
    for y in range(1,11):
        print(f'{x} * {y} = {x * y}')

print('--')

dias_semana = ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sabado']

for dia in dias_semana:
    print(f'Hoje é {dia}')

    print('--')

lista_pessoas = [{'id' : 1,'nome' : 'Andre', 'idade' : '35','altura' : 1.83, 'cursos': ['C#','Python','Node']},
                {'id' : 2,'nome' : 'Ana', 'idade' : '22','altura' : 1.57, 'cursos': ['C#','Python','Node','C++']},
                {'id' : 3,'nome' : 'João', 'idade' : '39','altura' : 1.78, 'cursos': ['Python','Node']},
                {'id' : 4,'nome' : 'Bia', 'idade' : '27','altura' : 1.63, 'cursos': ['C#','Java','React']}]

for pessoa in lista_pessoas:
    for curso in pessoa['cursos']:
        nome=pessoa['nome']
        print(f'A pessoa {nome} faz o curso {curso}')

