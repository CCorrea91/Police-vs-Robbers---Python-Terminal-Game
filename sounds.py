from pygame import mixer

# Sound player
def play_sound(sound):
    mixer.init()
    sound_effect = mixer.Sound(sound)
    sound_effect.set_volume(0.3)
    sound_effect.play(0, 1000)


def play_themesong(song):
    mixer.init()
    mixer.music.load(song)
    mixer.music.set_volume(0.15)
    mixer.music.play(-1)
    
def stop_themesong():
    mixer.stop()
    
sound_library = {
    "theme_song": "F:\Coding\Codecademy\Python Console Game\Python-Terminal-Game\sounds\Theme Music.mp3",
    "press_enter": "F:\Coding\Codecademy\Python Console Game\Python-Terminal-Game\sounds\Enter_key_sound.mp3",
    "game_over": "F:\Coding\Codecademy\Python Console Game\Python-Terminal-Game\sounds\Victory.mp3",
    "move": "F:\Coding\Codecademy\Python Console Game\Python-Terminal-Game\sounds\move.mp3",
    "shoot": "F:\Coding\Codecademy\Python Console Game\Python-Terminal-Game\sounds\ShotgunFire.wav",
    "missed-shot": "F:\Coding\Codecademy\Python Console Game\Python-Terminal-Game\sounds\Shoot.mp3",
    "cover": "F:\Coding\Codecademy\Python Console Game\Python-Terminal-Game\sounds\cover.mp3"
}
