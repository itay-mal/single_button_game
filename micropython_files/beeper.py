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
    
def new_highscore_tune():
    tune = [ # we are the champions
    (800, 293, 50),    # D4
    (200, 277, 50),     # C#4
    (200, 293, 50),    # D4
    (400, 277, 50),      # C#4
    (600, 220, 50),    # A3
    (200, 369, 50),    # F#4
    (400, 493, 50),      # B4
    (800, 369, 1000),    # F#4
    (200, 466, 50),     # A4
    (800, 293, 50),     # D4
    (200, 329, 50),    # E4
    (200, 369, 50),     # F#4
    (400, 440, 50),      # A4
    (600, 369, 50),    # F#4
    (100, 493, 50),     # B4
    (100, 277, 50),     # C#4
    (600, 293, 200)     # D4
    ]
    for t,f,s in tune:
        buzz(t,f,s)

def game_over_tune():
    tune = [ # another on bites the dust
    (400, 240, 200),    # 
    (400, 240, 200),    # 
    (400, 240, 400),    # 
    (100, 262, 30),     # C4
    (100, 262, 30),     # C4
    (100, 262, 30),     # C4
    (250, 262, 30),     # C4
    (350, 329, 30),     # D4
    (100, 262, 50),      # C4
    (400, 349, 50),     # F4
    ]
    for t,f,s in tune:
        buzz(t,f,s)

def start_screen_tune():
    tune = [ # eye of the tiger
    (350, 349, 50),    # F4
    (350, 392, 50),    # G4
    (200, 440, 50),    # A4
    (200, 440, 50),    # A4
    (40,  440, 50),    # A4
    (300, 440, 50),    # A4
    (200, 392, 50),    # G4
    (200, 349, 50),    # F4
    (200, 330, 50),    # E4
    (200, 330, 50),    # E4
    (200, 349, 50),    # F4
    (200, 392, 50),    # G4
    (200, 349, 200),   # F4
    (300, 349, 50),    # F4
    (300, 392, 50),    # G4
    (200, 440, 200),   # A4
    (200, 440, 50),    # A4
    (200, 440, 50),    # A4
    (200, 440, 50),    # A4
    (200, 392, 50),    # G4
    (50,  349, 50),    # F4
    (350, 330, 50),    # E4
    (400, 392, 50),    # G4
    (400, 349, 50)     # F4
    ]
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

