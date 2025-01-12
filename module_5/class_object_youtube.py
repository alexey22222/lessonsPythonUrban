from os.path import curdir
from time import sleep
class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self,nickname, password):
        for user in UrTube.users:
            if user.nickname == nickname:
                if user.password == hash(password):
                    UrTube.current_user = user
    def register(self, nickname, password, age):
        is_nickname = False
        if len(UrTube.users) == 0:
            UrTube.users.append(User(nickname, password, age))
            UrTube.log_in(self, nickname, password)
        else:
            for users in UrTube.users:
                if users.nickname == nickname:
                    is_nickname = True
                    break
            if is_nickname == True:
                print(f'Пользователь {nickname} уже существует')
            else:
                UrTube.users.append(User(nickname, password, age))
                UrTube.log_in(self, nickname, password)
    def log_out(self):
        UrTube.current_user = None
    def add(self, *args):
        for video in args:
            is_true = False
            if len(UrTube.videos) != 0:
                for video_videos in UrTube.videos:
                    if video_videos.title == video.title:
                        is_true = True
            if not(is_true):
                UrTube.videos.append(video)
        pass
    def get_videos(self, string) -> list:
        find_videos = []
        string = string.lower()
        for video in UrTube.videos:
            temp_title_lower = video.title.lower()
            if string in temp_title_lower:
                find_videos.append(video.title)
        return find_videos

    def watch_video(self, title_video_watch):
        def play_video(watch):
            for i in range(1, watch.duration + 2):
                if i == watch.duration + 1:
                    sleep(1)
                    print('Конец видео')
                else:
                    sleep(1)
                    print(i, end=" ")
        if UrTube.current_user is not None:
           for watch in UrTube.videos:
                if title_video_watch == watch.title:
                    if watch.adult_mode:
                        if UrTube.current_user.age >= 18:
                            play_video(watch)
                        else:
                            print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        play_video(watch)
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
    time_now = 0

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def __eq__(self, other):
        return self.nickname == other.nickname and self.age == other.age
    def __hash__(self):
        return hash((self.password,self.nickname))
    def __str__(self):
        return self.nickname


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    # Добавление видео
    ur.add(v1, v2)
    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))
    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')
    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)
    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
