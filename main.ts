radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 9) {
        basic.showNumber(3)
        music.playTone(262, music.beat(BeatFraction.Whole))
        basic.pause(500)
        basic.showNumber(2)
        music.playTone(262, music.beat(BeatFraction.Whole))
        basic.pause(500)
        basic.showNumber(1)
        music.playTone(262, music.beat(BeatFraction.Whole))
        basic.pause(200)
        basic.showString("Go")
        music.playTone(349, music.beat(BeatFraction.Double))
    }
})
input.onButtonPressed(Button.A, function () {
    radio.sendString("Salut")
})
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(9)
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function () {
    radio.sendString("Sam le p'tit")
})
input.onGesture(Gesture.Shake, function () {
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        `)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.clearScreen()
})
basic.clearScreen()
radio.setGroup(134)
