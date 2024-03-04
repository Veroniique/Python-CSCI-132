'''
Desc: Simple music playlist using lists. Add, remove and view songs.
Date: 27 February 2024
'''
#empty music playlist
playlist = []

while True:
    #user prompts for actions
    print("Choose your option below by adding the number you want to use: ")
    print("1. Add a song to the playlist")
    print("2. Remove a song from the playlist")
    print("3. View the playlist")
    print("4. Display number of songs in the playlist")
    print("5. Display the most frequently added song")
    print("6. I am done creating changes.")
    user_picks = int(input("What number would you like to make changes to: "))

    #loop for chosen actions
    if user_picks == 1:
        add_song = input("Add a song to the playlist: ")
        playlist.append(add_song)
    elif user_picks == 2:
        remove_song = input("What song do you want to remove: ")
        if remove_song in playlist:
            playlist.remove(remove_song)
        else:
            print("Song does not exist on the playlist")
    elif user_picks == 3:
        print("Playlist: ")
        for song in playlist:
            print(song)
    elif user_picks == 4:
        display_num = len(playlist)
        print(f'Number of songs on playlist: {display_num}')
    #check if playlist empty, iterates through each song
    #counts num of each song, stores in list
    #finds max count and prints most frequent song
    elif user_picks == 5:
        if playlist:
            song_count = {}
            max_count = 0
            for song in playlist:
                count = playlist.count(song)
                song_count[song] = count
                if count > max_count:
                    max_count = count
            dp_frequent = [song for song, count in song_count.items() if count == max_count]
            print("Most frequent song added: ")
            for song in dp_frequent:
                print(song)
    elif user_picks == 6:
        print("Thank you for using the Music Playlist Manager")
        break
    else:
        print("Invalid input. Please choose numbers between 1 and 6")