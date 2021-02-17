image macarooni logo = "gui/macarooni_logo.png"

image veggiecrew logo = "gui/veggiecrew_logo.png"

label splashscreen:
    scene black
    with Pause(0.5)

    show macarooni logo with dissolve
    with Pause(1.5)

    hide macarooni logo with dissolve
    with Pause(0.5)

    show veggiecrew logo with dissolve
    with Pause(1.5)

    hide veggiecrew logo with dissolve
    with Pause(0.5)
