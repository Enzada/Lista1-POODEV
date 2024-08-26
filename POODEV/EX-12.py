from enum import Enum

class DiasDaSemana(Enum):
    domingo = 1
    segunda = 2
    terca = 3
    quarta = 4
    quinta = 5
    sexta = 6
    sabado = 7

class Agenda():
    def __init__(self):
        self.compromissos = {dia: [] for dia in DiasDaSemana}

    def addCompromisso(self, dia, compromisso):
        if isinstance(dia, DiasDaSemana):
            self.compromissos[dia].append(compromisso)
        else:
            raise ValueError('O dia deve ser uma instância de DiasDaSemana')
        
    def listCompromisso(self, dia):
        if isinstance(dia, DiasDaSemana):
            return self.compromissos[dia]
        else:
            raise ValueError('O dia deve ser uma instância de DiasDaSemana')
        
agenda = Agenda()

agenda.addCompromisso(DiasDaSemana.segunda, 'Aula de Banco de Dados 2 das 10:00 às 12:00')
agenda.addCompromisso(DiasDaSemana.quinta, 'Aula de POO DEV das 14:00 às 16:00')

print('Compromissos na segunda-feira: ', agenda.listCompromisso(DiasDaSemana.segunda))
print('Compromissos na quinta-feira: ', agenda.listCompromisso(DiasDaSemana.quinta))