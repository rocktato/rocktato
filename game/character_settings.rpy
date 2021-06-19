## Character blipping sound things!

init python:
    def blip(file, event, **kwargs):
        if event == "show":
            renpy.music.play(file, channel="blip", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="blip")

    def no_blip(event, **kwargs):
        blip("audio/blips/no.ogg", event, **kwargs)

    def rt_blip(event, **kwargs):
        blip("audio/blips/rt.ogg", event, **kwargs)

    def wiz_blip(event, **kwargs):
        blip("audio/blips/wiz.ogg", event, **kwargs)

    def ph_blip(event, **kwargs):
        blip("audio/blips/ph.ogg", event, **kwargs)

    def bl_blip(event, **kwargs):
        blip("audio/blips/bl.ogg", event, **kwargs)

    def gin_blip(event, **kwargs):
        blip("audio/blips/gin.ogg", event, **kwargs)


## Place to put character settings for the characters who do things
## Character("Rocktato", color="#191970", what_color="#191970")

define no = Character(" ", callback=no_blip)

define space = Character(" ")

define que = Character("???", callback=no_blip)


define rt = Character("Rocktato", color="#bd2919", callback=rt_blip)
define rt_no = Character("Some Kid", color="#bd2919", size=43, callback=rt_blip)
define rt_que = Character("???", color="#bd2919", callback=rt_blip)

define mr = Character("Mr. Rock", color="#000000")

define wiz = Character("Wizpotato", color="#6c538c", size=43, callback=wiz_blip)
define wiz_yell = Character("WIZPOTATO", color="#6c538c", size=34, what_size=50, callback=wiz_blip)
define wiz_que = Character("???", color="#6c538c", size=43, callback=wiz_blip)
define wiz_yell_que = Character("???", color="#6c538c", size=43, what_size=50, callback=wiz_blip)

define ph = Character("Phrog", color="#47a65e", callback=ph_blip)

define bl = Character("Blairic", color="#142675", what_font="gui/fonts/calibri/Calibri Regular.ttf", what_size=36, y_offset=300, callback=bl_blip)

define gin = Character("Gin", color="#c76816", callback=gin_blip)


define chef = Character("Mangga", color="#bfa524", callback=no_blip)

define bt = Character("Bar Tender", color="#1e591a", size=43)

define fm = Character("Fireman", color="#1e591a", size=43)

define ff1 = Character("Firefighter 1", color="#fa691b", size=43) # Cobs
define ff2 = Character("Firefighter 2", color="#fa691b", size=43) # Ralph
define ff3 = Character("Firefighter 3", color="#fa691b", size=43) # Buggie
define ffu = Character("Unnamed Firefighter", color="#fa691b", size=40)

define bw = Character("Bowser", color="#784b13", callback=no_blip)
define bw_que = Character("???", color="#784b13", callback=no_blip)
