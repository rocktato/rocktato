label ep_4:
    stop music fadeout 1.0

    bl "help help help"

    if persistent.episode_fin == 3:
        $ persistent.episode_fin = 4
