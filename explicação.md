# Explicação do código `num_primo.py`

1. `from math import isqrt`
   - Importa a função `isqrt` para calcular a raiz quadrada inteira de um número.
   - Isso evita cálculos com ponto flutuante e melhora a precisão na verificação.

2. `from typing import Optional`
   - Importa o tipo `Optional` para declarar que a função pode retornar um inteiro ou `None`.
   - Isso deixa os tipos mais claros para quem lê o código.

3. `def eh_primo(numero: int) -> bool:`
   - Define a função que recebe um número inteiro e retorna um booleano.
   - Essa função verifica se `numero` é primo.

4. `    """Retorna True se numero for primo, caso contrário False."""`
   - Docstring que descreve o propósito da função.

5. `    if numero <= 1:`
   - Verifica se `numero` é menor ou igual a 1.
   - Números menores ou iguais a 1 não são primos.

6. `        return False`
   - Retorna `False` imediatamente para casos não primos.

7. `    if numero <= 3:`
   - Trata 2 e 3 como primos diretamente.
   - Evita checagens desnecessárias para esses casos.

8. `        return True`
   - Retorna `True` para 2 e 3.

9. `    if numero % 2 == 0:`
   - Verifica se o número é par.
   - Números pares maiores que 2 não são primos.

10. `        return False`
    - Retorna `False` se `numero` for divisível por 2.

11. `    limite = isqrt(numero)`
    - Calcula a raiz quadrada inteira de `numero`.
    - Isso limita os testes de divisores ao necessário.

12. `    for divisor in range(3, limite + 1, 2):`
    - Testa apenas divisores ímpares, pulando os pares.
    - Isso reduz o número de verificações.

13. `        if numero % divisor == 0:`
    - Verifica se `divisor` divide `numero` sem resto.

14. `            return False`
    - Retorna `False` ao encontrar um divisor, sinalizando que `numero` não é primo.

15. `    return True`
    - Se nenhum divisor for encontrado, retorna `True`.
    - Indica que o número é primo.

16. `def ler_inteiro(prompt: str) -> Optional[int]:`
    - Define a função de leitura de entrada separada.
    - Essa função converte texto em inteiro e trata erros de conversão.

17. `    """Lê e converte uma entrada para inteiro; retorna None em caso de erro."""`
    - Docstring que explica o comportamento da função.

18. `    try:`
    - Inicia o bloco de tratamento de exceção.

19. `        return int(input(prompt).strip())`
    - Lê a entrada do usuário, remove espaços e converte para inteiro.

20. `    except ValueError:`
    - Captura a exceção quando a conversão falha.

21. `        return None`
    - Retorna `None` para sinalizar entrada inválida.

22. `def main():`
    - Define a função principal do programa.
    - Organiza o fluxo de entrada, validação e saída.

23. `    print("=" * 40)`
    - Exibe um cabeçalho mais bonito no terminal.
    - Deixa a apresentação mais agradável.

24. `    numero = ler_inteiro("Digite um número inteiro: ")`
    - Solicita ao usuário que insira um número.

25. `    if numero is None:`
    - Verifica se a entrada foi inválida.

26. `        print("\nPor favor, insira um número inteiro válido.")`
    - Mostra uma mensagem amigável para entradas incorretas.

27. `    mensagem = (`
    - Cria texto de saída mais bonito usando expressão condicional.
    - Mostra o resultado com formatação e emoji.

28. `    print(mensagem)`
    - Exibe o resultado final para o usuário.

29. `if __name__ == "__main__":`
    - Verifica se o script está sendo executado diretamente, não importado.

30. `    main()`
    - Chama a função principal para executar o programa.

Resumo técnico:
- `eh_primo` realiza a verificação de primalidade.
- `ler_inteiro` separa a leitura e validação da entrada.
- `main` organiza o fluxo principal e mantém o código mais legível.
