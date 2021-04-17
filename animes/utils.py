import pandas as pd


def read_data():
    df = pd.read_csv("animes.csv")
    return df

#def reanmed_data(df):
df_renamed = df.rename(columns={
"Title":"title",
"Type":"type",
"Episodes":"episodes",
"Status":"status",
"Start airing":"start_airing",
"End airing":"end_airing",
"Starting season":"starting_season",
"Broadcast time":"broadcast_time",
"Producers":"producers",
"Licensors":"licensors",
"Studios":"studios",
"Sources":"sources",
"Genres":"genres",
"Duration":"duration",
"Rating":"rating",
"Score":"score",
"Scored by":"score_by",
"Members":"members",
"Favorites":"favorites",
"Description":"description" 
})
        #return df_renamed



#def save_data_db(df_renamed):
#    for key in df_renamed:
#        df_renamed[key]:

for indice in range(len(new_df)):
    anime.title = new_df.iloc[indice].title
    anime.episodes = new_df.iloc[indice].episodes
    anime.start_airing = new_df.iloc[indice].start_airing
    anime.end_airing = new_df.iloc[indice].end_airing
    anime.starting_season = new_df.iloc[indice].starting_season
    anime.broadcast_time = new_df.iloc[indice].broadcast_time
    anime.licensors = new_df.iloc[indice].licensors
    anime.producers = new_df.iloc[indice].producers
    anime.studios = new_df.iloc[indice].studios
    anime.sources = new_df.iloc[indice].sources
    anime.genres = new_df.iloc[indice].genres
    anime.duration = new_df.iloc[indice].duration
    anime.rating = new_df.iloc[indice].rating
    anime.score = new_df.iloc[indice].score
    anime.score_by = new_df.iloc[indice].score_by
    anime.members = new_df.iloc[indice].members
    anime.favorites = new_df.iloc[indice].favorites
    anime.description = new_df.iloc[indice].description
    anime.save()


anime.title = df_renamed.iloc[indice].title
anime.episodes = df_renamed.iloc[indice].episodes
anime.start_airing = df_renamed.iloc[indice].start_airing
anime.end_airing = df_renamed.iloc[indice].end_airing
anime.starting_season = df_renamed.iloc[indice].starting_season
anime.broadcast_time = df_renamed.iloc[indice].broadcast_time
anime.licensors = df_renamed.iloc[indice].licensors
anime.producers = df_renamed.iloc[indice].producers
anime.studios = df_renamed.iloc[indice].studios
anime.sources = df_renamed.iloc[indice].sources
anime.genres = df_renamed.iloc[indice].genres
anime.duration = df_renamed.iloc[indice].duration
anime.rating = df_renamed.iloc[indice].rating
anime.score = df_renamed.iloc[indice].score
anime.score_by = df_renamed.iloc[indice].score_by
anime.members = df_renamed.iloc[indice].members
anime.favorites = df_renamed.iloc[indice].favorites
anime.description = df_renamed.iloc[indice].description
anime.save()

