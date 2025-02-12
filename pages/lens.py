import streamlit as st
from serpapi import GoogleSearch
import pandas as pd

# Charger l'API Key depuis secrets.toml
API_KEY = st.secrets["serpapi"]["api_key"]

# Demander à l'utilisateur de saisir l'URL de l'image
image_url = st.text_input("Entrez l'URL de l'image :")

if st.button("Lancer la recherche"):
    if image_url:
        params = {
            "engine": "google_lens",
            "url": image_url,
            "api_key": API_KEY
        }

        # Exécuter la recherche avec SerpApi
        search = GoogleSearch(params)
        results = search.get_dict()

        visual_matches = results.get("visual_matches", [])
        if visual_matches:
            df_visual = pd.json_normalize(visual_matches)
            df_top10 = df_visual.sort_values(by="position").head(10)
            st.write("### Top 10 résultats les plus pertinents :")
            st.dataframe(df_top10)
        else:
            st.warning("Aucun résultat trouvé pour cette image.")
    else:
        st.error("Veuillez saisir une URL valide.")
