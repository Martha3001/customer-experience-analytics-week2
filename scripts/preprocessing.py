import pandas as pd

class Preprocessor:
    def __init__(self):
        pass

    def preprocess_reviews(self, df):
        """
        Preprocesses the reviews DataFrame by cleaning and formatting the data.
        Parameters:
            - df: DataFrame containing reviews with columns: content, score, at, app_name, source
        Returns:
            - Cleaned DataFrame with relevant columns and formatted data
        """
        if df.empty:
            return df
        
        # Remove duplicates
        df.drop_duplicates()

        # Identify missing data
        df.isnull().sum()

        # Drop rows with NaN values in critical columns
        df.dropna(subset=['content'], inplace=True)

        # Fill NaN values in 'score' with 0
        df['score'] = df['score'].fillna(0).astype(int)
                
        # Normalize dates to YYYY-MM-DD format
        df['at'] = pd.to_datetime(df['at']).dt.strftime('%Y-%m-%d')
        
        # Select and rename columns 
        df = df[['content', 'score', 'at', 'app_name', 'source']]
        
        df = df.rename(columns={
            'content': 'review',
            'score': 'rating',
            'at': 'date',
            'app_name': 'bank',
        })
        
        return df