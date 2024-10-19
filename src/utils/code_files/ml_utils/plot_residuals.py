import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_residuals(y_true, y_pred, model_name):
    residuals = y_true - y_pred
    plt.figure(figsize=(10, 6))
    plt.scatter(y_pred, residuals, color='blue', edgecolor='k', alpha=0.7)
    plt.hlines(y=0, xmin=min(y_pred), xmax=max(y_pred), color='red', linestyle='--')
    plt.xlabel('Predicted values')
    plt.ylabel('Residuals')
    plt.title(f'{model_name}_Residual_Plot')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'src/utils/objects/{model_name}_residuals_plot.png')
    plt.close()