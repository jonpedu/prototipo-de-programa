"""
Módulo de processamento de dados
Funções para validação, leitura e transformação de dados CSV
"""

import pandas as pd
from io import StringIO


def validate_inputs(uploaded_file, local_coleta):
    """
    Valida os inputs do usuário antes de processar
    
    Args:
        uploaded_file: Arquivo CSV enviado pelo usuário
        local_coleta: Nome do local da coleta
        
    Returns:
        str: Mensagem de erro ou None se validação passou
    """
    if uploaded_file is None:
        return "❌ Por favor, faça o upload de um arquivo CSV."
    
    if not local_coleta or local_coleta.strip() == "":
        return "❌ Por favor, informe o local da coleta."
    
    return None


def process_uploaded_file(uploaded_file, data_coleta, local_coleta, periodo_coleta):
    """
    Processa o arquivo CSV enviado e retorna um DataFrame com uma linha contendo
    as médias e os metadados
    
    Args:
        uploaded_file: Arquivo CSV enviado
        data_coleta: Data da coleta (datetime)
        local_coleta: Nome do local da coleta
        periodo_coleta: Período da coleta (Manhã/Tarde)
        
    Returns:
        pd.DataFrame: DataFrame com uma linha contendo as médias e metadados
        
    Raises:
        Exception: Se houver erro ao processar o arquivo
    """
    try:
        # Ler o conteúdo do arquivo
        content = uploaded_file.getvalue().decode('utf-8')
        
        # Tentar ler o CSV - primeiro tentando com cabeçalho
        try:
            df_temp = pd.read_csv(StringIO(content))
            
            # Verificar se tem as colunas esperadas
            expected_cols = ['temperatura', 'umidade', 'co2']
            
            # Normalizar nomes das colunas (lowercase e sem espaços)
            df_temp.columns = df_temp.columns.str.lower().str.strip()
            
            # Verificar se todas as colunas necessárias estão presentes
            missing_cols = [col for col in expected_cols if col not in df_temp.columns]
            
            if missing_cols:
                # Se faltar colunas, tentar sem cabeçalho
                raise ValueError("Tentando sem cabeçalho")
                
        except (ValueError, KeyError):
            # Tentar ler sem cabeçalho
            df_temp = pd.read_csv(
                StringIO(content),
                header=None,
                names=['temperatura', 'umidade', 'co2']
            )
        
        # Validar que o DataFrame tem dados
        if df_temp.empty:
            raise ValueError("O arquivo CSV está vazio.")
        
        # Validar que tem pelo menos as 3 colunas necessárias
        if len(df_temp.columns) < 3:
            raise ValueError("O arquivo deve conter pelo menos 3 colunas: temperatura, umidade e co2.")
        
        # Selecionar apenas as colunas necessárias
        df_temp = df_temp[['temperatura', 'umidade', 'co2']]
        
        # Converter para numérico, tratando possíveis erros
        for col in ['temperatura', 'umidade', 'co2']:
            df_temp[col] = pd.to_numeric(df_temp[col], errors='coerce')
        
        # Remover linhas com valores inválidos
        df_temp = df_temp.dropna()
        
        if df_temp.empty:
            raise ValueError("Nenhum dado válido encontrado no arquivo.")
        
        # Calcular médias
        temp_media = df_temp['temperatura'].mean()
        umidade_media = df_temp['umidade'].mean()
        co2_media = df_temp['co2'].mean()
        
        # Criar DataFrame de uma linha com as médias e metadados
        new_row = pd.DataFrame({
            'temperatura': [temp_media],
            'umidade': [umidade_media],
            'co2': [co2_media],
            'data': [pd.to_datetime(data_coleta)],
            'local': [local_coleta.strip()],
            'periodo': [periodo_coleta]
        })
        
        return new_row
        
    except Exception as e:
        raise Exception(f"Erro ao processar arquivo: {str(e)}")


def format_dataframe_for_display(df):
    """
    Formata o DataFrame para exibição na UI
    
    Args:
        df: DataFrame a ser formatado
        
    Returns:
        pd.DataFrame: DataFrame formatado
    """
    display_df = df.copy()
    
    # Formatar data
    if 'data' in display_df.columns:
        display_df['data'] = pd.to_datetime(display_df['data']).dt.strftime('%d/%m/%Y')
    
    # Arredondar valores numéricos
    numeric_cols = ['temperatura', 'umidade', 'co2']
    for col in numeric_cols:
        if col in display_df.columns:
            display_df[col] = display_df[col].round(2)
    
    return display_df


def get_statistics_summary(df):
    """
    Calcula estatísticas resumidas para um DataFrame
    
    Args:
        df: DataFrame com dados ambientais
        
    Returns:
        dict: Dicionário com estatísticas por variável
    """
    stats = {}
    
    for var in ['temperatura', 'umidade', 'co2']:
        if var in df.columns:
            stats[var] = {
                'media': df[var].mean(),
                'minimo': df[var].min(),
                'maximo': df[var].max(),
                'desvio_padrao': df[var].std()
            }
    
    return stats
