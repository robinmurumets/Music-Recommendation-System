def song_to_id(input_songs, merged_data):
    song_id_map = merged_data.assign(full_title=merged_data['artist_name'] + " - " + merged_data['title']).set_index('full_title')['song_id'].to_dict()
    song_id = set()

    for song in input_songs:
      if song in song_id_map:
          song_id.add(song_id_map[song])

    return song_id