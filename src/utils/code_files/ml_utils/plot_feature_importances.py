import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_feature_importances(importance, features, model_name, title='Feature Importances'):
    df = pd.DataFrame({'Feature': features, 'Importance': importance})
    df = df.sort_values(by='Importance', ascending=False)
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Importance', y='Feature', data=df, palette='viridis')
    plt.title(f'{title} for {model_name}')
    plt.tight_layout()
    plt.savefig(f'src/utils/objects/{model_name}_feature_importances.png')
    plt.close()