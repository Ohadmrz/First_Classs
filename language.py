from enum import Enum


class Language(Enum):
    Arabic = 'Arabic'
    Chinese = 'Chinese'
    Dutch = 'Dutch'
    English = 'English'
    French = 'French'
    German = 'German'
    Italian = 'Italian'
    Japanese = 'Japanese'
    Portuguese = 'Portuguese'
    Russian = 'Russian'
    Spanish = 'Spanish'
    Thai = 'Thai'
    Yiddish = 'Yiddish'
    Turkish = 'Turkish'
    Hebrew = 'Hebrew'
    Ancient_Egyptian = 'Ancient Egyptian'

    @staticmethod
    def get_all_languages() -> None:
        all_languages = ['Arabic', 'Chinese', 'Dutch', 'English', 'French', 'German', 'Italian',
                         'Japanese', 'Portuguese', 'Russian', 'Spanish', 'Thai', 'Yiddish', 'Turkish',
                         'Hebrew', 'Ancient Egyptian']

        print(f"\033[4;92;40m  All options for languages:  \033[00m")
        a = 1
        while a <= 9:
            language = all_languages[a - 1]
            print(f"   \033[1;30m({a})\033[00m  \033[1;92m {language} \033[00m", end='\n')
            a += 1
        a = 10
        while a < 17:
            language = all_languages[a - 1]
            print(f"   \033[1;30m({a})\033[00m \033[1;92m {language} \033[00m", end='\n')
            a += 1


if __name__ == '__main__':
    Language.get_all_languages()

