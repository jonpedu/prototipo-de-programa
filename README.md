# 🌱 Aplicação de Análise de Dados Ambientais

Uma aplicação web interativa desenvolvida em **Streamlit** para análise comparativa de dados ambientais (temperatura, umidade e CO₂).

## 📋 Características

- ✅ **Interface intuitiva** com upload de arquivos CSV
- ✅ **Associação de metadados** via UI (data, local, período)
- ✅ **Gerenciamento de sessão** com múltiplas coletas
- ✅ **Visualizações interativas** com Plotly
- ✅ **Filtros dinâmicos** por local
- ✅ **Download de gráficos** em PNG
- ✅ **Arquitetura modular** e escalável
- ✅ **Análise consolidada** com eixo Y secundário

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos

1. **Clone ou baixe este projeto**

2. **Instale as dependências:**

```powershell
pip install -r requirements.txt
```

## 📂 Estrutura do Projeto

```
prototipo de programa/
├── app.py                  # Arquivo principal da aplicação
├── data_processor.py       # Módulo de processamento de dados
├── visualizations.py       # Módulo de visualizações Plotly
├── requirements.txt        # Dependências do projeto
├── README.md              # Este arquivo
└── exemplos/              # Arquivos CSV de exemplo
    ├── coleta1.csv
    ├── coleta2.csv
    └── coleta3.csv
```

## 🎮 Como Usar

### 1. Iniciar a aplicação

```powershell
streamlit run app.py
```

A aplicação abrirá automaticamente no seu navegador em `http://localhost:8501`

### 2. Adicionar dados

1. **Faça o upload** de um arquivo CSV na barra lateral
2. **Selecione a data** da coleta
3. **Escolha o período** (Manhã ou Tarde)
4. **Digite o nome do local** da coleta
5. **Clique em "Adicionar Dados à Análise"**

### 3. Visualizar análises

- Os gráficos são gerados automaticamente
- Use o filtro "Filtrar por Local" para selecionar o local desejado
- Todos os gráficos incluem a funcionalidade de download (ícone da câmera)

### 4. Gerenciar sessão

- Use "Limpar Análise / Reiniciar Sessão" para começar do zero

## 📊 Formato dos Arquivos CSV

Os arquivos CSV devem conter 3 colunas com dados numéricos:

### Opção 1: Com cabeçalho
```csv
temperatura,umidade,co2
32.5,68.1,405
33.1,67.5,410
32.9,69.2,408
```

### Opção 2: Sem cabeçalho
```csv
32.5,68.1,405
33.1,67.5,410
32.9,69.2,408
```

**Importante:** A aplicação calcula automaticamente a **média** de cada variável do arquivo e cria uma única entrada no DataFrame mestre.

## 📈 Tipos de Gráficos

A aplicação gera 4 tipos de visualizações:

1. **Gráfico Consolidado**: Visão geral com todas as variáveis (CO₂ em eixo Y secundário)
2. **Variação de Temperatura**: Comparação Manhã vs Tarde
3. **Variação de Umidade**: Comparação Manhã vs Tarde
4. **Variação de CO₂**: Comparação Manhã vs Tarde

## 🔧 Arquitetura

### Modelo de Dados Interno

O DataFrame mestre mantém a seguinte estrutura:

| temperatura | umidade | co2 | data | local | periodo |
|------------|---------|-----|------|-------|---------|
| 32.5 | 68.1 | 405 | 2025-08-18 | Casa com Ype | Manhã |
| 33.1 | 67.5 | 410 | 2025-08-18 | Casa Vermelha | Tarde |

### Fluxo de Dados

```
CSV Upload → Validação → Cálculo de Médias → DataFrame Mestre → Filtros → Visualizações
```

## 🛠️ Tecnologias Utilizadas

- **Streamlit**: Framework web para aplicações de dados
- **Pandas**: Manipulação e análise de dados
- **Plotly**: Visualizações interativas

## 💡 Dicas de Uso

- ✨ A aplicação mantém o estado durante toda a sessão
- ✨ Você pode adicionar quantos locais desejar
- ✨ Use nomes descritivos para os locais (ex: "Casa com Ype", "Laboratório A")
- ✨ Os gráficos são interativos - passe o mouse para ver detalhes
- ✨ Use o ícone da câmera nos gráficos para download em alta qualidade

## 🎯 Casos de Uso

### Exemplo 1: Comparação de ambientes
Compare a temperatura de diferentes cômodos de uma casa ao longo do dia.

### Exemplo 2: Monitoramento temporal
Acompanhe como as condições ambientais variam entre manhã e tarde em um local específico.

### Exemplo 3: Análise multi-local
Compare múltiplos locais diferentes em datas e períodos variados.

## ⚠️ Observações

- A aplicação processa arquivos CSV em formato UTF-8
- Valores não numéricos são automaticamente removidos
- Cada arquivo CSV representa uma coleta (a média é calculada automaticamente)
- O estado da sessão é perdido ao fechar o navegador

## 🐛 Solução de Problemas

### Erro ao fazer upload do arquivo
- Verifique se o arquivo tem exatamente 3 colunas
- Certifique-se de que os valores são numéricos
- Tente salvar o arquivo em formato UTF-8

### Gráficos não aparecem
- Verifique se você selecionou um local no filtro
- Certifique-se de que há dados para o local selecionado

### Aplicação não inicia
- Verifique se todas as dependências foram instaladas
- Confirme que está usando Python 3.8 ou superior

## 📞 Suporte

Para questões ou problemas, verifique:
1. Se todas as dependências estão instaladas corretamente
2. Se os arquivos CSV estão no formato correto
3. Se há mensagens de erro no terminal

## 📄 Licença

Este projeto foi desenvolvido para análise de dados ambientais no contexto do PRODUTO 16 - Cientistas de Alcântara.

---

**Desenvolvido com ❤️ usando Streamlit**
