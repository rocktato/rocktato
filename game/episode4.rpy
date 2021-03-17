label ep_4:

    $ persistent.mainmenu_img = 4

    stop music fadeout 1.0

    bl "help help help"

    if persistent.episode_fin == 3:
        $ persistent.episode_fin = 4

    $ persistent.mainmenu_img = 5
