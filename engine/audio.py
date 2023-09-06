import pygame

class Audio:
    volume: float = 1

    def __init__(self, audio_path: str):
        try:
            self.sound = pygame.mixer.Sound(audio_path)
        except pygame.error as err:
            if str(err).startswith("Unable to open file"):
                raise Exception("Engine only supports .WAV audio files sorry kid")

    def play(self, repeat=False):
        self.sound.play((2 ** 32) if repeat else 0)
        
    def stop(self):
        self.sound.stop()