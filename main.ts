input.onGesture(Gesture.TiltRight, function () {
    basic.showNumber(Set_B * 10 + Count_player_B)
})
input.onButtonPressed(Button.A, function () {
    Count_player_A += 1
    basic.showNumber(Count_player_A)
})
input.onButtonPressed(Button.AB, function () {
    Count_player_A = 0
    Set_A = 0
    Count_player_B = 0
    Set_B = 0
    basic.showNumber(0)
})
input.onButtonPressed(Button.B, function () {
    Count_player_B += 1
    basic.showNumber(Count_player_B)
})
input.onGesture(Gesture.TiltLeft, function () {
    basic.showNumber(Set_A * 10 + Count_player_A)
})
let Set_A = 0
let Count_player_A = 0
let Count_player_B = 0
let Set_B = 0
basic.showNumber(0)
basic.forever(function () {
    if (Count_player_A == 10) {
        Set_A += 1
        Count_player_A = 0
        Count_player_B = 0
    }
    if (Count_player_B == 10) {
        Set_B += 1
        Count_player_A = 0
        Count_player_B = 0
    }
    if (Set_A == 3) {
        basic.showLeds(`
            . # # # .
            . # . # .
            . # # # .
            . # . # .
            . # . # .
            `)
    }
    if (Set_B == 3) {
        basic.showLeds(`
            . # # . .
            . # . # .
            . # # . .
            . # . # .
            . # # . .
            `)
    }
})
