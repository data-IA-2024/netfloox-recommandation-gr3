import streamlit as st
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
import requests
import json


class RecSysKNN :

    def __init__(self, n, df, data_path='./data/vec_clean_data.npy'):
        self._n = n+1
        self.load_model(data_path, df)
    
    def load_model(self, data_path, df):
        self._X = np.load(data_path)
        self.nbrs = NearestNeighbors(n_neighbors=self._n).fit(self._X)
        print(self._X.shape)
    
    def recommand(self, idx):
        _, idxs = self.nbrs.kneighbors(self._X[idx,:].reshape(1, -1))
    
        return idxs[0][1:]


ts_file = "./data/save_data_clean.tsv"
st.session_state["df"]=pd.read_csv(ts_file, sep="\t", encoding="utf-8", nrows=10000)   
df = st.session_state["df"] 

st.session_state["rec"] = RecSysKNN(n=5, df=df, data_path='./data/vec_clean_data.npy')
rec=st.session_state["rec"]

def Recommandation():
    st.markdown("<h1 style='text-align: center;'>🎬 Films Recommandation</h1>", unsafe_allow_html=True)
    listeRecommandations = []
    if "primaryTitle" in df.columns:
        option = st.selectbox("Which film did you watch ?", df["primaryTitle"], key="film")
        
        movie_data = requests.get(f"https://www.omdbapi.com/?apikey=1f2e1d6a&t={option}").text
        st.session_state["movie_data"]=json.loads(movie_data)
        
        movie_json = st.session_state["movie_data"]
        
        col1, col2 = st.columns([1, 2])
        with col1:
            poster_url = movie_json.get("Poster", "")
            if poster_url and poster_url != "N/A":
                st.image(poster_url, width=150)
            else:
                st.warning(f"Nothing found for {option}.")
            print(option)
        with col2:
            plot = movie_json.get("Plot", "No synopsis available")
            st.info(f"**Synopsis :** {plot}")
            st.header("Here, you're 5 recommanded films 🍿")
                
                # Garder uniquement les colonnes numériques et supprimer les NaN
            df_numeric = df
                
            if df_numeric.shape[1] > 0:
                print(option)
                idx = df[df["primaryTitle"] == option].index[0]
                print("indice", idx)
                indices = st.session_state["rec"].recommand(idx)
                listeRecommandations = st.session_state["df"]["primaryTitle"].iloc[indices]
                print(indices)
                #nbrs = NearestNeighbors(n_neighbors=7).fit(df_numeric)
                #ligne = df[df["primaryTitle"] == option].index[0]
                #distances, indices = nbrs.kneighbors(df_numeric.iloc[ligne].values.reshape(1, -1))
                listeRecommandations = df["primaryTitle"].loc[indices]
                st.write(f"Index recherché : {idx}, Taille du DataFrame : {len(df)}")
            else:
                st.error("No numeric Data available for the model")
                listeRecommandations = []
            print(len(listeRecommandations))
            for film in listeRecommandations[:5]:
                movie_data = requests.get(f"https://www.omdbapi.com/?apikey=1f2e1d6a&t={film}").text
                movie_json = json.loads(movie_data)
                poster_url = movie_json.get("Poster", "")
                if poster_url and poster_url != "N/A":
                    st.image(poster_url, width=150)
                else:
                    st.warning(f"No Poster found for {film}.")
                st.write(f"**{film}**")
                plot_en = movie_json.get("Plot", "")
                if plot_en and plot_en != "N/A":
                    st.caption(plot_en)
                else:
                    st.warning(f"no synopsis available for {film}.")