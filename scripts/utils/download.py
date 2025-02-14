from pypdl import Pypdl
import asyncio
dl = Pypdl()

data = "https://datasets.imdbws.com/"

files = ['name.basics.tsv.gz', 'title.akas.tsv.gz', 'title.basics.tsv.gz', 'title.crew.tsv.gz',
         'title.episode.tsv.gz', 'title.principals.tsv.gz', 'title.ratings.tsv.gz']

tasks = [{'url': data + file, 'path': 'test_download/' + file}
         for file in files]

print(tasks)
"""
async def dwnl(file):
    result = await dl.start(data + file, file_path='test_download',
                            block=True, segments=10, retries=4)
    print(result)

if __name__ == '__main__':
    for file in files:
        asyncio.run(dwnl(file))
"""
