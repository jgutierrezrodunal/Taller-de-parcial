# Juan Alberto Gutiérrez Rodríguez

# Respuestas Taller de Parcial


# Parte A: Conceptos y lectura de código

#1 RTA: A), B) y D).

#2 RTA: Imprime "False True".

#3 RTA: a) Falso, python no va a restringir realmente el acceso al atributo y aún se puede acceder a el.
#       b) Falso, aunque si genera una restricción aún se puede acceder al atributo con el name mangling _Clase__atributo.
#       c) Verdadero, en el name mangling se coloca el nombre de la clase al que pertenece el atributo protegido.

#4 RTA: Imprime "abc" y no hay error ya que _token no está restringido ni para la clase B ni la clase Sub

#5 RTA: Imprime "(2, 1)"

#6 RTA: Da un error pues el dunder __slots__ solo permite el atributo 'x', y se está creando el atributo 'y' en c = Caja()

#7 Completa para que b tenga un atributo “protegido por convención”.
#RTA:
class B:
    def __init__(self):
        self._num = 99

#8 RTA: Imprime: True False True, _step si existe porque no está restringido, __tick está restringido y por eso marca False, y _M_tick da
#                true porque se está usando el nombre mangle

#9

class S:
    def __init__(self):
        self.__data = [1, 2]

    def size(self):
        return len(self.__data)
  
s = S()

# Accede a __data (solo para comprobar), sin modificar el código de la clase:
# Escribe una línea que obtenga la lista usando name mangling y la imprima.

print(s._S__data)

#10 RTA: '__a' no puede aparecer pues al ser protegido hay que llamarlo por el name mangling, 'a' nunca se definió, pero _D__a si es
#        puede aparecer al ser el name mangling del atributo 'self.__a'

#11 Completa para que saldo nunca sea negativo.

class Cuenta:
    def __init__(self, saldo):
        self._saldo = 0
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        if self._saldo >= 0:
            self._saldo = value
        else:
            raise ValueError("El saldo no puede ser negativo")
        
#12 Convierte temperatura_f en un atributo de solo lectura que se calcula desde temperatura_c.

class Termometro:
    def __init__(self, temperatura_c):
        self._c = float(temperatura_c)

    @property
    def temperatura_f(self):
        return self._c * 9/5 + 32

#13 Haz que nombre sea siempre str. Si asignan algo que no sea str, lanza TypeError.

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    @property
    def nombre(self):
        return self.nombre
    
    @nombre.setter
    def nombre(self, valor):
        if isinstance(valor, str):
            self._nombre = valor
        else: 
            raise TypeError("El nombre debe ser un dato de tipo str")

#14 Expón una vista de solo lectura de una lista interna.

class Registro:
    def __init__(self):
        self.__items = []

    def add(self, x):
        self.__items.append(x)

    @property
    def items(self):
        return tuple(self.__items)
    
#15 Refactoriza para evitar acceso directo al atributo y validar que velocidad sea entre 0 y 200.

class Motor:
    def __init__(self, velocidad):
        self._velocidad = velocidad # refactor aquí

    @property
    def velocidad(self):
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self, valor):
        if 0 <= valor <= 200:
            self._velocidad = valor
        else:
            raise ValueError("La velocidad debe estar entre 0 y 200")
        
#16 RTA: Usaría _atributo para elementos de la librería que no deberían ser manipulados, o en caso que si, sea bajo el propio riesgo
#        del usuario, pero un __atributo para elementos que no deben ser manipulados por ningún usuario o si quiera ser visibles para el.

#17 ¿Qué problema hay aquí?

class Buffer:
    def __init__(self, data):
        self._data = list(data)

    def get_data(self):
        return self._data
    
# RTA: EL problema es que el atributo _data está protegido, pero el método get_data puede ser modificado pues no está encapsulado
# Propuesta de correción: Hacer que el return no devuelva la misma lista, en su lugar devuelva una tupla:

class Buffer:
    def __init__(self, data):
        self._data = list(data)

    def get_data(self):
        return tuple(self._data)  #De esta manera ya no se puede alterar la lista

#18 ¿Dónde fallará esto y cómo lo arreglas?

#class A:
#    def __init__(self):
#        self.__x = 1

#class B(A):
#    def get(self):
#        return self.__x
    
# RTA: Fallará al momento de retornar el self.__x, pues aunque fue heredado de la clase A, está llamando un atributo restringido fuera de
#      su clase, por lo que va a dar un error, en su lugar habría que llamarlo por su name mangling así:

class A:
    def __init__(self):
        self.__x = 1

class B(A):
    def get(self):
        return self._A__x
    
#19 Completa para exponer solo un método seguro de un objeto interno.
# Expón un método 'guardar' que delegue en el repositorio,
# pero NO expongas _dump ni __repo.

class _Repositorio:
    def __init__(self):
        self._datos = {}

    def guardar(self, k, v):
        self._datos[k] = v

    def _dump(self):
        return dict(self._datos)

class Servicio:
    def __init__(self):
        self.__repo = _Repositorio()

    def guardar(self, k, v):
        self.__repo.guardar(k, v)

#20 Escribe una clase ContadorSeguro con:
# • atributo “protegido” _n
# • método inc() que suma 1
# • propiedad n de solo lectura
# • método “privado” __log() que imprima "tick" cuando se incrementa
# • Muestra un uso básico con dos incrementos y la lectura final.

class ContadorSeguro:
    def __init__(self):
        self._n = 0

    def inc(self):
        self._n += 1
        self.__log()

    @property
    def n(self):
        return self._n
        
    def __log(self):
     print("tick")

def main():
    
    c = ContadorSeguro()

    c.inc()
    c.inc()
    print(c.n)

if __name__ == '__main__':
    main()