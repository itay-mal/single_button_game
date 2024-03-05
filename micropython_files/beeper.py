from machine import Pin, PWM
from time import sleep_ms

buzzer_pin = Pin(23, Pin.OUT)
buzzer_pwm = PWM(buzzer_pin)
buzzer_pwm.duty(0) # to start quiet

def buzz(duration_ms, frequency, quiet_ms):
    # musical notes frequencies:
    #        C4: 261.63 Hz
    #        C#4 / Db4: 277.18 Hz
    #        D4: 293.66 Hz
    #        D#4 / Eb4: 311.13 Hz
    #        E4: 329.63 Hz
    #        F4: 349.23 Hz
    #        F#4 / Gb4: 369.99 Hz
    #        G4: 392.00 Hz
    #        G#4 / Ab4: 415.30 Hz
    #        A4: 440.00 Hz
    #        A#4 / Bb4: 466.16 Hz
    #        B4: 493.88 Hz
    buzzer_pwm.freq(frequency)  # Set the PWM frequency
    buzzer_pwm.duty(512)        # Set the PWM duty cycle (50% for a beep)
    sleep_ms(duration_ms)
    buzzer_pwm.duty(0)
    sleep_ms(quiet_ms)
    
def game_over_tune():
    tune = [(400, 494, 0),  # B4
            (300, 415, 0),  # G#4
            (250, 370, 0),  # F#4
            (200, 330, 0),  # E4
            (150, 311, 0),  # D#4
            (100, 277, 0),  # C#4
            (100, 247, 0),  # B3
            (100, 208, 0),  # G#3
            (100, 185, 0),  # F#3
            (100, 165, 0),  # E3
            (100, 156, 0),  # D#3
            (100, 139, 0)]   # C#3
    for t,f,s in tune:
        buzz(t,f,s)

def extra_life_buzz():
    buzz(20,600,40)
    buzz(20,600,0)

def life_lost_buzz():
    buzz(20,400,0)

def wall_expand_buzz():
    buzz(30,400,0)
    buzz(30,450,0)
    buzz(30,550,0)

