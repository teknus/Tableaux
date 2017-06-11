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
    for i in nos_fechados:
        if i != -1:
            True
    return False

def ramo_fechado(main_branch):
    uni = [x for x in main_branch if is_uni(x)]
    for i in uni:
        for j in uni:
            if i[0] * -1 == j[0] and i[1] == j[1]:
                return True
    return False


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

    if n == 3:
        return 1
    elif n <= 1:
        return 0
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
        op_pos = split_form(form)
        if len(form) == 2:
            if op_pos == 0:
                if len(form[1]) == 4:
                    return(form[0],form[1][op_pos],form[1][2:len(form[1]) -1 ],"")
                f = form[1][2:len(form[1]) - 1]
                return(form[0],form[1][0],f,"")
            if is_uni(form):
                return form
            return (form[0],form[1][op_pos],form[1][1:op_pos],form[1][op_pos+1:len(form[1]) -1])

        #       (operador,formula esquerda, formula direita)

def is_uni(form):
    if len(form) > 2:
        return False
    else:
        return len(form[1]) <= 1

def add_to_main(f1,f2,main_branch):
    if len(f1) >= 1 and f1 != "":
        main_branch.append(f1)
    if len(f2) >= 1 and f2 != "":
        main_branch.append(f2)


def solve(main_branch,nos_fechados,betas):
    #alfas
    i = 0
    n = len(main_branch)
    while i < n:
        if nos_fechados[i] == -1:
            if not is_uni(main_branch[i]):
                if len(main_branch[i]) != 4:
                    main_branch[i] = format_formula(main_branch[i])
                if len(main_branch[i][1]) > 1:
                    main_branch[i] = format_formula(main_branch[i])
                alfa = is_alpha(main_branch[i][0],main_branch[i][1])
                if alfa:
                    f1 , f2 = expand_formula(main_branch[i][0],main_branch[i][1],main_branch[i][2],main_branch[i][3],alfa)
                    add_to_main(f1,f2,main_branch)
                    nos_fechados[i] = 1
                else:
                    betas.append(i)
            else:
                temp = main_branch[i]
                j = i -1 
                while j > 0:
                    if is_uni(main_branch[j]):
                        if temp[0] * -1 == main_branch[j][0] and temp[1] == main_branch[j][1]:
                            #print("alfa",i,j,main_branch)
                            nos_fechados[i] = 1
                            nos_fechados[j] = 1
                    j -= 1    
        i += 1
        n = len(main_branch)
    #Betas
    while len(betas) > 0:
        i = betas[0]
        betas.remove(i)
        if not is_uni(main_branch[i]):
            if len(main_branch[i][1]) > 1:
                main_branch[i] = format_formula(main_branch[i])
            alfa = is_alpha(main_branch[i][0],main_branch[i][1])
            if not alfa:
                f1 , f2 = expand_formula(main_branch[i][0],main_branch[i][1],main_branch[i][2],main_branch[i][3],alfa)
                nos_fechados[i] = 1
                temp_main = main_branch[:]
                temp_nos_fechados = nos_fechados[:]
                ####################################
                test = False
                if len(f2[1]) > 1:
                    f2 = format_formula(f2)
                    g1,g2 = expand_formula(f2[0],f2[1],f2[2],f2[3],is_alpha(f2[0],f2[1]))
                    pilha_ramos.append((main_branch[:]+[f1],[g1],[g2],nos_fechados))
                    test = True
                else:
                    pilha_ramos.append((main_branch[:]+[f1],[f2],nos_fechados))

                f,ramo,n = solve(pilha_ramos[-1][0],nos_fechados,betas)
                print("f1",f,ramo,ramo_fechado(ramo),f2)
                if not f :
                    if test:
                        main_branch = ramo+[g1]+[g2]
                        return f, main_branch,n
                    main_branch = ramo+[f2]
                    return f,main_branch,n
                ######################################
                main_branch = temp_main[:]
                nos_fechados = temp_nos_fechados[:]
                test = False
                if len(f1[1]) > 1:
                    f1 = format_formula(f1)
                    g1,g2 = expand_formula(f1[0],f1[1],f1[2],f1[3],is_alpha(f1[0],f1[1]))
                    pilha_ramos.append((main_branch[:]+[f2],[g1],[g2],nos_fechados))
                    test = True
                else:
                    pilha_ramos.append((main_branch[:]+[f2],[f1],nos_fechados))

                f,ramo,n = solve(pilha_ramos[-1][0],nos_fechados,betas)
                print("f2",f,ramo,ramo_fechado(ramo),f1)

                if not f :
                    if test:
                        main_branch = ramo+[g1]+[g2]
                        return f, main_branch ,n
                    main_branch = ramo+[f1]
                    return f,main_branch,n
                ########################################
        else:
            temp = main_branch[i]
            j = i -1 
            while j > 0:
                if is_uni(main_branch[j]):
                    if temp[0] * -1 == main_branch[j][0] and temp[1] == main_branch[j][1]:
                        nos_fechados[i] = 1
                        nos_fechados[j] = 1
                j -= 1
    if len(pilha_ramos) == 0:
        return ramo_fechado(main_branch),main_branch,nos_fechados
    return ramo_fechado(pilha_ramos[-1][0]),main_branch,nos_fechados

def expand_formula(value,op,left,right,alfa):
    def atribuir_valores(val, form):
        if type(form) == type(list()) or type(form) == type(tuple()):
            return [val] + [x for x in form]
        return (val,form)
    if right == "":
        return "",atribuir_valores(value * -1, left)

    if alfa:
        if op == "&":
            return atribuir_valores(1,left),atribuir_valores(1,right)
        elif op == "|":
            return atribuir_valores(-1,left),atribuir_valores(-1,right)
        elif op == ">":
            return atribuir_valores(1,left),atribuir_valores(-1,right)
    else:
        if op == "&":
            return atribuir_valores(-1,left),atribuir_valores(-1,right)
        elif op == "|":
            return atribuir_valores(1,left),atribuir_valores(1,right)
        elif op == ">":
            return atribuir_valores(-1,left),atribuir_valores(1,right)

def numero_nos(main_branch):
    t = ""
    for s in [x[1] for x in main_branch]:
        t += s
    return sum([1 for y in t if y != "(" and y != ")"])

##############################################################################

#Fomulas teste
form = [(-1,"(x>(a|!((c|b))))"),(-1, 'b'),(1, 'x'), (-1, 'a')]
#Criando ramo principal do tableaux
main_branch = list()
#adicionar fomulas reformatadas no ramo principal
main_branch += form
#lista de nos fechados
nos_fechados = [-1 for x in range(0,numero_nos(main_branch))]
#Pilha de ramos
pilha_ramos = list()
n = 0
betas = list()
betas = list()
v,m,n = solve(main_branch,nos_fechados,betas)
if v:
    print("Valida")
    print("Main: ",main_branch)
    print("Pilha: ",list(set([ x for x in pilha_ramos[-1][0] if is_uni(x)])))
elif len(pilha_ramos) > 1:
    print("Refutada")
    print("Valoracao: ",pilha_ramos[-1][0])
else:
    print("Refutada")
    print("Valoracao: ",pilha_ramos[-1][0])
