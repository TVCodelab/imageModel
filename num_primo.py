from math import isqrt
from typing import Optional


def eh_primo(numero: int) -> bool:
    """Retorna True se numero for primo, caso contrário False."""
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0:
        return False

    limite = isqrt(numero)
    for divisor in range(3, limite + 1, 2):
        if numero % divisor == 0:
            return False
    return True


def ler_inteiro(prompt: str) -> Optional[int]:
    """Lê e converte uma entrada para inteiro; retorna None em caso de erro."""
    try:
        return int(input(prompt).strip())
    except ValueError:
        return None


def main():
    print("=" * 40)
    print(" Verificador de número primo ".center(40, "-"))
    print("=" * 40)

    numero = ler_inteiro("Digite um número inteiro: ")
    if numero is None:
        print("\nPor favor, insira um número inteiro válido.")
        return

    mensagem = (
        f"\n>>> {numero} é primo! 🎉"
        if eh_primo(numero)
        else f"\n>>> {numero} não é primo. 😕"
    )
    print(mensagem)
    print("=" * 40)


if __name__ == "__main__":
    main()
