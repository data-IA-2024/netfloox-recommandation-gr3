import pandas as pd
import numpy as np
import datetime
from utils.timer import Timer
from utils.table import load_tsv
import glob

data_folder = './data/'
filenames = glob.glob(data_folder + '*.tsv.gz')

chunksize = 500_000

def get_max(A, B):
    if A is None or B is None : raise ValueError
    C = A.copy(deep=True)
    C.iloc[:,1] = np.maximum(A.iloc[:,1].to_numpy(), B.iloc[:,1].to_numpy())
    return C

def beauty_print(df):
    return ', '.join([ ':'.join(list(map(lambda x : str(x), row.tolist()))) for i, row in df.iterrows()])


start = Timer(now=True)
for filename in filenames:
    print(filename)
    nrows = 0
    max_counts = None
    for chunk in load_tsv(filename, chunksize=chunksize, nullchar=r'\N'):

        string_len = chunk.select_dtypes(include='object').apply(lambda x : x.str.len()).max().reset_index()

        try :
            max_counts = get_max(max_counts, string_len)
        except ValueError:
            max_counts = string_len

        nrows += chunk.shape[0]

        print(f"\rnrows {nrows:_} | {beauty_print(max_counts)} {start.elapsed()}\033[0K ", end="", flush=True)
    max_counts.loc[max_counts.shape[0]] = ['nrows', nrows]
    max_counts.to_csv(filename + '.info.csv', index=False)
    print()