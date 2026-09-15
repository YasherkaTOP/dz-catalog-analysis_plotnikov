import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet",
                                                    "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies):
    '''
    Вычисляет средний рейтинг фильмов.
    '''
    total_rating = sum(movie["rating"] for movie in movies)
    avg_rating = total_rating / len(movies)
    return round(avg_rating, 1)


def catalog_age_stats(movies, current_year=2026):
    '''
    Вычисляет статистику возраста фильмов.
    '''
    ages = [current_year - movie["year"] for movie in movies]
    average_age = math.ceil(sum(ages) / len(ages))
    oldest_age = max(ages)
    newest_age = min(ages)
    return (oldest_age, newest_age, average_age)


def duration_in_hours(minutes):
    '''
    Преобразует минуты в формат часов и минут.
    '''
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"


def rating_tier(rating):
    '''
    Определяет уровень рейтинга.
    '''
    if rating >= 9.0:
        return "шедевр"
    elif rating >= 7.0:
        return "хорошо"
    else:
        return "средне" if rating >= 5.0 else "слабо"


def decade_label(year):
    '''
    Определяет декаду выпуска фильма.
    '''
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


def print_not_comedy_movies(movies):
    '''
    Выводит названия фильмов, не относящихся к жанру комедия.
    '''
    for movie in movies:
        if "comedy" not in movie["genres"]:
            continue
        print(movie["title"])


def print_first_movie_with_rating_above_9(movies):
    '''
    Выводит название первого фильма с рейтингом выше 9.0.
    '''
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9.0:
            print(movies[i]["title"])
            break
        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    '''
    Считает количество фильмов с продолжительностью больше заданного порога.
    '''
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title):
    '''
    Нормализует название фильма в Title Case.
    '''
    words = title.split(" ")
    normalized_words = []
    for word in words:
        normalized_words.append(word[0].upper() + word[1:])
    normalized_title = " ".join(normalized_words)
    return normalized_title


def make_slug(title):
    '''
    Создает slug формат строку для названия фильма.
    '''
    normalized_title = normalize_title(title).lower()
    slug = normalized_title.replace(" ", "-")
    return slug


def format_report_line(movie):
    '''
    Формирует единую строку с информацией о фильме.
    '''
    title = normalize_title(movie["title"])
    year = movie["year"]
    duration = duration_in_hours(movie["duration_min"])
    rating = movie["rating"]
    genres = ", ".join(sorted(movie["genres"]))

    report_line = f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres}'
    return report_line


def titles_sorted_by_rating(movies):
    '''
    Возвращает список названий фильмов, отсортированных по рейтингу в порядке убывания.
    '''
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    sorted_titles = [movie["title"] for movie in sorted_movies]
    return sorted_titles


def top_n_by_rating(movies, n=3):
    '''
    Возвращает список из n лучших фильмов по рейтингу.
    '''
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    top_n_movies = [(movie["title"], movie["rating"]) for movie in sorted_movies][:n]
    return top_n_movies


def count_by_genre(movies):
    '''
    Считает количество фильмов по жанрам.
    '''
    genre_count = {}
    for movie in movies:
        for genre in movie["genres"]:
             genre_count[genre] = genre_count.get(genre, 0) + 1
    # В примере результата словарь отсортирован по убыванию количества фильмов в жанре. 
    # Я сделал также.
    sorted_genre_count = dict(sorted(genre_count.items(), key=lambda x: x[1], 
                                     reverse=True))
    return sorted_genre_count


def actor_filmography(movies):
    '''
    Возвращает словарь с фильмографией актеров.
    '''
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography[actor] = filmography.get(actor, [])
            filmography[actor].append(movie["title"])
    return filmography


def above_average_movies(movies):
    '''
    Возвращает словарь с фильмами, рейтинг которых выше среднего.
    '''
    average = average_rating(movies)
    above_average = {movie["title"]: 
                     movie["rating"] for movie in movies if movie["rating"] > average}
    return above_average


def all_genres(movies):
    '''
    Возвращает уникальное множество всех жанров фильмов.
    '''
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return genres


def common_actors(movie1, movie2):
    '''
    Возвращает множество актеров, участвовавших в обоих фильмах.
    '''
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])
    common = actors1 & actors2
    return common


def genres_only_in_one(movies_a, movies_b):
    '''
    Возвращает множество жанров, которые присутствуют только в первом из 
    двух списков фильмов.
    '''
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)
    unique_genres = genres_a - genres_b
    return unique_genres


def iter_high_rated(movies, min_rating=8.0):
    '''
    Генератор фильмов с рейтингом выше заданного.
    '''
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def demonstrate_iter_high_rated(movies):
    '''
    Демонстрирует использование генератора фильмов с рейтингом выше заданного.
    '''
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))


def sum_duration_with_rating_above_7(movies):
    '''
    Считает суммарную продолжительность фильмов с рейтингом выше 7.
    '''
    # В примере так предлагалось:
    total_duration = sum(m["duration_min"] for m in movies if m["rating"] > 7)
    # Но я сделал через генератор, чтобы показать его использование:
    total_duration = sum(movie["duration_min"] for movie in iter_high_rated(movies, 7))
    return total_duration


def build_report(movies):
    '''
    Строит финальный отчет по каталогу фильмов.
    '''
    avg_rating = average_rating(movies)
    _, _, average_age = catalog_age_stats(movies)
    top_movies = top_n_by_rating(movies, 3)
    genre_counts = count_by_genre(movies)
    genres = sorted(all_genres(movies))

    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {avg_rating}")
    print(f"Средний возраст фильмов: {average_age} лет")
    
    print("\nТоп-3 фильма:")
    for title, _ in top_movies:
        movie = next(movie for movie in movies if movie["title"] == title)
        print(f"  {format_report_line(movie)}")

    print("\nФильмов по жанрам:")
    # Уже был отсортирован в функции count_by_genre
    for genre, count in genre_counts.items():
        print(f"  {genre} — {count}")

    print(f"\nВсе жанры каталога: {', '.join(genres)}")

if __name__ == "__main__":
    build_report(movies)
