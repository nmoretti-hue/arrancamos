# Punto 4
class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha


# Punto 5

d = Nodo("D")
e = Nodo("E")
f = Nodo("F")
g = Nodo("G")
b = Nodo("B", d, e)
c = Nodo("C", f, g)
arbol = Nodo("A", b, c)


# Punto 6

def pre_order(nodo):
    if nodo is None:
        return []
    return [nodo.valor] + pre_order(nodo.izquierda) + pre_order(nodo.derecha)


def in_order(nodo):
    if nodo is None:
        return []
    return in_order(nodo.izquierda) + [nodo.valor] + in_order(nodo.derecha)


def post_order(nodo):
    if nodo is None:
        return []
    return post_order(nodo.izquierda) + post_order(nodo.derecha) + [nodo.valor]


def level_order(nodo):
    if nodo is None:
        return []
    lista = []
    cola = [nodo]
    while cola:
        actual = cola.pop(0)
        lista.append(actual.valor)
        if actual.izquierda:
            cola.append(actual.izquierda)
        if actual.derecha:
            cola.append(actual.derecha)
    return lista


print("pre-order  :", pre_order(arbol))
print("in-order   :", in_order(arbol))
print("post-order :", post_order(arbol))
print("level-order:", level_order(arbol))

# Punto 9

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def inverse_polish_parser(expresion):
    pila = Stack()
    for simbolo in expresion.split():
        if simbolo in ["+", "-", "*", "/"]:
            derecha = pila.pop()
            izquierda = pila.pop()
            pila.push(Nodo(simbolo, izquierda, derecha))
        else:
            pila.push(Nodo(simbolo))
    return pila.pop()


arbol2 = inverse_polish_parser("4 5 + 5 3 - *")
print("post-order del parser:", " ".join(post_order(arbol2)))


# Punto 10

def calculate(nodo):
    if nodo.izquierda is None and nodo.derecha is None:
        return float(nodo.valor)
    izquierda = calculate(nodo.izquierda)
    derecha = calculate(nodo.derecha)
    if nodo.valor == "+":
        return izquierda + derecha
    if nodo.valor == "-":
        return izquierda - derecha
    if nodo.valor == "*":
        return izquierda * derecha
    if nodo.valor == "/":
        return izquierda / derecha


print("calculate 1:", calculate(arbol2))
print("calculate 2:", calculate(inverse_polish_parser("2 6 + 8 / 9 2 - *")))
print("calculate 3:", calculate(Nodo("+", Nodo("10"), Nodo("*", Nodo("3"), Nodo("4")))))


# Punto 11

def evaluate(expresion):
    return calculate(inverse_polish_parser(expresion))

print("evaluate 1:", evaluate("4 5 + 5 3 - *"))
print("evaluate 2:", evaluate("2 6 + 8 / 9 2 - *"))
print("evaluate 3:", evaluate("7 2 /"))