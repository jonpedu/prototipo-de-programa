"""
Módulo de visualizações
Funções para criar gráficos Plotly para análise de dados ambientais
"""

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd


def create_temperature_chart(df, local_name):
    """
    Cria gráfico de barras para variação de temperatura por período
    
    Args:
        df: DataFrame filtrado com dados do local
        local_name: Nome do local para o título
        
    Returns:
        plotly.graph_objects.Figure: Gráfico de temperatura
    """
    # Preparar dados com ordenação cronológica correta
    df_sorted = df.copy()
    df_sorted['periodo_order'] = df_sorted['periodo'].map({'Manhã': 0, 'Tarde': 1})
    df_sorted = df_sorted.sort_values(['data', 'periodo_order'])
    df_sorted = df_sorted.drop('periodo_order', axis=1)
    df_sorted['data_str'] = df_sorted['data'].dt.strftime('%d/%m/%Y')
    
    # Separar dados por período
    df_manha = df_sorted[df_sorted['periodo'] == 'Manhã']
    df_tarde = df_sorted[df_sorted['periodo'] == 'Tarde']
    
    # Criar figura
    fig = go.Figure()
    
    # Adicionar barras para Manhã
    fig.add_trace(go.Bar(
        x=df_manha['data_str'],
        y=df_manha['temperatura'],
        name='Manhã',
        marker_color='#FF9999',
        text=df_manha['temperatura'].round(2),
        textposition='outside',
        texttemplate='%{text}°C',
        hovertemplate='<b>Manhã</b><br>Data: %{x}<br>Temperatura: %{y:.2f}°C<extra></extra>'
    ))
    
    # Adicionar barras para Tarde
    fig.add_trace(go.Bar(
        x=df_tarde['data_str'],
        y=df_tarde['temperatura'],
        name='Tarde',
        marker_color='#FF6666',
        text=df_tarde['temperatura'].round(2),
        textposition='outside',
        texttemplate='%{text}°C',
        hovertemplate='<b>Tarde</b><br>Data: %{x}<br>Temperatura: %{y:.2f}°C<extra></extra>'
    ))
    
    # Adicionar linha de média diária (pontilhada)
    df_media = df_sorted.groupby('data_str', sort=False)['temperatura'].mean().reset_index()
    fig.add_trace(go.Scatter(
        x=df_media['data_str'],
        y=df_media['temperatura'],
        name='Média Diária',
        mode='lines+markers',
        line=dict(color='#CC0000', width=2, dash='dash'),
        marker=dict(size=8, symbol='diamond', color='#CC0000'),
        hovertemplate='<b>Média Diária</b><br>Data: %{x}<br>Temperatura: %{y:.2f}°C<extra></extra>'
    ))
    
    # Obter ordem cronológica única das datas
    datas_ordenadas = df_sorted['data_str'].unique().tolist()
    
    # Layout
    fig.update_layout(
        title=f'Variação de Temperatura - {local_name}',
        xaxis_title='Data',
        yaxis_title='Temperatura (°C)',
        barmode='group',
        hovermode='x unified',
        template='plotly_white',
        height=400,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        xaxis=dict(
            categoryorder='array',
            categoryarray=datas_ordenadas
        )
    )
    
    return fig


