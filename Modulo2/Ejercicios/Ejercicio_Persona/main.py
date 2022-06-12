from Modulo2.Ejercicios.Ejercicio_Persona.Address import Address
from Modulo2.Ejercicios.Ejercicio_Persona.Person import Person

if __name__ == '__main__':
    address = Address("Av. Rivadavia", "1234", "Ciudad Autonoma de Buenos Aires")
    fulano = Person()
    fulano.name('Fulano')
    fulano.surname('Gomez')
    fulano.address(address)
    print(fulano.full_name())
    # invocando al método __str__
    print(fulano)
    sultano = Person()
    sultano.name('Sultano')
    sultano.surname('Perez')
    sultano.address(address)
    address.number('4578')
    print(sultano.full_name())
    # invocando al método __str__
    print(sultano)
