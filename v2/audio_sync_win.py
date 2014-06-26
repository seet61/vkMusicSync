#! /usr/bin/python
# -*- coding: utf-8 -*-
"""Данный скрипт предназначен для синхронизации плейлиста пользователя
    на локальный компьютер"""

import connect, manipulation, sys, os
import logging
        
if __name__ == '__main__':
    if os.name == 'nt':
        tmp = os.environ["TMP"]
    elif os.name == 'posix':
        tmp = '/var/tmp'
    logging.basicConfig(format = '%(levelname)-8s [%(asctime)s] %(message)s', level = logging.INFO, filename = r'{0}/vk_audio_sync.log'.format(tmp))
    print u'Добро пожаловать в программу синзронизации вашего плейлиста вк!'
    print u'Введите ваш логин: '
    login = raw_input()
    print u'Введите ваш пароль: '
    password = raw_input()
    print u'Введите название директории: '
    path = raw_input()
    if len(path) < 2:
        path = 'vkmusic'
    profile = connect.connect_vk(login, password)
    user = profile.my_id()
    counter = profile.audio_count(user)
    manip = manipulation.manip()
    dirr = manip.check_dir(path)
    for i in xrange(counter):
        print u'-'*80
        artist, title, url = profile.track_info(i)
        name = artist + '-' + title
        check = manip.check_track(name)
        if check == False:
            manip.download(url, name, dirr)
    del profile