def create_humidity_chart(df, local_name):
    """
    Cria gráfico de barras para variação de umidade por período
    
    Args:
        df: DataFrame filtrado com dados do local
        local_name: Nome do local para o título
        
    Returns:
        plotly.graph_objects.Figure: Gráfico de umidade
    """
    # Preparar dados com ordenação cronológica correta
    df_sorted = df.copy()
    df_sorted['periodo_order'] = df_sorted['periodo'].map({'Manhã': 0, 'Tarde': 1})
    df_sorted = df_sorted.sort_values(['data', 'periodo_order'])
    df_sorted = df_sorted.drop('periodo_order', axis=1)
    df_sorted['data_str'] = df_sorted['data'].dt.strftime('%d/%m/%Y')
    
    # Separar dados por período
    df_manha = df_sorted[df_sorted['periodo'] == 'Manhã']
    df_tarde = df_sorted[df_sorted['periodo'] == 'Tarde']
    
    # Criar figura
    fig = go.Figure()
    
    # Adicionar barras para Manhã
    fig.add_trace(go.Bar(
        x=df_manha['data_str'],
        y=df_manha['umidade'],
        name='Manhã',
        marker_color='#99CCFF',
        text=df_manha['umidade'].round(2),
        textposition='outside',
        texttemplate='%{text}%',
        hovertemplate='<b>Manhã</b><br>Data: %{x}<br>Umidade: %{y:.2f}%<extra></extra>'
    ))
    
    # Adicionar barras para Tarde
    fig.add_trace(go.Bar(
        x=df_tarde['data_str'],
        y=df_tarde['umidade'],
        name='Tarde',
        marker_color='#3399FF',
        text=df_tarde['umidade'].round(2),
        textposition='outside',
        texttemplate='%{text}%',
        hovertemplate='<b>Tarde</b><br>Data: %{x}<br>Umidade: %{y:.2f}%<extra></extra>'
    ))
    
    # Adicionar linha de média diária (pontilhada)
    df_media = df_sorted.groupby('data_str', sort=False)['umidade'].mean().reset_index()
    fig.add_trace(go.Scatter(
        x=df_media['data_str'],
        y=df_media['umidade'],
        name='Média Diária',
        mode='lines+markers',
        line=dict(color='#0066CC', width=2, dash='dash'),
        marker=dict(size=8, symbol='diamond', color='#0066CC'),
        hovertemplate='<b>Média Diária</b><br>Data: %{x}<br>Umidade: %{y:.2f}%<extra></extra>'
    ))
    
    # Obter ordem cronológica única das datas
    datas_ordenadas = df_sorted['data_str'].unique().tolist()
    
    # Layout
    fig.update_layout(
        title=f'Variação de Umidade - {local_name}',
        xaxis_title='Data',
        yaxis_title='Umidade (%)',
        barmode='group',
        hovermode='x unified',
        template='plotly_white',
        height=400,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        xaxis=dict(
            categoryorder='array',
            categoryarray=datas_ordenadas
        )
    )
    
    return fig


def create_co2_chart(df, local_name):
    """
    Cria gráfico de barras para variação de CO₂ por período
    
    Args:
        df: DataFrame filtrado com dados do local
        local_name: Nome do local para o título
        
    Returns:
        plotly.graph_objects.Figure: Gráfico de CO₂
    """
    # Preparar dados com ordenação cronológica correta
    df_sorted = df.copy()
    df_sorted['periodo_order'] = df_sorted['periodo'].map({'Manhã': 0, 'Tarde': 1})
    df_sorted = df_sorted.sort_values(['data', 'periodo_order'])
    df_sorted = df_sorted.drop('periodo_order', axis=1)
    df_sorted['data_str'] = df_sorted['data'].dt.strftime('%d/%m/%Y')
    
    # Separar dados por período
    df_manha = df_sorted[df_sorted['periodo'] == 'Manhã']
    df_tarde = df_sorted[df_sorted['periodo'] == 'Tarde']
    
    # Criar figura
    fig = go.Figure()
    
    # Adicionar barras para Manhã
    fig.add_trace(go.Bar(
        x=df_manha['data_str'],
        y=df_manha['co2'],
        name='Manhã',
        marker_color='#99FF99',
        text=df_manha['co2'].round(2),
        textposition='outside',
        texttemplate='%{text} ppm',
        hovertemplate='<b>Manhã</b><br>Data: %{x}<br>CO₂: %{y:.2f} ppm<extra></extra>'
    ))
    
    # Adicionar barras para Tarde
    fig.add_trace(go.Bar(
        x=df_tarde['data_str'],
        y=df_tarde['co2'],
        name='Tarde',
        marker_color='#33CC33',
        text=df_tarde['co2'].round(2),
        textposition='outside',
        texttemplate='%{text} ppm',
        hovertemplate='<b>Tarde</b><br>Data: %{x}<br>CO₂: %{y:.2f} ppm<extra></extra>'
    ))
    
    # Adicionar linha de média diária (pontilhada)
    df_media = df_sorted.groupby('data_str', sort=False)['co2'].mean().reset_index()
    fig.add_trace(go.Scatter(
        x=df_media['data_str'],
        y=df_media['co2'],
        name='Média Diária',
        mode='lines+markers',
        line=dict(color='#009900', width=2, dash='dot'),
        marker=dict(size=8, symbol='diamond', color='#009900'),
        hovertemplate='<b>Média Diária</b><br>Data: %{x}<br>CO₂: %{y:.2f} ppm<extra></extra>'
    ))
    
    # Obter ordem cronológica única das datas
    datas_ordenadas = df_sorted['data_str'].unique().tolist()
    
    # Layout
    fig.update_layout(
        title=f'Variação de CO₂ - {local_name}',
        xaxis_title='Data',
        yaxis_title='CO₂ (ppm)',
        barmode='group',
        hovermode='x unified',
        template='plotly_white',
        height=400,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        xaxis=dict(
            categoryorder='array',
            categoryarray=datas_ordenadas
        )
    )
    
    return fig


