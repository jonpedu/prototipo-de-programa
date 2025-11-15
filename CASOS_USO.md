# 💼 Casos de Uso Práticos

## Cenários Reais de Aplicação

### 🏠 Caso de Uso 1: Monitoramento Residencial

**Objetivo:** Comparar diferentes ambientes de uma casa ao longo do dia.

**Exemplo:**
```
Local: Quarto
- Manhã: 25°C, 60%, 400 ppm
- Tarde: 28°C, 65%, 420 ppm

Local: Sala
- Manhã: 27°C, 58%, 410 ppm
- Tarde: 30°C, 62%, 430 ppm

Local: Cozinha
- Manhã: 26°C, 70%, 450 ppm
- Tarde: 32°C, 75%, 500 ppm
```

**Como usar:**
1. Prepare um CSV para cada medição
2. Adicione todas as coletas com nomes de locais distintos
3. Use o filtro para alternar entre os ambientes
4. Baixe os gráficos comparativos

**Insights esperados:**
- Identificar qual ambiente tem melhor qualidade do ar
- Ver qual período (manhã/tarde) é mais confortável
- Detectar ambientes com CO₂ elevado

---

### 🌳 Caso de Uso 2: Comparação de Áreas Arborizadas

**Objetivo:** Avaliar impacto da vegetação na qualidade do ar.

**Exemplo:**
```
Local: Casa com Ypê (árvore grande)
Local: Casa sem Vegetação
Local: Casa com Jardim
```

**Como usar:**
1. Coletar dados nos mesmos horários
2. Usar mesmas datas para comparação justa
3. Adicionar todas as coletas
4. Comparar os valores médios de CO₂

**Insights esperados:**
- Áreas arborizadas tendem a ter menor CO₂
- Temperatura pode ser mais amena perto de vegetação
- Umidade pode ser mais alta em áreas verdes

---

### 🔬 Caso de Uso 3: Experimento Científico Escolar

**Objetivo:** Projeto de ciências sobre qualidade do ar.

**Coletas Sugeridas:**
```
Semana 1:
- Segunda: Sala de aula fechada (manhã e tarde)
- Terça: Sala de aula aberta (manhã e tarde)

Semana 2:
- Segunda: Com plantas na sala (manhã e tarde)
- Terça: Sem plantas na sala (manhã e tarde)
```

**Como usar:**
1. Coletar dados sistematicamente
2. Manter padrão de nomenclatura dos locais
3. Registrar todas as variáveis contextuais
4. Usar gráficos para apresentação do projeto

**Relatório:**
- Exportar gráficos em PNG
- Incluir tabela de dados
- Apresentar análise estatística

---

### 🏢 Caso de Uso 4: Qualidade de Ar em Escritório

**Objetivo:** Otimizar ventilação e conforto térmico.

**Locais a Monitorar:**
```
- Sala de reuniões (antes e depois de reunião longa)
- Área de trabalho aberta
- Sala com ar-condicionado
- Área próxima às janelas
```

**Análise:**
- CO₂ > 1000 ppm → Ventilação inadequada
- Temperatura ideal: 20-24°C
- Umidade ideal: 40-60%

---

### 📊 Caso de Uso 5: Estudo Longitudinal

**Objetivo:** Acompanhar mudanças ao longo do tempo.

**Estratégia:**
```
Semana 1: Medições diárias (manhã/tarde)
Semana 2: Medições diárias (manhã/tarde)
...
Semana N: Medições diárias (manhã/tarde)
```

**Padrão de Nomenclatura:**
```
Local: Casa Principal - Semana 1
Local: Casa Principal - Semana 2
```

**Benefícios:**
- Ver evolução temporal
- Identificar padrões sazonais
- Detectar anomalias

---

## 🎯 Dicas para Coletas Eficazes

### ✅ Boas Práticas

1. **Nomenclatura Consistente**
   - Use nomes claros e descritivos
   - Mantenha padrão: "Local - Contexto"
   - Ex: "Sala - Com Ventilador", "Sala - Sem Ventilador"

