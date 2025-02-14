-- DROP SCHEMA "Jonathan";

CREATE SCHEMA "Jonathan" AUTHORIZATION azure_pg_admin;


CREATE TABLE "Jonathan".name_basics (
	nconst varchar(10) NOT NULL,
	"primaryName" varchar(105) NULL,
	"birthYear" int2 NULL,
	"deathYear" int2 NULL,
	"primaryProfession" varchar(67) NULL,
	"knownForTitles" varchar(43) NULL,
	CONSTRAINT name_basics_pk PRIMARY KEY (nconst)
);
CREATE INDEX name_basics_nconst_idx ON "Jonathan".name_basics USING btree (nconst);

-- "Jonathan".title_akas definition

CREATE TABLE "Jonathan".title_akas (
	"titleId" varchar(12) NOT NULL,
	"ordering" int4 NOT NULL,
	title varchar(850) NULL,
	region varchar(4) NULL,
	"language" varchar(4) NULL,
	"types" varchar(24) NULL,
	"attributes" _varchar NULL,
	"isOriginalTitle" bool NULL,
	CONSTRAINT title_akas_pkey PRIMARY KEY ("titleId", ordering)
);


-- "Jonathan".title_basics definition

CREATE TABLE "Jonathan".title_basics (
	tconst varchar(12) NOT NULL,
	"titleType" varchar(12) NULL,
	"primaryTitle" varchar(512) NULL,
	"originalTitle" varchar(512) NULL,
	"isAdult" bool NULL,
	"startYear" int2 NULL,
	"endYear" int2 NULL,
	"runtimeMinutes" int4 NULL,
	genres _varchar NULL,
	CONSTRAINT title_basics_pkey PRIMARY KEY (tconst)
);
CREATE INDEX title_basics_startyear_idx ON "Jonathan".title_basics USING btree ("startYear");


-- "Jonathan".title_crew definition

CREATE TABLE "Jonathan".title_crew (
	tconst varchar(12) NOT NULL,
	directors _varchar NULL,
	writers _varchar NULL,
	CONSTRAINT title_crew_pkey PRIMARY KEY (tconst)
);


-- "Jonathan".title_episode definition

CREATE TABLE "Jonathan".title_episode (
	id serial4 NOT NULL,
	tconst varchar(12) NULL,
	"parentTconst" varchar(12) NULL,
	"seasonNumber" int4 NULL,
	"episodeNumber" int4 NULL,
	CONSTRAINT title_episode_pkey PRIMARY KEY (id)
);


-- "Jonathan".title_principals definition

CREATE TABLE "Jonathan".title_principals (
	tconst varchar(12) NOT NULL,
	"ordering" int4 NOT NULL,
	nconst varchar(12) NULL,
	category varchar(24) NULL,
	job varchar(300) NULL,
	"characters" varchar(500) NULL,
	CONSTRAINT title_principals_pk PRIMARY KEY (tconst, ordering)
);

-- "Jonathan".title_ratings definition

CREATE TABLE "Jonathan".title_ratings (
	id serial4 NOT NULL,
	tconst varchar(12) NULL,
	"averageRating" float4 NULL,
	"numVotes" int4 NULL,
	CONSTRAINT title_ratings_pkey PRIMARY KEY (id)
);
CREATE INDEX title_ratings_tconst_idx ON "Jonathan".title_ratings USING btree (tconst);


