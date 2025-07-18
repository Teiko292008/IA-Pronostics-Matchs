import streamlit as st

st.set_page_config(page_title="IA Pronos", page_icon="🤖")

st.title("🧠 IA – Meilleurs Pronostics Sportifs")
st.write("Bienvenue dans ton app IA de pronostics sportifs.")

# Ajoutons une zone pour entrer un match
match = st.text_input("Quel match veux-tu analyser ?")

if match:
    st.success(f"Analyse en cours pour : {match}")
    # Ici, on pourra ajouter ton IA de pronostics
    st.write("👉 Résultat probable : Équipe A gagne (simulé)")
