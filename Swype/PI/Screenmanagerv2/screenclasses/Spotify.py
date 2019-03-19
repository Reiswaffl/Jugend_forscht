# coding=utf-8
from Screenmanagerv2.ScreenHandler import gethome
from Screenmanagerv2.TouchHandler import *

stepwidth = 0.1


class Spotify(Screen):
    play = False

    def startSpotify(self):
        write_Shortcut('openspotify')

    def getHome(self):
        return gethome()

    def getStep(self):
        global stepwidth
        return stepwidth

    def getValue(self):
        return receive_spotifycom('getValue')

    def getRange(self):
        return 1, 100  # receive_spotifycom('getRange')

    def getVolume(self):
        return receive_spotifycom('getVolume')

    def setVolume(self, value):
        write_spotifycom('v' + str(int(value)))

    def getTitle(self):
        return receive_spotifycom('getTitle')

    def playPause(self):
        if not self.play:
            self.ids.playButton.source = 'sources/spotify/pause.png'
            write_spotifycom('play')
            self.play = True
        elif self.play:
            self.ids.playButton.source = 'sources/spotify/play.png'
            write_spotifycom('pause')
            self.play = False

    def forward(self):
        write_spotifycom('forward')

    def back(self):
        write_spotifycom('back')

    def on_touch_down(self, touch):
        on_touch_down(self, touch, Screen)

    def on_touch_move(self, touch):
        on_touch_move(self, touch, Screen)

    def on_touch_up(self, touch):
        on_touch_up(self, touch, Screen)
