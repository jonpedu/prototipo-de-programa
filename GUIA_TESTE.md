# 🧪 Guia de Teste da Aplicação

## Teste Completo em 10 Minutos

### Preparação (1 minuto)
```powershell
# Execute para instalar dependências
pip install -r requirements.txt

# Execute para iniciar a aplicação
streamlit run app.py
```

---

## 🎯 Cenário de Teste 1: Primeira Coleta

### Passo 1: Adicionar Casa com Ype (Manhã)
1. Clique em **"Browse files"** na barra lateral
2. Selecione: `exemplos/coleta1_casa_ype_manha.csv`
3. **Data**: 18/08/2025
4. **Período**: Manhã
5. **Local**: Casa com Ype
6. Clique em **"➕ Adicionar Dados à Análise"**

**Resultado Esperado:**
- ✅ Mensagem de sucesso aparece
- ✅ Tabela mostra 1 linha com os dados
- ✅ Filtro "Filtrar por Local" mostra "Casa com Ype"
- ✅ 4 gráficos são exibidos (1 consolidado + 3 individuais)
- ✅ Métrica "Total de Coletas" mostra 1
- ✅ Métrica "Locais Diferentes" mostra 1

---

## 🎯 Cenário de Teste 2: Segunda Coleta (Mesmo Local)

### Passo 2: Adicionar Casa com Ype (Tarde)
1. Clique em **"Browse files"** novamente
2. Selecione: `exemplos/coleta2_casa_ype_tarde.csv`
3. **Data**: 18/08/2025
4. **Período**: Tarde
5. **Local**: Casa com Ype (mesmo nome!)
6. Clique em **"➕ Adicionar Dados à Análise"**

**Resultado Esperado:**
- ✅ Tabela mostra 2 linhas agora
- ✅ Gráficos mostram COMPARAÇÃO Manhã vs Tarde
- ✅ Barras lado a lado nos gráficos individuais
- ✅ Métrica "Total de Coletas" mostra 2
- ✅ Métrica "Locais Diferentes" ainda mostra 1

---

## 🎯 Cenário de Teste 3: Novo Local

### Passo 3: Adicionar Casa Vermelha (Manhã)
1. Upload: `exemplos/coleta3_casa_vermelha_manha.csv`
2. **Data**: 19/08/2025
3. **Período**: Manhã
4. **Local**: Casa Vermelha
5. Clique em **"Adicionar"**

**Resultado Esperado:**
- ✅ Tabela mostra 3 linhas
- ✅ Filtro agora tem 2 opções: "Casa com Ype" e "Casa Vermelha"
- ✅ Gráficos AINDA mostram "Casa com Ype" (filtro não mudou)
- ✅ Métrica "Total de Coletas" mostra 3
- ✅ Métrica "Locais Diferentes" mostra 2

### Passo 4: Testar Filtro
1. No filtro "Filtrar por Local", selecione **"Casa Vermelha"**

**Resultado Esperado:**
- ✅ Todos os gráficos são ATUALIZADOS instantaneamente
- ✅ Gráficos mostram apenas dados da Casa Vermelha
- ✅ Apenas 1 coleta (Manhã) aparece nos gráficos
- ✅ Título dos gráficos mostra "Casa Vermelha"

---

## 🎯 Cenário de Teste 4: Completar Casa Vermelha

### Passo 5: Adicionar Casa Vermelha (Tarde)
1. Upload: `exemplos/coleta4_casa_vermelha_tarde.csv`
2. **Data**: 19/08/2025
3. **Período**: Tarde
4. **Local**: Casa Vermelha
5. Clique em **"Adicionar"**

**Resultado Esperado:**
- ✅ Tabela mostra 4 linhas
- ✅ Como filtro está em "Casa Vermelha", gráficos atualizam automaticamente
- ✅ Agora mostra comparação Manhã vs Tarde para Casa Vermelha
- ✅ Métrica "Total de Coletas" mostra 4

---

## 🎯 Cenário de Teste 5: Arquivo sem Cabeçalho

### Passo 6: Testar CSV sem Cabeçalho
1. Upload: `exemplos/coleta5_sem_cabecalho.csv`
2. **Data**: 20/08/2025
3. **Período**: Manhã
4. **Local**: Laboratório
5. Clique em **"Adicionar"**

