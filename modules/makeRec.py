import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from pathlib import Path
import matplotlib.pyplot as plt
from prepdata import encodingMaps

def showRecommendation(dataFrame,items_datframe):
    uid = dataFrame.userId.sample(1).iloc[0]
    items_by_user = dataFrame[dataFrame.userId == uid]
    items_not_watched = items_dataFrame[
        ~items_dataFrame["itemId"].isin(items_by_user.itemId.values)
    ]["itemId"]
    items_not_watched = list(
        set(items_not_watched).intersection(set(encodingMaps(dataFrame,"item").keys()))
    )
    items_not_watched = [[encodingMaps(dataFrame, "item").get(x)] for x in items_not_watched]
    user_encoder = encodingMaps(dataFrame, "user").get(uid)
    user_item_array = np.hstack(
        ([[user_encoder]] * len(items_not_watched), items_not_watched)
    )
    ratings = model.predict(user_item_array).flatten()
    top_ratings_indices = ratings.argsort()[-10:][::-1]
    recommended_item_ids = [
        selfEncoding("item").get(items_not_watched[x][0]) for x in top_ratings_indices
    ]
    
    print("Showing recommendations for user: {}".format(uid))
    print("====" * 9)
    print("Items with high ratings from user")
    print("----" * 8)
    top_item_user = (
        items_by_user.sort_values(by="rating", ascending=False)
        .head(5)
        .book_id.values
    )
    items_df_rows = items_dataFrame[items_dataFrame["itemId"].isin(top_item_user)]
    
    
    if list_of_items=="movies":
        for row in movie_df_rows.itertuples():
            print(row.title, ":", row.genres)

        print("----" * 8)
        print("Top 10 movie recommendations")
        print("----" * 8)
        recommended_movies = movie_df[movie_df["itemId"].isin(recommended_movie_ids)]
        for row in recommended_movies.itertuples():
            print(row.title, ":", row.genres)
    
    
    elif list_of_items=="books":
        for row in items_df_rows.itertuples():
            print(row.original_title, "by", row.authors)

        print("----" * 8)
        print("Top 10 book recommendations")
        print("----" * 8)
        recommended_items = items_dataFrame[items_dataFrame["book_id"].isin(recommended_item_ids)]
        for row in recommended_items.itertuples():
            print(row.original_title, "by", row.authors)
    
    
    else:
        for row in items_df_rows.itertuples():
            print(row.productId, "with rating of ", row.rating)

        print("----" * 8)
        print("Top 10 product recommendations")
        print("----" * 8)
        recommended_items = items_df[items_df["productId"].isin(recommended_item_ids)]
        for row in recommended_items.itertuples():
            print(row.productId)
        