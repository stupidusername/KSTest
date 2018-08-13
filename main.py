import kivy
from kivy.app import App
from kivy.core.audio import SoundLoader

kivy.require('1.11.0')


class KSTestApp(App):

    def play(self):
        sound = SoundLoader.load('test.wav')
        sound.play()


if __name__ == '__main__':
    KSTestApp().run()
