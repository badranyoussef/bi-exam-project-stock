# Logbog

## Data Collection
We have managed to collect to data regarding stocks represented as the S&P500 prices, and interest and inflation rates from 1962 till now. This will be our primary working data sources.

The data sources are obtained from Kaggle and USA Federal Reserve Bank (FED).

## Data Cleaning
In the data cleaning process we have processed our files seperately to drop irrelevant columns.

The date is of importance for our data, and we have to combine the data sets on the date. Therefore we have converted date information to DateTime object, to have comparable columns en each data set.

Now we can merge the different data frames together on the date. This gives us a lot of NaN cells, which we need to decide what to do with. We can't drop rows, because we need the index price data later.

Because we have interest rates from two different data frames, we have a combined data frame with two rate columns, that we need to combine.

For interest rate we have decided to forward fill the data, because we asume that the rate is the same until it is changed.

For the inflation rate we could use forward fill, but maybe it will also be an idea to calculate an average and divide the change on the dates in between registered changes.

## Data Exploration and Analysis

## Data Modelling

## Data Validation

## Deployment and Optimization
