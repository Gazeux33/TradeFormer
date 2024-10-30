# TradeFormer

The aim of this project is to create a model capable of predicting stock market values. To do this I used an uncommon approach which is the Transformer. More specifically, the Autoformer architecture, which specialises in predicting temporal data.

Autoformer Paper : https://arxiv.org/abs/2106.13008
<br>
Alapa API : https://alpaca.markets/docs/api-documentation/api-v2/
<br>
Alpaca-py : https://alpaca.markets/sdks/python/

## Model

The model is based on the Autoformer architecture. The Autoformer is a transformer-based model that is designed to predict temporal data. The model is composed of an encoder and a decoder. The encoder is responsible for encoding the input data and the decoder is responsible for decoding the output data. The model is trained using a multi-task learning approach, where the model is trained to predict multiple time series at the same time. The model is trained using a combination of supervised and unsupervised learning, where the model is trained to predict the future values of the time series and to reconstruct the input data.

<div>
	<img src="https://github.com/Gazeux33/TradeFormer/blob/master/assets/Autoformer.png">
</div>

## Data

To train this model I have downloaded the data for all the symbols available on Alpaca from **2020 to 2022 for each minute**. 
This corresponds to around **10 GB** of data




## Training


| Property       | Value         |
|----------------|---------------|
| Framework      | PyTorch       |
| Device         | RTX 2070      |
| Optimizer      | Adam          |
| seq_len      | 96         |
| label_len      | 48          |
| pred_len      | 24          |
| embedding_dim      | 512          |
| batch_size     | 32         |
| start lr     | 0.0001         |
| loss     | mse        |
| n_heads     | 8        |
| dropout    | 0.05       |





## Results

At the end of the training session, I realised that the model was not really capable of understanding trends and was far too unstable to be used.

## Improvements

I tried an approach using Transformer technology to create this model, but most models of this type are based on reinforcement learning. It's probably much more appropriate to use this approach and it will probably be the subject of a future project. 
<br>

Another idea would be to combine the two technologies and create an agent that takes into account the predictions of another model and makes its decisions autonomously.







## Acknowledgement

https://github.com/zhouhaoyi/Informer2020

https://github.com/zhouhaoyi/ETDataset

https://github.com/laiguokun/multivariate-time-series-data

https://github.com/thuml/Autoformer
