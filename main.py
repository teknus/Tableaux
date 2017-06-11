from Tableaux import *


#Fomulas teste
form = [(-1,"(x>(a|!((c|b))))"),(-1, 'b'),(1, 'x'), (-1, 'a')]
#Criando ramo principal do tableaux
main_branch = list()
#adicionar fomulas reformatadas no ramo principal
main_branch += form
run(main_branch)
#lista de nos fechados
#Pilha de ramos