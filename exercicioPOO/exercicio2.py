class Contato:
    def __init__(self, nome='', numero=''):
        self.nome = nome
        self.numero = numero
        
class Agenda(Contato):
    def __init__(self,contatos):
        self.contatos= contatos

    def mostrar(self):
        for number in range (len(self.contatos)):
            print(self.nome[number])
    
def main():
    con1 = Contato('Fefe','11974177977')
    con2 = Contato('robertao','11974177978')
    lista=[con1,con2]
    agenda=Agenda(lista)
    agenda.mostrar()

if __name__ == '__main__':
    main()