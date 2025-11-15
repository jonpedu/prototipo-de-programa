# 🚀 Guia Rápido de Início

## Instalação (Execute apenas uma vez)

```powershell
pip install -r requirements.txt
```

## Executar a Aplicação

```powershell
streamlit run app.py
```

A aplicação abrirá automaticamente em: http://localhost:8501

## 📝 Fluxo de Uso

### Passo 1: Upload do CSV
Na barra lateral, clique em "Browse files" e selecione um arquivo CSV

### Passo 2: Preencher Metadados
- **Data da Coleta**: Selecione no calendário
- **Período**: Escolha "Manhã" ou "Tarde"
- **Local**: Digite o nome (ex: "Casa com Ype")

### Passo 3: Adicionar
Clique no botão "➕ Adicionar Dados à Análise"

### Passo 4: Visualizar
Os gráficos serão gerados automaticamente!

### Passo 5: Filtrar
Use o filtro "Filtrar por Local" para alternar entre os locais

## 📊 Arquivos de Exemplo

Na pasta `exemplos/` você encontrará 5 arquivos CSV prontos para testar:

1. `coleta1_casa_ype_manha.csv` - Casa com Ype (Manhã)
2. `coleta2_casa_ype_tarde.csv` - Casa com Ype (Tarde)
3. `coleta3_casa_vermelha_manha.csv` - Casa Vermelha (Manhã)
4. `coleta4_casa_vermelha_tarde.csv` - Casa Vermelha (Tarde)
5. `coleta5_sem_cabecalho.csv` - Exemplo sem cabeçalho

## ⚡ Teste Rápido

1. Execute: `streamlit run app.py`
2. Faça upload de `coleta1_casa_ype_manha.csv`
3. Data: 18/08/2025
4. Período: Manhã
5. Local: Casa com Ype
6. Clique em "Adicionar"
7. Repita com `coleta2_casa_ype_tarde.csv` (mesmo local, período Tarde)
8. Veja os gráficos comparativos!

## 💾 Download de Gráficos

Passe o mouse sobre qualquer gráfico e clique no ícone da câmera 📷 no canto superior direito para baixar em PNG.

## 🔄 Reiniciar

Para começar uma nova análise do zero, clique em "🗑️ Limpar Análise / Reiniciar Sessão" na barra lateral.

## ❓ Problemas Comuns

### "Erro ao processar arquivo"
- Verifique se o CSV tem 3 colunas
- Certifique-se que os valores são numéricos

### "Por favor, informe o local da coleta"
- Preencha o campo "Local da Coleta" antes de adicionar

### Aplicação não inicia
- Execute: `pip install -r requirements.txt`
- Verifique se tem Python 3.8+

---

**Pronto para começar! 🎉**
