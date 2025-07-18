  import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="IA Pronos Pro", page_icon="🤖", layout="wide")

st.markdown("<h1 style='text-align:center;color:#4B0082;'>IA Pronostics Sportifs Pro</h1>", unsafe_allow_html=True)
match = st.text_input("Exemple: Espagne - Suisse (Euro F)")

if match:
    with st.spinner("Recherche des données..."):
        # Exemple statique simulée
        data = {
            "date":"18/07/2025",
            "comp":"Euro F",
            "forms":{
                "Espagne": {"W":7,"D":2,"L":1,"goals_for":24,"goals_against":6},
                "Suisse": {"W":4,"D":3,"L":3,"goals_for":10,"goals_against":19}
            },
            "stats": {"xG_Espagne":2.3,"xG_Suisse":1.1,"shots_Espagne":8.5,"shots_Suisse":4.2},
            "h2h":{"Espagne":3,"Suisse":1},
            "injuries":{"Espagne":0,"Suisse":1},
            "bets": {
                "Espagne": {"prob":0.92,"odd":1.08},
                "BTTS_No": {"prob":0.78,"odd":1.65},
                "Over1.5": {"prob":0.84,"odd":1.34}
            }
        }
        st.subheader(f"{match} – {data['comp']} le {data['date']}")
        st.markdown(f"**Forme récente** (10 derniers matchs) :")
        forms = data["forms"]
        st.dataframe(forms)
        st.markdown("**Statistiques clés :**")
        st.write(f"xG – Espagne: {data['stats']['xG_Espagne']} vs Suisse: {data['stats']['xG_Suisse']}")
        st.write(f"Tirs cadrés – Espagne: {data['stats']['shots_Espagne']} vs Suisse: {data['stats']['shots_Suisse']}")
        st.write(f"Confrontations directes (5 derniers) : Espagne {data['h2h']['Espagne']} – {data['h2h']['Suisse']} Suisse")
        st.write(f"Blessures : Espagne={data['injuries']['Espagne']}, Suisse={data['injuries']['Suisse']}")

        st.markdown("### 🎯 Pronostics & Probabilités")
        bets = data["bets"]
        for key, val in bets.items():
            st.write(f"- **{key.replace('Over1.5','Plus de 1.5 buts')}: {val['prob']*100:.0f}% – cotes {val['odd']}")

        st.markdown("### 🧠 Analyse complète")
        st.markdown("> • L’Espagne est en pleine forme, avec 7 victoires /10 matchs → **probabilité élevée**\n"
                    "> • Leur xG est deux fois supérieur, ils dominent les stats d’attaque\n"
                    "> • La Suisse subit plus de buts et manque souvent de souffle\n"
                    "> • En face à face, Espagne gagne 3 sur 4\n"
                    "> **Conclusion : pari sûr sur la victoire Espagne + over 1.5 buts**.")
