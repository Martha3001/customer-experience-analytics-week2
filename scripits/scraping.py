from google_play_scraper import app, Sort, reviews
import pandas as pd

class GooglePlayScraper:
    def __init__(self):
        pass

    def get_app_reviews(app_id, app_name, count=400):
        """
        Fetches reviews for a given app from the Google Play Store.
        Parameters:
            - app_id: str, the unique identifier for the app
            - app_name: str, the name of the app
            - count: int, number of reviews to fetch (default is 400)
        Returns:
            - DataFrame containing reviews with columns: review, rating, date, app_name, source
        """
        try:
            # Get first batch of reviews
            results, _ = reviews(
                app_id,
                lang='en',
                country='us',
                sort=Sort.NEWEST,
                count=count
            )
            
            # Save the reviews to a CSV file	
            results = [{
                'content': review['content'],
                'score': review['score'],
                'at': review['at'],
            } for review in results]


            # Convert to DataFrame
            df = pd.DataFrame(results)
            df['app_name'] = app_name
            df['source'] = 'Google Play Store'

            print(f"Finished scraping {len(df)} reviews for {app_id}")
            
            return df
        
        except Exception as e:
            print(f"Error getting reviews for {app_id}: {e}")
            return pd.DataFrame()