def generate_recommendations(merged_data):

  top_n_similar_users = 10
  target_user = 'b048f21afd5e7467f187bf9f9d413e97c32313a9'
  user_song_groups = merged_data.groupby('user_id')['song_id'].apply(set)
  target_user_songs = user_song_groups[target_user]

  threshold = top_n_similar_users * 0.4
  song_counts = {}
  similarities = {}
  filtered_songs = {}
  recommended_songs = []
  similar_users_song_sets = []


  def jaccard_similarity(set1, set2):
      intersection = len(set1 & set2)
      union = len(set1 | set2)
      return intersection / union if union != 0 else 0


  for user, songs in user_song_groups.items():
      if user == target_user:
          continue
      similarity = jaccard_similarity(target_user_songs, songs)
      similarities[user] = similarity


  most_similar_users = sorted(similarities, key=similarities.get, reverse=True)[:top_n_similar_users]


  for user in most_similar_users:
      similar_users_song_sets.append(user_song_groups[user])


  for song_set in similar_users_song_sets:
      for song in song_set:
          song_counts[song] = song_counts.get(song, 0) + 1


  for song, count in song_counts.items():
      if count >= threshold:
          filtered_songs[song] = count


  filtered_songs_list = list(filtered_songs.items())
  sorted_songs = sorted(filtered_songs_list, key=lambda x: x[1], reverse=True)
  for song, count in sorted_songs:
      if song not in target_user_songs:
          recommended_songs.append(song)
          if len(recommended_songs) >= 10:
              break


  return recommended_songs