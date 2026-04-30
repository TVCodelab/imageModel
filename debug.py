from math import isqrt
from typing import Optional


def eh_primo(numero: int) -> bool:
    """Verifica se um número é primo.

    Args:
        numero (int): Número inteiro a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.
    """
    if numero <= 1:
        # Inclui negativos, zero e 1 — por definição matemática, nenhum deles é primo.
        # Verificar logo no início evita qualquer processamento desnecessário.
        return False

    if numero <= 3:
        # 2 e 3 são os únicos primos consecutivos; pulá-los no loop evitaria detectá-los,
        # então retornamos True diretamente antes de qualquer filtragem.
        return True

    if numero % 2 == 0:
        # Todo par > 2 tem 2 como divisor, logo nunca será primo.
        # Descartar aqui é crucial: o loop abaixo só testa ímpares,
        # então sem este guarda um número como 4 passaria direto.
        return False

    # Só precisamos testar divisores até √numero.
    # Se numero = a × b e a ≤ b, então a ≤ √numero — qualquer fator maior que isso
    # já teria um par menor que já foi testado.
    limite = isqrt(numero)

    # Começa em 3 e avança de 2 em 2 (apenas ímpares), porque:
    #   - 2 como divisor já foi descartado acima;
    #   - qualquer múltiplo par também seria divisível por 2, logo irrelevante.
    for divisor in range(3, limite + 1, 2):
        if numero % divisor == 0:
            # Encontrou um divisor exato: o número é composto. Para imediatamente —
            # não é necessário continuar testando os demais candidatos.
            return False

    # Nenhum divisor foi encontrado no intervalo [3, √numero].
    # Pelo crivo de primalidade, isso garante que o número é primo.
    return True


def ler_inteiro(prompt: str) -> Optional[int]:
    """Lê e converte uma entrada para inteiro; retorna None em caso de erro."""
    try:
        return int(input(prompt).strip())
    except ValueError:
        # int() lança ValueError para qualquer string que não represente um inteiro válido.
        # Converter o erro em None desacopla a lógica de leitura da lógica de validação em main().
        return None


def main():
    print("=" * 40)
    print(" Verificador de número primo ".center(40, "-"))
    print("=" * 40)

    numero = ler_inteiro("Digite um número inteiro: ")

    if numero is None:
        # ler_inteiro sinaliza falha com None em vez de lançar exceção,
        # permitindo que main() decida como reagir sem precisar de try/except aqui.
        print("\nPor favor, insira um número inteiro válido.")
        return  # Encerra o fluxo sem chamar eh_primo com um valor inválido.

    # Expressão condicional inline: mantém a atribuição e a lógica de exibição juntas,
    # evitando um if/else separado só para montar uma string.
    mensagem = (
        f"\n>>> {numero} é primo! 🎉"
        if eh_primo(numero)
        else f"\n>>> {numero} não é primo. 😕"
    )
    print(mensagem)
    print("=" * 40)


# --- Bloco de debug ---
# Execute este arquivo diretamente para rodar os casos de teste sem precisar de input manual.
# Cada chamada imprime o número, o resultado esperado e o resultado real,
# facilitando identificar regressões quando a função for modificada.

def _debug():
    casos = [
        # (numero, esperado)
        (-5,   False),  # negativo
        (0,    False),  # zero
        (1,    False),  # 1 não é primo por definição
        (2,    True),   # menor primo (par)
        (3,    True),   # menor primo ímpar
        (4,    False),  # par > 2
        (9,    False),  # composto ímpar (3 × 3) — testa se o loop pega divisores ímpares
        (15,   False),  # composto ímpar (3 × 5)
        (17,   True),   # primo ímpar simples
        (25,   False),  # quadrado perfeito ímpar (5²) — testa o limite = isqrt(numero)
        (97,   True),   # primo próximo de 100
        (100,  False),  # par > 2
        (101,  True),   # primo acima de 100
        (9973, True),   # primo de 4 dígitos — estresse no loop
    ]

    print("=" * 50)
    print(" DEBUG: eh_primo ".center(50, "-"))
    print("=" * 50)
    print(f"{'Número':>8}  {'Esperado':<10}  {'Obtido':<10}  {'Status'}")
    print("-" * 50)

    falhas = 0
    for numero, esperado in casos:
        obtido = eh_primo(numero)
        # Compara esperado vs obtido para sinalizar falhas individualmente.
        status = "✅ OK" if obtido == esperado else "❌ FALHA"
        if obtido != esperado:
            falhas += 1
        print(f"{numero:>8}  {str(esperado):<10}  {str(obtido):<10}  {status}")

    print("=" * 50)
    if falhas == 0:
        print("Todos os casos passaram.")
    else:
        # Resumo no final para facilitar a leitura quando há muitos casos.
        print(f"{falhas} caso(s) falharam.")
    print("=" * 50)


if __name__ == "__main__":
    # Quando executado diretamente, roda o debug em vez do fluxo interativo.
    # Para usar o programa normalmente, importe main() ou remova esta linha.
    _debug()
