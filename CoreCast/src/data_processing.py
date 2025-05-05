import pandas as pd
import numpy as np

def load_data(file_path: str) -> pd.DataFrame:
    """
    Carrega os dados de um arquivo CSV.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pré-processa os dados:
    - Remove valores nulos
    - Converte tipos de dados se necessário
    - Cria colunas derivadas se aplicável
    """
    df_clean = df.dropna()
    # Exemplo: converter colunas de data para datetime
    # if 'timestamp' in df_clean.columns:
    #     df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp'])
    return df_clean
