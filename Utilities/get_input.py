import streamlit as st

def get_input():
    with st.expander("Add Your Favorite Songs", expanded=True):
        st.write("Enter songs in the format '*Artist Name* - *Song Name*'. Leave fields empty if not needed.")
        input_songs = set()
        for i in range(10):
            song_input = st.text_input(f"Song {i + 1}:", key=f"song_{i}").strip()
            if song_input:
                input_songs.add(song_input)
    return input_songs