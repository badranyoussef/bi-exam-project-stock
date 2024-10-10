# Business Intelligence Exam Project
*By: **Youssef Badran** () and **Lasse Kjær Hauerberg** ()*

In this file you can find info about our exam project. The problem statement, and a guide to this repository.

## Problem Statement
**Title:** Stock Price Prediction Based on Macroeconomic Factors

### Challenge:
How does changes in macroeconomic factors, like interest rates and inflation, affect the stock market development, and how can we predict these changes using historical data?

### Importance:
Macroeconomic changes have a direct impact on companies' borrowing costs and earnings, which in turn affect their stock prices. Being able to predict these changes can help investors make informed decisions and reduce market risks.

### Expected Solution:
This study will help us determine if the macroeconomic factors have a influence on the stock prices, and whether investors should invest or not, based macroecomomic factors.

We will work towards developing a machine learning model that predicts stock price changes based on historical macroeconomic factors. In this study we mainly focus on interest rate and inflation.

### Positive Impact:
The solution will provide investors and financial analysts with valuable insights that enhance their ability to forecast market movements. This will enable them to make more accurate decisions regarding their investments.

### Further questions to investigate
During our work several new questions have arrived and ideas to improve our data.

1. What other macroeconomic factors can we find, to include?
2. Other kinds of feature engineering
3. Introduction of new data sets (other indicies)
4. The effect of movement in different indicies on other indicies

## Guide to the repository
We have several folders and files, here you can read where to find what.

**Folders:**
- ['app'-folder](https://github.com/badranyoussef/bi-exam-project-stock/tree/main/app): our Streamlit app, with visual representation of data and a use case with a trained model.
- ['datasets'-folder](https://github.com/badranyoussef/bi-exam-project-stock/tree/main/datasets): here you can find original and cleaned datasets, which we have used to make our final train/test data frame.
- ['models'-folder](https://github.com/badranyoussef/bi-exam-project-stock/tree/main/models): dump of our to best trained models for predicting S&P 500 and Russell 2000. Ignore the the 'not in use'-folder as we haven't used that data.
- ['notebooks'-folder](https://github.com/badranyoussef/bi-exam-project-stock/tree/main/notebooks): we have divided our code in three notebooks, to have a better view of what we have done.
  1. The first with data collection and cleaning process: [data_collect_clean.ipynb](https://github.com/badranyoussef/bi-exam-project-stock/blob/main/notebooks/data_collect_clean.ipynb)
  2. The second with data exploration and analysis: [exploration_analysis.ipynb](https://github.com/badranyoussef/bi-exam-project-stock/blob/main/notebooks/exploration_analysis.ipynb)
  3. The thrid with modeling: [modeling.ipynb](https://github.com/badranyoussef/bi-exam-project-stock/blob/main/notebooks/modeling.ipynb)

**Files**
- [SOURCES.md](https://github.com/badranyoussef/bi-exam-project-stock/blob/main/SOURCES.md): Links to our data sources.

## Results
We ended up with our best trained model using cross validation, being the DescissionTreeClassifier.

WWe split our time series data in 11 train/test sets and got a result of 0.56 accuracy on the training data, and 0.63 accuracy on the test data, predicting wether the S&P 500 data goes up or down next month.

We tried including different features (X), but did not get a better result. Maybe we would increase the accuracy by introducing new data to our dataset and model. We only base our result on data from one month, but we could base it on the last two months or three months, or use weeks.

Other models also provided somewhat good results, and by introducing new data og feature engineering further data, these models are alså worth training and testing again to search for better results.
