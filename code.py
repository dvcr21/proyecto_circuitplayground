#importa los modulos
import random as r
from adafruit_circuitplayground import cp
import time

#Declaracion de notas
D = 261.63
F = 349.23
S = 392
L = 440
T = 493.88
D2 = 523.25
R2 = 587.33
Mb = 311.13
F2 = 698.46

#Union en submelodias y concatenacion
mel1 = [D, F, S, L, S, F, D2, S, T, L, S, F, Mb, F, S, D]
mel2 = [D2, D2, L, F, F2, R2, T, L, S, F, S, F, Mb, F]
melody = mel1+mel2

#Melodia
def playmelody(input):
    for i in range(len(melody)):
	#Permite cambio de color aleatorio en todos los pixeles
        cp.pixels.fill((r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)))
        if input:
            cp.play_tone(melody[i], 1)

        else:
            break


cp.pixels.brightness = 0.02
while True:
    switch = cp.switch
    if switch:
        cp.pixels.fill((r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)))
        playmelody(switch)
        time.sleep(0.5)
    else:
        cp.pixels.fill((0, 0, 0))
