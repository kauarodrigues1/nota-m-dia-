notaMedia = int(input('Qual a sua média? '))
presenca = int(input('Qual a sua presença? '))
 
if notaMedia > 90 and presenca > 90:
    print('Você esta habilitado para fazer mestrado!')
 
elif notaMedia > 90 and (80 < presenca <90):
    print('Você deverá fazer uma prova prática!')
 
elif notaMedia > 90 and (70 < presenca < 80):
    print('Você deverá fazer uma prova prática e uma prova de inglês!')
 
elif notaMedia >90 and presenca <70:
    print('Você não poderá realizar o mestrado.')
 
elif notaMedia <90 and presenca >90:
    print('O aluno podera conversar com um orientador')