import functools
import json
import random

with open("songs.json",encoding="utf-8")as f:
    data=json.load(f)
# print(data)
# print total number of songs in album1

# num_songs=[song for song in data if song["album"]=="album1"]
# print(num_songs)

num_songs=list(filter(lambda song: song["album"]=="album1",data))
print(len(num_songs))

# heigst rating song?

# top_song=max(data,key=lambda song:song["rating"])
# print(top_song["rating"])
# higst_rate_song =[song["name"] for song in data if song["rating"]>=5]
# print(higst_rate_song)
#

# top_song=functools.reduce(lambda song1,song2:song1 if song1["rating"]>song2["rating"] else song2,data)
# print(top_song)

# random sample of two sad songs
sad_songs=[song for song in data if song["mode"]=="sad"]
print(random.sample(sad_songs,2))

# total number of albums?
num_albums=set([alb["album"] for alb in data if alb["album"][1]])
print(len(num_albums))

# which album contains most songs?
dict={}
for song in data:
    album_name=song.get("album")
    if album_name in dict:
        dict[album_name]+=1
    else:
        dict[album_name]=1

print(dict)
print(max(dict.items(),key=lambda song:song[1]))
