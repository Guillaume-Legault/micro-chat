def on_received_number(receivedNumber):
    if receivedNumber == 9:
        basic.show_number(3)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        basic.pause(500)
        basic.show_number(2)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        basic.pause(500)
        basic.show_number(1)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        basic.pause(200)
        basic.show_string("Go")
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_string("Salut")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_number(9)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_string("Sam le p'tit")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
    """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

basic.clear_screen()
radio.set_group(134)