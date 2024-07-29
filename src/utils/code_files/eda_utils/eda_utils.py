import numpy as np
import os
import pandas as pd
import yaml
import zipfile
import shutil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
from prettytable import PrettyTable
from scipy import stats


def category_column_analysis(df:pd.DataFrame,col:str,target:str,n_rows:int=5,countplot:bool=True,boxplot:bool=True)->None:
    ## Unique Value Count
    print(f'Value Counts of Top {n_rows} Frequent elements of Column: {col}')
    print('\n')
    val_cnt=pd.DataFrame(df[col].value_counts()).reset_index().sort_values(by='count',ascending=False)
    mean_targets=[]
    for row in range(val_cnt.shape[0]):
        mean_target=df[df[col]==val_cnt.iloc[row,0]][target].mean()
        mean_targets.append(round(mean_target,2))

    val_cnt['Mean_of_target']=mean_targets
    
    t=PrettyTable()
    t.field_names=[col,'Count','Mean of Target']
    for row in range(n_rows):
        t.add_row(val_cnt.loc[row])
    print(t)
    print('\n')

    #Basic Column Info
    print(f'Basic Info of Column {col}')
    print('\n')
    t=PrettyTable()
    t.field_names=['Measure','Value']
    t.add_row(['Distinct Count', df[col].nunique()])
    t.add_row(['Missing Count', df[col].isna().sum()])
    t.add_row(['Missing %', df[col].isna().sum()/df.shape[0]*100])
    print(t)
    print('\n')


    #Count Plot
    value_count = df[col].value_counts()

    # Select the top 5 most frequently occurring states
    top_n = value_count.nlargest(n_rows).index

    # Filter the DataFrame to include only the top 5 states
    filtered_df = df[df[col].isin(top_n)]
    
    # Create a countplot 
    if countplot==True:
        sns.set_theme(style="darkgrid")
        plt.figure(figsize=(10, 6))
        palette = sns.color_palette("husl", len(top_n))
        plot = sns.countplot(x=col, hue=col, data=filtered_df, order=top_n, palette=palette, dodge=False)

        # Adding labels on top of the bars
        for p in plot.patches:
            plot.annotate(format(p.get_height(), '.0f'), 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha = 'center', va = 'center', 
                        xytext = (0, 9), 
                        textcoords = 'offset points')


        # Adding labels and title
        plt.xlabel(col,fontsize=12)
        plt.ylabel('Count',fontsize=12)
        plt.title(f'Count of {col}',fontsize=16)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
    #Boxplot
    if boxplot==True:
        sns.set_theme(style="darkgrid")

    # Create a box plot of state with listed_price
        plt.figure(figsize=(12, 8))
        plot = sns.boxplot(x=filtered_df[target].apply(np.log), y=col, data=filtered_df)

        # Adding labels and title
        plt.xlabel(target, fontsize=14)
        plt.ylabel(col, fontsize=14)
        plt.title(f'Box Plot of {target} by {col}', fontsize=16)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
    return

