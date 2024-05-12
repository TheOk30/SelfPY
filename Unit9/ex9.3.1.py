def my_mp3_playlist(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    new_list = []
    max__length = 0
    song_count = 0
    artist_count = {}
    song_max_length = ""
    for line in lines:
        song, artist, length  = line.strip().split(";")

        if length > max__length:
            max__length = length
            song_max_length = song

        if artist in artist_count:
            artist_count[artist] += 1
        else:
            artist_count[artist] = 1
        
        song_count += 1

    
    return (song_max_length, song_count, max(artist_count, key=artist_count.get)
)

def main():
    print(my_mp3_playlist(r"c:\my_files\songs.txt"))
    # [("Tudo Bom", 5, "The black Eyed Peas")]

if __name__ == "__main__":
    main()