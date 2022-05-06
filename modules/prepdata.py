import os
import pandas as pd
import numpy as np

def load(need, path):
    new_header= ['userId', 'itemId', 'rating']
    if os.path.isdir(path)== False:
        need = None
        old = pd.read_csv(path)
        new = old[old.columns[:3]]
        new.columns = new_header
        return new
    if os.path.isdir(path)== True:
        ratingsFile = path +"/ratings.csv"
        itemsFile = path +"/"+ need +".csv"
    
        old = pd.read_csv(ratingsFile)
        new = old[old.columns[:3]]
        new.columns = new_header
        if need == 'books':
            new.columns = [new_header[1],new_header[0],new_header[2]]
        itemsdf = pd.read_csv(itemsFile)
        
        return new, itemsdf
   
    

def createList(dataFrame,pram):
    if (pram == "user"):
        userId = dataFrame["userId"].unique().tolist()
        return userId
    elif(pram == "item"):
        itemId = dataFrame["itemId"].unique().tolist()
        return itemId
    
def encodingMaps(dataFrame, userOrItem):
    #We have to encode both the user and the items
    #encoding the user
    if (userOrItem == "user"):
        userEncoding = {x: i for i, x in enumerate(createList(dataFrame, "user"))}
        user2UserEncoding = {i: x for i, x in enumerate(createList(dataFrame, "user"))}
        #maps the user after encoding
        dataFrame["user"] = dataFrame["userId"].map(userEncoding)
        return userEncoding
    elif (userOrItem == "item"):
        #encoding the items
        itemEncoding = {x: i for i, x in enumerate(createList(dataFrame, "item"))}
        item2ItemEncoding = {i: x for i, x in enumerate(createList(dataFrame, "item"))}
        #maps the item
        dataFrame["item"] = dataFrame["itemId"].map(itemEncoding)
        return itemEncoding
    
def selfEncoding(dataFrame, userOrItem):
    #We have to encode both the user and the items 
    #encoding the user
    if (userOrItem == "user"):
        user2UserEncoding = {i: x for i, x in enumerate(createList(dataFrame, "user"))}
        #maps the user after encoding
        dataFrame["user"] = dataFrame["userId"].map(user2UserEncoding)
        return user2UserEncoding
    elif (userOrItem == "item"):
        #encoding the items
        item2ItemEncoding = {i: x for i, x in enumerate(createList(dataFrame, "item"))}
        #maps the item
        dataFrame["item"] = dataFrame["itemId"].map(item2ItemEncoding)
        return item2ItemEncoding
def formatData(dataFrame,user,item):
    num_users=len(encodingMaps(dataFrame, "user"))
    num_items=len(encodingMaps(dataFrame, "item"))
    dataFrame["rating"] = dataFrame["rating"].values.astype(np.float32)
    min_rating= min(dataFrame["rating"])
    max_rating= max(dataFrame["rating"])

    print("Number of users: {}, Number of Books: {}, Min rating: {}, Max rating: {}".format(num_users, num_items, min_rating, max_rating))
    return num_users, num_items

def prepData(dataFrame):
    dataFrame=dataFrame.sample(frac=1,random_state=42)
    min_rating= min(dataFrame["rating"])
    max_rating= max(dataFrame["rating"])
    x= dataFrame[["user","item"]].values
    y= y = dataFrame["rating"].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values
    train_indices = int(0.9 * dataFrame.shape[0])
    x_train, x_val, y_train, y_val = (
        x[:train_indices],
        x[train_indices:],
        y[:train_indices],
        y[train_indices:],
    )
    return x_train, x_val, y_train, y_val