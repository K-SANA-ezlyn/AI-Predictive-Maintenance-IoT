def add_rul(df):
    max_cycle = df.groupby('unit')['time'].max().reset_index()
    max_cycle.columns = ['unit', 'max_time']

    df = df.merge(max_cycle, on='unit')
    df['RUL'] = df['max_time'] - df['time']

    return df

def create_label(df, threshold=30):
    df['failure'] = df['RUL'].apply(lambda x: 1 if x <= threshold else 0)
    return df
