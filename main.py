#Pyhton 3
from Tableaux import *

# > implicacao
# !	negacao
# | ou
# & e
#Fomulas Notavel de teste

main_branch = [(1,"(a|b)"),(1, '(a>(c|d))'),(1, "(b>(c|d))"),(1,"(c>(e|f))"),(1,"(d>(e|f))"),(-1,"(e|f)")]
#main_branch = [(-1,"(c>(!(c)|d))")]
run(main_branch)
#lista de nos fechados
#Pilha de ramos