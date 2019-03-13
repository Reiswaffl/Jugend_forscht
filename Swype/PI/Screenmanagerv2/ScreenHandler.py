# coding=utf-8
home = "main"


def switch():
    global home
    if home == 'main':
        home = 'testscreen2'
        return home
    elif home == 'testscreen2':
        home = 'testscreen3'
        return home
    elif home == 'testscreen3':
        home = 'main'
        return home
    else:
        home = 'main'
        return home


def sethome(nHome):
    global home
    home = nHome


def gethome():
    # global home
    return home