def create_consolidated_chart(df, local_name):
    """
    Cria gráfico consolidado com todas as variáveis, destacando manhã/tarde e médias diárias
    
    Args:
        df: DataFrame filtrado com dados do local
        local_name: Nome do local para o título
        
    Returns:
        plotly.graph_objects.Figure: Gráfico consolidado
    """
    # Preparar dados com ordenação cronológica correta
    df_sorted = df.copy()
    df_sorted['periodo_order'] = df_sorted['periodo'].map({'Manhã': 0, 'Tarde': 1})
    df_sorted = df_sorted.sort_values(['data', 'periodo_order'])
    df_sorted = df_sorted.drop('periodo_order', axis=1)
    df_sorted['data_str'] = df_sorted['data'].dt.strftime('%d/%m/%Y')
    df_sorted['data_periodo'] = df_sorted['data_str'] + ' - ' + df_sorted['periodo']
    
    # Criar figura com eixo Y secundário
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Separar por período para barras lado a lado
    df_manha = df_sorted[df_sorted['periodo'] == 'Manhã']
    df_tarde = df_sorted[df_sorted['periodo'] == 'Tarde']
    
    # TEMPERATURA - Manhã e Tarde
    if not df_manha.empty:
        fig.add_trace(
            go.Bar(
                x=df_manha['data_str'],
                y=df_manha['temperatura'],
                name='Temp Manhã',
                marker_color='#FFB3B3',
                text=df_manha['temperatura'].round(1),
                texttemplate='%{text}°C',
                textposition='outside',
                hovertemplate='<b>Temperatura - Manhã</b><br>%{y:.1f}°C<extra></extra>'
            ),
            secondary_y=False
        )
    
    if not df_tarde.empty:
        fig.add_trace(
            go.Bar(
                x=df_tarde['data_str'],
                y=df_tarde['temperatura'],
                name='Temp Tarde',
                marker_color='#FF6666',
                text=df_tarde['temperatura'].round(1),
                texttemplate='%{text}°C',
                textposition='outside',
                hovertemplate='<b>Temperatura - Tarde</b><br>%{y:.1f}°C<extra></extra>'
            ),
            secondary_y=False
        )
    
    # UMIDADE - Manhã e Tarde
    if not df_manha.empty:
        fig.add_trace(
            go.Bar(
                x=df_manha['data_str'],
                y=df_manha['umidade'],
                name='Umid Manhã',
                marker_color='#99CCFF',
                text=df_manha['umidade'].round(1),
                texttemplate='%{text}%',
                textposition='outside',
                hovertemplate='<b>Umidade - Manhã</b><br>%{y:.1f}%<extra></extra>'
            ),
            secondary_y=False
        )
    
    if not df_tarde.empty:
        fig.add_trace(
            go.Bar(
                x=df_tarde['data_str'],
                y=df_tarde['umidade'],
                name='Umid Tarde',
                marker_color='#3399FF',
                text=df_tarde['umidade'].round(1),
                texttemplate='%{text}%',
                textposition='outside',
                hovertemplate='<b>Umidade - Tarde</b><br>%{y:.1f}%<extra></extra>'
            ),
            secondary_y=False
        )
    
    # Obter ordem cronológica única das datas ANTES do groupby
    datas_ordenadas = df_sorted['data_str'].unique().tolist()
    
    # Calcular médias diárias
    df_medias = df_sorted.groupby('data_str', sort=False).agg({
        'temperatura': 'mean',
        'umidade': 'mean',
        'co2': 'mean'
    }).reset_index()
    # Reordenar df_medias pela ordem cronológica original
    df_medias['data_str'] = pd.Categorical(df_medias['data_str'], categories=datas_ordenadas, ordered=True)
    df_medias = df_medias.sort_values('data_str')
    
    # LINHA MÉDIA DE TEMPERATURA (pontilhada)
    fig.add_trace(
        go.Scatter(
            x=df_medias['data_str'],
            y=df_medias['temperatura'],
            name='Média Temp',
            mode='lines+markers',
            line=dict(color='#CC0000', width=2, dash='dash'),
            marker=dict(size=8, symbol='diamond', color='#CC0000'),
            hovertemplate='<b>Média Diária Temp</b><br>%{y:.1f}°C<extra></extra>'
        ),
        secondary_y=False
    )
    
    # LINHA MÉDIA DE UMIDADE (pontilhada)
    fig.add_trace(
        go.Scatter(
            x=df_medias['data_str'],
            y=df_medias['umidade'],
            name='Média Umid',
            mode='lines+markers',
            line=dict(color='#0066CC', width=2, dash='dash'),
            marker=dict(size=8, symbol='diamond', color='#0066CC'),
            hovertemplate='<b>Média Diária Umid</b><br>%{y:.1f}%<extra></extra>'
        ),
        secondary_y=False
    )
    
    # CO₂ - Linha por período
    if not df_manha.empty:
        fig.add_trace(
            go.Scatter(
                x=df_manha['data_str'],
                y=df_manha['co2'],
                name='CO₂ Manhã',
                mode='lines+markers',
                line=dict(color='#66FF66', width=2),
                marker=dict(size=8, color='#66FF66'),
                hovertemplate='<b>CO₂ - Manhã</b><br>%{y:.0f} ppm<extra></extra>'
            ),
            secondary_y=True
        )
    
    if not df_tarde.empty:
        fig.add_trace(
            go.Scatter(
                x=df_tarde['data_str'],
                y=df_tarde['co2'],
                name='CO₂ Tarde',
                mode='lines+markers',
                line=dict(color='#33CC33', width=2),
                marker=dict(size=8, color='#33CC33'),
                hovertemplate='<b>CO₂ - Tarde</b><br>%{y:.0f} ppm<extra></extra>'
            ),
            secondary_y=True
        )
    
    # LINHA MÉDIA DE CO₂ (pontilhada)
    fig.add_trace(
        go.Scatter(
            x=df_medias['data_str'],
            y=df_medias['co2'],
            name='Média CO₂',
            mode='lines+markers',
            line=dict(color='#009900', width=3, dash='dot'),
            marker=dict(size=10, symbol='diamond', color='#009900'),
            hovertemplate='<b>Média Diária CO₂</b><br>%{y:.0f} ppm<extra></extra>'
        ),
        secondary_y=True
    )
    
    # Configurar títulos dos eixos
    fig.update_xaxes(title_text="Data")
    fig.update_yaxes(title_text="Temperatura (°C) / Umidade (%)", secondary_y=False)
    fig.update_yaxes(title_text="CO₂ (ppm)", secondary_y=True)
    
    # Layout
    fig.update_layout(
        title=f'Análise Consolidada - {local_name}',
        barmode='group',
        hovermode='x unified',
        template='plotly_white',
        height=600,
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=1.15,
            bgcolor="rgba(255,255,255,0.8)",
            bordercolor="gray",
            borderwidth=1
        ),
        # Garantir que os eixos não se sobreponham
        yaxis=dict(side='left'),
        yaxis2=dict(side='right', overlaying='y'),
        margin=dict(r=200),  # Espaço para a legenda
        xaxis=dict(
            categoryorder='array',
            categoryarray=datas_ordenadas
        )
    )
    
    return fig


