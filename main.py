def on_gesture_tilt_right():
    basic.show_number(Set_B * 10 + Count_player_B)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_button_pressed_a():
    global Count_player_A
    Count_player_A += 1
    basic.show_number(Count_player_A)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Count_player_A, Set_A, Count_player_B, Set_B
    Count_player_A = 0
    Set_A = 0
    Count_player_B = 0
    Set_B = 0
    basic.show_number(0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Count_player_B
    Count_player_B += 1
    basic.show_number(Count_player_B)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_left():
    basic.show_number(Set_A * 10 + Count_player_A)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

Set_A = 0
Count_player_A = 0
Count_player_B = 0
Set_B = 0
basic.show_number(0)

def on_forever():
    global Set_A, Count_player_A, Count_player_B, Set_B
    if Count_player_A == 10:
        Set_A += 1
        Count_player_A = 0
        Count_player_B = 0
    if Count_player_B == 10:
        Set_B += 1
        Count_player_A = 0
        Count_player_B = 0
    if Set_A == 3:
        basic.show_leds("""
            . # # # .
            . # . # .
            . # # # .
            . # . # .
            . # . # .
            """)
    if Set_B == 3:
        basic.show_leds("""
            . # # . .
            . # . # .
            . # # . .
            . # . # .
            . # # . .
            """)
basic.forever(on_forever)
