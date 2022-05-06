# Recommendation System using Collaborative Filtering 

Small Group Project for DATA 4380 course at The University of Texas at Arlington.
<br>
This repository holds an attempt to build a Recommendation system model using three different datasets from Kaggle. 

## Overview  
* The goal is to build a collaborative-filtering recommendation system model that is capable to take in different datasets. The model is able to predict ratings for items a user has not bought/seen/or used. The 10 items with the highest predicted ratings can then be recommended to the user. 


## Summary of Workdone

### Data  
* Data:
  * ![pics](https://github.com/citgua/CF_RecSystems/blob/main/repopics/00712D0E-EA83-4D4D-BA2C-C131B71D0880.jpeg)
  * [Datasets](https://github.com/citgua/CF_RecSystems/tree/main/datasets)

* Preprocessing / Clean up:
  * In preparing the data, we created a function that takes in the directory of the file/ dataset and returns a dataframe.
  * The function was modified in a way that it could be used for any datasets, that has the attributes of user_id, ratings, item_id.
  * For the item_id column the header was originally book_id, movie_id, product_id for the datasets we worked with. 
  * We then created a function that will help format the dataframe 
Then, we also created a function that could format the dataframe into the necessary x,y inputs for the model. 
  * Within this function we created a 90-10 split for data training and data validation, and also the data was randomized/ Shuffle.


### Problem Formulation
Recommandation System model breakdown: 
  * Input: x, y vectors for items and modified ratings
  * Output: Probability that  find other items that those users or similar users also liked

* Adam Optimizer used 

### Training
* In the first attempt, trained the model for 5 epochs, (for all the dataset) 

* In the second attempt, trained the model for 10 epochs (for all the datasets)

* We used MoldelCheckpoint from Keras for training callbacks, checkpoint was set to save model weights at each epochs if loss improved from the epoch before. 



### Performance Comparison
* Losses at 5 epochs and then 10 epochs
* Losses at 5 epochs and then 10 epochs - Movies

![100 Radom Generated Images at 15 epochs](https://github.com/citgua/CF_RecSystems/blob/main/repopics/129460AA-7F0A-448B-B715-9E609C983EE3.jpeg) 

* Losses at 5 epochs and then 10 epochs - Books
![100 Radom Generated Images at 100 epochs](https://github.com/citgua/CF_RecSystems/blob/main/repopics/4E41314E-54EF-4198-8C3F-AED67A37E4AF.jpeg)  




### Future Work
* For further, we plan to train the models for longer, for more accuracy. 
* Although, we were able to make predictions when we initially trained for the separate datasets, but while incorporating it to function we are having some problem with model saving weights, so we would work on it in future.
* We also plan to work on evaluating RMSE (Root Mean Square Error for the predictions we made, to reduce bad predictions or outliers.



## How to reproduce results

### Overview of files in repository
* [modules](https://github.com/citgua/CF_RecSystems/tree/main/modules)
  * makeRec: function to make 10 recommandations of dataset items given random user
  * prepData: functions that help create the loading and pre-processing of data
  * recmodel: recommandation model architecture

* [book_logs in logs folder](https://github.com/citgua/CF_RecSystems/tree/main/logs/booklogs)
  * Saved model at each epoch if loss improved from prev epoch for Book dataset 

* [movies_logs in loss folder](https://github.com/citgua/CF_RecSystems/tree/main/logs)
  * Saved model at each epoch if loss improved from prev epoch for Movies dataset


* [books_history.pkl](https://github.com/citgua/ACGAN_ASL/blob/main/asl_acgan_history.pkl)
  * Saved history of losses at each epoch for Books Dataset under log_losses

* [movies_history.pkl](https://github.com/citgua/ACGAN_ASL/blob/main/asll_acgan_history.pkl)
  * Saved history of losses at each epoch for Movie Dataset under log_losses


* [CFRC_BooksF.ipynb](https://github.com/citgua/CF_RecSystems/blob/main/CFRC_BooksF.ipynb)
  * Breakdown of:
    * Loading data
    * Building model
    * Training model
    * Evaluating losses
    * Example of 10 reccomndations
    
    
* [CFRC_MoviesF.ipynb](https://github.com/citgua/CF_RecSystems/blob/main/CFRC_MoviesF.ipynb)
   * With same breakdown as Books notebook.

* [CFRC_Amazon_Still_Working.ipynb](https://github.com/citgua/CF_RecSystems/blob/main/CFRC_Amazon_Still_Working.ipynb)
   * With same breakdown as Books notebook.
  


### Software Setup
* Packages used in notebook: numpy, pandas, matplotlib, tenserflow, sklearn, scipy cv2, os, PIL, pickle
* Tensorflow-metal PluggableDevice was installed to accelerate training with Metal on Mac GPUs using this [link](https://developer.apple.com/metal/tensorflow-plugin/).

### References
* https://keras.io/examples/structured_data/collaborative_filtering_movielens/
* https://realpython.com/build-recommendation-engine-collaborative-filtering/
* https://www.kaggle.com/code/gspmoreira/recommender-systems-in-python-101/notebook

