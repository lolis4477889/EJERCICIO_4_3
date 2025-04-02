# -*- coding: utf-8 -*-
"""EJERCICIO_3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12qqH9eO6aO17WV3ZiUlAuGtjCbv62OC7
"""

import numpy as np
import matplotlib.pyplot as plt

def simpson_rule(f, a, b, n):
    """Aproxima la integral de f(x) en [a, b] usando la regla de Simpson."""
    if n % 2 == 1:
        raise ValueError("El número de subintervalos (n) debe ser par.")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)  # Puntos del intervalo
    fx = f(x)  # Evaluamos la función en esos puntos

    # Regla de Simpson
    integral = (h / 3) * (fx[0] + 2 * np.sum(fx[2:n:2]) + 4 * np.sum(fx[1:n:2]) + fx[n])

    return integral

#EJERCICIO #2
# Función de ejemplo
def funcion(x):
    return 100*np.exp(-2*x)   # Cambiar esta función según el problema

C = 10**-6   # Capacitancia en Faradios
a, b = 0, 5  # Intervalo de integración [0, T] con T = 5s
n = 30  # Número de subintervalos (debe ser par). Cambiar según el problema: 6,10,20,30

# Se multiplica por C para obtener la carga Q
resultado = C * simpson_rule(funcion, a, b, n)
print(f"Para n = {n}, la carga almacenada aproximada es: {resultado:.6e} C")

# --- Solución analítica de la integral ---
solucion_analitica = C * (-50 * np.exp(-2 * b) + 50 * np.exp(-2 * a))
print(f"Solución analítica: {solucion_analitica:.6e} C")
"""
"""
# Gráfica de la función y la aproximación con la regla de Simpson
x_vals = np.linspace(a, b, 100)
y_vals = funcion(x_vals)


#plt.plot(x_vals, y_vals, label=r"$f(x) = kx$", color="blue")
#plt.plot(x_vals, y_vals, label=r"$V(t) = 100e^{-2t}$", color="blue")
plt.plot(x_vals, y_vals, label=r"$\frac{dT}{dx}=-100x$", color="blue")
plt.fill_between(x_vals, y_vals, alpha=0.3, color="cyan", label="Área aproximada")
plt.scatter(np.linspace(a, b, n+1), funcion(np.linspace(a, b, n+1)), color="red", label="Puntos de interpolación")
#EJERCICIO#1
#plt.xlabel("x")
#plt.ylabel("f(x)")
#EJERCICIO"2
#plt.xlabel("t (s)")
#plt.ylabel("V(t) (V)")
plt.xlabel("x (m)")
plt.ylabel("dT/dx (K/m)")
plt.legend()
plt.title(f"Aproximación con la regla de Simpson (n={n})")
plt.grid()

# Guardar la figura
plt.savefig(f"simpson_n{n}.png")
plt.show()