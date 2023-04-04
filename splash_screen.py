import pygame
import math
from pygame import mixer
import pygame, sys
import cv2
class Sp_Screen:
 def show_splash_screen(self):
   mixer.init()  
# Loading the song
   mixer.music.load("titlesong.mp3")
# Setting the volume
   mixer.music.set_volume(0.7)
# Start playing the song
   mixer.music.play()
   video = cv2.VideoCapture("bg.mp4")
   success, video_image = video.read()
   fps = video.get(cv2.CAP_PROP_FPS)
   window = pygame.display.set_mode(video_image.shape[1::-1])
   clock = pygame.time.Clock()
   run = success
   while run:
     clock.tick(16)
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            mixer.music.stop()
        if event.type==pygame.KEYUP:
            run=False
            mixer.music.stop()

     success, video_image = video.read()
     if success:
        
        video_surf = pygame.image.frombuffer(
            video_image.tobytes(), video_image.shape[1::-1], "BGR")
     else:
        run = False
        mixer.music.stop()
     pygame.display.set_caption("Maze Wizard")
     #pygame.display.set_palette(TITLE)
     icon=pygame.image.load('icon.png')
     pygame.display.set_icon(icon)
     window.blit(video_surf, (0, 0))
   #pygame.display.update()
     pygame.display.flip()
     pygame.display.update()

