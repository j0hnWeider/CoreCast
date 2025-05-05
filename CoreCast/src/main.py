from src.data_processing import load_data, preprocess_data
from src.data_analysis import plot_histogram, plot_correlation_heatmap
from src.modeling import train_model

def main():
    # Exemplo de uso do projeto
    data_path = 'data/exemplo_dados.csv'  # Substitua pelo caminho do seu arquivo de dados
    df = load_data(data_path)
    if df.empty:
        print("Nenhum dado carregado. Verifique o arquivo.")
        return

    df_clean = preprocess_data(df)

    # Análise exploratória
    if 'sensor_value' in df_clean.columns:
        plot_histogram(df_clean, 'sensor_value')
    plot_correlation_heatmap(df_clean)

    # Modelagem preditiva
    if 'target' in df_clean.columns:
        train_model(df_clean, 'target')
    else:
        print("Coluna 'target' não encontrada para modelagem.")

if __name__ == "__main__":
    main()
