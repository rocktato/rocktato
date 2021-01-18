screen battle_health():
    for x in range(len(chara_healths)):
        $ health = chara_healths[x]
        $ max_health = chara_maxhealths[x]
        $ hp_x, hp_y = chara_hppositions[x]

        fixed:
            text str(health) + "/" + str(max_health) xpos hp_x + 235 ypos hp_y - 18 size 24

        bar value AnimatedValue(value = health, range = max_health, delay = 0.5):
                 xpos hp_x
                 ypos hp_y
                 xmaximum 271
                 ymaximum 38
                 left_bar Frame("gui/bar/hpbar_full.png")
                 right_bar Frame("gui/bar/hpbar_empty.png")
                 thumb None
                 thumb_shadow None
