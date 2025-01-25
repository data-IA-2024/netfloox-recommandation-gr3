import pandas as pd

from utils.db_connection import build_engine
from utils.table import table_dtype_mapping, table_name, table_data, prepare_df
from utils.timer import Timer
from tables.models import Base, schema, title_akas


engine = build_engine()
Base.metadata.create_all(engine, checkfirst=True)

data_folder = './data/'
models = [title_akas]

chunksize = 500_000

with engine.connect() as conn:
    timer = Timer(now=True)
    for model in models:
        filename = table_data(model)
        name     = table_name(model)
        dtype    = table_dtype_mapping(model)

        print(filename)
        
        nb_rows_sent = 0

        for chunk in pd.read_csv(data_folder + filename, sep='\t', chunksize=chunksize, quoting=3):
            chunk = prepare_df(chunk, dtype, nullchar=r'\N')
            chunk.to_sql(name, con=engine, schema=schema, if_exists='append', index=False)
            nb_rows_sent += chunk.shape[0]

            print(f"\r{nb_rows_sent:_} rows uploaded. Elapsed Time : {timer.elapsed()}\033[0K", end="")
        print()