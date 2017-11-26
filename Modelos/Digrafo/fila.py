
class fila(object):
    def __init__(self):
        self.vet = []

    def pop(self):
        if not self.vazia():
            return self.vet.pop(0)
        return None

    def push(self, valor):
        if valor not in self.vet:
            self.vet.append(valor)

    def vazia(self):
        if len(self.vet) == 0:
            return True
        return False

    def print(self):
        if self.vazia():
            print("FILA VAZIA")
        for i in self.vet:
            print(i)

'''
f = fila()
f.pop()
f.push(10)
f.push(20)
f.push(50)

f.print()

f.pop()

f.print()
'''
