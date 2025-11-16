# 🎉 Atualização: Suporte a Arquivos Excel!

## 📊 O que mudou?

A aplicação agora aceita **arquivos Excel (.xlsx, .xls)** além de CSV!

### ✅ Formatos Suportados:

1. **Excel (.xlsx, .xls)** ⭐ NOVO!
   - Formato mais comum
   - Facilita trabalhar com dados tabulares
   - Não precisa se preocupar com delimitadores

2. **CSV com qualquer delimitador**
   - Vírgula (,)
   - Ponto e vírgula (;)
   - Tabulação (tab)
   - Pipe (|)
   - **Detecção automática!**

---

## 🚀 Como Usar

### Passo 1: Prepare seus dados no Excel

Crie uma planilha com 3 colunas:

| temperatura | umidade | co2 |
|-------------|---------|-----|
| 32.5        | 68.1    | 405 |
| 33.1        | 67.5    | 410 |
| 32.9        | 69.2    | 408 |

### Passo 2: Salve como .xlsx

- **Arquivo → Salvar Como → Escolha "Pasta de Trabalho do Excel (.xlsx)"**

### Passo 3: Faça Upload na Aplicação

- Clique em "Browse files"
- Selecione seu arquivo .xlsx
- Preencha os metadados (data, local, período)
- Clique em "Adicionar"

---

## 💡 Vantagens do Excel

✅ **Mais fácil de editar** - use o Excel normalmente  
✅ **Sem problemas de delimitador** - funciona sempre  
✅ **Formatação visual** - veja os dados organizados  
✅ **Familiar** - todos conhecem Excel  
✅ **Compatível** - com seus arquivos existentes  

---

## 🔧 O que foi Instalado

- **openpyxl**: Biblioteca para ler arquivos Excel

---

## 📝 Exemplos Criados

Novos arquivos de exemplo na pasta `exemplos/`:

- `exemplo_casa_ype_manha.xlsx` ⭐
- `exemplo_casa_ype_tarde.xlsx` ⭐

---

## 🧪 Teste Agora!

1. Execute a aplicação:
   ```powershell
   .\iniciar.ps1
   ```

2. Faça upload de um dos arquivos .xlsx de exemplo

3. Veja funcionando!

---

## ⚠️ Observações

### Se você tem CSVs com formato estranho:

A aplicação agora tenta **automaticamente** detectar o delimitador correto!

**Exemplo:** Se seu CSV está assim (separado por tabs ou ;):
```
temperatura	umidade	co2
32.5	68.1	405
```

**Solução Fácil:** Basta abrir no Excel e salvar como .xlsx!

---

## 🎯 Resumo

**ANTES:** ❌ Só CSV com vírgula  
**AGORA:** ✅ Excel + CSV com qualquer formato

**Seu workflow agora:**
1. Coletar dados no Excel
2. Salvar .xlsx
3. Upload direto na aplicação
4. Pronto! 🎉

---

**Tudo mais simples e profissional!** 🚀
