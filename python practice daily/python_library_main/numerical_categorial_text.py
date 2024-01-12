import pandas as pd

class FeatureCategorizer:
    def __init__(self, df):
        self.df = df

    def _get_features(self):
        return self.df.columns.tolist()

    def _is_numerical(self, feature):
        return self.df[feature].dtype != 'object'

    def _is_categorical(self, feature):
        return self.df[feature].dtype == 'object'

    def categorize_features(self):
        try:
            features = self._get_features()

            Num_features = [feature for feature in features if self._is_numerical(feature)]
            Cat_features = [feature for feature in features if self._is_categorical(feature)]
            Text_features = [feature for feature in features if feature not in Num_features and feature not in Cat_features]

            return {
                "Numerical_Features": Num_features,
                "Categorical_Features": Cat_features,
                "Text_Features": Text_features
            }

        except Exception as e:
            return f"An error occurred: {e}"


