# 🔢 Verificador de Número Primo

Projeto de estudo em Python com foco em boas práticas: verificação de primalidade, leitura segura de entrada, debug estruturado e refatoração de código legado.

---

## 📁 Estrutura do projeto

```
.
├── num_primo.py              # Programa principal
├── debug.py                  # Suite de testes manuais para eh_primo
├── refatoracao.py            # Exemplo de refatoração de código legado
├── explicação.md             # Explicação linha a linha do num_primo.py
└── explicacao_refatoração.md # Documentação das decisões de refatoração
```

---

## 🚀 Como usar

### Programa principal

```bash
python num_primo.py
```

Solicita um número inteiro via terminal e informa se ele é primo ou não.

```
========================================
-------- Verificador de número primo --------
========================================
Digite um número inteiro: 97

>>> 97 é primo! 🎉
========================================
```

### Suite de debug

```bash
python debug.py
```

Roda 14 casos de teste cobrindo negativos, zero, bordas (1, 2, 3), pares, compostos ímpares, quadrados perfeitos e primos de 4 dígitos — sem precisar de input manual.

```
==================================================
------------------ DEBUG: eh_primo ------------------
==================================================
  Número  Esperado    Obtido      Status
--------------------------------------------------
      -5  False       False       ✅ OK
       0  False       False       ✅ OK
       1  False       False       ✅ OK
       2  True        True        ✅ OK
      ...
==================================================
Todos os casos passaram.
==================================================
```

---

## 🧠 Como funciona `eh_primo`

A verificação usa três guardas sequenciais antes do loop, eliminando casos triviais o mais cedo possível:

| Condição | Ação | Motivo |
|---|---|---|
| `numero <= 1` | `return False` | Negativos, zero e 1 não são primos por definição |
| `numero <= 3` | `return True` | 2 e 3 são primos; o loop ímpar os excluiria |
| `numero % 2 == 0` | `return False` | Todo par > 2 tem 2 como divisor |

O loop testa apenas divisores ímpares de `3` até `√numero` (`isqrt`). O limite em `√numero` vem do fato de que se `n = a × b` e `a ≤ b`, então `a ≤ √n` — qualquer fator acima disso já teria um par menor já testado.

---

## 🔄 Refatoração (`refatoracao.py`)

Demonstra a transformação de um código com nomes crípticos (`c`, `l`, `t`, `mx`) e loops manuais em código idiomático Python:

| Antes | Depois |
|---|---|
| `def c(l):` | `def compute_statistics(numbers: Iterable[float]) -> Statistics:` |
| `for i in range(len(l)): t += l[i]` | `sum(numbers)` |
| Retorno de tupla anônima | `@dataclass(frozen=True) Statistics` |
| `print` no escopo global | `main()` com `if __name__ == "__main__"` |
| Sem validação de lista vazia | `raise ValueError` explícito |

---

## 🐍 Requisitos

- Python 3.8+
- Sem dependências externas
