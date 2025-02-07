from utils.db_connection import build_engine
import pandas as pd
import sqlalchemy
from utils.timer import Timer


def extract_chunk(chunksize=50000, offset=0):
    sql = f"""
    WITH tb_minified AS (
        SELECT tconst, "titleType", "isAdult", "runtimeMinutes", "startYear", genres FROM "Jonathan".title_basics
        WHERE "startYear" >= 2000
    ),

    table_full AS (
        SELECT tm.*, 
                tp.nconst,
                tp.ordering,
                tp.category,
                nb."primaryName",
                nb."knownForTitles",
                tr."averageRating",
                tr."numVotes"
        FROM tb_minified tm
        JOIN "Jonathan".title_ratings tr ON tm.tconst = tr.tconst
        LEFT JOIN "Jonathan".title_principals tp ON tm.tconst = tp.tconst
        LEFT JOIN "Jonathan".name_basics nb ON tp.nconst = nb.nconst
    ),
    ratings_extracts AS (
        SELECT tconst,
            MIN("titleType") as "titleType",
            genres,
            MIN("startYear") as "startYear",
            ARRAY_AGG(nconst) as nconst,
            STRING_TO_ARRAY(STRING_AGG(DISTINCT "primaryName", ','), ',') as "primaryName",
            STRING_TO_ARRAY(STRING_AGG(DISTINCT "knownForTitles", ','), ',') as "knownForTitles",
            STRING_TO_ARRAY(STRING_AGG(DISTINCT "category", ','), ',') as "category",
            MIN("averageRating") as "averageRating",
            MIN("numVotes") as "numVotes"
        FROM table_full
        GROUP BY tconst, genres
    ),

    clean_data AS (
    SELECT tconst,
            "genres",
            "knownForTitles",
            category,
            "titleType",
            nconst,
            "startYear",
            "numVotes",
            "averageRating"
    FROM ratings_extracts
    )
    SELECT * FROM clean_data LIMIT {chunksize} OFFSET {offset};
    """
    return sql

engine = build_engine()
filename='./data/table_pop.tsv'
start = Timer(now=True)
with engine.connect() as conn:
    chunksize=50000
    offset = 0
    nb_lines = 0
    while True :
        try :
            print(f"\rNb. lines {nb_lines:_}. Elapsed time : {start.elapsed()}\033[0K", end="")
            mode = "a"
            header = False
            sql = extract_chunk(chunksize, offset)
            df = pd.read_sql_query(sql, con=conn)

            if nb_lines == 0 :
                mode = "w"
                header = True

            df.to_csv(filename, sep="\t", mode=mode, header=header)
            offset += chunksize
            nb_lines += chunksize
            
        except sqlalchemy.exc.ProgrammingError as e:
            print(e)
            break
        except KeyboardInterrupt:
            break
    print()