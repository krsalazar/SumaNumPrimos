def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def suma_primos_hasta(numero):
    suma = 0
    for num in range(2, numero + 1):
        if es_primo(num):
            suma += num
    return suma

numero = int(input("Ingrese un número: "))
suma_primos = suma_primos_hasta(numero)
print(f"La suma de los números primos hasta {numero} es: {suma_primos}")
