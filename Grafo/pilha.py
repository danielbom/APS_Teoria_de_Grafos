
class pilha(object):
    def __init__(self):
        self.vet = []

    def desempilha(self):
        if not self.vazia():
            return self.vet.pop(-1)
        return None

    def empilha(self, valor):
<<<<<<< HEAD
        self.vet.append(valor)
=======
        self.vet.insert(0, valor)
>>>>>>> 60c4c357e40e4df78d586984c35181d889a7d675

    def vazia(self):
        if len(self.vet) == 0:
            return True
        return False

    def print(self):
        if self.vazia():
            print("PILHA VAZIA")
        for i in self.vet:
            print(i)
    
<<<<<<< HEAD
    def getTopo(self):
        return self.vet[-1]
=======
>>>>>>> 60c4c357e40e4df78d586984c35181d889a7d675
