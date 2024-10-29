import pandas as pd



def prepare(data,size,freq):
    seq_len = size[0]
    label_len = size[1]
    pred_len = size[2]

    data = data.iloc[-seq_len:]
    print(data.shape)

    df_stamp = data[['date']]
    df_stamp['date'] = pd.to_datetime(df_stamp.date)



if __name__ == "__main__":
    df = pd.read_csv("../data/ACBI.csv")
    prepare(df,[96,48,24],"m")