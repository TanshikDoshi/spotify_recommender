import pandas as pd
import streamlit as st
df = pd.read_csv('final.csv')

st.write("""
# Spotify Recommender
""")
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

features = ['Track Popularity','acousticness','danceability','instrumentalness','liveness','loudness','tempo','valence']

scaler = MinMaxScaler()
df[features] = scaler.fit_transform(df[features])

cosine_sim = cosine_similarity(df[features], df[features])
#print(cosine_sim)

def get_recommendations(title):
    song_index = df[df['Track Name'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[song_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in sim_scores[1:5+1]]
    r = df['Track Name'].iloc[top_indices]
    return r.to_frame(name="Song")

text_input = st.text_input(
        "Enter a Song"
    )

if text_input:
    recommendations = get_recommendations(text_input)
    st.subheader('Recommendation')
    st.write(recommendnations)