def numeric_column_analysis(df:pd.DataFrame,col:str,target:str,n_rows:int=5
                            ,dist_plot:bool=True,bins:int=20,box_plot:bool=True,line_plot:bool=True
                            ,value_counts:bool=True,basic_info:bool=True,quantile:bool=True,extreme:bool=True)-> None:
    
    if value_counts==True:
    #Value Count of top n most frequently occuring elements with mean of target
        print(f'Value Counts of Top {n_rows} Frequent elements of Column: {col}')
        print('\n')
        val_cnt=pd.DataFrame(df[col].value_counts()).reset_index().sort_values(by='count',ascending=False)
        mean_targets=[]
        for row in range(val_cnt.shape[0]):
            mean_target=df[df[col]==val_cnt.iloc[row,0]][target].mean()
            mean_targets.append(round(mean_target,2))

        val_cnt['Mean_of_target']=mean_targets
        
        t=PrettyTable()
        t.field_names=[col,'Count','Mean of Target']
        for row in range(n_rows):
            t.add_row(val_cnt.loc[row])
        print(t)
        print('\n')

    #Basic info of column
    if basic_info==True:
        print(f'Basic Info of Column {col}')
        t = PrettyTable(['Measure', 'Value'])
        t.add_row(['Distinct Count', df[col].nunique()])
        t.add_row(['Distinct %', df[col].nunique()/df.shape[0]*100])
        t.add_row(['Missing Count', df[col].isna().sum()])
        t.add_row(['Missing %', df[col].isna().sum()/df.shape[0]*100])
        t.add_row(['Mean', df[col].mean()])
        t.add_row(['Minimum', df[col].min()])
        t.add_row(['Maximum', df[col].max()])
        print(t)
        print('\n')

    #Quantile stats for column
    if quantile==True: 
        quantile_stats = {}
        quantile_stats['min'] = df[col].min()
        quantile_stats['5%'] = df[col].quantile(0.05)
        quantile_stats['Q1'] = df[col].quantile(0.25)
        quantile_stats['median'] = df[col].median()
        quantile_stats['Q3'] = df[col].quantile(0.75)
        quantile_stats['95%'] = df[col].quantile(0.95)
        quantile_stats['max'] = df[col].max()
        quantile_stats['IQR'] = quantile_stats['Q3'] - quantile_stats['Q1']

        # Display the quantile stats
        print(f'Quantile stats for column "{col}"')
        t = PrettyTable(['Statistic', 'Value'])
        t.add_row(['Minimum', quantile_stats['min']])
        t.add_row(['5th Percentile', quantile_stats['5%']])
        t.add_row(['First Quartile, Q1', quantile_stats['Q1']])
        t.add_row(['Median', quantile_stats['median']])
        t.add_row(['Third Quartile, Q3', quantile_stats['Q3']])
        t.add_row(['95th Percentile', quantile_stats['95%']])
        t.add_row(['Maximum', quantile_stats['max']])
        t.add_row(['Interquartile Range', quantile_stats['IQR']])
        print(t)

        print('\n')

    #Maximum and Min n values along with count
    if extreme==True:

        extremums_max = pd.DataFrame(df[col].value_counts().sort_index(ascending=False).head(n=n_rows).reset_index())
        extremums_min = pd.DataFrame(df[col].value_counts().sort_index(ascending=True).head(n=n_rows).reset_index())

        # Display the extremums
        print(f'Extremums for column "{col}"')

        print(f'Maximum {n_rows} values')
        t = PrettyTable([col, 'Count'])
        for row in range(n_rows):
            t.add_row(extremums_max.loc[row])

        print(t)

        print(f'Minimum {n_rows} values')
        t = PrettyTable([col, 'Count'])
        for row in range(n_rows):
            t.add_row(extremums_min.loc[row])
        print(t)

        print('\n')

    if dist_plot==True:
        sns.set_theme(style="dark")
        plt.figure(figsize=(10, 6))  # Set the figure size
        sns.histplot(x=df[col], bins=bins, kde=True, color='skyblue', edgecolor='black')

        # Add titles and labels
        plt.title('Histogram of {}'.format(col), fontsize=16)
        plt.xlabel(col, fontsize=14)
        plt.ylabel('Frequency', fontsize=14)

        # Customize the grid
        plt.grid(True, linestyle='--', alpha=0.7)

        # Adjust the ticks
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.gca().set_facecolor('#2E2E2E')
        plt.show()
    if box_plot==True:
        
        plt.figure(figsize=(10, 6))  # Set the figure size
        sns.boxplot(x=df[col])

        # Add titles and labels
        plt.title('Boxplot of {}'.format(col), fontsize=16)
        plt.xlabel(col, fontsize=14)

        # Adjust the ticks
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        
        plt.show()
    if line_plot==True:
        plt.figure(figsize=(10, 6))
        sns.lineplot(df, x=df[col], y=df[target])
        plt.title('Lineplot of {}'.format(col), fontsize=16)
        plt.xlabel(col, fontsize=14)

        # Adjust the ticks
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.show()
    return


def annova_test(df: pd.DataFrame, col: str, q: float = 0.05):
    df = df.copy()
    groups = df.groupby(col).groups
    
    print(f"Null Hypothesis: There is no difference between groups of {col}")
    
    dfd = len(groups.keys())
    dfn = df[col].shape[0]
    
    f_c = stats.f.ppf(q, dfd, dfn)
    ind_cats = []
    for group in groups:
        ind_cats.append(groups[group])
    
    annova = stats.f_oneway(*ind_cats)
    f_stat = annova[0]
    pvalue = annova[1]
    
    t = PrettyTable(['F(c)', 'F statistic', 'pvalue', 'q', 'dfd', 'dfn'])
    t.add_row([f_c, f_stat, pvalue, q, dfd, dfn])
    
    print(t)
    
    return annova