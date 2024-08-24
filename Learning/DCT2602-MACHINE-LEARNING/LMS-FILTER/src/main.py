import matplotlib.pyplot as plt
import numpy as np


def gerar_sinal_desejado(n_samples: int):
    """
    Gera o sinal desejado s(n) como uma função seno.

    Args:
        n_samples (int): Número de amostras do sinal.
    """
    n = np.arange(n_samples)
    s = np.sin(0.075 * np.pi * n)
    return s


def gerar_ruido_branco(n_samples: int, seed: int = 0):
    """
    Gera o ruído branco v(n) com média nula e variância unitária.

    Args:
        n_samples (int): Número de amostras do ruído.
        seed (int): Semente para a geração de números aleatórios.
    """
    np.random.seed(seed)
    return np.random.normal(0, 1, n_samples)


def gerar_sinais_sensores(n_samples: int, v: np.ndarray):
    """
    Gera os sinais de ruído captados pelos sensores.

    Args:
        n_samples (int): Número de amostras dos sinais.
        v (np.ndarray): Sinal de ruído branco v(n).
    """
    v1 = np.zeros(n_samples)
    v2 = np.zeros(n_samples)

    for i in range(1, n_samples):
        v1[i] = -0.5 * v1[i - 1] + v[i]
        v2[i] = 0.8 * v2[i - 1] + v[i]

    return v1, v2


def filtro_lms(x: np.ndarray, d: np.ndarray, mu: float, num_coef: int) -> np.ndarray:
    """
    Implementa o filtro LMS genérico para estimar um sinal desejado.

    Args:
        x (np.ndarray): Sinal de entrada.
        d (np.ndarray): Sinal desejado.
        mu (float): Fator de aprendizado do LMS.
        num_coef (int): Número de coeficientes do filtro.

    Returns:
        np.ndarray: Sinal estimado pelo filtro LMS.
    """
    n_samples = len(x)
    h = np.zeros(num_coef)  # Inicializando os pesos do filtro
    y_lms = np.zeros(n_samples)  # Sinal estimado pelo LMS
    e_lms = np.zeros(n_samples)  # Erro entre d(n) e y_lms(n)

    # Inicializando o buffer de entrada
    buffer = np.zeros(num_coef)

    for i in range(num_coef, n_samples):
        # Atualizando o buffer de entrada com os valores mais recentes
        buffer = x[i - num_coef : i]

        # Calcular o sinal estimado pelo filtro LMS (y_lms[i])
        y_lms[i] = np.dot(h, buffer)

        # Calcular o erro entre o sinal desejado e o sinal estimado
        e_lms[i] = d[i] - y_lms[i]

        # Atualizar os pesos do filtro LMS
        h += mu * e_lms[i] * buffer

    return y_lms


def plot(
    n: np.ndarray,
    s: np.ndarray,
    x: np.ndarray,
    y_lms: np.ndarray,
    coefs: int,
):
    """
    Plota os resultados dos sinais.

    Args:
        n (np.ndarray): Vetor de amostras.
        s (np.ndarray): Sinal desejado.
        x (np.ndarray): Sinal captado.
        y_lms (np.ndarray): Sinal filtrado pelo LMS.
        coefs (int): Número de coeficientes do filtro LMS.
    """
    plt.figure(figsize=(12, 8))

    ruido = x - s

    plt.subplot(2, 1, 1)
    plt.plot(n, ruido, label="Ruído", alpha=0.25)
    plt.plot(n, x, label="Sinal Captado x(n)", alpha=0.25)
    plt.plot(n, s, "--", color="red", label="Sinal Desejado s(n)")
    plt.title("Sinal Captado, Sinal Desejado e Ruído")
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(n[coefs:], y_lms[coefs:], label="Sinal Estimado (LMS)")
    plt.plot(n[coefs:], s[coefs:], "--", label="Sinal Desejado s(n)", alpha=0.25)
    plt.title("Ruído de x(n) e Ruído Estimado pelo Filtro LMS")
    plt.legend()

    plt.tight_layout()
    plt.show()


def main():
    # Configurações iniciais
    n_samples = 1024  # Número de amostras

    # Gerando os sinais
    s = gerar_sinal_desejado(n_samples)
    v = gerar_ruido_branco(n_samples)
    v1, v2 = gerar_sinais_sensores(n_samples, v)

    # Gerando o sinal captado pelo sensor 1: x(n) = s(n) + v1(n)
    x = s + v1
    coefs = 10
    # Filtro LMS
    y_lms = filtro_lms(s, v2, mu=0.01, num_coef=coefs)

    # Plotando os resultados
    n = np.arange(n_samples)
    plot(n, s, x, y_lms, coefs)


if __name__ == "__main__":
    main()
