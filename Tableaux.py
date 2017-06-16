operadores = [">","|","&","!"]
pilha_ramos = list()
nos = 0
max_nos = 0
num_i = []
# -1 False
# 1 True
pilha_ramos_fechados = list()
#Essa classe torna possivel ordenar as formulas de entrada
class FormulaDeEntrada:
    def __init__(self, value,form):
        self.value = 1 if value >= 1 else -1
        self.form = form
    def __it__(self,other):
        return len(self.form) < len(other.form)
    def __le__(self,other):
        return len(self.form) <= len(other.form)
    def __eq__(self,other):
        return len(self.form) == len(other.form)
    def __ne__(self,other):
        return len(self.form) != len(other.form)
    def __ge__(self,other):
        return len(self.form) >= len(other.form)
    def __gt__(self,other):
        return len(self.form) > len(other.form)
    def __str__(self):
        return str(self.value) + " " + self.form
    def __repr__(self):
        return (str(self.value) + " " + self.form)


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
    #Retorna a posicao do operador,(>,|,&,!)se hover um 
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
    #Retorna a fomula em um formato que torna as  operacoes sobre elas mais facil
    # Este formato eh (operador,formula esquerda, formula direita)
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

def is_uni(form):
    #Faz a checagem se a formula eh unitaria
    if len(form) > 2:
        return False
    elif len(form) > 1:
        return len(form[1]) <= 1
    return False

def add_to_main(f1,f2,main_branch):
    #Tratamento para formulas alfas serem adicionadas diretamente no 
    #Ramo principal
    if len(f1) >= 1 and f1 != "":
        main_branch.append(f1)
    if len(f2) >= 1 and f2 != "":
        main_branch.append(f2)


def solve(main_branch,nos_fechados,betas,num_ramos=1,i=0):
    #alfas
    n = len(main_branch)
    while i < n:
        if i > nos:
            max_nos = i
            nos_fechados.append(-1)
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
                            nos_fechados[i] = 1
                            nos_fechados[j] = 1
                    j -= 1    
        i += 1
        n = len(main_branch)
    #Betas
    while len(betas) > 0:
        i = betas[-1]
        nos_fechados[i] = 1
        betas.remove(i)
        if not is_uni(main_branch[i]):
            if len(main_branch[i][1]) > 1:
                main_branch[i] = format_formula(main_branch[i])
            alfa = is_alpha(main_branch[i][0],main_branch[i][1])
            if not alfa:
                num_ramos += 1
                f1 , f2 = expand_formula(main_branch[i][0],main_branch[i][1],main_branch[i][2],main_branch[i][3],alfa)
                nos_fechados[i] = 1
                temp_main = main_branch[:]
                temp_nos_fechados = nos_fechados[:]
                ####################################
                test = False
                if len(f2[1]) > 1:
                    f2 = format_formula(f2)
                    g1,g2 = expand_formula(f2[0],f2[1],f2[2],f2[3],is_alpha(f2[0],f2[1]))
                    pilha_ramos.append((main_branch[:]+[f1],[g1]+[g2],nos_fechados,False))
                    test = True
                else:
                    pilha_ramos.append((main_branch[:]+[f1],[f2],nos_fechados,False))
                f,ramo,n,num_ramos = solve(pilha_ramos[-1][0],nos_fechados,betas,num_ramos,i)
                if not f :
                    if test:
                        main_branch = ramo+[g1]+[g2]
                        pilha_ramos_fechados.append((f, main_branch,n, num_ramos))
                    main_branch = ramo+[f2]
                    pilha_ramos_fechados.append((f,main_branch,n, num_ramos))
                temp_ramo = pilha_ramos.pop()
                pilha_ramos.append((temp_ramo[0],temp_ramo[1],temp_ramo[2],True))
                ######################################
                main_branch = temp_main[:]
                nos_fechados = temp_nos_fechados[:]
                test = False
                if len(f1[1]) > 1:
                    f1 = format_formula(f1)
                    g1,g2 = expand_formula(f1[0],f1[1],f1[2],f1[3],is_alpha(f1[0],f1[1]))
                    pilha_ramos.append((main_branch[:]+[f2],[g1]+[g2],nos_fechados,False))
                    test = True
                else:
                    pilha_ramos.append((main_branch[:]+[f2],[f1],nos_fechados,False))
                f,ramo,n,num_ramos = solve(pilha_ramos[-1][0],nos_fechados,betas,num_ramos,i)
                if not f :
                    if test:
                        main_branch = ramo+[g1]+[g2]
                        pilha_ramos_fechados.append((f, main_branch ,n , num_ramos))
                    main_branch = ramo+[f1]
                    pilha_ramos_fechados.append((f,main_branch,n,num_ramos))
                temp_ramo = pilha_ramos.pop()
                pilha_ramos.append((temp_ramo[0],temp_ramo[1],temp_ramo[2],True))
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
        return ramo_fechado(main_branch),main_branch,nos_fechados,num_ramos 
    num_i.append(i)
    return ramo_fechado(pilha_ramos[-1][0]),main_branch,nos_fechados,num_ramos

