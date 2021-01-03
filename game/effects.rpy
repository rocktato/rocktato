#############################################
## FILE WHERE I PUT A BONCH OF CUSTOM EFFECTS N TRANSITIONS N ALL THAT YEAH
#############################################


## Character does a lil hop!!! A lil bounce!! Boinininig!!
init:
    transform bounce:
        yoffset 0.0
        easein 0.175 yoffset -20
        easeout 0.075 yoffset 0
        easein 0.175 yoffset -4
        easeout 0.075 yoffset 0
        yoffset 0.0


## Repeated bouncing!

init:
    transform bouncing:
        yoffset 0.0
        easein 0.175 yoffset -20
        easeout 0.075 yoffset 0
        easein 0.175 yoffset -4
        easeout 0.075 yoffset 0
        linear 0.5 yoffset 0.0
        repeat



## Shake Transition!! (For some reason Renpy center is whack so idk)
init:
    transform shake(rate, strength, loop=1):
        linear rate xoffset (strength*2) yoffset (strength*-6)
        linear rate xoffset (strength*-2.8) yoffset (strength*-2)
        linear rate xoffset (strength*2.8) yoffset (strength*-2)
        linear rate xoffset (strength*-2) yoffset (strength*-6)
        linear rate xoffset (strength*0) yoffset (strength*0)
        repeat loop

init:
    transform shakecenter(rate, strength, loop=1):
        linear rate xoffset (strength*-12) yoffset (strength*-6)
        linear rate xoffset (strength*-14.8) yoffset (strength*-2)
        linear rate xoffset (strength*-11.2) yoffset (strength*-2)
        linear rate xoffset (strength*-16) yoffset (strength*-6)
        linear rate xoffset (strength*-14) yoffset (strength*0)
        repeat loop


## Repeated shaking (slow and fast)
init:
    transform slow_shaking:
        xzoom 1.22 yzoom 1.22

        block:
            linear 0.15 xoffset -2 yoffset 2
            linear 0.15 xoffset -1 yoffset 1
            linear 0.15 xoffset 0 yoffset 0
            linear 0.15 xoffset 1 yoffset -1
            linear 0.15 xoffset 2 yoffset -2
            linear 0.15 xoffset 3 yoffset -3
            linear 0.15 xoffset 4 yoffset -4
            linear 0.15 xoffset -1 yoffset -5
            linear 0.15 xoffset -6 yoffset -6
            linear 0.15 xoffset -5 yoffset -4
            linear 0.15 xoffset -4 yoffset -2
            linear 0.15 xoffset -3 yoffset 0
            linear 0.15 xoffset -2 yoffset 2
            linear 0.15 xoffset -3 yoffset 3
            linear 0.15 xoffset -4 yoffset 4
            linear 0.15 xoffset -3 yoffset 2
            linear 0.15 xoffset -2 yoffset 0
            linear 0.15 xoffset -1 yoffset -1
            linear 0.15 xoffset 1 yoffset -2
            linear 0.15 xoffset 3 yoffset -3
            linear 0.15 xoffset 2 yoffset -1
            linear 0.15 xoffset 1 yoffset 2
            linear 0.15 xoffset 0 yoffset 1
            linear 0.15 xoffset -1 yoffset -1
            linear 0.15 xoffset -2 yoffset -2
            linear 0.15 xoffset 1 yoffset -3
            linear 0.15 xoffset 4 yoffset -4
            linear 0.15 xoffset 1 yoffset -5
            linear 0.15 xoffset -1 yoffset -4
            linear 0.15 xoffset -3 yoffset -3
            linear 0.15 xoffset -2 yoffset -1
            linear 0.15 xoffset -4 yoffset 2
            linear 0.15 xoffset -3 yoffset 0
            linear 0.15 xoffset -2 yoffset -2
            linear 0.15 xoffset 1 yoffset -3
            linear 0.15 xoffset 4 yoffset -4
            linear 0.15 xoffset 5 yoffset -5
            linear 0.15 xoffset 6 yoffset -6

            repeat


init:
    transform fast_shaking:

        block:
            linear 0.01 xoffset -12 yoffset 12
            linear 0.01 xoffset -6 yoffset 6
            linear 0.01 xoffset 0 yoffset 0
            linear 0.01 xoffset 4 yoffset -4
            linear 0.01 xoffset 16 yoffset -16
            linear 0.01 xoffset 10 yoffset -10
            linear 0.01 xoffset 6 yoffset -6
            linear 0.01 xoffset 12 yoffset 12

            repeat
