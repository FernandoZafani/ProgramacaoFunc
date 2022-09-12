class Contato:
    def __init__(self, nome='', numero=''):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f"Nome: {self.nome}, Numero: {self.numero}"
    
        
class Agenda(Contato):
    def __init__(self,lista):
        self.lista= lista

    def mostrar(self):
        for number in range (len(self.lista)):
            print(self.lista[number])
    
def main():
    con1 = Contato('Fefe','11974177977')
    con2 = Contato('robertao','11974177978')
    lista=[con1,con2]
    agenda=Agenda(lista)
    agenda.mostrar()

if __name__ == '__main__':
    main()