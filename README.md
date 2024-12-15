# Music Recommendation System 🎵

This project is a music recommendation system that generates personalized song suggestions based on user inputs. Using collaborative filtering and Jaccard similarity, the system analyzes user listening histories and recommends songs from similar users' preferences.

## Features
- Accepts user song input in the format `*Artist Name* - *Song Name*`.
- Recommends up to 10 songs based on collaborative filtering.
- Interactive interface built with **Streamlit**.

## Data
- For the User Listening History Data. Download the Triplets For 1M users dataset from http://millionsongdataset.com/tasteprofile/
- For the Song Metadata. Download the list of tracks (3rd linked text) from http://millionsongdataset.com/blog/12-1-2-matching-errors-taste-profile-and-msd/

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/robinmurumets/Music-Recommendation-System.git
   cd Music-Recommendation-System
   ```
2. **Install Libraries**
   ```bash
   pip install pandas
   pip install streamlit
   ```


## Run app
1. **How Do Run Input Based Recommendation App**
   1. Open cmd
   2. Go to main.py directory
   ```bash
   streamlit run main.py
   ```
2. **How Do Use Input Based Recommendation App**
   1. Provide your favorite songs:
  
       1. Enter songs in the format ARTIST - SONG in the input fields.

   3. Get recommendations:

       2. Click the "Get Recommendations" button to view personalized song suggestions.

## How our code works
1. The process began by calculating the Jaccard similarity between the input user's listening history and the histories of all other users in the dataset. 
2. Then we ranked users by how closely their song preferences matched the input user. 
3. From these rankings, we selected the n (usually we set n=10) most similar users and aggregated their listening histories.
4. Next, we counted how many of these n users had listened to each song. 
5. To qualify as a recommendation, a song needed to have been played by at least n% of the most similar users, ensuring that the suggestions were popular within this group.
6. Furthermore, we filtered out any songs that the input user had already listened to, ensuring that the recommendations were genuinely new and personalized. 
7. The final list of recommended songs was sorted by popularity and limited to the top 10 results for relevance and simplicity. This method ensured that the recommendations were both meaningful and diverse, drawing from the collective preferences of similar users.



   
