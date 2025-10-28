import win32com.client
import datetime as dt
import speech_recognition as sr
import math as m
import time
import random
import pygame
import tkinter
import turtle as t
from gues_number import game_2
from uravn2_pyton import uravn
from cliker import klicer
from уклон import game1
from таймер import timerminut
from PIL import ImageGrab
import ctypes
from переводчик import перевод
password = 11402
p = int(input("Введите пароль, для запуска голосового помощника под названием Нейра."))
if password == p:
    print('Запуск...')
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    r = sr.Recognizer()
    now = dt.datetime.now()
    c_time = int(now.strftime("%H"))
    if c_time < 12 and c_time >= 5:
        print('Доброе утро, Святослав!')
        speaker.Speak('Доброе утро, Святослав!')
    if c_time >= 12 and c_time <= 17:
        print('Добрый день, Святослав!')
        speaker.Speak('Добрый день, Святослав!')
    if c_time >= 17 or c_time <5:
        print('Добрый вечер, Святослав!')
        speaker.Speak('Добрый вечер, Святослав!')
    pygame.init()
    def speak_time():
        now = dt.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speaker.Speak(f"Текущее время: {current_time}")
    def speak_date(): 
        today = dt.date.today()
        date = today.strftime("%d %B %Y года")
        speaker.Speak(f"Сегоднейшая дата: {date}")
    def stepen():
        a = int(input('Введите число которое хотите возвести в степень.'))
        b = int(input('Введите степень.'))
        s = a ** b
        print(s)
        speaker.Speak(f'Получилось: {s}')
    def factorial():
        f = int(input('Введите число, у которого хотите найти факториал.'))
        print(m.factorial(f))
        q = m.factorial(f)
        speaker.Speak(f'Получилось: {q}')
    sound1 = pygame.mixer.Sound(r"C:\Users\Igori\Downloads\Neizvesten_-_Funk_estranho_ULTRA-SLOWED_77713519.mp3")#мой плейлист
    sound2 = pygame.mixer.Sound(r"C:\Users\Igori\Downloads\ATLXS_-_PASSO_BEM_SOLTO_79094573.mp3")
    sound3 = pygame.mixer.Sound(r"C:\Users\Igori\Downloads\nightfxrce_-_VALHALLA_77036516.mp3")
    sound4 = pygame.mixer.Sound(r"C:\Users\Igori\Downloads\Eminem_-_-_Mocingbird_75000096.mp3")
    sound5 = pygame.mixer.Sound(r"C:\Users\Igori\Downloads\Eminem_-_Venom_Remix_Remix_73321874.mp3")
    channel1 = pygame.mixer.Channel(1)
    channel2 = pygame.mixer.Channel(2)
    channel3 = pygame.mixer.Channel(3)
    channel4 = pygame.mixer.Channel(4)
    channel5 = pygame.mixer.Channel(5)
    def мойплейлист():
        channel1.play(sound1)
        time.sleep(177)
        channel2.play(sound2)
        time.sleep(123)
        channel3.play(sound3)
        time.sleep(86)
        channel4.play(sound4)
        time.sleep(249)
        channel5.play(sound5)
        time.sleep(281)
        pygame.mixer.Sound.stop()
    mem1 = pygame.mixer.Sound(r"C:\Users\Igori\Downloads\SHrek_igraet_na_saksofone_-_Shrek_(TheMP3.Info).mp3")#мемы
    chan1 = pygame.mixer.Channel(1)
    def мемчики():
        chan1.play(mem1)
    today = dt.date.today()
    day = today.strftime("%d.%m")
    '''def birthday():
        birthdays = {
            "14.02": "вас",
            "22.03": "Мирославу",
            "03.01": "Веру",
            "10.08": "вашу маму",
            "27.11": "вашего папу"
            }
        if day in birthdays:
            name = birthdays[day]
            print(f'Поздравляю {name} с днём рождения!')
            speaker.Speak(f'Поздравляю {name} с днём рождения!')'''
    def party():
        par = {
            "31.12": "Новым годом",
            "07.01": "Рождеством",
            "20.04": "Пасхой"
            }
        if day in par:
            p = par[day]
            print(f'Поздравляю вас с {p}!')
            speaker.Speak(f'Поздравляю вас с {p}!')
    birthday()
    party()
    while True:
        try:
            with sr.Microphone(device_index=1) as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                mic_text = r.recognize_google(audio, language="ru-RU")
                mic_text = mic_text.lower()
                print(f'Вы: {mic_text}')
                today = dt.date.today()
                date = today.strftime("%d %B %Y года")
                now = dt.datetime.now()
                current_time = now.strftime("%H:%M:%S")
                user_input = mic_text
                user_input = user_input.lower()
                if  'когда я тебя создал' in user_input or 'когда я тебя начинал создовать' in user_input:
                    print("Согласно моим данным, вы меня начали создовать 01.08.2025, примерно в 22:11")
                    speaker.Speak("Согласно моим данным, вы меня начали создовать 01.08.2025, примерно в 22:11")
                if  'сколько времени' in user_input or 'который час' in user_input or 'какое время' in user_input or 'время' in user_input:
                    print(f'Текущее время: {current_time}')
                    speak_time()
                if  'какая сегодня дата' in user_input or 'какая дата' in user_input or 'дата' in user_input or 'какое сегодня число' in user_input:
                    print(f"Сегоднейшая дата: {date}")
                    speak_date()
                if 'реши уравнение' in user_input:
                    uravn()
                if 'возведи в степень' in user_input or 'степень' in user_input:
                    stepen()
                if 'найди факториал' in user_input or 'факториал' in user_input:
                    factorial()
                if 'привет' in user_input or 'здарово' in user_input or 'здравствуй' in user_input:
                    print('Здравствуйте!')
                    speaker.Speak('Здравствуйте!')
                if 'как дела' in user_input or "как у тебя дела" in user_input:
                    ran = ["Отлично!", "Хорошо!", "Лучше всех!"]
                    howareyou = random.choice(ran)
                    print(howareyou)
                    speaker.Speak(howareyou)
                if 'повторяй за мной' in user_input or 'повтори за мной' in user_input:
                    print('Я готова повторять, сказанные вами слова.')
                    speaker.Speak('Я готова повторять, сказанные вами слова.')
                    print('Когда захотите, чтобы я перестала, скажите СТОП.')
                    speaker.Speak('Когда захотите, чтобы я перестала скажите СТОП.')
                    while True:
                        with sr.Microphone(device_index=1) as source:
                            r.adjust_for_ambient_noise(source)
                            audio = r.listen(source)
                            mic_text = r.recognize_google(audio, language="ru-RU")
                            print(mic_text)
                            user_input = mic_text
                            user_input = user_input.lower()
                        speaker.Speak(f'{user_input}')
                        if 'стоп' in user_input:
                            break
                            print('Я остановилась.')
                            speaker.Speak('Я остановилась.')
                if user_input == 'нарисуй квадрат' or user_input  == 'нарисуй мне квадрат' or user_input  == 'нарисуй нам квадрат':
                    width = 800
                    height = 800
                    screen = pygame.display.set_mode((width, height))
                    pygame.display.set_caption("Квадрат")
                    white = [255, 255, 255]
                    screen.fill(white)
                    red = [255, 0, 0]
                    green = [0, 255, 0]
                    blue = [0, 0, 255]
                    purpur = [255, 0, 255]
                    yellow = [255, 255, 0]
                    col = [red, green, blue, purpur, yellow]
                    color = random.choice(col)
                    x = 310
                    y = 310
                    side = 200
                    rect = (x, y, side, side)
                    running = True
                    print('Готово!')
                    speaker.Speak('Готово!')
                    while running:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                        screen.fill((255, 255, 255))
                        pygame.draw.rect(screen, color, rect)
                        pygame.display.flip()
                    pygame.quit()
                if 'нарисуй квадрат карандашом' in user_input or 'нарисуй мне квадрат карандашом' in user_input or 'нарисуй нам квадрат карандашом' in user_input:
                    pencil = t.Turtle()
                    print('Рисую...')
                    speaker.Speak('Рисую...')
                    for pen in range(4):
                        pencil.forward(200)
                        pencil.left(90)
                    t.done()
                if 'запусти игру с космическим кораблём' in user_input or 'запусти игру с космосом' in user_input or 'кос' in user_input:
                    print('Запускаю...')
                    speaker.Speak('Запускаю...')
                    score = game1()#в игре присутствуют громкие звуки 
                    if score >= 5:   
                        speaker.Speak(f'Вы набрали {score} очков.')
                    if score <= 4 and score > 0 and score > 1:
                        speaker.Speak(f'Вы набрали {score} очка.')
                    if score == 1:
                        speaker.Speak(f'Вы набрали {score} очко.')
                    if score == 0:
                        speaker.Speak(f'Вы набрали {score} очков.')
                if 'запусти игру кликер' in user_input or 'запусти кликер' in user_input or 'запусти clicer' in user_input or 'запусти игру clicer' in user_input:
                    print('Запускаю...')
                    speaker.Speak('Запускаю...')
                    klicer()
                if 'включи мой плейлист' in user_input or 'запусти мой плейлист' in user_input:
                    vkl = 'включи мой плейлист'
                    zap = 'запусти мой плейлист'
                    if user_input == vkl:
                        print("Включаю.")
                        speaker.Speak("Включаю.")
                    elif user_input == zap:
                        print("Запускаю.")
                        speaker.Speak("Запускаю.")
                    print('Перезапустите программу, для запуска голосового помощника Нейра.')
                    мойплейлист()
                    break
                if 'как тебя зовут' in user_input:
                    print('Меня зовут, Нейра.')
                    speaker.Say('Меня зовут, Нейра.')
                if 'запусти игру угадай число' in user_input or 'включи игру угадай число' in user_input:
                    vkl = 'включи игру угадай число'
                    zap = 'запусти игру угадай число'
                    if user_input == vkl:
                        print("Включаю.")
                        speaker.Speak("Включаю.")
                    elif user_input == zap:
                        print("Запускаю.")
                        speaker.Speak("Запускаю.")
                    game_2()
                if 'а-у' == user_input or 'ау' == user_input:
                    print('Я здесь!')
                    speaker.Speak('Я здесь!')
                if 'отключись' in user_input or 'вырубись' in user_input:
                    print('Отключилась.')
                    speaker.Speak('Отключилась.')
                    break
                if 'засеки таймер' in user_input:
                    timerminut()
                if 'включи приятное для ушей' in user_input or 'включи мемчики' in user_input or 'включи мемы' in user_input:
                    print('Перезапустите программу, для запуска голосового помощника Нейра.')
                    мемчики()
                    break
                if 'сделай скриншот' in user_input:
                    screenshot = ImageGrab.grab()
                    screenshot.save("screenshot.png")
                    print('Готово!(Сохранила в папку PYTON)')
                    speaker.Speak('Готово!')
                if 'переведи текст' in user_input or 'сделай перевод' in user_input or 'перевод' in user_input:
                    translation = перевод()
                    speaker.Speak(f"Перевод: {translation}")
        except sr.UnknownValueError:
            print('Пожалуйста, скажите чётче.')
            speaker.Speak('Пожалуйста, скажите чётче.')
else:
    print('Неверный пароль. Перезапустите программу.')
print('/')
