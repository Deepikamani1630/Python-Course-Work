# Netflix App - Show Information System

# Task 1: Take Show/Movie Details as Input
show_id = int(input("Enter Show ID: "))
title = input("Enter Title: ")
imdb_rating = float(input("Enter IMDb Rating: "))
genres = input("Enter Genres (comma-separated): ").split(',')

seasons = int(input("Enter Number of Seasons: "))
episodes = int(input("Enter Total Episodes: "))
seasons_episodes = (seasons, episodes)

completion_rate = float(input("Enter Completion Rate (%): "))
features = set(input("Enter Available Features (comma-separated): ").split(','))

creator_name = input("Enter Creator Name: ")
creator_contact = input("Enter Creator Contact: ")
creator_country = input("Enter Creator Country: ")
creator_info = {
    "Name": creator_name,
    "Contact": creator_contact,
    "Country": creator_country
}

# Task 2: Display Details Using Different Formatting Methods

# 1. Using Comma Separation (sep=',')
print("\n****Show Details (Comma Separated)**** ")
print("Show ID, Title, IMDb Rating:", show_id, title, imdb_rating, sep=',')

# 2. Using Percentage Formatting
print("\n****Completion Rate ***")
print("Completion Rate: %.2f%%" % completion_rate)

# 3. Using f-strings
print("\n**** Show Summary (f-strings) ****")
print(f"Title: {title}")
print(f"IMDb Rating: ⭐ {imdb_rating}/10")
print(f"Genres: {', '.join(genres)}")
print(f"Seasons: {seasons_episodes[0]}, Episodes: {seasons_episodes[1]}")
print(f"Features: {', '.join(features)}")

# 4. Using .format() Method
print("\n**** Creator Info (.format method) ****")
print("Creator: Name - {}, Contact - {}, Country - {}".format(
    creator_info["Name"], creator_info["Contact"], creator_info["Country"]
))
