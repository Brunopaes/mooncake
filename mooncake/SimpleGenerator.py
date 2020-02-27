import datetime
import pandas
import random


def generator(path):
    """This function aims on generating manual data for overcoming overfitting
    in fraud detection problems!

    Parameters
    ----------
    path : str
        CSV Path;
    Returns
    -------

    """
    df = pandas.read_csv(path)
    df_fraud = df[df['Fraude'] == 1]
    df_non = df[~df.index.isin(df_fraud.index)]

    k = list(df_fraud.columns)
    v = []
    for i in df_fraud.columns[:-1]:
        max_ = df_fraud[i].max()
        min_ = df_fraud[i].min()

        v.append([random.uniform(min_, max_) for i in range(len(df_non))])

    df_gan = pandas.DataFrame(dict(zip(k, v)))
    df_gan['Fraude'] = 1

    df_final = df_non.append(df_gan).reset_index(drop=True)

    df_final.to_csv('../data/new_train-{}.csv'.format(datetime.date.today()))
    df_fraud.to_csv('../data/validation-{}.csv'.format(datetime.date.today()))


generator('https://raw.githubusercontent.com/Brunopaes/picpay-sherock_holmes/master/data/datasource.csv')
