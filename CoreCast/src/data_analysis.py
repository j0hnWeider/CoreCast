import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_histogram(df: pd.DataFrame, column: str):
    """
    Plota um histograma para a coluna especificada.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f'Histograma de {column}')
    plt.show()

def plot_correlation_heatmap(df: pd.DataFrame):
    """
    Plota um mapa de calor das correlações entre as variáveis numéricas.
    """
    plt.figure(figsize=(12, 8))
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Mapa de Calor das Correlações')
    plt.show()
