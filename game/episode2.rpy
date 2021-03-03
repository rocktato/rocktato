label ep_2:
    stop music fadeout 1.0

    bl "I TOLD YOU NOT TO PLAY THE OTHER EPISODES"

    bl "YOU MORON!!!!!"

    if persistent.episode_fin == 2:
        $ persistent.episode_fin = 3
