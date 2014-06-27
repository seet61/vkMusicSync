# -*- coding: utf-8 -*-

import os, shutil
import logging
import urllib as request

class manip:
    def check_dir(self, path):
        """Метод проверяет наличие папки 'vkmusic' в директории в /home"""
        try:
            os.chdir(os.environ["HOME"])
            os.chdir('{0}'.format(path))
            logging.info(u'Переходим в папку {0}'.format(os.getcwd()))
            print(u'Переходим в папку {0}'.format(os.getcwd()))
            return os.getcwd()
        except:
            logging.warning(u'Папка {0} не существует!'.format(path))
            print(u'Папка {0} не существует!'.format(path))
            os.chdir(os.environ["HOME"])
            os.mkdir('{0}'.format(path))
            os.chdir(r'{0}'.format(path))
            logging.info(u'Создаем папку')
            print(u'Создаем папку')
            return os.getcwd()

    def check_track(self, name):
        """Проверяем не скачан ли данный файл"""
        if name in os.listdir(os.getcwd()):
            print u'Файл есть'
            return True
        else:
            print u'Файла нет'
            logging.info('Файла %s нет' % name)
            return False

    def download(self, url, name, dirr):
        """Скачиваем файл и приводим его название в нормальный вид"""
        print(u'Скачиваем файл')
        file     = request.URLopener()
        response = file.retrieve(url)
        response = list(response)[0]
        if os.path.exists(response):
            print u'Перемещаем файл в директорию {0}'.format(dirr)
            shutil.move(response, dirr)
            if '\\' in response:
                os.rename(dirr+'\\{0}'.format(response.split('\\')[-1]), '{0}.mp3'.format(name))
            elif '/' in response:
                os.rename(dirr+'/{0}'.format(response.split('/')[-1]), '{0}.mp3'.format(name))
            print(u'Переименовываем файл')
            logging.info('Переименовываем файл {0}'.format(name))
        else:
            print(u'Произошла какая-то ошибка')
            logging.info(u'Произошла какая-то ошибка')
        del response
        file.close()
