""" checking the number of outlaiers present for each feature using zscore"""
import numpy as np
import scipy.stats


class OutlaiersCheck:
    def __init__(self, dataframe):
        self.df = dataframe

    def check_outlaiers(self, num_features):
        """ return a dict with num of outliers for numerical data"""
        outliers_dict = {}

        for feature in num_features:
            z = np.abs(scipy.stats.zscore(self.df[feature]))
            outliers = self.df[z > 3][feature]
            outliers_dict[feature] = len(outliers.tolist())

        return outliers_dict



