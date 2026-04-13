import pandas as pd

def load_data(path):
    cols = ['unit', 'time'] + [f'op{i}' for i in range(1,4)] + [f'sensor{i}' for i in range(1,22)]
    
    df = pd.read_csv(path, sep=" ", header=None)
    df = df.dropna(axis=1)
    df.columns = cols
    
    return df
