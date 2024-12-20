import pandas as pd
import streamlit as st
from Utilities.song_to_id import song_to_id
from Utilities.get_input import get_input
from Recommenders.input_recommendations import input_recommendations as ir


unique_tracks = pd.read_csv('unique_tracks.txt', sep='<SEP>', names=['track_id', 'song_id', 'artist_name', 'title'])
train_triplets = pd.read_csv('train_triplets.txt', sep='\t', names=['user_id', 'song_id', 'play_count'])

train_triplets_sorted = train_triplets.sort_values('user_id').head(1000000)
merged_df = pd.merge(train_triplets_sorted, unique_tracks.drop_duplicates('song_id'), on='song_id', how='left')
merged_df.to_csv('Data/merged_data.csv', index=False)



merged_data = pd.read_csv('Data/merged_data.csv')

st.title("Music Recommendation System")
st.write("Provide your favorite songs, and we'll recommend similar ones for you!")

st.subheader("Enter your favorite songs:")


# User inputs
input_songs = get_input()


if st.button("Get Recommendations"):
    if not input_songs:
        st.warning("Please enter at least one song to get recommendations.")
    else:
        # Converts songs to ID-s
        input_song_ids = song_to_id(input_songs, merged_data)
        
        # Generates recommendations for user
        recommended_song_titles = merged_data[merged_data['song_id'].isin(ir(input_song_ids, merged_data))]['full_title'].unique()
        
        # Output
        if len(recommended_song_titles) == 0:
            st.success("Since you have amazing music taste, there aren't any songs to be recommended :))")
        else:
            st.subheader("Recommended Songs:")
            for row in recommended_song_titles:
                st.write(row)
