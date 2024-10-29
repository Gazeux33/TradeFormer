# TradeFormer

The aim of this project is to create a model capable of predicting stock market values. To do this I used an uncommon approach which is the Transformer. More specifically, the Autoformer architecture, which specialises in predicting temporal data.

Autoformer Paper : https://arxiv.org/abs/2106.13008
Alapa API : https://alpaca.markets/docs/api-documentation/api-v2/
Alpaca-py : https://alpaca.markets/sdks/python/

## Model

The model is based on the Autoformer architecture. The Autoformer is a transformer-based model that is designed to predict temporal data. The model is composed of an encoder and a decoder. The encoder is responsible for encoding the input data and the decoder is responsible for decoding the output data. The model is trained using a multi-task learning approach, where the model is trained to predict multiple time series at the same time. The model is trained using a combination of supervised and unsupervised learning, where the model is trained to predict the future values of the time series and to reconstruct the input data.

## Data

To train this model I have downloaded the data for all the symbols available on Alpaca from **2020 to 2022 for each minute**. 
This corresponds to around **10 GB** of data


## Training

## Results

## Improvements







## Acknowledgement

https://github.com/zhouhaoyi/Informer2020

https://github.com/zhouhaoyi/ETDataset

https://github.com/laiguokun/multivariate-time-series-data

https://github.com/thuml/Autoformer
