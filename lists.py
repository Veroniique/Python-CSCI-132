'''
Pair assignment - Creating lists and printing results
26 February 2024
'''

#number1 - creating a list
movies = ["Honey I shrunk the kids", "Avatar", "The Lord of the Rings", "The Godfather", "Lost in Translation"]
print(movies)

#number2 - adding to list
movies.append("Cheaper by the Dozen")
movies.append("Taken")
movies.append("Toy Story")
print(movies)

#number3 - creating a loop
#print colors in a loop that start with a -
for movie in movies:
        print("-" + movie)

#number4
print(movies[1]) #second movie
print(movies[-1]) #last movie
movies[2] = "Wakanda Forever" #changes 3rd movie
print(movies)
print(movies[2])

index_god = movies.index("The Godfather")
print("Index of The Godfather: ", index_god)
movies[index_god] = "Parasite"
print(movies)

#number5
del movies[1]
print(movies)
del movies[2]
print(movies)

#number6
movies.insert(0,"Bend it Like Beckham")
print(movies)

#number7
print(len(movies))
print(sorted(movies))

#number8
new_movies = ["Cheaper by the Dozen", "Taken", "Toy Story"]
print(new_movies)

#number9
user_movie = input("Enter a movie name to see if it is on the list: ")
if user_movie in new_movies:
    print("The movie exists on the list!")

#number10
user_search = input("Enter a term for a movie you'd like to search: ")
count = 0
print("Movies containing the search term: ")
for movie in movies:
    if user_search.lower() in movie.lower():
        print(movie)
        count += 1

print("Total number of movies containing your search term: ", count)