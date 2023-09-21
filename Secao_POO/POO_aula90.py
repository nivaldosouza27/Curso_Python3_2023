class Carro:
    def __init__(self, marca, modelo, ano_fabricacao, modelo_motor, nome_fabricante) -> None:
        self.marca_carro = marca
        self.modelo_carro = modelo
        self.ano_fabricacao_carro = ano_fabricacao
        self.modelo_motor = modelo_motor
        self.nome_fabricante = nome_fabricante

    @property
    def motor(self):
        return self.modelo_motor
    
    @motor.setter
    def motor(self, valor):
        self.modelo_motor = valor
   
    @property
    def fabricante(self):
        return self.nome_fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self.nome_fabricante = valor

    def salvar_modelo_carro_motor_fabricante(self):
        carro = [
                {'Marca' : self.marca_carro},
                {'Modelo' : self.modelo_carro} ,
                {'Ano Fabricacao' : self.ano_fabricacao_carro} ,
                {'Modelo Motor' : self.modelo_motor},
                {'Fabricante' : self.nome_fabricante},
                ]
        return print(*carro, end='\n\n', sep='\n')
        
    
class Motor:
    def __init__(self, modelo) -> None:
        self.modelo_motor = modelo

class Fabricante:
    def __init__(self, nome) -> None:
        self.nome_fabricante = nome


c1 = Carro('Volkswagen', 'Voyage', 2016, '1.6 Flex', 'Volkswagen')
c1.salvar_modelo_carro_motor_fabricante()

c2 = Carro('Volkswagen', 'GOL', 2020,'1.6 Flex', 'Volkswagen')
c2.salvar_modelo_carro_motor_fabricante()

c3 = Carro('FIAT', 'Palio', 2010,'1.0 Flex', 'FIAT')
c3.salvar_modelo_carro_motor_fabricante()

c4 = Carro('FIAT', 'Palio Weekend', 2011, '1.0 Flex', 'FIAT')
c4.salvar_modelo_carro_motor_fabricante()

