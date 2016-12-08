print (" FEITO PELO ALFA")
nome = raw_input("\nNome do aluno: ")
nota1 = input("nota prova 1: ")
nota2 = input("nota prova 2: ")
nota3 = input("nota prova 3: ")
nota4 = input("nota prova 4: ")

media = (nota1 + nota2 + nota3 + nota4)/4.0
nota_final = media > 5 <7
if  media >= 7:
  print (" Aluno(a)-> " +str(nome)+"| Sua Media-> "+str(media)+"|Aprovado")
 
elif nota_final:
  print (" Aluno(a)-> " +str(nome)+"| Sua Media-> "+str(media)+"|Prova Final")
else:
  print (" Aluno(a)-> " +str(nome)+"| Sua Media-> "+str(media)+"|reprovado")