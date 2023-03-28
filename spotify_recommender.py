import pandas as pd
df = pd.read_csv('final.csv')

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

features = ['Popularity','acousticness','danceability','instrumentalness','liveness','loudness','tempo','valence']

scaler = MinMaxScaler()
df[features] = scaler.fit_transform(df[features])

cosine_sim = cosine_similarity(df[features], df[features])
#print(cosine_sim)

def get_recommendations(title, number_of_recommendations=5):
    song_index = df[df['Track Name'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[song_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in sim_scores[1:number_of_recommendations+1]]
    r = df['Track Name'].iloc[top_indices]
    return r.to_frame(name="Song")

text_input = st.text_input(
        "Enter anything"
    )

if text_input:
    best_index = get_recommendations(text_input)
    st.subheader('Recommendation')
    st.write(df[['Title', 'Description', 'Industry', 'Type of Solution']].iloc[best_index])