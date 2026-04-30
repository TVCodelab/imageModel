from math import isqrt
from typing import Optional


def eh_primo(numero: int) -> bool:
    """Verifica se um número é primo.

    Args:
        numero (int): Número inteiro a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.
    """
    # Números menores ou iguais a 1 não são primos.
    if numero <= 1:
        return False

    # 2 e 3 são primos e não precisam de checagens adicionais.
    if numero <= 3:
        return True

    # Elimina todos os pares maiores que 2, porque já sabemos que não são primos.
    if numero % 2 == 0:
        return False

    # A partir daqui, só há chance de ser primo se nenhum divisor ímpar for encontrado.
    limite = isqrt(numero)
    for divisor in range(3, limite + 1, 2):
        # Testa apenas números ímpares, pois todos os divisores pares já foram descartados.
        if numero % divisor == 0:
            return False
    return True


def ler_inteiro(prompt: str) -> Optional[int]:
    """Lê e converte uma entrada para inteiro; retorna None em caso de erro."""
    try:
        return int(input(prompt).strip())
    except ValueError:
        # Retorna None para sinalizar que a entrada não pôde ser convertida.
        return None


def main():
    print("=" * 40)
    print(" Verificador de número primo ".center(40, "-"))
    print("=" * 40)

    numero = ler_inteiro("Digite um número inteiro: ")
    if numero is None:
        print("\nPor favor, insira um número inteiro válido.")
        return

    # Usa eh_primo para determinar a mensagem mais apropriada para o usuário.
    mensagem = (
        f"\n>>> {numero} é primo! 🎉"
        if eh_primo(numero)
        else f"\n>>> {numero} não é primo. 😕"
    )
    print(mensagem)
    print("=" * 40)


if __name__ == "__main__":
    main()