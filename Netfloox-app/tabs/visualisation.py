import streamlit as st


def Visualisation():
    st.markdown("<h1 style='text-align: center;'>📊 Data Visualisation</h1>", unsafe_allow_html=True)

# Créer des colonnes pour afficher les images en paires
    col1, col2 = st.columns(2)
    with col1:
        st.image("assets/films_vs_startyear.webp", use_container_width=True)
    with col2:
        st.image("assets/genres_vs_startyear.webp", use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        st.image("assets/ratings.webp", use_container_width=True)
    with col4:
        st.image("assets/titletype_vs_startyear.webp", use_container_width=True)

    col5, col6 = st.columns(2)
    with col5:
        st.image("assets/top10_genres_after-2000df_tp_series.webp", use_container_width=True)
    with col6:
        st.image("assets/top10_genres_after-2000df_tp.webp", use_container_width=True)
    