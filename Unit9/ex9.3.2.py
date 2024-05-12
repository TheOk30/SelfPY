def my_mp4_playlist(file_path, new_song):
    with open(file_path, 'r') as f:
        playlist = f.readlines()
    
    while len(playlist) < 3:
        playlist.append(";;\n")

    playlist = list(playlist)
    playlist.insert(new_song + ';Unknown;4:15;\n')

    with open(file_path, 'w') as f:
        f.writelines(playlist)
