
class pilha(object):
    def __init__(self):
        self.vet = []

    def desempilha(self):
        if not self.vazia():
            return self.vet.pop(-1)
        return None

    def empilha(self, valor):
        self.vet.append(valor)
<<<<<<< HEAD
=======
        self.vet.insert(0, valor)
>>>>>>> b713866d0fba99c5b0014f42ae152625a211bbaf

    def vazia(self):
        if len(self.vet) == 0:
            return True
        return False

    def print(self):
        if self.vazia():
            print("PILHA VAZIA")
        for i in self.vet:
            print(i)
    
    def getTopo(self):
        return self.vet[-1]
<<<<<<< HEAD

=======
>>>>>>> b713866d0fba99c5b0014f42ae152625a211bbaf
