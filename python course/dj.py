Size=int(input("Enter the number of songs: "))
Play_List=[]
for i in range(Size):
    song_name=(input(f"Enter the song Name : "))
    Play_List.append(song_name)
print(Play_List)
print(Play_List[::-1])
