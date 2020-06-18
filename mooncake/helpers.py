from sklearn.model_selection import train_test_split
from sklearn import metrics


import datetime
import pandas
import random


def oversampling(path):
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

    df_ros = pandas.DataFrame(dict(zip(k, v)))
    df_ros['Fraude'] = 1

    df_final = df_non.append(df_ros).reset_index(drop=True)

    df_final.to_csv('../data/new_train-{}.csv'.format(datetime.date.today()))
    df_fraud.set_index('Ocorrencia', drop=True)
    df_fraud.to_csv('../data/validation-{}.csv'.format(datetime.date.today()))


def data_separation(df, proportion=0.2):
    """This method separates the original dataframe into train/test sets.

    Parameters
    ----------
    df : pandas.DataFrame
        To be spliced dataframe;
    proportion : float, optional
        The train/test proportion;
    Returns
    -------
    train_test : list
        A list of 2 dataframes (Train/Test respectively);

    """
    return train_test_split(df, test_size=proportion)


def time_screening(dt):
    """This function calculates the time difference..

    Parameters
    ----------
    dt : datetime.datetime
        The initial time
    Returns
    -------

    """
    print(datetime.datetime.now() - dt)


def confusion_matrix(df, headers, labels=None):
    """This method generates the confusion matrix for a given dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        Model assertiveness table - to be parsed into confusion matrix;
    headers : iterable, tuple
        List of headers for the given dataframe;
    labels : tuple, optional
        Used for naming the indexes.

    Returns
    -------

    """
    if labels:
        return pandas.DataFrame(metrics.confusion_matrix(
            df[headers[0]], df[headers[1]]), labels, labels)
    else:
        return pandas.DataFrame(metrics.confusion_matrix(
            df[headers[0]], df[headers[1]]))


def x_and_y_separation(df):
    """This function splices the given dataframe into two dataframes - x an y

    Parameters
    ----------
    df : pandas.DataFrame
        A given dataframe;

    Returns
    -------
    x : pandas.DataFrame
        The x variables dataframe;
    y : pandas.DataFrame
        The y variable dataframe;

    """
    return df[df.columns[0:-1]], df[df.columns[-1]]
