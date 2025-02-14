from utils.sqlclient import SQLClient
from utils.db_connection import build_engine

## Requete SQL d'extraction

sql = """
    WITH tb_mini as (
        select tconst,
            "titleType", 
            genres[1] as genre_1, 
            genres[2] as genre_2, 
            genres[3] as genre_3, 
            "primaryTitle", 
            "isAdult", 
            "startYear",
            "runtimeMinutes"  
        from "Jonathan".title_basics
        where "titleType" in ('movie', 'tvMovie', 'tvSeries', 'tvMiniSeries') and "startYear" >= 2000 
    ),
    actors AS (
    SELECT 
        tp.tconst,
        ARRAY_AGG(tp.nconst) as actors
    FROM "Jonathan".title_principals tp
    LEFT JOIN "Jonathan".name_basics nb on tp.nconst = nb.nconst
    WHERE category LIKE 'act%%'
    GROUP BY tp.tconst
),
directors AS (
    SELECT 
        tconst,
        ARRAY_AGG(tp.nconst) as directors
    FROM "Jonathan".title_principals tp
    WHERE category = 'director'
    GROUP BY tp.tconst
)
SELECT 
    tb.*,
    (a.actors)[1] as actor_1,
    (a.actors)[2] as actor_2,
    (a.actors)[3] as actor_3,
    (d.directors)[1] as director_1,
    (d.directors)[2] as director_2,
    (d.directors)[3] as director_3,
    "averageRating",
    "numVotes"
from tb_mini tb
left join "Jonathan".title_ratings tr on tb.tconst = tr.tconst
left join actors a on tb.tconst = a.tconst
LEFT JOIN directors d ON tb.tconst = d.tconst
"""


if __name__ == '__main__':
    config = '../config/.env'
    output = '../data/data_extract.tsv'
    
    engine = build_engine(config)
    client = SQLClient(engine=engine)

    print('Extraction ...')
    df = client.run_sql(sql)
    df.to_csv(output, sep='\t')
    print('Extraction done.')