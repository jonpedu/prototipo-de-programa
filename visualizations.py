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
    
    # Obter ordem cronológica das datas
    datas_ordenadas = df_sorted['data_str'].unique().tolist()
    
    # Separar dados por período
    df_manha = df_sorted[df_sorted['periodo'] == 'Manhã']
    df_tarde = df_sorted[df_sorted['periodo'] == 'Tarde']
    
    # Criar figura
    fig = go.Figure()
    
    # Adicionar linha de média diária PRIMEIRO (fica atrás das barras)
    df_media_diaria = df_sorted.groupby('data_str', sort=False)['temperatura'].mean().reset_index()
    fig.add_trace(go.Scatter(
        x=df_media_diaria['data_str'],
        y=df_media_diaria['temperatura'],
        name='Média Diária',
        mode='lines+markers',
        line=dict(color='#CC0000', width=2, dash='dash'),
        marker=dict(size=8, symbol='diamond'),
        opacity=0.4,
        hovertemplate='<b>Média Diária</b><br>Data: %{x}<br>Temperatura: %{y:.2f}°C<extra></extra>'
    ))
    
    # Adicionar barras para Manhã (por cima das linhas)
    fig.add_trace(go.Bar(
        x=df_manha['data_str'],
        y=df_manha['temperatura'],
        name='Manhã',
        marker_color='#FF9999',
        text=df_manha['temperatura'].round(1),
        textposition='outside',
        texttemplate='<b>%{text}°C</b>',
        textfont=dict(size=16, color='#000000', family='Arial Black'),
        hovertemplate='<b>Manhã</b><br>Data: %{x}<br>Temperatura: %{y:.2f}°C<extra></extra>'
    ))
    
    # Adicionar barras para Tarde (por cima das linhas)
    fig.add_trace(go.Bar(
        x=df_tarde['data_str'],
        y=df_tarde['temperatura'],
        name='Tarde',
        marker_color='#FF6666',
        text=df_tarde['temperatura'].round(1),
        textposition='outside',
        texttemplate='<b>%{text}°C</b>',
        textfont=dict(size=16, color='#000000', family='Arial Black'),
        hovertemplate='<b>Tarde</b><br>Data: %{x}<br>Temperatura: %{y:.2f}°C<extra></extra>'
    ))
    
<<<<<<< HEAD
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
=======
    # Layout com margem superior e ordem cronológica forçada
    max_temp = df_sorted['temperatura'].max()
>>>>>>> secundária
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
<<<<<<< HEAD
=======
        yaxis=dict(range=[0, max_temp * 1.15]),  # 15% de margem superior
>>>>>>> secundária
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
    
    # Obter ordem cronológica das datas
    datas_ordenadas = df_sorted['data_str'].unique().tolist()
    
    # Separar dados por período
    df_manha = df_sorted[df_sorted['periodo'] == 'Manhã']
    df_tarde = df_sorted[df_sorted['periodo'] == 'Tarde']
    
    # Criar figura
    fig = go.Figure()
    
    # Adicionar linha de média diária PRIMEIRO (fica atrás das barras)
    df_media_diaria = df_sorted.groupby('data_str', sort=False)['umidade'].mean().reset_index()
    fig.add_trace(go.Scatter(
        x=df_media_diaria['data_str'],
        y=df_media_diaria['umidade'],
        name='Média Diária',
        mode='lines+markers',
        line=dict(color='#0066CC', width=2, dash='dash'),
        marker=dict(size=8, symbol='diamond'),
        opacity=0.4,
        hovertemplate='<b>Média Diária</b><br>Data: %{x}<br>Umidade: %{y:.2f}%<extra></extra>'
    ))
    
    # Adicionar barras para Manhã (por cima das linhas)
    fig.add_trace(go.Bar(
        x=df_manha['data_str'],
        y=df_manha['umidade'],
        name='Manhã',
        marker_color='#99CCFF',
        text=df_manha['umidade'].round(1),
        textposition='outside',
        texttemplate='<b>%{text}%</b>',
        textfont=dict(size=16, color='#000000', family='Arial Black'),
        hovertemplate='<b>Manhã</b><br>Data: %{x}<br>Umidade: %{y:.2f}%<extra></extra>'
    ))
    
    # Adicionar barras para Tarde (por cima das linhas)
    fig.add_trace(go.Bar(
        x=df_tarde['data_str'],
        y=df_tarde['umidade'],
        name='Tarde',
        marker_color='#3399FF',
        text=df_tarde['umidade'].round(1),
        textposition='outside',
        texttemplate='<b>%{text}%</b>',
        textfont=dict(size=16, color='#000000', family='Arial Black'),
        hovertemplate='<b>Tarde</b><br>Data: %{x}<br>Umidade: %{y:.2f}%<extra></extra>'
    ))
    
<<<<<<< HEAD
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
=======
    # Layout com margem superior e ordem cronológica forçada
    max_umid = df_sorted['umidade'].max()
