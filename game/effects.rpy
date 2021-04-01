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






    transform transform_zoom(x=1.0, y=1.0):
        xzoom x
        yzoom y


    transform transform_easein_pos(xstart=0, ystart=0, xend=0, yend=0, time):
        subpixel True
        xanchor 0.5
        xpos xstart ypos ystart
        easein time xpos xend ypos yend


    transform transform_easeout_pos(xstart=0, ystart=0, xend=0, yend=0, time):
        subpixel True
        xanchor 0.5
        xpos xstart ypos ystart
        easeout time xpos xend ypos yend


    transform transform_offset(x=0, y=0, speed=0.0):
        linear speed xoffset x
        linear speed yoffset y


    transform transform_easein_offset(x=0, y=0, time=0.5):
        easein time xoffset x yoffset y


    transform transform_easeout_offset(x=0, y=0, time=0.5):
        easeout time xoffset x yoffset y
