from Tableaux import *

# > implicacao
# !	negacao
# | ou
# & e
#Fomulas Notavel de teste

main_branch = [FormulaDeEntrada(1, '(a>(c|d))'),FormulaDeEntrada(1, "(b>(c|d))"),FormulaDeEntrada(1,"(c>(e|f))"),FormulaDeEntrada(1,"(d>(e|f))"),FormulaDeEntrada(-1,"(e|f)"),FormulaDeEntrada(1,"(a|b)")]
main_branch = [FormulaDeEntrada(1,"(c>d)"),FormulaDeEntrada(1,"c"),FormulaDeEntrada(-1,"d")]
run(main_branch)
#lista de nos fechados
#Pilha de ramos