2. **Horários Padronizados**
   - Manhã: 08:00-12:00
   - Tarde: 12:00-18:00
   - Mantenha consistência

3. **Número de Medições**
   - Mínimo: 10 leituras por arquivo CSV
   - Ideal: 50-100 leituras
   - Intervalo: A cada 30s ou 1min

4. **Condições Controladas**
   - Anote variáveis externas (chuva, sol, etc.)
   - Mantenha sensor na mesma posição
   - Evite obstruções

5. **Documentação**
   - Registre contexto de cada coleta
   - Anote eventos especiais
   - Mantenha log de alterações no ambiente

---

## 📈 Interpretação dos Resultados

### Temperatura
- **< 18°C**: Frio
- **18-24°C**: Confortável
- **24-28°C**: Quente
- **> 28°C**: Muito quente

### Umidade
- **< 30%**: Muito seco (desconfortável)
- **30-40%**: Seco
- **40-60%**: Ideal
- **60-70%**: Úmido
- **> 70%**: Muito úmido

### CO₂
- **< 400 ppm**: Ar externo (referência)
- **400-600 ppm**: Excelente
- **600-800 ppm**: Bom
- **800-1000 ppm**: Aceitável
- **1000-1500 ppm**: Ruim (ventilar)
- **> 1500 ppm**: Péssimo (ventilação urgente)

---

## 🔍 Análise Comparativa

### Comparar Dois Locais

**Método:**
1. Adicione coletas dos dois locais
2. Use o filtro para ver cada um separadamente
3. Compare visualmente os gráficos
4. Observe as estatísticas (média, mín, máx)

**Perguntas a Fazer:**
- Qual local tem menor CO₂?
- Qual é mais estável termicamente?
- Qual tem umidade mais adequada?
- Qual varia mais entre manhã e tarde?

### Comparar Manhã vs Tarde

**Método:**
1. Adicione coletas do mesmo local em ambos períodos
2. Observe as barras lado a lado nos gráficos
3. Calcule a diferença percentual

**Insights:**
- Tarde geralmente mais quente
- CO₂ pode acumular ao longo do dia
- Umidade pode variar com temperatura

---

## 💡 Ideias de Projetos

### Projeto 1: "Impacto das Plantas"
Compare ambientes com e sem plantas

### Projeto 2: "Ventilação Natural vs Artificial"
Compare sala com janelas abertas vs ar-condicionado

### Projeto 3: "Densidade de Ocupação"
Meça CO₂ com diferentes números de pessoas

### Projeto 4: "Orientação Solar"
Compare ambientes voltados para norte, sul, leste, oeste

### Projeto 5: "Isolamento Térmico"
Compare casas com diferentes tipos de construção

---

## 📋 Template de Relatório

```markdown
# Relatório de Análise Ambiental

## Informações Gerais
- **Data**: [data]
- **Locais Analisados**: [lista]
- **Períodos**: Manhã e Tarde
- **Número de Coletas**: [número]

## Metodologia
[Descrever como os dados foram coletados]

## Resultados

### Local 1: [nome]
- Temperatura Média: X°C
- Umidade Média: Y%
- CO₂ Médio: Z ppm

[Inserir gráfico]

### Local 2: [nome]
...

## Análise Comparativa
[Comparar os locais]

## Conclusões
[Insights principais]

## Recomendações
[Ações sugeridas]
```

---

## 🎓 Para Educadores

### Atividade 1: Método Científico
Ensine hipótese → experimento → análise → conclusão

### Atividade 2: Análise de Dados
Ensine leitura e interpretação de gráficos

### Atividade 3: Sustentabilidade
Discuta qualidade do ar e conforto ambiental

### Atividade 4: Estatística
Ensine conceitos de média, mínimo, máximo

### Atividade 5: Tecnologia
Mostre como sensores e software auxiliam pesquisa

---

**Explore, experimente e descubra! 🚀**
