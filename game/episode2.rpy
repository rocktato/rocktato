label ep_2:

    $ persistent.mainmenu_img = 2

    stop music fadeout 1.0

    bl "help help help"

    if persistent.episode_fin == 1:
        $ persistent.episode_fin = 2

    $ persistent.mainmenu_img = 3
