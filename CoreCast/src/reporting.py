import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd

def generate_report(data: pd.DataFrame, filename: str):
    """
    Gera um relatório PDF com gráficos básicos a partir dos dados fornecidos.

    :param data: DataFrame contendo os dados a serem analisados.
    :param filename: Nome do arquivo PDF de saída.
    """
    with PdfPages(filename) as pdf:
        plt.figure(figsize=(8, 6))
        data.plot(kind='line')
        plt.title('Relatório de Dados')
        plt.xlabel('Índice')
        plt.ylabel('Valores')
        plt.grid(True)
        pdf.savefig()
        plt.close()

        # Exemplo de outro gráfico
        plt.figure(figsize=(8, 6))
        data.hist()
        plt.suptitle('Histograma dos Dados')
        pdf.savefig()
        plt.close()
