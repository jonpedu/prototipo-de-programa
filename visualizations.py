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
    # Preparar dados
    df_sorted = df.sort_values('data')
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
    # Preparar dados
    df_sorted = df.sort_values('data')
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
    # Preparar dados
    df_sorted = df.sort_values('data')
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
        )
    )
    
    return fig


def create_consolidated_chart(df, local_name):
    """
    Cria gráfico consolidado com todas as variáveis, usando eixo Y secundário para CO₂
    
    Args:
        df: DataFrame filtrado com dados do local
        local_name: Nome do local para o título
        
    Returns:
        plotly.graph_objects.Figure: Gráfico consolidado
    """
    # Preparar dados
    df_sorted = df.sort_values('data')
    df_sorted['data_str'] = df_sorted['data'].dt.strftime('%d/%m/%Y')
    
    # Criar figura com eixo Y secundário
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Agrupar por data para ter uma barra por data (média dos períodos)
    df_grouped = df_sorted.groupby('data_str').agg({
        'temperatura': 'mean',
        'umidade': 'mean',
        'co2': 'mean'
    }).reset_index()
    
    # Adicionar barras para Temperatura (eixo Y primário)
    fig.add_trace(
        go.Bar(
            x=df_grouped['data_str'],
            y=df_grouped['temperatura'],
            name='Temperatura (°C)',
            marker_color='#FF6666',
            text=df_grouped['temperatura'].round(2),
            texttemplate='%{text}°C',
            textposition='outside',
            hovertemplate='<b>Temperatura</b><br>%{y:.2f}°C<extra></extra>'
        ),
        secondary_y=False
    )
    
    # Adicionar barras para Umidade (eixo Y primário)
    fig.add_trace(
        go.Bar(
            x=df_grouped['data_str'],
            y=df_grouped['umidade'],
            name='Umidade (%)',
            marker_color='#3399FF',
            text=df_grouped['umidade'].round(2),
            texttemplate='%{text}%',
            textposition='outside',
            hovertemplate='<b>Umidade</b><br>%{y:.2f}%<extra></extra>'
        ),
        secondary_y=False
    )
    
    # Adicionar barras para CO₂ (eixo Y secundário)
    fig.add_trace(
        go.Bar(
            x=df_grouped['data_str'],
            y=df_grouped['co2'],
            name='CO₂ (ppm)',
            marker_color='#33CC33',
            text=df_grouped['co2'].round(2),
            texttemplate='%{text} ppm',
            textposition='outside',
            hovertemplate='<b>CO₂</b><br>%{y:.2f} ppm<extra></extra>'
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
        height=500,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
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
