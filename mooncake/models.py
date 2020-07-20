# -*- coding: utf-8 -*-
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier


class TreeDecision:
    def __init__(self, x, y):
        self.tree = DecisionTreeClassifier()
        self.x = x
        self.y = y

    def fit(self):
        return self.tree.fit(self.x, self.y)

    def predict(self, df):
        return self.tree.predict(df)


class RandomForest:
    def __init__(self, x, y):
        self.r_forest = RandomForestClassifier(n_estimators=110, criterion='entropy')
        self.x = x
        self.y = y

    def fit(self):
        return self.r_forest.fit(self.x, self.y)

    def predict(self, df):
        return self.r_forest.predict(df)
