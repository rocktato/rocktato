#############################################
## FILE WHERE I PUT A BONCH OF CUSTOM EFFECTS N TRANSITIONS N ALL THAT YEAH
#############################################

init:


    transform phrog_goes_in_and_out_a_door(loop="", where=200, otherwhere=-200):
        subpixel True
        block:
            easeout 0.5 xpos otherwhere
            pause 1.0
            easein 0.5 xpos where
            pause 1.0
            repeat loop



    transform super_cool_rocktato_tm_kick_attack:
        rotate 0.0
        yanchor 0.875
        linear 0.5 xoffset 200 rotate 90.0 yoffset 80
        linear 0.3 xoffset -1100


    transform super_cool_rocktato_tm_kick_attack_victim(wait=0):
        pause wait
        linear 0.3 xoffset -1100



    transform funny_expand:
        zoom 1.0
        linear 1.0 zoom 5.0 xzoom 10.0 ycenter 1.0



    ## Character does a lil hop!!! A lil bounce!! Boinininig!!
    transform bounce:
        yoffset 0.0
        easein 0.175 yoffset -20
        easeout 0.075 yoffset 0
        easein 0.175 yoffset -4
        easeout 0.075 yoffset 0
        yoffset 0.0


    ## Repeated bouncing!
    transform bouncing:
        yoffset 0.0
        easein 0.175 yoffset -20
        easeout 0.075 yoffset 0
        easein 0.175 yoffset -4
        easeout 0.075 yoffset 0
        linear 0.5 yoffset 0.0
        repeat



    ## Repeated shaking (slow and fast)
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



    ## Animation used in loading screen.
    transform loading_anim:
        xzoom 0.5 yzoom 0.5

        block:
            rotate None
            ease 0.5 rotate 360.0
            pause 0.5

            repeat
