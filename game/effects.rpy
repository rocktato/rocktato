#############################################
## FILE WHERE I PUT A BONCH OF CUSTOM EFFECTS N TRANSITIONS N ALL THAT YEAH
#############################################

init:


    ## Nothing.
    transform none:
        pass



    ## Flips character across y axis yeah MATH
    transform flip:
        xzoom -1.0



    ## Shake Transition!! (For some reason Renpy center is whack so idk)
    transform shake(rate, strength, loop=1):
        linear rate xoffset (strength*2) yoffset (strength*-6)
        linear rate xoffset (strength*-2.8) yoffset (strength*-2)
        linear rate xoffset (strength*2.8) yoffset (strength*-2)
        linear rate xoffset (strength*-2) yoffset (strength*-6)
        linear rate xoffset (strength*0) yoffset (strength*0)
        repeat loop



    transform transform_offset(x=0, y=0, speed=0.0):
        linear speed xoffset x
        linear speed yoffset y



    transform transform_zoom(x=1.0, y=1.0):
        xzoom x
        yzoom y



    transform transform_ease(start, end, time):
        subpixel True
        xanchor 0.5
        xpos start
        easein time xpos end
