movies=open("cinemadetails.txt","r")


all_movies=[]
all_movies=[movie.rstrip("\n").split(",")for movie in movies]
print(all_movies)

# number of movies released in 2022?
movies_rel_2022=[movie for movie in all_movies if movie[1]=="2022"]
print(len(movies_rel_2022))

# number malayalam movies
malaylam_movies=[mal for mal in all_movies if mal[3]=="malayalam"]
print(len(malaylam_movies))
# theater released movies
theater_released_movies=[Theater for Theater in all_movies if Theater[-1]=="theater"]
print(theater_released_movies)
# list of movies whose rating > 5
rate_five=[five for five in all_movies if five[2]=="5"]
print(rate_five)

# {2022:,4,2021:6,2020:2}
# 2021


movie_out={}
for movie in all_movies:
    year=movie[1]
    if year in movie_out:
        movie_out[year]+=1
    else:
        movie_out[year]=1
print(movie_out)
print(movie_out.items())
out=max(movie_out.items(),key=lambda item:item[1])
print(out)