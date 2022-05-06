# Recommendation System using Collaborative Filtering 

Small Group Project for DATA 4380 course at The University of Texas at Arlington.
<br>
This repository holds an attempt to build a Recommendation system model using three different datasets from Kaggle. 

## Overview  
* The goal is to build a collaborative-filtering recommendation system model that is capable to take in different datasets. The model is able to predict ratings for items a user has not bought/seen/or used. The 10 items with the highest predicted ratings can then be recommended to the user. 


## Summary of Workdone

### Data  
* Data:
  * a

* Preprocessing / Clean up:
  * a
### Problem Formulation
* 
* Adam Optimizer used 

### Training
* 


### Performance Comparison
* 

### Conclusions
* 

### Future Work
* 


## How to reproduce results

### Overview of files in repository
* [modules](https://github.com/citgua/CF_RecSystems/tree/main/modules)
  * a

* [book_logs](https://github.com/citgua/CF_RecSystems/tree/main/logs)
  * Saved model at each epoch for Book dataset

* [movies_logs](https://github.com/citgua/CF_RecSystems/tree/main/logs)
  * Saved model at each epoch for Movies dataset

* [amazon_logs](https://github.com/citgua/CF_RecSystems/tree/main/logs)
  * Saved model at each epoch for Movies dataset

* [books_history.pkl](https://github.com/citgua/ACGAN_ASL/blob/main/asl_acgan_history.pkl)
  * Saved history of losses at each epoch for Books Dataset

* [movies_history.pkl](https://github.com/citgua/ACGAN_ASL/blob/main/asll_acgan_history.pkl)
  * Saved history of losses at each epoch for Movie Dataset

* [amazon_history.pkl](https://github.com/citgua/ACGAN_ASL/blob/main/asl_acgan_history.pkl)
  * Saved history of losses at each epoch for Amazon Dataset


* [CFRC_Books.ipynb](https://github.com/citgua/ACGAN_ASL/blob/main/ASL_ACGAN.ipynb)
  * Breakdown of:
    * Background
    * Examine and understand data
    * Loading data
    * Building model
    * Training model
    * Evaluating losses
    * Example of 10 reccomndations
  


### Software Setup
* Packages used in notebook: numpy, pandas, matplotlib, tenserflow, sklearn, scipy cv2, os, PIL, pickle
* Tensorflow-metal PluggableDevice was installed to accelerate training with Metal on Mac GPUs using this [link](https://developer.apple.com/metal/tensorflow-plugin/).

### References
* https://keras.io/examples/structured_data/collaborative_filtering_movielens/
* https://realpython.com/build-recommendation-engine-collaborative-filtering/
* https://www.kaggle.com/code/gspmoreira/recommender-systems-in-python-101/notebook

