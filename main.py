from jeraconv import jeraconv
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def func1(df: pd.DataFrame):
    search_col = '国・地域'
    df = df[df[search_col] == '総数']
    df = df.drop([search_col], axis=1)
    df = df[~df['国・地域(人)'].str.contains('総数')]
    df = df[~df['国・地域(人)'].str.contains('部')]
    df = df[~df['国・地域(人)'].str.contains('市')]
    df = df[~df['国・地域(人)'].str.contains('町')]
    df = df[~df['国・地域(人)'].str.contains('村')]
    df = df[~df['国・地域(人)'].str.contains('支庁')]
    df = df.sort_values(by=['令和6年'], ascending=False)

    j2w = jeraconv.J2W()
    pre_x = df.columns[1:]
    x = [j2w.convert(s) for s in pre_x]

    bulk_size = 10
    groups = np.arange(len(df)) // bulk_size
    for group, subset in df.groupby(groups):
        plt.figure(figsize=(10, 5))
        for _, row in tqdm(subset.iterrows()):
            label = row['国・地域(人)']
            y = list(i.replace(',', '') if isinstance(i, str) else i for i in row[1:])
            y = [float(i) for i in y]
            plt.plot(x, y, label=label)

        plt.xticks(x, rotation='vertical')
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.savefig(f"output/func1_{group}.png", dpi=300)
        plt.clf()


def func2(df: pd.DataFrame):
    search_col = '国・地域(人)'
    df = df[df[search_col] == '総数']
    df = df.drop([search_col], axis=1)
    df = df[~df['国・地域'].str.contains('総数')]
    df = df[~df['国・地域'].str.contains('その他')]
    df = df.sort_values(by=['令和6年'], ascending=False)

    j2w = jeraconv.J2W()
    pre_x = df.columns[1:]
    x = [j2w.convert(s) for s in pre_x]

    bulk_size = 6
    groups = np.arange(len(df)) // bulk_size
    for group, subset in df.groupby(groups):
        plt.figure(figsize=(10, 5))
        for _, row in tqdm(subset.iterrows()):
            label = row['国・地域']
            y = list(i.replace(',', '') if isinstance(i, str) else i for i in row[1:])
            y = [float(i) for i in y]
            plt.plot(x, y, label=label)

        plt.xticks(x, rotation='vertical')
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.savefig(f"output/func2_{group}.png", dpi=300)
        plt.clf()


plt.rcParams['font.family'] = 'IPAexGothic'
df = pd.read_csv('input/ga000v0001.csv')
df.fillna(0, inplace=True)
df = df.drop(['地域階層', '地域コード'], axis=1)
func1(df)
func2(df)
