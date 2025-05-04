# AnalyseImage

**Accédez à  l'application ici :** https://analyseimage.streamlit.app/ 

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://analyseimage.streamlit.app/)

📌 Application Streamlit : Connexion & Recherche Google Lens

📝 Description

Cette application Streamlit permet aux utilisateurs de :

Créer un compte et se connecter via Supabase

Rechercher des images similaires avec Google Lens API (via SerpApi)

Afficher les résultats de recherche sous forme de tableau interactif

L'authentification est sécurisée via Streamlit Authenticator et les clés API sont gérées via Streamlit Secrets.

🚀 Déploiement et Installation

🔧 1. Prérequis

Assurez-vous d'avoir installé Python 3.8+ et pip.

📥 2. Cloner le projet

git clone https://github.com/votre-utilisateur/nom-du-repo.git
cd nom-du-repo

📦 3. Installer les dépendances

pip install -r requirements.txt

🔑 4. Configurer les clés API

Créez un fichier .streamlit/secrets.toml et ajoutez-y :

[supabase]
url = "https://kpyzqxhqcjqwcvbdwmqp.supabase.co"
key = "VOTRE_SUPABASE_KEY"

[serpapi]
api_key = "VOTRE_SERPAPI_KEY"

🔹 Si vous utilisez Streamlit Cloud, ajoutez ces secrets directement dans la section "Secrets".

▶️ 5. Lancer l'application

streamlit run app.py

🖥️ Fonctionnalités Principales

🔹 Authentification & Gestion des Comptes

Création de compte et connexion via Supabase

Stockage sécurisé des mots de passe

🔹 Recherche d'images avec Google Lens

Entrée d'une URL d'image pour analyse

Affichage des résultats les plus pertinents

Interface interactive avec Streamlit

🔹 Sécurité et Gestion des API Keys

Utilisation de secrets.toml pour cacher les clés API

Gestion des accès avec streamlit_authenticator

📸 Captures d'écran

Connexion

Recherche Google Lens





🛠️ Technologies Utilisées

Python 3.8+ 🐍

Streamlit 🚀

Supabase 🔥 (Base de données & Authentification)

SerpApi 🔎 (Google Lens API)

Pandas 🏷️ (Analyse des résultats)

📜 License

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser et de le modifier.

🤝 Contribuer

Les contributions sont les bienvenues !

Forkez le projet 🍴

Créez une branche (git checkout -b feature-nouvelle-fonctionnalite)

Ajoutez vos modifications (git commit -m "Ajout d'une fonctionnalité")

Poussez vers GitHub (git push origin feature-nouvelle-fonctionnalite)

Ouvrez une Pull Request ✅

💡 Auteurs

👤 Kassim Said Ahmed
📧 Contact : kassim.said.ahmed2003@gmail.com
📂 GitHub : ksa2003