>>>>>>> secundária
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
<<<<<<< HEAD
=======
        yaxis=dict(range=[0, max_umid * 1.15]),  # 15% de margem superior
>>>>>>> secundária
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
    
    # Obter ordem cronológica das datas
    datas_ordenadas = df_sorted['data_str'].unique().tolist()
    
    # Separar dados por período
    df_manha = df_sorted[df_sorted['periodo'] == 'Manhã']
    df_tarde = df_sorted[df_sorted['periodo'] == 'Tarde']
    
    # Criar figura
    fig = go.Figure()
    
    # Adicionar linha de média diária PRIMEIRO (fica atrás das barras)
    df_media_diaria = df_sorted.groupby('data_str', sort=False)['co2'].mean().reset_index()
    fig.add_trace(go.Scatter(
        x=df_media_diaria['data_str'],
        y=df_media_diaria['co2'],
        name='Média Diária',
        mode='lines+markers',
        line=dict(color='#009900', width=2, dash='dash'),
        marker=dict(size=8, symbol='diamond'),
        opacity=0.4,
        hovertemplate='<b>Média Diária</b><br>Data: %{x}<br>CO₂: %{y:.2f} ppm<extra></extra>'
    ))
    
    # Adicionar barras para Manhã (por cima das linhas)
    fig.add_trace(go.Bar(
        x=df_manha['data_str'],
        y=df_manha['co2'],
        name='Manhã',
        marker_color='#99FF99',
        text=df_manha['co2'].round(1),
        textposition='outside',
        texttemplate='<b>%{text} ppm</b>',
        textfont=dict(size=16, color='#000000', family='Arial Black'),
        hovertemplate='<b>Manhã</b><br>Data: %{x}<br>CO₂: %{y:.2f} ppm<extra></extra>'
    ))
    
    # Adicionar barras para Tarde (por cima das linhas)
    fig.add_trace(go.Bar(
        x=df_tarde['data_str'],
        y=df_tarde['co2'],
        name='Tarde',
        marker_color='#33CC33',
        text=df_tarde['co2'].round(1),
        textposition='outside',
        texttemplate='<b>%{text} ppm</b>',
        textfont=dict(size=16, color='#000000', family='Arial Black'),
        hovertemplate='<b>Tarde</b><br>Data: %{x}<br>CO₂: %{y:.2f} ppm<extra></extra>'
    ))
    
<<<<<<< HEAD
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
=======
    # Layout com margem superior e ordem cronológica forçada
    max_co2 = df_sorted['co2'].max()
>>>>>>> secundária
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
<<<<<<< HEAD
=======
        yaxis=dict(range=[0, max_co2 * 1.15]),  # 15% de margem superior
>>>>>>> secundária
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
    
    # Obter ordem cronológica das datas
    datas_ordenadas = df_sorted['data_str'].unique().tolist()
    
    # Criar figura com eixo Y secundário
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
<<<<<<< HEAD
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
=======
    # Separar por período
    df_manha = df_sorted[df_sorted['periodo'] == 'Manhã']
    df_tarde = df_sorted[df_sorted['periodo'] == 'Tarde']
    
    # Linhas de média diária PRIMEIRO (ficam atrás) com opacidade reduzida
    df_media = df_sorted.groupby('data_str', sort=False).agg({
>>>>>>> secundária
        'temperatura': 'mean',
        'umidade': 'mean',
        'co2': 'mean'
    }).reset_index()
    # Reordenar df_medias pela ordem cronológica original
    df_medias['data_str'] = pd.Categorical(df_medias['data_str'], categories=datas_ordenadas, ordered=True)
    df_medias = df_medias.sort_values('data_str')
    
<<<<<<< HEAD
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
=======
    # Média Temperatura (atrás)
    fig.add_trace(
        go.Scatter(
            x=df_media['data_str'],
            y=df_media['temperatura'],
            name='Média Temp',
            mode='lines',
            line=dict(color='#CC0000', width=2, dash='dash'),
            opacity=0.4,
            hovertemplate='<b>Média Temperatura</b><br>%{y:.1f}°C<extra></extra>'
>>>>>>> secundária
        ),
        secondary_y=False
    )
    
<<<<<<< HEAD
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
=======
    # Média Umidade (atrás)
    fig.add_trace(
        go.Scatter(
            x=df_media['data_str'],
            y=df_media['umidade'],
            name='Média Umid',
            mode='lines',
            line=dict(color='#0066CC', width=2, dash='dash'),
            opacity=0.4,
            hovertemplate='<b>Média Umidade</b><br>%{y:.1f}%<extra></extra>'
>>>>>>> secundária
        ),
        secondary_y=False
    )
    
