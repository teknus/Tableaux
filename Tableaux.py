operadores = [">","|","&","!"]
# -1 False
# 1 True

def split_form(input_tuple):
    stack_form = list()
    temp_stack = list()
    op_stack = list()
    last = None
    input_string = input_tuple[1]
    i = 0
    n = len(input_string)
    if n == 3:
        return 1, input_tuple[0]
    while i < n:
        if input_string[i] in operadores:
            op_stack.append(i)
        if input_string[i] == "(":
            temp_stack.append(i)
        if input_string[i] == ")":
            stack_form.append(op_stack[-1])
            op_stack.pop()
        i += 1
    return list(reversed(stack_form))[0],input_tuple[0]

def is_alpha(value, op):
    if op in ["|" ,"!" ,">",""] and value -1:
        return True
    elif value == 1 and op in ["&","!",""]:
        return True
    else:
        return False

def is_beta(value,op):
    if value == 1 and op in ["|",">"]:
        return True
    elif value == -1 and op == "&":
        return True
    else:
        return False
def format_formula(i,form):
    #           valoração,operador,formula esquerda, formula direita
    if len(form[1]) == 3:
        return [i[1],"",form[1][1],""]
    if form[1][i[0]] == "!":
        return [i[1],form[1][i[0]],form[1][:i[0]][1:],form[1][i[0]+2:][:-1]]
    return [i[1],form[1][i[0]],form[1][:i[0]][1:],form[1][i[0]+1:][:-1]]


def expand_formula(form):
    value = form[0]
    op = form[1]
    left = form[2]
    right = form[3]
    if is_alpha(value, op):
        if op == "&":
            return [1,left],[1,right]
        elif op == "|":
            return [-1,left],[-1,right]
        elif op == ">":
            return [1,left],[-1,right]
        elif op == "!":
            return [value * -1, right]
    elif is_beta(value, op):
        if op == "&":
            return [-1,left],[-1,right]
        elif op == "|":
            return [1,left],[1,right]
        elif op == ">":
            return [-1,left],[1,right]

def ramo_fechado(main_branch):
    uni = [x for x in main_branch if len(x) == 2]
    for i in uni:
        for j in uni:
            if i[0] * -1 == j[0] and i[1] == j[1]:
                return True
    return False

def ramo_saturado(nos_fechados,form):
    i = len(form)
    while i > -1:
        if i not in nos_fechados:
            return False
        i -= 1
    return True

def expndir_alphas(main_branch,nos_fechados,form):
    i = 0
    while i < len(main_branch):
        if i not in nos_fechados:
            if not ramo_saturado(nos_fechados, main_branch):
                if is_alpha(main_branch[i][0], main_branch[i][1]) and not is_beta(main_branch[i][0], main_branch[i][1]):
                    try:
                        a1,a2=expand_formula(main_branch[i])
                        main_branch.append(a1)
                        main_branch.append(a2)
                        nos_fechados.add(i)
                    except TypeError:
                        main_branch.append([main_branch[i][0],main_branch[i][2]])
                        nos_fechados.add(i)
        i += 1

def expandir_betas(main_branch,nos_fechados,form):
    i = 0
    while i < len(main_branch):
        if not ramo_saturado(nos_fechados, main_branch):
            if i not in nos_fechados:
                if is_beta(main_branch[i][0], main_branch[i][1]):
                    beta1, beta2 = expand_formula(main_branch[i])
                    nos_fechados.add(i)
                    main_branch.append(beta1)
                    pilha_ramos.append((i, main_branch[:]))
                    if solve(main_branch,nos_fechados,form):
                        pilha_ramos.pop()
                    main_branch.append(beta2)
                    pilha_ramos.append((i, beta1, main_branch[:]))
                    if solve(main_branch,nos_fechados,form):
                        pilha_ramos.pop()
                else:
                    nos_fechados.add(i)
        i += 1


def solve(main_branch,nos_fechados,form):
    expndir_alphas(main_branch,nos_fechados,form)
    if not ramo_saturado(main_branch,nos_fechados):
        expandir_betas(main_branch,nos_fechados,form)
    if ramo_fechado(main_branch):
        return True
    return False

#Fomulas teste
form = [[-1,"(c|h)"],[-1,"(c>b)"]]
#Deixando as Formulas com o fomato que pode ser processado
form = [format_formula(split_form(x),x) for x in form]
print(form)
#Criando um vetor de betas não sei como usar ainda
betas = [-1 for x in range(0,sum([len(x[2])+len(x[3])+1 for x in form]))]
#Criando ramo principal do tableaux
main_branch = list()
#adicionar fomulas reformatadas no ramo principal
main_branch += form
#lista de nos fechados
nos_fechados = set()
#Pilha de ramos
pilha_ramos = list()
###################################################################################################################
if solve(main_branch,nos_fechados,form):
    print(nos_fechados, main_branch)
else:
    print(nos_fechados, pilha_ramos)
#form_2 = [expand_formula(y) for y in form if is_alpha(y[0],y[1])]
