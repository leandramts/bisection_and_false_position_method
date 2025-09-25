import math
import matplotlib.pyplot as plt

def bisection_method(f, a, b, tol, max_inter):

    storage = []

    if f(a)*f(b) > 0:
        raise ValueError("f(a)*f(b) deve ser negativo")


    for i in range(max_inter):
        m = (a+b)/2.0

        storage.append(m)

        if f(m) == 0 or abs(f(m)) < tol or (b - a)/2.0 < tol:
            break
            
        if f(a)*f(m) < 0:
            b = m
        else:
            a = m
        
    return m, storage
         
def false_position_method(f, a, b, tol, max_inter):

    storage = []

    if f(a)*f(b) > 0:
        raise ValueError("f(a)*f(b) deve ser negativo")


    for i in range(max_inter):
        m = (a * f(b) - b * f(a)) / (f(b) - f(a))

        storage.append(m)

        if f(m) == 0 or abs(f(m)) < tol:
            break

        if f(a)*f(m) < 0:
            b = m
        else:
            a = m
        
    return m, storage


if __name__ == "__main__":
    f = lambda x: x**3 - 2*x - 5  #alterar conforme o problema proposta
    a, b = 2, 3
    tol  = 1e-6
    max_iter = 100


    root_bisection, storage_bisection = bisection_method (f, a, b, tol, max_iter)
    root_false_position, storage_false_position = false_position_method (f,a, b, tol, max_iter)

    print("\n===== RESULTADOS =====")
    print(f"Raiz (Bisseccao): {root_bisection}")
    print(f"Raiz (Falsa Posicao): {root_false_position}")

    # ---------------------------
    # Gráficos de comparação
    # ---------------------------
    plt.style.use('seaborn-v0_8-whitegrid') 
    plt.figure(figsize=(14,6))
    
    # Evolução Bisseção
    plt.subplot(1,2,1)
    plt.plot(storage_bisection, 
    marker = 's', 
    label="Método por Bisseção",
    color = '#0077b6',
    linestyle = '-'
    )


    plt.axhline(y=root_bisection, color='r', linestyle=':', label="Raiz Final")
    plt.text(0.5, root_bisection + 0.0005, f'Raiz ≈ {root_bisection:.6f}', color='r', fontsize=10)
    plt.xlabel("Iteração")
    plt.ylabel("Aproximação da Raiz")
    plt.title("Evolução da Raiz - Método por Bisseção", fontsize = 16, fontweight = 'bold')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(loc='best', fontsize=10)
    
    # Evolução Falsa Posição
    plt.subplot(1,2,2)
    plt.plot(storage_false_position,
    label="Método por Falsa Posição",
    color='#1e8449',
    marker='o',        
    linestyle='-',
    linewidth=2,
    markersize=6
)

    plt.axhline(y=root_false_position, color='r', linestyle=':', label="Raiz Final")
    plt.xlabel("Iteração", fontsize = 12)
    plt.ylabel("Aproximação da Raiz")
    plt.text(0.5, root_false_position + 0.0005, f'Raiz ≈ {root_false_position:.6f}', color='r', fontsize=10)
    plt.title("Evolução da Raiz - Método por Falsa Posição",  fontsize=16, fontweight='bold')    # Grade personalizada
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(loc='best', fontsize=10)
        
    plt.tight_layout()
    plt.show()


