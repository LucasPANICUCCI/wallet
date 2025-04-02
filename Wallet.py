import streamlit as st
from datetime import datetime

st.set_page_config(page_title="💼 Wallet Juridique Local DSP", layout="centered")

# Initialisation
if "solde" not in st.session_state:
    st.session_state.solde = 0
if "historique" not in st.session_state:
    st.session_state.historique = []

# Titre
st.markdown("""
<div style='text-align: center;'>
    <h1 style='font-family: Georgia, serif;'>💼 Mon Wallet Juridique Local</h1>
    <p style='font-size: 18px;'>Accès progressif au droit – Initiative DSP Avocats</p>
</div>
""", unsafe_allow_html=True)

# Solde affiché
st.markdown(f"""
<div style='text-align:center; font-size: 36px; margin-top:20px; color:#006400; font-weight:bold;'>
    Solde : {st.session_state.solde} crédits DSP
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Ajout de crédits par actions
st.subheader("🔁 Cumule des crédits")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("💡 +1 crédit (clic)"):
        st.session_state.solde += 1
        st.session_state.historique.append((datetime.now(), "+1 crédit par clic"))
with col2:
    if st.button("🤝 +5 crédits (parrainage)"):
        st.session_state.solde += 5
        st.session_state.historique.append((datetime.now(), "+5 crédits par parrainage"))
with col3:
    if st.button("🎁 +10 crédits (code bonus)"):
        st.session_state.solde += 10
        st.session_state.historique.append((datetime.now(), "+10 crédits par code"))

st.markdown("---")

# Utilisation de crédits
st.subheader("🎟️ Utilise tes crédits")
if st.session_state.solde >= 50:
    if st.button("🎫 Générer un billet juridique (50 crédits)"):
        st.session_state.solde -= 50
        st.session_state.historique.append((datetime.now(), "-50 crédits pour billet juridique"))
        st.success("🎉 Tu as généré un billet juridique numérique (simulation)")
else:
    st.info("Il faut au moins 50 crédits pour générer un billet juridique.")

st.markdown("---")

# Historique
st.subheader("📜 Historique de ton wallet")
if not st.session_state.historique:
    st.write("Aucune activité enregistrée.")
else:
    for date, action in reversed(st.session_state.historique):
        st.markdown(f"- **{date.strftime('%d/%m/%Y %H:%M')}** → {action}")