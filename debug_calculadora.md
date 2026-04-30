# 🐛 Prática 3 — Debug com IA

## Arquivo analisado: `calculadora_bugada.py`

---

## Código original

```python
# calculadora_bugada.py
# Programa simples de calculadora com erros propositais

def somar(a, b)
    return a + b

def dividir(a, b):
    return a / b

numeros = [10, 20, 30, 40]

print("Soma:", somar(5, 3))
print("Divisão:", dividir(10, 0))
print("Primeiro número:", numeros[10])
```

---

## Erros identificados

### ❌ Erro 1 — Sintaxe: dois-pontos ausente na definição da função

**Linha:** 4  
**Tipo:** `SyntaxError`

**Trecho com erro:**
```python
def somar(a, b)
```

**Causa:**  
Em Python, toda definição de função precisa terminar com `:` (dois-pontos). Sem ele, o interpretador não consegue nem começar a executar o programa — o erro acontece antes de qualquer linha rodar.

**Correção:**
```python
def somar(a, b):
```

---

### ❌ Erro 2 — Lógica: divisão por zero

**Linha:** 13  
**Tipo:** `ZeroDivisionError`

**Trecho com erro:**
```python
print("Divisão:", dividir(10, 0))
```

**Causa:**  
Matematicamente (e em Python), dividir qualquer número por `0` é indefinido. O Python lança uma exceção em tempo de execução quando isso acontece.

**Correção:**  
Adicionar uma verificação antes de dividir:
```python
def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b
```

---

### ❌ Erro 3 — Índice fora do intervalo

**Linha:** 14  
**Tipo:** `IndexError`

**Trecho com erro:**
```python
print("Primeiro número:", numeros[10])
```

**Causa:**  
A lista `numeros` tem apenas 4 elementos (índices `0` a `3`). Tentar acessar o índice `10` ultrapassa o limite da lista — o Python não permite acessar uma posição que não existe.

**Correção:**
```python
print("Primeiro número:", numeros[0])
```

---

## ✅ Código corrigido

```python
# calculadora_corrigida.py

def somar(a, b):          # ✅ dois-pontos adicionado
    return a + b

def dividir(a, b):
    if b == 0:            # ✅ verificação de divisão por zero
        return "Erro: divisão por zero!"
    return a / b

numeros = [10, 20, 30, 40]

print("Soma:", somar(5, 3))
print("Divisão:", dividir(10, 0))
print("Primeiro número:", numeros[0])  # ✅ índice válido
```

**Saída esperada após correção:**
```
Soma: 8
Divisão: Erro: divisão por zero!
Primeiro número: 10
```

---

## Resumo dos erros

| # | Linha | Tipo | Descrição |
|---|-------|------|-----------|
| 1 | 4 | `SyntaxError` | Faltou `:` no `def somar(a, b)` |
| 2 | 13 | `ZeroDivisionError` | Divisão por zero sem tratamento |
| 3 | 14 | `IndexError` | Índice `10` não existe na lista |
