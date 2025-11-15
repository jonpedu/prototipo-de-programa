"""
Aplicação Interativa para Análise de Dados Ambientais
Desenvolvida com Streamlit para análise comparativa de temperatura, umidade e CO₂
"""

import streamlit as st
import pandas as pd
from datetime import datetime
from data_processor import process_uploaded_file, validate_inputs
from visualizations import (
    create_temperature_chart,
    create_humidity_chart,
    create_co2_chart,
    create_consolidated_chart
)

# Configuração da página
st.set_page_config(
    page_title="Análise de Dados Ambientais",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("🌱 Análise de Dados Ambientais")
st.markdown("---")

# Inicialização do estado da sessão
if 'master_df' not in st.session_state:
    st.session_state.master_df = pd.DataFrame(
        columns=['temperatura', 'umidade', 'co2', 'data', 'local', 'periodo']
    )

# ========== BARRA LATERAL: INSERÇÃO DE DADOS ==========
st.sidebar.header("📥 Adicionar Nova Coleta")
st.sidebar.markdown("Faça o upload do arquivo CSV e preencha os metadados da coleta.")

# Widgets de entrada
uploaded_file = st.sidebar.file_uploader(
    "Arquivo CSV (temperatura, umidade, co2)",
    type=['csv'],
    help="Arquivo CSV contendo as colunas: temperatura, umidade e co2"
)

data_coleta = st.sidebar.date_input(
    "Data da Coleta",
    value=datetime.now(),
    help="Selecione a data em que a coleta foi realizada"
)

periodo_coleta = st.sidebar.selectbox(
    "Período da Coleta",
    options=["Manhã", "Tarde"],
    help="Selecione o período do dia"
)

local_coleta = st.sidebar.text_input(
    "Local da Coleta",
    placeholder="Ex: Casa com Ype",
    help="Digite o nome do local onde a coleta foi realizada"
)

# Botão para adicionar dados
if st.sidebar.button("➕ Adicionar Dados à Análise", type="primary", use_container_width=True):
    # Validação dos inputs
    validation_error = validate_inputs(uploaded_file, local_coleta)
    
    if validation_error:
        st.sidebar.error(validation_error)
    else:
        try:
            # Processar arquivo e adicionar ao DataFrame mestre
            new_row = process_uploaded_file(
                uploaded_file,
                data_coleta,
                local_coleta,
                periodo_coleta
            )
            
            # Adicionar nova linha ao DataFrame mestre
            st.session_state.master_df = pd.concat(
                [st.session_state.master_df, new_row],
                ignore_index=True
            )
            
            st.sidebar.success(f"✅ Dados adicionados com sucesso! ({local_coleta} - {periodo_coleta})")
            st.rerun()
            
        except Exception as e:
            st.sidebar.error(f"❌ Erro ao processar arquivo: {str(e)}")

# Botão para limpar análise
st.sidebar.markdown("---")
if st.sidebar.button("🗑️ Limpar Análise / Reiniciar Sessão", use_container_width=True):
    st.session_state.master_df = pd.DataFrame(
        columns=['temperatura', 'umidade', 'co2', 'data', 'local', 'periodo']
    )
    st.sidebar.success("✅ Análise limpa com sucesso!")
    st.rerun()

# ========== ÁREA PRINCIPAL: VISUALIZAÇÃO E ANÁLISE ==========

# Verificar se há dados para exibir
if st.session_state.master_df.empty:
    st.info("👈 Use a barra lateral para adicionar sua primeira coleta de dados.")
    st.markdown("""
    ### 📋 Como usar esta aplicação:
    
    1. **Faça o upload** de um arquivo CSV contendo as colunas: `temperatura`, `umidade` e `co2`
    2. **Selecione a data** da coleta
    3. **Escolha o período** (Manhã ou Tarde)
    4. **Digite o nome do local** da coleta
    5. **Clique em "Adicionar Dados à Análise"**
    
    Os dados serão processados e os gráficos serão gerados automaticamente! ✨
    """)
else:
    # Exibir DataFrame mestre
    st.subheader("📊 Dados Consolidados")
    
    # Criar cópia formatada para exibição
    display_df = st.session_state.master_df.copy()
    display_df['data'] = pd.to_datetime(display_df['data']).dt.strftime('%d/%m/%Y')
    display_df['temperatura'] = display_df['temperatura'].round(2)
    display_df['umidade'] = display_df['umidade'].round(2)
    display_df['co2'] = display_df['co2'].round(2)
    
    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "temperatura": st.column_config.NumberColumn("Temperatura (°C)", format="%.2f"),
            "umidade": st.column_config.NumberColumn("Umidade (%)", format="%.2f"),
            "co2": st.column_config.NumberColumn("CO₂ (ppm)", format="%.2f"),
            "data": "Data",
            "local": "Local",
            "periodo": "Período"
        }
    )
    
    st.markdown("---")
    
    # Filtro por local
    unique_locals = sorted(st.session_state.master_df['local'].unique())
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        selected_local = st.selectbox(
            "🏠 Filtrar por Local:",
            options=unique_locals,
            help="Selecione um local para visualizar os dados específicos"
        )
    
    with col2:
        total_coletas = len(st.session_state.master_df)
        st.metric("Total de Coletas", total_coletas)
    
    with col3:
        total_locais = len(unique_locals)
        st.metric("Locais Diferentes", total_locais)
    
    # Filtrar dados pelo local selecionado
    filtered_df = st.session_state.master_df[
        st.session_state.master_df['local'] == selected_local
    ].copy()
    
    # Converter data para datetime para ordenação
    filtered_df['data'] = pd.to_datetime(filtered_df['data'])
    filtered_df = filtered_df.sort_values('data')
    
    st.markdown("---")
    st.subheader(f"📈 Análise Gráfica - {selected_local}")
    
    # Verificar se há dados suficientes
    if filtered_df.empty:
        st.warning(f"Nenhum dado encontrado para o local: {selected_local}")
    else:
        # Gráfico consolidado em destaque
        st.markdown("#### 📊 Visão Geral Consolidada")
        consolidated_fig = create_consolidated_chart(filtered_df, selected_local)
        st.plotly_chart(consolidated_fig, use_container_width=True)
        
        st.markdown("---")
        
        # Gráficos individuais em colunas
        st.markdown("#### 🔍 Análises Detalhadas por Variável")
        
        col_left, col_right = st.columns(2)
        
        with col_left:
            st.markdown("##### 🌡️ Temperatura")
            temp_fig = create_temperature_chart(filtered_df, selected_local)
            st.plotly_chart(temp_fig, use_container_width=True)
            
            st.markdown("##### 💧 Umidade")
            humidity_fig = create_humidity_chart(filtered_df, selected_local)
            st.plotly_chart(humidity_fig, use_container_width=True)
        
        with col_right:
            st.markdown("##### 🌫️ CO₂")
            co2_fig = create_co2_chart(filtered_df, selected_local)
            st.plotly_chart(co2_fig, use_container_width=True)
            
            # Estatísticas resumidas
            st.markdown("##### 📈 Estatísticas")
            stats_df = pd.DataFrame({
                'Métrica': ['Temperatura (°C)', 'Umidade (%)', 'CO₂ (ppm)'],
                'Média': [
                    filtered_df['temperatura'].mean(),
                    filtered_df['umidade'].mean(),
                    filtered_df['co2'].mean()
                ],
                'Mín': [
                    filtered_df['temperatura'].min(),
                    filtered_df['umidade'].min(),
                    filtered_df['co2'].min()
                ],
                'Máx': [
                    filtered_df['temperatura'].max(),
                    filtered_df['umidade'].max(),
                    filtered_df['co2'].max()
                ]
            })
            st.dataframe(
                stats_df.round(2),
                use_container_width=True,
                hide_index=True
            )

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; font-size: 0.9em;'>
    💡 Dica: Use o ícone da câmera nos gráficos para fazer o download em PNG
    </div>
    """,
    unsafe_allow_html=True
)
