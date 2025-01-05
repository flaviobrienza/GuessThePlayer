import streamlit as st
from utils import player_pick, comparison, unique_players, reset_selection

st.title("Guess the Player :soccer::question:")
st.warning(':warning: Only Serie A players from season 2020-2021 to 2024-2025 are available.')
@st.cache_data
def get_player():
    player_picked = player_pick()
    return player_picked
player_picked = get_player()
player_guessed = st.selectbox('Select a player :man-running:', options=unique_players(), index=None, key='selection')

if player_picked != player_guessed:
    retry_button = st.button('Quit :arrows_counterclockwise:')
    if retry_button:
        st.write(f"The player was **{player_picked}**")
        restart_button = st.button('**Start again**', on_click=reset_selection)
        st.cache_data.clear()
    else: 
        if player_guessed is not None:
            similarity_score = comparison(player_picked, player_guessed)
            st.progress(similarity_score, player_guessed)
        else:
            pass
else:
    st.write(f"Awesome the player was **{player_picked}**. You won :medal:")
    restart_button = st.button('**Start again**', on_click=reset_selection)
    st.cache_data.clear()