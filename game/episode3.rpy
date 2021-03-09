label ep_3:

    $ persistent.mainmenu_img = 3

    stop music fadeout 1.0

    bl "help help help"

    if persistent.episode_fin == 2:
        $ persistent.episode_fin = 3

    $ persistent.mainmenu_img = 4
