import streamlit as st

# Titre de l'application
st.title("Quel est votre style de pensée dominant ?")

# Instructions
st.write("""
Répondez aux questions ci-dessous en cochant celles qui vous correspondent le plus.
À la fin, découvrez votre style de pensée dominant !
""")

# Questionnaire
questions = [
    "Je préfère analyser des chiffres et des données pour prendre une décision.",
    "J'aime imaginer des solutions créatives et innovantes.",
    "Je planifie toujours mes journées et je respecte les étapes fixées.",
    "Je suis à l'aise pour écouter et comprendre les émotions des autres.",
    "J'adore résoudre des énigmes logiques et des problèmes mathématiques.",
    "Je trouve de l'inspiration dans les arts, la musique et les métaphores.",
    "Je suis organisé(e) et méthodique dans mon travail.",
    "Je préfère travailler en équipe et créer des liens avec mes collègues."
]

# Réponses de l'utilisateur
responses = []
for question in questions:
    response = st.checkbox(question)
    responses.append(response)

# Analyse des résultats
if st.button("Afficher mon style dominant"):
    if any(responses):  # Vérifie si au moins une case est cochée
        style_counts = {
            "Cortical Gauche (Logique et analytique)": responses[0] + responses[4],
            "Cortical Droit (Créatif et conceptuel)": responses[1] + responses[5],
            "Limbique Gauche (Organisé et méthodique)": responses[2] + responses[6],
            "Limbique Droit (Relationnel et émotionnel)": responses[3] + responses[7]
        }
        
        # Style dominant
        dominant_style = max(style_counts, key=style_counts.get)
        
        # Résultat
        st.subheader("Votre style dominant est :")
        st.write(f"**{dominant_style}**")
        
        # Détails des styles
        st.write("### Explications :")
        st.write("- **Cortical Gauche** : Logique, analytique, orienté vers les chiffres.")
        st.write("- **Cortical Droit** : Créatif, imaginatif, artistique.")
        st.write("- **Limbique Gauche** : Organisé, méthodique, axé sur la planification.")
        st.write("- **Limbique Droit** : Relationnel, émotionnel, axé sur les interactions humaines.")
    else:
        st.warning("Veuillez cocher au moins une affirmation avant de soumettre.")

# Lien vers l'application
st.write("""
Partagez cette application avec vos amis en scannant le QR code généré !
""")
