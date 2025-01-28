import pandas as pd
import re 

def load_tsv(data_path: str, nullchar=None, chunksize =None):
    return pd.read_csv(data_path, sep='\t', na_values=nullchar, chunksize=chunksize, quoting=3, low_memory=False)

def table_dtype_mapping(model_class):
    dtype_mapping = {}
    for column_name, column in model_class.__table__.columns.items():
        dtype_mapping[column_name] = column.type
    return dtype_mapping

def prepare_df(df : pd.DataFrame, target_dtypes : dict):
    #if nullchar is not None:
    #    df = df.replace(fr'^{re.escape(nullchar)}$', None, regex=True)
    for column, dtype in target_dtypes.items():
        if 'ARRAY' in str(dtype):
            df[column] = df[column].str.split(',')
        if 'BOOLEAN' in str(dtype):
            df[column] = df[column].astype(bool)
    return df

def table_name(model):
    return model.__tablename__

def table_data(model):
    return model.__doc__.strip()