import pandas as pd
import streamlit as st
import joblib


def Popularity() :
    st.markdown("<h1 style='text-align: center;'>⭐ Popularity index</h1>", unsafe_allow_html=True)    
    
    
    def reset_features():
        st.session_state['features'] = pd.DataFrame({
            'startYear' : [2025],
            'titleType' : [''],
            'genre_1' : ['None1'],
            'genre_2' : ['None2'],
            'genre_3' : ['None3'],
            'actor_1' : [''],
            'actor_2' : [''],
            'actor_3' : [''],
            'director_1' : [''],
            'director_2' : [''],
            'director_3' : [''],
            'title' : ['notitle']
            
        })
        
    def reset_genres():
        if '_genres' in st.session_state.keys(): 
            st.session_state._genres = []

    def reset_actors():
        if '_actors' in st.session_state.keys(): 
            st.session_state._actors = []

    def reset_directors():
        if '_directors' in st.session_state.keys(): 
            st.session_state._directors= []
    def reset_startYear():
        if '_year' in st.session_state.keys():
            st.session_state._year = 2025
    def reset_display():
        if 'display' in st.session_state.keys():
            st.session_state.display = False

    def load_genres(): st.session_state['genres'] = pd.read_csv("./data/genres.csv", )
    def load_names() : st.session_state['names']  = pd.read_csv("./data/names_ad.csv", nrows=10000)
    def load_types() : st.session_state['types']  = pd.read_csv("./data/titletype.csv")

    def set_startYear() : 
        st.session_state.features.loc[0,'startYear'] = st.session_state._year
    def set_titleType() : 
        st.session_state.features.loc[0,'titleType'] = st.session_state._titleType

    def set_genres():
        for i in range(len(st.session_state._genres)): 
            st.session_state.features.loc[0, f'genre_{1+i}'] = st.session_state._genres[i]

    def set_actors():
        for i in range(len(st.session_state._actors)): 
            st.session_state.features.loc[0, f'actor_{1+i}'] = st.session_state._actors[i]    

    def set_directors():
        for i in range(len(st.session_state._directors)): 
            st.session_state.features.loc[0, f'director_{1+i}'] = st.session_state._directors[i]     
    def set_display(b):
        st.session_state.display = b

    def reset_all():
        reset_features()
        reset_genres()
        reset_actors()
        reset_directors()
        reset_startYear()
        reset_display()
        set_display(False)

    def predict() :
        set_titleType() 
        set_startYear()
        set_genres()
        set_actors()
        set_directors()
        set_display(True)

        if '_model' not in st.session_state.keys():
            st.session_state['rating'] = "No model available for prediction."
        else :
            st.session_state['rating'] = st.session_state._qt.inverse_transform(st.session_state._model.predict(st.session_state.features).reshape(-1, 1))
    if 'features' not in st.session_state.keys() : reset_features()
    if 'genres'   not in st.session_state.keys() : load_genres()
    if 'names'    not in st.session_state.keys() : load_names()
    if 'types'    not in st.session_state.keys() : load_types()
    if 'display'  not in st.session_state.keys() : st.session_state['display'] = False
    if 'rating'   not in st.session_state.keys() : st.session_state['rating']  = -1.0
    if '_model'    not in st.session_state.keys() : st.session_state['_model'] = joblib.load('./model/modelgbr.pkl')
    if '_qt'    not in st.session_state.keys() : st.session_state['_qt'] = joblib.load('./model/ratingmodel.pkl')

    col1, col2= st.columns([0.5, 0.5], gap='large')
    with col1 :
        option_t = st.selectbox(
            "Make you're choice",
            st.session_state.types,
            key="_titleType",
            on_change=set_titleType
        )
        options_a = st.multiselect(
            "Select 3 actors or actresses max",
            st.session_state.names['primaryName'].tolist(), default=[],
            max_selections=3,
            on_change=set_actors,
            key='_actors'
        )
    with col2:
        options_g = st.multiselect(
            "Sélect 3 types max",
            st.session_state.genres['genres'].tolist(), default=[],
            max_selections=3,
            key='_genres',
            on_change=set_genres
        )
        options_d = st.multiselect(
        "Select 3 directors max",
        st.session_state.names['primaryName'].tolist(), default=[],
        max_selections=3,
        on_change=set_directors,
        key='_directors'
        )

    option_y = st.slider(
        "Select one year",
        min_value=2025,
        max_value=2035,
        value=2025,
        on_change=set_startYear,
        key = '_year'
    )

    col3, col4= st.columns([0.75, 0.25], gap='large')
    with col3 : 
        button_r = st.button(
            "Reset All",
            key = '_reset',
            on_click=reset_all
        )
    with col4 : 
        button_p = st.button(
            "popularity prediction",
            key = '_pred',
            on_click=predict
        )

    if st.session_state.display:
        #st.session_state.features
        st.write(f"__You're popularity prediction is : {st.session_state.rating[0,0]}__")
    