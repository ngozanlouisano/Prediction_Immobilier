import pandas as pd
import streamlit as st
import numpy as np
from joblib import load

def layout():
    # Sidebar
    st.sidebar.title("Liste des Paramètres ")
    st.sidebar.write("*Tous les champs sont obligatoires*")
    
@st.cache_data()
def my_cached_function():
    path_data = 'X_train_up.csv'
    df = pd.read_csv(path_data)
    return df

def parametres(df):
    
    defaut = 'TOUT'
    
    #### la qualité générale de la maison (évaluée sur une échelle de 1 à 10)#####  
    OverallQual_val = sorted(list(df['Overall Qual'].unique()))
    OverallQual_options = st.sidebar.selectbox("évaluée sur une échelle de 1 à 10", OverallQual_val, index = 0)
    
    #### l'année de construction de la maison #####  
    YearBuilt_val = sorted(list(df['Year Built'].unique()))
    YearBuilt_options = st.sidebar.selectbox("'Year Built' ( Année de construction )", YearBuilt_val, index = 0)
    

    #### la superficie totale du sous-sol en pieds carrés #####  
    TotalBsmtSF_val = sorted(list(df['Total Bsmt SF'].unique()))
    TotalBsmtSF_options = st.sidebar.selectbox("la superficie totale du sous-sol en pieds carrés", TotalBsmtSF_val, index = 0)
    
    ####  la surface habitable au-dessus du niveau du sol en pieds carrés #####  
    GrLivArea_val = sorted(list(df['Gr Liv Area'].unique()))
    GrLivArea_options = st.sidebar.selectbox("superficie du premier étage de la maison en pieds carrés", GrLivArea_val, index = 0)
    
    ####  la superficie du garage en pieds carrés #####  
    GrLivArea_val = sorted(list(df['Gr Liv Area'].unique()))
    GrLivArea_options = st.sidebar.selectbox("la surface habitable au-dessus du niveau du sol en pieds carrés", GrLivArea_val, index = 0)
    
   #### a superficie du garage en pieds carrés #####  
    GarageArea_val = sorted(list(df['Garage Area'].unique()))
    GarageArea_options = st.sidebar.selectbox("la superficie du garage en pieds carrés", GarageArea_val, index = 0)

    return OverallQual_options, YearBuilt_options, TotalBsmtSF_options, GrLivArea_options, GarageArea_options


def load_model():
    model = load(filename='Housing_final.joblib')
    return model
    
def prediction(model, data):
    resultat = model.predict(data)
    return resultat



########################################### MAIN ###########################################################
############################################################################################################
if __name__ == "__main__":
    st.set_page_config(
        page_title="App Immobilier",
        layout="centered"
    )
    st.title("Application prédiction de Prix Immobiliers")
    st.header("*# Ano N'gozan Louis*")
    st.subheader("@2023")
    
    layout()
    
    ############ READ DATA ##########################
   # Utilisation de la nouvelle commande de mise en cache
    cached_data = my_cached_function()
    # st.write(df.head())
    model = load_model()
    
    ############ PARAMETRES ##########################
    formulaire = parametres(cached_data)
    
    st.caption('Ci-dessous - Dataframe d\' informations sur les ventes de maisons.')
    
    ############ Données Formuliaire ##########################
        # Création du DataFrame à partir du tuple
    donnees = [formulaire]
    df_formulaire = pd.DataFrame(donnees, columns=['Overall Qual', 'Year Built', 'Total Bsmt SF', 'Gr Liv Area', 'Garage Area'])
    st.write(df_formulaire)
    
    # Bouton pour appeller le Modèle
    if st.sidebar.button('Valider'):
        resultat = prediction(model, df_formulaire)
        st.info(f'Prix de Vente: {resultat}')
        
      