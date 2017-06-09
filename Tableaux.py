operadores = [">","|","&","!"]
# -1 False
# 1 True
def is_alpha(value, op):
    if op in ["|" ,"!" ,">",""] and value == -1:
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

def ramo_saturado(nos_fechados,form):
    i = len(form)
    while i > -1:
        if i not in nos_fechados:
            return False
        i -= 1
    return True

def ramo_fechado(main_branch):
    uni = [x for x in main_branch if len(x) == 2]
    for i in uni:
        for j in uni:
            if i[0] * -1 == j[0] and i[1] == j[1]:
                return True
    return False


def solve(main_branch,nos_fechados):
    pass


def split_form(input_tuple):
    if len(input_tuple) == 2:
        input_string = input_tuple[1]
    else:
        input_string = input_tuple
    stack_form = list()
    temp_stack = list()
    op_stack = list()
    i = 0
    n = len(input_string)

    if n == 3 or n <= 1:
        return input_string
    while i < n:
        if input_string[i] in operadores:
            op_stack.append(i)
        if input_string[i] == "(":
            temp_stack.append(i)
        if input_string[i] == ")":
            stack_form.append(op_stack[-1])
            op_stack.pop()
        i += 1
    return list(reversed(stack_form))[0]

def format_formula(form):
    n = len(form)
    if n >= 2:
        posicao_op = split_form(form[1])
        op = form[1][posicao_op]
        if op == "!":
            return (form[0], op, form[1][1:posicao_op], form[1][posicao_op + 2:len(form[1]) - 1])
        return (form[0], op, form[1][1:posicao_op], form[1][posicao_op + 1:len(form[1]) - 1])
        #      ( valoração,operador,formula esquerda, formula direita)
    elif n == 1:
        posicao_op = split_form(form[0])
        if type(posicao_op) == type(tuple()):
            posicao_op = posicao_op[0]
        elif type(posicao_op) != type(0):
            return form
        op = form[0][posicao_op]
        if op == "!":
            return (form[0][posicao_op], form[0][1:posicao_op], form[0][posicao_op + 2:len(form[0]) - 1])
        return (form[0][posicao_op], form[0][1:posicao_op], form[0][posicao_op + 1:len(form[0]) - 1])
        #       ( valoração,operador,formula esquerda, formula direita)
    return form

#Fomulas teste
form = [[-1,'!((c>(b&(g|a))))']]
#Criando ramo principal do tableaux
main_branch = list()
#adicionar fomulas reformatadas no ramo principal
main_branch += form
#lista de nos fechados
nos_fechados = list()
#Pilha de ramos
pilha_ramos = list()
n = 0
###################################################################################################################
def expand_formula(value,form,alfa,expanded_formula):
    def atribuir_valores(val, form):
        if type(form) == type(list()) or type(form) == type(tuple()):
            return [val] + [x for x in form]
        return [val,form]
    if expanded_formula:
        if len(form) == 4:
            op = form[1]
            left = format_formula([form[2]])
            right = format_formula([form[3]])
        else:
            op = form[0]
            left = format_formula([form[1]])
            right = format_formula([form[2]])
    else:
        form = format_formula(form)
        if len(form) == 4:
            op = form[1]
            left = format_formula([form[2]])
            right = format_formula([form[3]])
        else:
            op = form[0]
            left = format_formula([form[1]])
            right = format_formula([form[2]])

    if alfa:
        if op == "&":
            return atribuir_valores(1,left),atribuir_valores(1,right)
        elif op == "|":
            return atribuir_valores(-1,left),atribuir_valores(-1,right)
        elif op == ">":
            return atribuir_valores(1,left),atribuir_valores(-1,right)
        elif op == "!":
            return atribuir_valores(value * -1, right)
    else:
        if op == "&":
            return atribuir_valores(-1,left),atribuir_valores(-1,right)
        elif op == "|":
            return atribuir_valores(1,left),atribuir_valores(1,right)
        elif op == ">":
            return atribuir_valores(-1,left),atribuir_valores(1,right)


posicao_op = split_form(form[0])
#print(form[0][0],form[0][1][posicao_op], form[0][1][1:posicao_op], form[0][1][posicao_op+1:len(form[0][1]) - 1])
main_branch.append(expand_formula(form[0][0],form[0],True,False))
f1, f2 = expand_formula(main_branch[-1][0],main_branch[-1],True,True)
main_branch.append(f1)
main_branch.append(f2)
f1, f2 = expand_formula(main_branch[-1][0],main_branch[-1],True,True)
main_branch.append(f1)
main_branch.append(f2)
f1, f2 = expand_formula(main_branch[-1][0],main_branch[-1],True,True)
main_branch.append(f1)
main_branch.append(f2)
print(main_branch)
print(ramo_fechado(main_branch))
'''
right = form[0][1][posicao_op+1:]
form = right[:len(right)-1]
posicao_op = split_form(form)
print(form[posicao_op], form[1:posicao_op], form[posicao_op+1:len(form) - 1])'''
