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
<<<<<<< HEAD
st.sidebar.header("📥 Adicionar Nova Coleta")
st.sidebar.markdown("Faça o upload do arquivo CSV e preencha os metadados da coleta.")

# Widgets de entrada
uploaded_file = st.sidebar.file_uploader(
    "Arquivo de Dados (Excel ou CSV)",
    type=['xlsx', 'xls', 'csv'],
    help="Arquivo Excel (.xlsx, .xls) ou CSV contendo as colunas: temperatura, umidade e co2"
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
=======
st.sidebar.header("📥 Upload de Coletas")
st.sidebar.markdown("Faça upload de um ou mais arquivos e configure os metadados.")
>>>>>>> secundária

# Nome do local (comum para todos os arquivos)
local_coleta = st.sidebar.text_input(
    "Local da Coleta",
    placeholder="Ex: Casa Vermelha",
    help="Nome do local (aplicado a todos os arquivos)"
)

# Upload múltiplo de arquivos
uploaded_files = st.sidebar.file_uploader(
    "Arquivos de Dados (Excel ou CSV)",
    type=['xlsx', 'xls', 'csv'],
    accept_multiple_files=True,
    help="Selecione um ou mais arquivos contendo: temperatura, umidade e co2"
)

# Se houver arquivos, mostrar configuração individual
if uploaded_files:
    st.sidebar.markdown("---")
    st.sidebar.subheader("📋 Configurar Cada Arquivo")
    
    # Dicionário temporário para armazenar metadados (não usar session_state para files)
    current_metadata = {}
    
    # Para cada arquivo, criar campos de data e período
    for idx, file in enumerate(uploaded_files):
        with st.sidebar.expander(f"📄 {file.name}", expanded=True):
            col1, col2 = st.columns(2)
            
            with col1:
                data = st.date_input(
                    "Data",
                    value=datetime.now(),
                    key=f"data_{idx}_{file.name}",
                    help="Data da coleta"
                )
            
            with col2:
                periodo = st.selectbox(
                    "Período",
                    options=["Manhã", "Tarde"],
                    key=f"periodo_{idx}_{file.name}",
                    help="Período do dia"
                )
            
            # Armazenar metadados no dicionário temporário
            current_metadata[file.name] = {
                'file': file,
                'data': data,
                'periodo': periodo
            }
    
    # Botão para processar todos os arquivos
    st.sidebar.markdown("---")
    if st.sidebar.button("➕ Adicionar Todos à Análise", type="primary", use_container_width=True):
        if not local_coleta:
            st.sidebar.error("❌ Por favor, preencha o nome do local!")
        else:
            success_count = 0
            error_count = 0
            errors_list = []
            
            # Processar cada arquivo do dicionário temporário
            for filename, metadata in current_metadata.items():
                try:
                    # Processar arquivo
                    new_row = process_uploaded_file(
                        metadata['file'],
                        metadata['data'],
                        local_coleta,
                        metadata['periodo']
                    )
                    
                    # Adicionar ao DataFrame mestre
                    st.session_state.master_df = pd.concat(
                        [st.session_state.master_df, new_row],
                        ignore_index=True
                    )
                    success_count += 1
                    
                except Exception as e:
                    error_count += 1
                    errors_list.append(f"{filename}: {str(e)}")
            
            # Mensagens de resultado
            if success_count > 0:
                st.sidebar.success(f"✅ {success_count} arquivo(s) adicionado(s) com sucesso!")
            
            if error_count > 0:
                st.sidebar.error(f"❌ {error_count} arquivo(s) com erro:")
                for error_msg in errors_list:
                    st.sidebar.error(f"  • {error_msg}")
            
            # Forçar rerun para atualizar visualizações
            if success_count > 0:
                st.rerun()

# Botão para limpar análise
st.sidebar.markdown("---")
if st.sidebar.button("🗑️ Limpar Análise / Reiniciar", use_container_width=True):
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
    
<<<<<<< HEAD
    1. **Faça o upload** de um arquivo Excel (.xlsx) ou CSV contendo as colunas: `temperatura`, `umidade` e `co2`
    2. **Selecione a data** da coleta
    3. **Escolha o período** (Manhã ou Tarde)
    4. **Digite o nome do local** da coleta
    5. **Clique em "Adicionar Dados à Análise"**
    
    Os dados serão processados e os gráficos serão gerados automaticamente! ✨
    
    💡 **Aceita:** Arquivos Excel (.xlsx, .xls) e CSV (com qualquer delimitador)
=======
    1. **Digite o nome do local** da coleta (aplicado a todos os arquivos)
    2. **Faça upload de um ou mais arquivos** Excel (.xlsx) ou CSV contendo: `temperatura`, `umidade` e `co2`
    3. **Configure cada arquivo individualmente:**
       - Selecione a **data** da coleta
       - Escolha o **período** (Manhã ou Tarde)
    4. **Clique em "Adicionar Todos à Análise"**
    
    Os dados serão processados e os gráficos gerados automaticamente! ✨
    
    💡 **Dica:** Você pode fazer upload de múltiplos arquivos de uma vez e configurar data/turno para cada um!
>>>>>>> secundária
    """)
else:
    # Exibir DataFrame mestre
    st.subheader("📊 Dados Consolidados")
    
<<<<<<< HEAD
    # Criar cópia formatada para exibição com valores min/max
    display_df = st.session_state.master_df.copy()
    display_df['data'] = pd.to_datetime(display_df['data']).dt.strftime('%d/%m/%Y')
    
    # Arredondar valores médios
=======
    # Adicionar barra de ferramentas de gerenciamento
    col_tools1, col_tools2, col_tools3, col_tools4 = st.columns(4)
    
    with col_tools1:
        # Botão para exportar dados para CSV
        if st.button("💾 Exportar CSV", use_container_width=True):
            csv_data = st.session_state.master_df.to_csv(index=False)
            st.download_button(
                label="⬇️ Baixar arquivo CSV",
                data=csv_data,
                file_name=f"dados_ambientais_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                use_container_width=True
            )
    
    with col_tools2:
        # Botão para editar local em massa
        if st.button("✏️ Renomear Local", use_container_width=True):
            st.session_state.show_rename_modal = True
    
    with col_tools3:
        # Seletor de linhas para deletar
        if st.button("🗑️ Excluir Registros", use_container_width=True):
            st.session_state.show_delete_modal = True
    
    with col_tools4:
        # Estatísticas gerais
        if st.button("📊 Ver Estatísticas", use_container_width=True):
            st.session_state.show_stats_modal = True
    
    # Modal de renomear local
    if 'show_rename_modal' in st.session_state and st.session_state.show_rename_modal:
        with st.expander("✏️ Renomear Local", expanded=True):
            unique_locals = sorted(st.session_state.master_df['local'].unique())
            col_r1, col_r2, col_r3 = st.columns([2, 2, 1])
            
            with col_r1:
                old_name = st.selectbox("Local atual:", unique_locals, key="rename_old")
            with col_r2:
                new_name = st.text_input("Novo nome:", key="rename_new")
            with col_r3:
                st.write("")
                st.write("")
                if st.button("✅ Aplicar", key="rename_apply"):
                    if new_name:
                        st.session_state.master_df.loc[
                            st.session_state.master_df['local'] == old_name, 'local'
                        ] = new_name
                        st.success(f"Local '{old_name}' renomeado para '{new_name}'!")
                        st.session_state.show_rename_modal = False
                        st.rerun()
            
            if st.button("❌ Cancelar", key="rename_cancel"):
                st.session_state.show_rename_modal = False
                st.rerun()
    
    # Modal de exclusão
    if 'show_delete_modal' in st.session_state and st.session_state.show_delete_modal:
        with st.expander("🗑️ Excluir Registros", expanded=True):
            st.warning("⚠️ Atenção: Esta ação não pode ser desfeita!")
            
            # Criar tabela interativa para seleção
            delete_df = st.session_state.master_df.copy()
            delete_df['ID'] = range(len(delete_df))
            delete_df['data_formatada'] = pd.to_datetime(delete_df['data']).dt.strftime('%d/%m/%Y')
            
            # Mostrar tabela com checkbox
            display_delete = delete_df[['ID', 'data_formatada', 'local', 'periodo', 'temperatura', 'umidade', 'co2']]
            display_delete.columns = ['ID', 'Data', 'Local', 'Período', 'Temp (°C)', 'Umid (%)', 'CO₂ (ppm)']
            
            st.dataframe(display_delete, use_container_width=True, hide_index=True)
            
            # Opções de exclusão
            col_d1, col_d2, col_d3 = st.columns(3)
            
            with col_d1:
                delete_option = st.radio(
                    "Modo de exclusão:",
                    ["Por IDs específicos", "Por Local", "Por Data"],
                    key="delete_mode"
                )
            
            with col_d2:
                if delete_option == "Por IDs específicos":
                    ids_to_delete = st.multiselect(
                        "Selecione IDs:",
                        options=delete_df['ID'].tolist(),
                        key="delete_ids"
                    )
                elif delete_option == "Por Local":
                    local_to_delete = st.selectbox(
                        "Selecione Local:",
                        options=sorted(st.session_state.master_df['local'].unique()),
                        key="delete_local"
                    )
                else:  # Por Data
                    dates_available = pd.to_datetime(st.session_state.master_df['data']).dt.strftime('%d/%m/%Y').unique()
                    date_to_delete = st.selectbox(
                        "Selecione Data:",
                        options=sorted(dates_available),
                        key="delete_date"
                    )
            
            with col_d3:
                st.write("")
                st.write("")
                if st.button("🗑️ Confirmar Exclusão", key="delete_confirm", type="primary"):
                    if delete_option == "Por IDs específicos" and ids_to_delete:
                        st.session_state.master_df = st.session_state.master_df.drop(ids_to_delete).reset_index(drop=True)
                        st.success(f"✅ {len(ids_to_delete)} registro(s) excluído(s)!")
                    elif delete_option == "Por Local":
                        count = len(st.session_state.master_df[st.session_state.master_df['local'] == local_to_delete])
                        st.session_state.master_df = st.session_state.master_df[
                            st.session_state.master_df['local'] != local_to_delete
                        ].reset_index(drop=True)
                        st.success(f"✅ {count} registro(s) do local '{local_to_delete}' excluído(s)!")
                    elif delete_option == "Por Data":
                        date_obj = datetime.strptime(date_to_delete, '%d/%m/%Y')
                        count = len(st.session_state.master_df[
                            pd.to_datetime(st.session_state.master_df['data']).dt.strftime('%d/%m/%Y') == date_to_delete
                        ])
                        st.session_state.master_df = st.session_state.master_df[
                            pd.to_datetime(st.session_state.master_df['data']).dt.strftime('%d/%m/%Y') != date_to_delete
                        ].reset_index(drop=True)
                        st.success(f"✅ {count} registro(s) da data '{date_to_delete}' excluído(s)!")
                    
                    st.session_state.show_delete_modal = False
                    st.rerun()
            
            if st.button("❌ Cancelar", key="delete_cancel"):
                st.session_state.show_delete_modal = False
                st.rerun()
    
    # Modal de estatísticas
    if 'show_stats_modal' in st.session_state and st.session_state.show_stats_modal:
        with st.expander("📊 Estatísticas Gerais", expanded=True):
            col_s1, col_s2, col_s3 = st.columns(3)
            
            with col_s1:
                st.metric("Total de Coletas", len(st.session_state.master_df))
                st.metric("Locais Diferentes", st.session_state.master_df['local'].nunique())
                st.metric("Datas Diferentes", st.session_state.master_df['data'].nunique())
            
            with col_s2:
                st.write("**Por Período:**")
                periodo_counts = st.session_state.master_df['periodo'].value_counts()
                for periodo, count in periodo_counts.items():
                    st.write(f"- {periodo}: {count}")
                
            with col_s3:
                st.write("**Por Local:**")
                local_counts = st.session_state.master_df['local'].value_counts()
                for local, count in local_counts.items():
                    st.write(f"- {local}: {count}")
            
            st.markdown("---")
            
            # Estatísticas globais
            st.write("**📈 Estatísticas Globais (todos os locais):**")
            stats_global = pd.DataFrame({
                'Variável': ['Temperatura (°C)', 'Umidade (%)', 'CO₂ (ppm)'],
                'Média': [
                    st.session_state.master_df['temperatura'].mean(),
                    st.session_state.master_df['umidade'].mean(),
                    st.session_state.master_df['co2'].mean()
                ],
                'Mínimo': [
                    st.session_state.master_df['temperatura'].min(),
                    st.session_state.master_df['umidade'].min(),
                    st.session_state.master_df['co2'].min()
                ],
                'Máximo': [
                    st.session_state.master_df['temperatura'].max(),
                    st.session_state.master_df['umidade'].max(),
                    st.session_state.master_df['co2'].max()
                ],
                'Desvio Padrão': [
                    st.session_state.master_df['temperatura'].std(),
                    st.session_state.master_df['umidade'].std(),
                    st.session_state.master_df['co2'].std()
                ]
            })
            st.dataframe(stats_global.round(2), use_container_width=True, hide_index=True)
            
            if st.button("✅ Fechar", key="stats_close"):
                st.session_state.show_stats_modal = False
                st.rerun()
    
    st.markdown("---")
    
    # Criar cópia formatada para exibição com min/max
    display_df = st.session_state.master_df.copy()
    display_df['data'] = pd.to_datetime(display_df['data']).dt.strftime('%d/%m/%Y')
    
    # Calcular min/max por local
    for idx, row in display_df.iterrows():
        local_data = st.session_state.master_df[st.session_state.master_df['local'] == row['local']]
        display_df.at[idx, 'temp_min'] = local_data['temperatura'].min()
        display_df.at[idx, 'temp_max'] = local_data['temperatura'].max()
        display_df.at[idx, 'umid_min'] = local_data['umidade'].min()
        display_df.at[idx, 'umid_max'] = local_data['umidade'].max()
        display_df.at[idx, 'co2_min'] = local_data['co2'].min()
        display_df.at[idx, 'co2_max'] = local_data['co2'].max()
    
    # Arredondar valores
>>>>>>> secundária
    display_df['temperatura'] = display_df['temperatura'].round(2)
    display_df['umidade'] = display_df['umidade'].round(2)
    display_df['co2'] = display_df['co2'].round(2)
    
<<<<<<< HEAD
    # Calcular valores mínimos e máximos para cada variável por local
    for _, row in display_df.iterrows():
        local_data = st.session_state.master_df[st.session_state.master_df['local'] == row['local']]
        display_df.loc[display_df.index == _, 'temp_min'] = local_data['temperatura'].min()
        display_df.loc[display_df.index == _, 'temp_max'] = local_data['temperatura'].max()
        display_df.loc[display_df.index == _, 'umid_min'] = local_data['umidade'].min()
        display_df.loc[display_df.index == _, 'umid_max'] = local_data['umidade'].max()
        display_df.loc[display_df.index == _, 'co2_min'] = local_data['co2'].min()
        display_df.loc[display_df.index == _, 'co2_max'] = local_data['co2'].max()
    
    # Reordenar colunas para melhor visualização
=======
    # Reordenar colunas
>>>>>>> secundária
    display_df = display_df[[
        'temperatura', 'temp_min', 'temp_max',
        'umidade', 'umid_min', 'umid_max',
        'co2', 'co2_min', 'co2_max',
        'data', 'local', 'periodo'
    ]]
    
    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "temperatura": st.column_config.NumberColumn("Temperatura (°C)", format="%.2f"),
<<<<<<< HEAD
            "temp_min": st.column_config.NumberColumn("Temp. Mín ⬇️", format="%.2f", help="Menor temperatura registrada neste local"),
            "temp_max": st.column_config.NumberColumn("Temp. Máx ⬆️", format="%.2f", help="Maior temperatura registrada neste local"),
            "umidade": st.column_config.NumberColumn("Umidade (%)", format="%.2f"),
            "umid_min": st.column_config.NumberColumn("Umid. Mín ⬇️", format="%.2f", help="Menor umidade registrada neste local"),
            "umid_max": st.column_config.NumberColumn("Umid. Máx ⬆️", format="%.2f", help="Maior umidade registrada neste local"),
            "co2": st.column_config.NumberColumn("CO₂ (ppm)", format="%.2f"),
            "co2_min": st.column_config.NumberColumn("CO₂ Mín ⬇️", format="%.2f", help="Menor CO₂ registrado neste local"),
            "co2_max": st.column_config.NumberColumn("CO₂ Máx ⬆️", format="%.2f", help="Maior CO₂ registrado neste local"),
=======
            "temp_min": st.column_config.NumberColumn("Temp Mín ⬇️", format="%.2f"),
            "temp_max": st.column_config.NumberColumn("Temp Máx ⬆️", format="%.2f"),
            "umidade": st.column_config.NumberColumn("Umidade (%)", format="%.2f"),
            "umid_min": st.column_config.NumberColumn("Umid Mín ⬇️", format="%.2f"),
            "umid_max": st.column_config.NumberColumn("Umid Máx ⬆️", format="%.2f"),
            "co2": st.column_config.NumberColumn("CO₂ (ppm)", format="%.2f"),
            "co2_min": st.column_config.NumberColumn("CO₂ Mín ⬇️", format="%.2f"),
            "co2_max": st.column_config.NumberColumn("CO₂ Máx ⬆️", format="%.2f"),
>>>>>>> secundária
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
    
    # Converter data para datetime para ordenação cronológica
    filtered_df['data'] = pd.to_datetime(filtered_df['data'])
    # Ordenar por data E período para garantir ordem cronológica correta
    filtered_df['periodo_order'] = filtered_df['periodo'].map({'Manhã': 0, 'Tarde': 1})
    filtered_df = filtered_df.sort_values(['data', 'periodo_order'])
    filtered_df = filtered_df.drop('periodo_order', axis=1)
    
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
            st.markdown("##### 📈 Estatísticas Resumidas")
            stats_df = pd.DataFrame({
                'Variável': ['Temperatura (°C)', 'Umidade (%)', 'CO₂ (ppm)'],
                'Média': [
                    filtered_df['temperatura'].mean(),
                    filtered_df['umidade'].mean(),
                    filtered_df['co2'].mean()
                ],
                'Mínimo': [
                    filtered_df['temperatura'].min(),
                    filtered_df['umidade'].min(),
                    filtered_df['co2'].min()
                ],
                'Máximo': [
                    filtered_df['temperatura'].max(),
                    filtered_df['umidade'].max(),
                    filtered_df['co2'].max()
                ],
                'Amplitude': [
                    filtered_df['temperatura'].max() - filtered_df['temperatura'].min(),
                    filtered_df['umidade'].max() - filtered_df['umidade'].min(),
                    filtered_df['co2'].max() - filtered_df['co2'].min()
                ]
            })
            st.dataframe(
                stats_df.round(2),
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Variável": st.column_config.TextColumn("Variável", width="medium"),
                    "Média": st.column_config.NumberColumn("Média", format="%.2f"),
                    "Mínimo": st.column_config.NumberColumn("Mínimo ⬇️", format="%.2f"),
                    "Máximo": st.column_config.NumberColumn("Máximo ⬆️", format="%.2f"),
                    "Amplitude": st.column_config.NumberColumn("Amplitude", format="%.2f")
                }
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
