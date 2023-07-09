def spaces(string): #quita lso espacion del estrin
    evaluation = ""
    for carac in string:
        if carac != " ":
            evaluation = evaluation + carac
    return evaluation

def Paren_evaluate(string,a,b): # evalua los parentesis del estrin separando todo en lista y genera un mapa de prioridades para luedo hacer bien el calculo
    string = spaces(string)
    evaluated_string = ""
    evaluation = []
    pos_prioritis = []
    op = False
    for carac in string:
        if carac == a or carac == b:
            if op == False:
                evaluation.append(evaluated_string)
                evaluated_string = ""
                pos_prioritis.append(1)
                op = True
            else:
                evaluation.append(evaluated_string)
                evaluated_string = ""
                pos_prioritis.append(2)
                op = False
        else:
            evaluated_string = evaluated_string + carac
    evaluation.append(evaluated_string)
    pos_prioritis.append(1)
    return evaluation,pos_prioritis

def Ope_evaluation(string):#separa las operaciones de los numeros
    nums = "0123456789"
    ope = "+-*/"
    numero = ""
    resultado = []
    for carac in string:
        if carac in nums:
            numero = numero + carac
        elif carac in ope:
            resultado.append(numero)
            numero = ""
            resultado.append(carac)
    resultado.append(numero)
    return resultado

def Remuve_list_spaces(lista):#elimina artefactos generados por la funcion que evaluan los string y las listas
    while "" in lista:
        lista.remove("")
    return lista

def math_evaluation(lista,ope):#evalua las operaciones amtematicas
    for i in range(len(lista)):
        if lista[i] == ope:
            if ope == "/":
                lista[i] = float(lista[i-1])/float(lista[i+1])
                lista[i-1] = ""
                lista[i+1] = ""
                return lista
            elif ope == "*":
                lista[i] = float(lista[i-1])*float(lista[i+1])
                lista[i-1] = ""
                lista[i+1] = ""
                return lista
            elif ope == "+":
                lista[i] = float(lista[i-1])+float(lista[i+1])
                lista[i-1] = ""
                lista[i+1] = ""
                return lista
            elif ope == "-":
                lista[i] = float(lista[i-1])-float(lista[i+1])
                lista[i-1] = ""
                lista[i+1] = ""
                return lista
    
def main_math_evaluation(lista):#usa la funcion anterio para evaluara todas las operaciones
    while "/" in lista:
        lista = math_evaluation(lista,"/")
        lista = Remuve_list_spaces(lista)
    while "*" in lista:
        lista = math_evaluation(lista,"*")
        lista = Remuve_list_spaces(lista)
    while "+" in lista:
        lista = math_evaluation(lista,"+")
        lista = Remuve_list_spaces(lista)
    while "-" in lista:
        lista = math_evaluation(lista,"-")
        lista = Remuve_list_spaces(lista)
    return lista

def main(string):#usa la funcion anterio para evaluar primero las parenteris, luego junta todo en un string y lo evalua entero
    resultado = ""
    evaluation,pos_prioritis = Paren_evaluate(string,"(",")")
    for i in range(len(pos_prioritis)):
        if pos_prioritis[i] == 2:
            evaluation[i] = (main_math_evaluation(Remuve_list_spaces(Ope_evaluation(evaluation[i])))[0])/10

    for i in range(len(evaluation)):
        resultado = resultado + str(evaluation[i])
    a =  main_math_evaluation(Remuve_list_spaces(Ope_evaluation(resultado)))
    return float(a[0])

A = "2+2"
print(main(A))