**Resultado Esperado:**
- ✅ Arquivo é processado CORRETAMENTE (mesmo sem cabeçalho)
- ✅ Mensagem de sucesso aparece
- ✅ Tabela mostra 5 linhas
- ✅ Novo local "Laboratório" aparece no filtro

---

## 🎯 Cenário de Teste 6: Download de Gráficos

### Passo 7: Baixar um Gráfico
1. Passe o mouse sobre qualquer gráfico
2. Observe a barra de ferramentas aparecer no canto superior direito
3. Clique no ícone da **câmera** 📷
4. O gráfico é salvo como PNG

**Resultado Esperado:**
- ✅ Barra de ferramentas Plotly visível
- ✅ Ícone da câmera clicável
- ✅ Download inicia automaticamente
- ✅ Arquivo PNG de alta qualidade

---

## 🎯 Cenário de Teste 7: Validações

### Passo 8: Testar Validação de Local
1. Deixe o campo "Local da Coleta" VAZIO
2. Faça upload de qualquer CSV
3. Clique em "Adicionar"

**Resultado Esperado:**
- ✅ Mensagem de erro: "❌ Por favor, informe o local da coleta."
- ✅ Dados NÃO são adicionados

### Passo 9: Testar Validação de Arquivo
1. NÃO faça upload de arquivo
2. Preencha todos os outros campos
3. Clique em "Adicionar"

**Resultado Esperado:**
- ✅ Mensagem de erro: "❌ Por favor, faça o upload de um arquivo CSV."
- ✅ Dados NÃO são adicionados

---

## 🎯 Cenário de Teste 8: Limpar Análise

### Passo 10: Reiniciar Aplicação
1. Role a barra lateral até o final
2. Clique em **"🗑️ Limpar Análise / Reiniciar Sessão"**

**Resultado Esperado:**
- ✅ Mensagem de sucesso: "✅ Análise limpa com sucesso!"
- ✅ Tabela desaparece
- ✅ Gráficos desaparecem
- ✅ Filtro desaparece
- ✅ Mensagem inicial aparece novamente
- ✅ Aplicação volta ao estado inicial

---

## 📊 Checklist de Verificação Final

Após completar todos os testes, verifique:

- [ ] Upload de CSV funciona
- [ ] Validações impedem dados incorretos
- [ ] Dados são adicionados corretamente à tabela
- [ ] Médias são calculadas corretamente
- [ ] Filtro de local funciona
- [ ] Gráficos atualizam ao selecionar local
- [ ] Gráfico consolidado mostra 3 variáveis
- [ ] Gráficos individuais mostram Manhã vs Tarde
- [ ] CO₂ usa eixo Y secundário no gráfico consolidado
- [ ] Download de gráficos funciona
- [ ] Estatísticas são exibidas corretamente
- [ ] Limpar análise reseta tudo
- [ ] Interface é responsiva e intuitiva
- [ ] Mensagens de erro são claras

---

## 🐛 Teste de Casos Extremos

### Teste Extra 1: Múltiplas Coletas no Mesmo Dia
Adicione 3+ coletas para o mesmo local e data (variando apenas o período).

**Esperado:** Todas devem ser armazenadas e exibidas corretamente.

### Teste Extra 2: Nomes de Locais Similares
Adicione locais como "Casa 1", "Casa 2", "Casa  1" (com espaço extra).

**Esperado:** São tratados como locais diferentes.

### Teste Extra 3: Datas Diferentes
Adicione coletas para o mesmo local em datas diferentes (18/08, 19/08, 20/08).

**Esperado:** Gráficos mostram progressão temporal com múltiplas barras.

---

## ✅ Resultados Esperados Globais

Após completar todos os testes:

- ✅ **Funcionalidade**: 100% operacional
- ✅ **Validações**: Todas funcionando
- ✅ **Visualizações**: Gráficos corretos e interativos
- ✅ **Filtros**: Funcionam perfeitamente
- ✅ **Downloads**: Gráficos salvam em PNG
- ✅ **Performance**: Rápido e responsivo
- ✅ **UX**: Intuitivo e sem confusões

---

## 🎉 Conclusão

Se todos os testes passaram, a aplicação está **100% funcional e pronta para uso em produção**!

**Tempo total de teste:** ~10 minutos  
**Arquivos testados:** 5 CSVs de exemplo  
**Funcionalidades verificadas:** Todas (15+)  
**Status:** ✅ APROVADO
