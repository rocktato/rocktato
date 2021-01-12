## Character blipping sound things!

init python:
    def blip(file, event, **kwargs):
        if event == "show":
            renpy.music.play(file, channel="blip", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="blip")

    def no_blip(event, **kwargs):
        blip("audio/blips/no.wav", event, **kwargs)

    def rt_blip(event, **kwargs):
        blip("audio/blips/rt.wav", event, **kwargs)

    def wiz_blip(event, **kwargs):
        blip("audio/blips/wiz.wav", event, **kwargs)

    def ph_blip(event, **kwargs):
        blip("audio/blips/ph.wav", event, **kwargs)

    def bl_blip(event, **kwargs):
        blip("audio/blips/bl.wav", event, **kwargs)

    def gin_blip(event, **kwargs):
        blip("audio/blips/gin.wav", event, **kwargs)


## Place to put character settings for the characters who do things
## Character("Rocktato", color="#191970", what_color="#191970")

define no = Character(" ", callback=no_blip)

define space = Character(" ")


define rt = Character("Rocktato", color="#ffffff", callback=rt_blip)

define mr = Character("Mr. Rock", color="#ffffff")

define wiz = Character("Wizpotato", color="#ffffff", size=43, callback=wiz_blip)

define wiz_yell = Character("WIZPOTATO", color="#ffffff", size=34, what_size=70, callback=wiz_blip)

define ph = Character("Phrog", color="#ffffff", callback=ph_blip)

define bl = Character("Blairic", color="#ffffff", what_font="gui/fonts/calibri/Calibri Regular.ttf", callback=bl_blip)

define gin = Character("Gin", color="#ffffff", callback=gin_blip)