def create_comparison_chart(df, variable='temperatura'):
    """
    Cria gráfico comparativo entre todos os locais para uma variável específica
    
    Args:
        df: DataFrame completo com todos os locais
        variable: Nome da variável a ser comparada ('temperatura', 'umidade', 'co2')
        
    Returns:
        plotly.graph_objects.Figure: Gráfico comparativo
    """
    # Configurações por variável
    config = {
        'temperatura': {
            'title': 'Comparação de Temperatura entre Locais',
            'yaxis': 'Temperatura (°C)',
            'color': '#FF6666',
            'suffix': '°C'
        },
        'umidade': {
            'title': 'Comparação de Umidade entre Locais',
            'yaxis': 'Umidade (%)',
            'color': '#3399FF',
            'suffix': '%'
        },
        'co2': {
            'title': 'Comparação de CO₂ entre Locais',
            'yaxis': 'CO₂ (ppm)',
            'color': '#33CC33',
            'suffix': ' ppm'
        }
    }
    
    cfg = config.get(variable, config['temperatura'])
    
    # Agrupar por local e calcular média
    df_grouped = df.groupby('local')[variable].mean().reset_index()
    df_grouped = df_grouped.sort_values(variable, ascending=False)
    
    # Criar figura
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=df_grouped['local'],
        y=df_grouped[variable],
        marker_color=cfg['color'],
        text=df_grouped[variable].round(2),
        texttemplate='%{text}' + cfg['suffix'],
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>' + cfg['yaxis'] + ': %{y:.2f}' + cfg['suffix'] + '<extra></extra>'
    ))
    
    # Layout
    fig.update_layout(
        title=cfg['title'],
        xaxis_title='Local',
        yaxis_title=cfg['yaxis'],
        template='plotly_white',
        height=400,
        showlegend=False
    )
    
    return fig
