from enum import Enum


class Genre(Enum):
    Science = 'Science'
    Fiction = 'Fiction'
    Fantasy = 'Fantasy'
    Drama = 'Drama'
    Romance = 'Romance'
    Comedy = 'Comedy'
    Zombies = 'Zombies'
    Action = 'Action'
    Historical = 'Historical'
    Horror = 'Horror'
    War = 'War'
    Story_Telling = 'Story Telling'
    Folklore = 'Folklore'
    Fairy_tale = 'Fairy tale'
    Fable = 'Fable'

    @staticmethod
    def get_all_genres() -> None:
        all_genres = ['Science', 'Fiction', 'Fantasy', 'Drama', 'Romance', 'Comedy', 'Zombies', 'Action',
                      'Historical', 'Horror', 'War', 'Story_Telling', 'Folklore', 'Fairy_tale', 'Fable']
        print("\033[4;95;40m  All options for genres:  \033[00m")

        a = 1
        while a <= 9:
            genre = all_genres[a - 1]
            print(f"  \033[1;30m({a})\033[00m  \033[1;95m {genre} \033[00m", end='\n')
            a += 1
        a = 10
        while a < 16:
            genre = all_genres[a - 1]
            print(f"  \033[1;30m({a})\033[00m \033[1;95m {genre} \033[00m", end='\n')
            a += 1


if __name__ == '__main__':
    Genre.get_all_genres()