<<<<<<< HEAD
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
=======
    # Média CO₂ (atrás)
    fig.add_trace(
        go.Scatter(
            x=df_media['data_str'],
            y=df_media['co2'],
            name='Média CO₂',
            mode='lines',
            line=dict(color='#009900', width=2, dash='dash'),
            opacity=0.4,
            hovertemplate='<b>Média CO₂</b><br>%{y:.1f} ppm<extra></extra>'
>>>>>>> secundária
        ),
        secondary_y=True
    )
    
    # Temperatura - Barras Manhã (por cima das linhas)
    fig.add_trace(
        go.Bar(
            x=df_manha['data_str'],
            y=df_manha['temperatura'],
            name='Temp Manhã',
            marker_color='#FF9999',
            text=df_manha['temperatura'].round(1),
            texttemplate='<b>%{text}°C</b>',
            textposition='outside',
            textfont=dict(size=15, color='#000000', family='Arial Black'),
            hovertemplate='<b>Temperatura - Manhã</b><br>%{y:.1f}°C<extra></extra>'
        ),
        secondary_y=False
    )
    
    # Temperatura - Barras Tarde (por cima das linhas)
    fig.add_trace(
        go.Bar(
            x=df_tarde['data_str'],
            y=df_tarde['temperatura'],
            name='Temp Tarde',
            marker_color='#FF6666',
            text=df_tarde['temperatura'].round(1),
            texttemplate='<b>%{text}°C</b>',
            textposition='outside',
            textfont=dict(size=15, color='#000000', family='Arial Black'),
            hovertemplate='<b>Temperatura - Tarde</b><br>%{y:.1f}°C<extra></extra>'
        ),
        secondary_y=False
    )
    
    # Umidade - Barras Manhã (por cima das linhas)
    fig.add_trace(
        go.Bar(
            x=df_manha['data_str'],
            y=df_manha['umidade'],
            name='Umid Manhã',
            marker_color='#99CCFF',
            text=df_manha['umidade'].round(1),
            texttemplate='<b>%{text}%</b>',
            textposition='outside',
            textfont=dict(size=15, color='#000000', family='Arial Black'),
            hovertemplate='<b>Umidade - Manhã</b><br>%{y:.1f}%<extra></extra>'
        ),
        secondary_y=False
    )
    
    # Umidade - Barras Tarde (por cima das linhas)
    fig.add_trace(
        go.Bar(
            x=df_tarde['data_str'],
            y=df_tarde['umidade'],
            name='Umid Tarde',
            marker_color='#3399FF',
            text=df_tarde['umidade'].round(1),
            texttemplate='<b>%{text}%</b>',
            textposition='outside',
            textfont=dict(size=15, color='#000000', family='Arial Black'),
            hovertemplate='<b>Umidade - Tarde</b><br>%{y:.1f}%<extra></extra>'
        ),
        secondary_y=False
    )
    
    # CO₂ - Linha Manhã (eixo secundário, por cima de tudo)
    fig.add_trace(
        go.Scatter(
            x=df_manha['data_str'],
            y=df_manha['co2'],
            name='CO₂ Manhã',
            mode='lines+markers+text',
            line=dict(color='#33CC33', width=3),
            marker=dict(size=10, color='#33CC33'),
            text=df_manha['co2'].round(1),
            texttemplate='<b>%{text} ppm</b>',
            textposition='top center',
            textfont=dict(size=15, color='#000000', family='Arial Black'),
            hovertemplate='<b>CO₂ - Manhã</b><br>%{y:.1f} ppm<extra></extra>'
        ),
        secondary_y=True
    )
    
    # CO₂ - Linha Tarde (eixo secundário, por cima de tudo)
    fig.add_trace(
        go.Scatter(
            x=df_tarde['data_str'],
            y=df_tarde['co2'],
            name='CO₂ Tarde',
            mode='lines+markers+text',
            line=dict(color='#228B22', width=3),
            marker=dict(size=10, color='#228B22'),
            text=df_tarde['co2'].round(1),
            texttemplate='<b>%{text} ppm</b>',
            textposition='top center',
            textfont=dict(size=15, color='#000000', family='Arial Black'),
            hovertemplate='<b>CO₂ - Tarde</b><br>%{y:.1f} ppm<extra></extra>'
        ),
        secondary_y=True
    )
    
    # Calcular máximos para margem superior
    max_temp_umid = max(df_sorted['temperatura'].max(), df_sorted['umidade'].max())
    max_co2 = df_sorted['co2'].max()
    
    # Configurar títulos dos eixos
    fig.update_xaxes(
        title_text="Data",
        categoryorder='array',
        categoryarray=datas_ordenadas
    )
    fig.update_yaxes(
        title_text="Temperatura (°C) / Umidade (%)",
        secondary_y=False,
        range=[0, max_temp_umid * 1.15]
    )
    fig.update_yaxes(
        title_text="CO₂ (ppm)",
        secondary_y=True,
        range=[0, max_co2 * 1.15]
    )
    
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
<<<<<<< HEAD
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
=======
            x=1.02
>>>>>>> secundária
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
