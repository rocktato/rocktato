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


define rt = Character("Rocktato", color="#bd2919", callback=rt_blip)

define mr = Character("Mr. Rock", color="#000000")

define wiz = Character("Wizpotato", color="#6c538c", size=43, callback=wiz_blip)

define wiz_yell = Character("WIZPOTATO", color="#6c538c", size=34, what_size=50, callback=wiz_blip)

define ph = Character("Phrog", color="#47a65e", callback=ph_blip)

define bl = Character("Blairic", color="#142675", what_font="gui/fonts/calibri/Calibri Regular.ttf", callback=bl_blip)

define gin = Character("Gin", color="#c76816", callback=gin_blip)
