# Coins forecasting servise

Service to forecast crypto market

## Problem statment

Time series prediction is an extremely useful field if you apply its methods to predicting the stock market, currencies, cryptocurrencies and other things.

This service allows you to make a prediction for a given horizon based on the data provided.

For example, models have already been trained to predict the cryptocurrency TONCOIN

To use this service for other cryptocurrencies or assets. And also if you want to update the data. You will need to replace the dataset and train the models. To do this, follow the steps described in the Prediction on your own data section.

Based on the result of the forecast you can draw conclusions about the rise or fall in the value of the asset.

## How to use

1. Clone this repository

```bash
git clone 
```

To run docker container:

```bash
docker build -t coins_forecasting .
docker run -p 9696:9696 coins_forecasting
```

To run without docker (locally):

Install dependencies

```bash
pipenv install
```

Activate virtual environment

```bash
pipenv shell
```

[ OPTIONAL ] Run the [train.py](src/train.py) file by running the command:

```bash
python src/train.py
```

TODO: Add next steps


## Exploratory data analysis

You can find the EDA in the [notebook](src/eda.ipynb)

## Model training

Model training is described in the file [train.py](src/train.py)

## Dataset

The dataset is located in the data folder.
You can get this dataset from the [site](https://bitscreener.com/coins/toncoin/price-history).

## Prediction on your own data

> [!IMPORTANT]
> You need to have a dataset in the same
> format as the one in the data folder.

**Example:**

|    | Date       |      Volume |    Open |   Close |    High |     Low |
|---:|:-----------|------------:|--------:|--------:|--------:|--------:|
|  0 | 2023/11/08 | 5.23551e+07 | 2.53952 | 2.65021 | 2.70932 | 2.53312 |
|  1 | 2023/11/07 | 4.79396e+07 | 2.44311 | 2.53962 | 2.58965 | 2.37122 |
|  2 | 2023/11/06 | 1.31434e+07 | 2.27305 | 2.44042 | 2.4707  | 2.27305 |
|  3 | 2023/11/05 | 6.23979e+06 | 2.24356 | 2.2715  | 2.29839 | 2.23797 |
|  4 | 2023/11/04 | 7.39826e+06 | 2.26289 | 2.24054 | 2.27168 | 2.21834 |


1. Paste your dataset into the data folder
2. Rename `dataset_path` in the [config file](conf/conf.yaml) file to the name of your dataset.
3. Run the [train.py](src/train.py) file by running the command:

```bash
python src/train.py
```

## Self-check

1. EDA - 2
2. Model training - 0
3. Script for model training - 0
4. Dataset - 1
5. Model deployment - 0
6. Dependencies - 2
7. Containerization - 0
8. Deployment to the cloud - 0