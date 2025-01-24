import streamlit as st
import random

def generate_random_color():
    # Génère une couleur hexadécimale aléatoire
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def main():
    # Initialisation de la couleur de fond
    if 'background_color' not in st.session_state:
        st.session_state['background_color'] = generate_random_color()

    # CSS pour que la div prenne tout l'écran et positionne le bouton au centre
    st.markdown(
        f"""
        <style>
        .fullscreen-div {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: {st.session_state['background_color']};
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }}
        .stButton>button {{
            font-size: 20px;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
            background-color: white;
            color: black;
            cursor: pointer;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Div qui prend tout l'écran
    st.markdown(
        f'<div class="fullscreen-div"></div>',
        unsafe_allow_html=True
    )

    # Bouton pour changer la couleur de fond
    if st.button("Changer la couleur de fond", key="color_button"):
        st.session_state['background_color'] = generate_random_color()
        st.rerun()

    # Affichage de la vidéo
    st.video("video.mp4")

if __name__ == "__main__":
    main()