def input_recommendations(input, merged_data):

  top_n_similar_users = 10
  user_song_groups = merged_data.groupby('user_id')['song_id'].apply(set)
  input_songs = input

  threshold = top_n_similar_users * 0.1
  song_counts = {}
  similarities = {}
  filtered_songs = {}
  input_recommended_songs = []
  similar_users_song_sets = []


  def jaccard_similarity(set1, set2):
      intersection = len(set1 & set2)
      union = len(set1 | set2)
      return intersection / union if union != 0 else 0


  for user, songs in user_song_groups.items():
      similarity = jaccard_similarity(input_songs, songs)
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
      if song not in input_songs:
          input_recommended_songs.append(song)
          if len(input_recommended_songs) >= 10:
              break

  return input_recommended_songs