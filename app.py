import streamlit as st
from streamlit_authenticator import Authenticate
from supabase import create_client, Client
from streamlit_option_menu import option_menu
from serpapi import GoogleSearch
import pandas as pd

# =============================================================================
# 1) Connexion sécurisée à Supabase via secrets.toml
# =============================================================================
SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# =============================================================================
# 2) Fonction pour récupérer les utilisateurs
# =============================================================================
def get_users_from_supabase():
    response = supabase.table("users").select("*").execute()
    users_data = response.data or []
    
    comptes = {"usernames": {}}
    for user in users_data:
        username = user["username"]
        comptes["usernames"][username] = {
            "name": user["name"],
            "password": user["password"],  # ⚠️ Ne pas stocker en clair en prod
            "email": user["email"],
            "failed_login_attempts": 0,
            "logged_in": False
        }
    return comptes

# =============================================================================
# 3) Interface principale : Connexion & Création de compte
# =============================================================================
st.title("Bienvenue !")

# Onglets Connexion / Création de compte
tab1, tab2 = st.tabs(["Se connecter", "Créer un compte"])

# =============================================================================
# 4) Connexion des utilisateurs
# =============================================================================
with tab1:
    st.subheader("Connexion")

    # Récupération des utilisateurs
    lesDonneesDesComptes = get_users_from_supabase()

    authenticator = Authenticate(
        lesDonneesDesComptes,
        "cookie_name",
        "cookie_key",
        30
    )

    # Formulaire de connexion
    authenticator.login("main")

    if st.session_state.get("authentication_status"):
        st.success(f"Bienvenue {st.session_state['name']} !")
        selection = option_menu(None, ["Accueil", "Google Lens"])
        
        if selection == "Accueil":
            st.write("Contenu de la page d'accueil")
        
        elif selection == "Google Lens":
            st.subheader("Recherche avec Google Lens")

            image_url = st.text_input("Entrez l'URL de l'image :")
            if st.button("Lancer la recherche"):
                if image_url:
                    API_KEY = st.secrets["serpapi"]["api_key"]
                    params = {
                        "engine": "google_lens",
                        "url": image_url,
                        "api_key": API_KEY
                    }

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

        authenticator.logout("Déconnexion")

    elif st.session_state.get("authentication_status") is False:
        st.error("Nom d'utilisateur ou mot de passe incorrect.")

    else:
        st.warning("Veuillez entrer vos identifiants pour vous connecter.")

# =============================================================================
# 5) Création d'un compte
# =============================================================================
with tab2:
    st.subheader("Créer un compte")

    with st.form("form_creation_compte"):
        new_name = st.text_input("Nom complet")
        new_username = st.text_input("Nom d'utilisateur (unique)")
        new_email = st.text_input("Email")
        new_password = st.text_input("Mot de passe", type="password")
        new_password_conf = st.text_input("Confirmer le mot de passe", type="password")
        submit_creation = st.form_submit_button("Créer un compte")

    if submit_creation:
        if not new_name or not new_username or not new_email:
            st.error("Veuillez remplir tous les champs.")
        elif new_password != new_password_conf:
            st.error("Les mots de passe ne correspondent pas.")
        else:
            existing = supabase.table("users").select("*")\
                .eq("username", new_username).execute()
            
            if existing.data:
                st.error("Ce nom d'utilisateur existe déjà. Choisissez-en un autre.")
            else:
                data_to_insert = {
                    "name": new_name,
                    "username": new_username,
                    "email": new_email,
                    "password": new_password  # ⚠️ A hacher avant insertion en prod !
                }
                try:
                    supabase.table("users").insert(data_to_insert).execute()
                    st.success("Compte créé avec succès ! Vous pouvez maintenant vous connecter.")
                    st.info("Allez dans l'onglet **Se connecter** pour vous authentifier.")
                except Exception as e:
                    st.error(f"Une erreur s'est produite : {e}")