def expand_formula(value,op,left,right,alfa):
    #Trata de dar a valoracao correta para as novas formulas
    # com expancao baseada no operador e valor da formula original
    def atribuir_valores(val, form):
        if type(form) == type(list()) or type(form) == type(tuple()):
            return [val] + [x for x in form]
        return (val,form)
    # esse caso trata quando a formula e uma negacao
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
    for s in [x.form for x in main_branch]:
        t += s
    return sum([1 for y in t if y != "(" and y != ")"])



def getValoracao(pilha_ramos):
    i = 0 
    j = pilha_ramos[-1]
    val = [x for x in j[0]+j[1] if is_uni(x)]
    while  i < len(j[0])-1:
        if j[2][i] == -1 and len(j[0][i]) >= 2:
            if len(j[0][i]) == 2:
                if len(j[0][i][1]) > 1:
                    j[0][i]= format_formula(j[0][i])
                else:
                    i += 1
                    continue
            f1, f2 = expand_formula(j[0][i][0],j[0][i][1],j[0][i][2],j[0][i][3],is_alpha(j[0][i][0],j[0][i][1]))
            add_to_main(f1,f2,val)
            add_to_main(f1,f2,j[0])
            j[2].append(-1)
        i += 1
    i = 0
    temp = list()
    while i < len(val):
        j = i+1
        contradicao = False
        while j < len(val):
            if val[i][0] * -1 == val[j][0] and val[i][1] == val[j][1]:
                contradicao = True
            j += 1
        if not contradicao:
            print(val[i])
            temp.append(val[i])
        i += 1
    return list(x for x in temp if len(x[1]) < 2 )

def run(main_branch):
    main_branch = [FormulaDeEntrada(x[0],x[1]) for x in main_branch]
    main_branch.sort()
    nos = numero_nos(main_branch)
    main_branch = [(f.value,f.form) for f in main_branch]
    betas = list()
    nos_fechados = [-1 for x in range(0,nos)]
    from time import time
    ini = time()
    v,m,n,num_ramos = solve(main_branch,nos_fechados,betas)
    end = time()
    if v:
        # print("Valida")
        # print("Numero de Nos: {}".format(nos))
        # print("Numero de Ramos: {}".format(num_ramos))
        # print("Tempo: {} ms".format((end-ini) *1000))
        return (end-ini) *1000,num_ramos,nos
    elif len(pilha_ramos) > 1:
        # print("Refutada")
        # print("Valoracao:")
        # print(list(set([ x for x in pilha_ramos[-1][0]+pilha_ramos[-1][1] if is_uni(x)])))
        # print("Tempo: {} ms".format((end-ini) *1000))
        val = getValoracao(pilha_ramos)
        return (end-ini) *1000,val
    else:
        # print("Refutada")
        # print("Valoracao: ")
        # print(list(set([ x for x in m if is_uni(x)])))
        # print("Tempo: {} ms".format((end-ini) *1000))
        return (end-ini) *1000,list(set([ x for x in m if is_uni(x)]))
##############################################################################