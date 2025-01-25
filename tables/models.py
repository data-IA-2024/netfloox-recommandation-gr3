from sqlalchemy import Column, MetaData, PrimaryKeyConstraint
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import VARCHAR, SMALLINT, INTEGER, REAL, BOOLEAN, ARRAY


#######################################################################
####                      Declarative Base                          ### 
#######################################################################

# DB schema 
schema='Jonathan'

# Metadata
metadata_obj = MetaData(schema=schema)

Base = declarative_base(metadata=metadata_obj)

#######################################################################
####                 Table Declarative Models                       ### 
#######################################################################

class title_akas(Base):
    """ title.akas.tsv.gz """

    __tablename__   = 'title_akas'

    titleId         = Column(VARCHAR(12), primary_key=True, nullable=False) 
    ordering        = Column(INTEGER, primary_key=True, nullable=False)
    title           = Column(VARCHAR(850))
    region          = Column(VARCHAR(4))
    language        = Column(VARCHAR(4))
    types           = Column(VARCHAR(24))
    attributes      = Column(ARRAY(VARCHAR(70)))
    isOriginalTitle = Column(BOOLEAN)

    __table_args__  = (PrimaryKeyConstraint('titleId', 'ordering'),)
	
	
class title_basics(Base): 
    """ title.basics.tsv.gz """

    __tablename__  = 'title_basics'

    tconst         = Column(VARCHAR(12), primary_key=True, nullable=False)
    titleType      = Column(VARCHAR(12))
    primaryTitle   = Column(VARCHAR(512))
    originalTitle  = Column(VARCHAR(512))
    isAdult        = Column(BOOLEAN)
    startYear      = Column(SMALLINT)
    endYear        = Column(SMALLINT)
    runtimeMinutes = Column(SMALLINT)
    genres         = Column(ARRAY(VARCHAR(24)))
	
	
class title_crew(Base) :
    """ title.crew.tsv.gz """

    __tablename__  = 'title_crew'

    tconst         = Column(VARCHAR(12), primary_key=True, nullable=False)
    directors      = Column(ARRAY(VARCHAR(12)))
    writers        = Column(ARRAY(VARCHAR(12)))

class title_episode(Base) :
    """ title.episode.tsv.gz """

    __tablename__ = 'title_episode'

    id            = Column(INTEGER, primary_key=True, nullable=False)
    tconst        = Column(VARCHAR(12))
    parentTconst  = Column(VARCHAR(12))
    seasonNumber  = Column(INTEGER)
    episodeNumber = Column(INTEGER)


class title_principals(Base):
    """ title.principals.tsv.gz """

    __tablename__ = 'title_principals'

    tconst        = Column(VARCHAR(12), primary_key=True, nullable=False)
    nconst        = Column(VARCHAR(12))
    ordering      = Column(INTEGER, primary_key=True, nullable=False)
    category      = Column(VARCHAR(24))
    job           = Column(VARCHAR(300))
    characters    = Column(VARCHAR(500))

    __table_args__  = (PrimaryKeyConstraint('tconst', 'ordering'),)

class title_ratings(Base):
    """ title.ratings.tsv.gz """

    __tablename__ = 'title_ratings'

    id            = Column(INTEGER, primary_key=True, nullable=False)
    tconst        = Column(VARCHAR(12))
    averageRating = Column(REAL)
    numVotes      = Column(INTEGER)

class name_basics(Base):
    """ name.basics.tsv.gz """

    __tablename__     = 'name_basics'

    nconst            = Column(VARCHAR(10), primary_key=True, nullable=False)
    primaryName       = Column(VARCHAR(110))
    birthYear         = Column(SMALLINT)
    deathYear         = Column(SMALLINT) 
    primaryProfession = Column(ARRAY(VARCHAR(24)))
    knownForTitles    = Column(ARRAY(VARCHAR(12)))