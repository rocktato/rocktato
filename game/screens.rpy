################################################################################
## Initialization
################################################################################

init offset = -1

default persistent.confirm_saveload = True

default saveable = True

default choice_screen_type = "choice"

default persistent.episode_fin = 0

default persistent.mainmenu_img = 0

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/bar_left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/bar_right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/bar_top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bar_bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

transform namerotation:
    rotate -2
    xpos 110
    ypos 27
    xanchor 0.5
    yanchor 0.5

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who" at namerotation

        text what id "what"


    ## If there's a side image, display it above the text.
    add SideImage() xalign 0.0 yalign 1.0

## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


## Textbox, Namebox, and Border
style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    outlines [ (3, "#FFFFFF") ]
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    outlines [ (3, "#1e146b") ]

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    outlines [ (3, "#1e146b") ]
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width
    color "ffffff"
    outlines [ (3, "#1e146b") ]


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

# TODO CHOICE BOXES SPRITES

init:
    transform choiceboxfadein:
        subpixel True
        alpha 0.0
        parallel:
            easein 0.3 alpha 1.0
        on hide:
            alpha 1 zoom 1 xanchor 0.5 yanchor 0.5

screen choice(items):
    style_prefix choice_screen_type

    window:
        frame:
            background None

            vbox:
                at choiceboxfadein
                style str(choice_screen_type) + "_vbox"

                for i in items:
                    textbutton i.caption action i.action



## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xanchor 0.5
    xpos 640
    ypos -250
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    hover_sound "audio/ui/choice_hover.ogg"
    activate_sound "audio/ui/choice_activate.ogg"
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


style fight_choice_vbox is hbox
style fight_choice_button is button
style fight_choice_button_text is button_text

style fight_choice_vbox:
    xanchor 0.5
    xpos 640
    ypos -400
    yanchor 0.5


    spacing gui.choice_spacing

style fight_choice_button is default:
    hover_sound "audio/ui/choice_hover.ogg"
    activate_sound "audio/ui/choice_activate.ogg"
    properties gui.button_properties("fight_choice_button")

style fight_choice_button_text is default:
    yoffset 10
    properties gui.button_text_properties("fight_choice_button")


## The Pause sCREen #############################################################
##

## TODO FIX

screen pause():
    python:
        renpy.music.stop(channel="blip", fadeout=None)

    tag menu
    zorder 1000
    modal True

    key "K_ESCAPE" action Return()

    fixed:
        add "gui/pause_screen.png"


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.


screen quick_menu():
    ## Ensure this appears on top of other screens.
    zorder 100

    # KEYMAPS
    key "ctrl_shift_K_q" action renpy.quit
    key "K_ESCAPE" action Play("sound", "audio/ui/pause.ogg"), ShowMenu("pause")
    key "a" action MainMenu()
    key "s" action ShowMenu("save")
    key "d" action ShowMenu('preferences')

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.02
            ypos 15
            spacing 10

            imagebutton auto "gui/quick menu/menubutton_%s.png" action MainMenu() hover_sound "audio/ui/menu_hover.ogg"
            imagebutton auto "gui/quick menu/savebutton_%s.png" action ShowMenu('save') hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/menu_activate.ogg"
            imagebutton auto "gui/quick menu/settingsbutton_%s.png" action ShowMenu('preferences') hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/menu_activate.ogg"
            imagebutton auto "gui/quick menu/rollback_%s.png" action Rollback() hover_sound "audio/ui/menu_hover.ogg"
            imagebutton auto "gui/quick menu/forward_%s.png" action RollForward() hover_sound "audio/ui/menu_hover.ogg"
            imagebutton auto "gui/quick menu/fastforward_%s.png" action Skip(fast=False) hover_sound "audio/ui/menu_hover.ogg"




## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")
    config.gl_resize=False


default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Game Menu Screen
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the game menu, and provides navigation
## to other menus.

screen navigation():
    python:
        renpy.music.stop(channel="blip", fadeout=None)

    fixed:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.3

        add "gui/game menu/geeary.png"

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.85

        spacing gui.navigation_spacing

        imagebutton auto "gui/game menu/savefiles_%s.png" action ShowMenu("save") hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/menu_activate.ogg"

        imagebutton auto "gui/game menu/settings_%s.png" action ShowMenu("preferences") hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/menu_activate.ogg"

        # if _in_replay:
            # textbutton _("End Replay") action EndReplay(confirm=True)

        if not main_menu:
            imagebutton auto "gui/game menu/mainmenu_%s.png" action MainMenu() hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/menu_activate.ogg"

            imagebutton auto "gui/game menu/quitgame_%s.png" action Quit(confirm=not main_menu) hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/menu_activate.ogg"


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu
init:
    transform mm_zoom:
        zoom 0.85

screen main_menu():
    key "ctrl_shift_K_q" action renpy.quit

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    python:
        renpy.music.stop(channel="blip", fadeout=None)
        renpy.music.stop(channel="sound", fadeout=None)
        renpy.music.stop(channel="voice", fadeout=None)
        if renpy.music.is_playing(channel="music") == False and renpy.get_screen("main_menu"):
            renpy.music.play("audio/music/midnight stinkies/midnight stinkies p" + str(persistent.episode_fin) + ".mp3", channel="music", loop=True, fadeout=None)

    add "gui/ep thumbs/" + str(persistent.mainmenu_img) + ".PNG" at slow_shaking

    ## This empty frame darkens the main menu.
    frame:
        pass

    fixed:
        xpos 15
        ypos 15

        add gui.game_title

    imagebutton auto "gui/main menu/epSel_%s.png":
        xpos 20
        ypos 270
        hover_sound "audio/ui/menu_hover.ogg"
        activate_sound "audio/ui/menu_activate.ogg"

        action ShowMenu("ep_select") at mm_zoom

    imagebutton auto "gui/main menu/continue_%s.png":
        xpos 100
        ypos 395
        hover_sound "audio/ui/menu_hover.ogg"
        activate_sound "audio/ui/menu_activate.ogg"

        action [ SensitiveIf(persistent.mainmenu_img > 0), ShowMenu("continue")] at mm_zoom

    imagebutton auto "gui/main menu/extras_%s.png":
        xpos 20
        ypos 510
        hover_sound "audio/ui/menu_hover.ogg"
        activate_sound "audio/ui/menu_activate.ogg"

        action ShowMenu("mm_preferences") at mm_zoom

    imagebutton auto "gui/main menu/settings_%s.png":
        xpos 100
        ypos 628
        hover_sound "audio/ui/menu_hover.ogg"
        activate_sound "audio/ui/menu_activate.ogg"

        action ShowMenu("mm_preferences") at mm_zoom

    imagebutton auto "gui/main menu/exit_%s.png":
        xpos 250
        ypos 628
        hover_sound "audio/ui/menu_hover.ogg"
        activate_sound "audio/ui/menu_activate.ogg"

        action Quit(confirm=not main_menu) at mm_zoom

    # if gui.show_name:

        # vbox:
            # text "[config.name!t]":
                # style "main_menu_title"

    #text "[config.version]":
        # Determines position of the version number
        #xpos 1265
        #ypos 675
        #style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/main menu/main_menu_bar.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

## THIS ONE WILL BE USED IN GAME (HAS SAVE FILES, SETTINGS, UHHHHHH YKNO)


screen game_menu(title, scroll=None, yinitial=0.0):
    python:
        renpy.music.stop(channel="blip", fadeout=None)

    # KEYMAP
    key "a" action MainMenu()
    key "ctrl_shift_K_q" action renpy.quit

    style_prefix "game_menu"


    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    imagebutton auto "gui/x_%s.png":
        xpos 17
        ypos 17
        hover_sound "audio/ui/menu_hover.ogg"
        activate_sound "audio/ui/menu_activate.ogg"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30



## Load and Save screen #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

default persistent.slot_files = dict()
default persistent.saveepisode_img = 1

init:
    python:
        def deletefiles():
            for i in range(6):
                fn = str(i+1) + "-" + str(1)

                renpy.unlink_save(fn)

init:
    python:
        def savefile(slot):
            persistent.slot_files[slot] = persistent.saveepisode_img
            renpy.run(FileSave(slot, confirm=persistent.confirm_saveload, newest=True))

        def loadfile(slot):
            persistent.mainmenu_img = persistent.slot_files.get(slot)
            renpy.run(FileLoad(slot, confirm=persistent.confirm_saveload))

screen save():

    tag menu

    key "s" action Return()
    key "d" action Play("sound", "audio/ui/menu_activate.ogg"), ShowMenu("preferences")

    default page_name_value = FilePageNameInputValue(pattern=_("page {}"))

    use game_menu(_("Save Files")):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            hbox:
                style "page_label"
                xalign 0.565
                yalign -0.1

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.7
                yalign 0

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_(""), empty=_("empty slot")):
                            #"{#file_time}%A, %B %d %Y, %H:%M"
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

            ## Buttons to delete, save, or load a file :)
            imagebutton auto "gui/save menu/save_%s.png":
                xpos 200
                ypos 450
                hover_sound "audio/ui/menu_hover.ogg"
                activate_sound "audio/ui/save_activate.ogg"

                action [ Function(savefile, slot), SensitiveIf(saveable == True) ] #FileSave(slot, confirm=True, newest=True)

            imagebutton auto "gui/save menu/play_%s.png":
                xpos 460
                ypos 450
                hover_sound "audio/ui/menu_hover.ogg"

                action Function(loadfile, slot), SensitiveIf(FileLoadable(1, page_name_value.get_page()))  #FileLoad(slot)

            imagebutton auto "gui/save menu/trash_%s.png":
                xpos 720
                ypos 450
                hover_sound "audio/ui/menu_hover.ogg"
                activate_sound "audio/ui/trash_activate.ogg"

                action FileDelete(slot)


            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.765
                yalign 0.4

                spacing gui.page_spacing

                textbutton _("<"):
                    hover_sound "audio/ui/menu_hover.ogg"
                    activate_sound "audio/ui/menu_activate.ogg"

                    action FilePagePrevious(max=6, wrap=True, auto=False, quick=False)
                textbutton _(">"):
                    hover_sound "audio/ui/menu_hover.ogg"
                    activate_sound "audio/ui/menu_activate.ogg"

                    action FilePageNext(max=6, wrap=True, auto=False, quick=False)

                ## Number of save sloterinos
                # for page in range(1, 6):
                    # textbutton "[page]" action FilePage(page)


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen settings screen allows the player to configure
## the game to better suit themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    key "s" action ShowMenu("save")
    key "d" action Return()

    use game_menu(_("Preferences")):

        vbox:
            xpos 150
            ypos -100

            hbox:
                box_wrap True
                spacing 27

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "check"
                        label _("skip unseen text?")
                        textbutton _("no") action Preference("skip", "seen") hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"
                        textbutton _("yeah") action Preference("skip", "all") hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"

                    vbox:
                        style_prefix "check"
                        label _("confirm saving/loading?")
                        textbutton _("yeah") action SetField(persistent, "confirm_saveload", True) hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"
                        textbutton _("n o") action SetField(persistent, "confirm_saveload", False) hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"

                    vbox:
                        style_prefix "radio"
                        label _("display type?")
                        textbutton _("window") action Preference("display", "window") hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"
                        textbutton _("fullscreen") action Preference("display", "fullscreen") hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"

            null height (0.1 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                spacing 27
                box_wrap True

                vbox:

                    if config.has_music:
                        label _("music volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("sound volume")

                        hbox:
                            bar value Preference("sound volume")

                            # if config.sample_sound:
                            #     textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("voice volume")

                        hbox:
                            bar value Preference("voice volume")

                            # if config.sample_voice:
                            #     textbutton _("Test") action Play("voice", config.sample_voice)

                    label _("blip volume")

                    hbox:
                        bar value Preference("blip volume")

                        # if config.sample_blip:
                        #     textbutton _("Test") action Play("blip", config.sample_blip)

                vbox:
                    style_prefix "radio"
                    label _("text speed")
                    textbutton _("chill :)") action Preference("text speed", 20) hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"
                    textbutton _("default steve") action Preference("text speed", 40) hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"
                    textbutton _("SPEEEEEED") action Preference("text speed", 60) hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"

                    text ("") size 23

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("mute all"):
                            action Preference("all mute", "toggle")
                            hover_sound "audio/ui/menu_hover.ogg"
                            activate_sound "audio/ui/settings_menu_activate.ogg"
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


################################################################################
## Ep select screen or episode select screen
## For selecting the episodes I mean the title is self explanitory
## I MADE THIS SCREEN MYSELF OKAY I'M SO SMART
###

init:
    transform select_options:
        zoom 0.35

init python:
    import os
    import random
    from threading import Timer

    def show_ep_desc(i):
        if i == 0:
            l_name = "start"
        else:
            l_name = "ep_" + str(i+1)
        renpy.run(Show("ep_desc", None, ep_titles[i], ep_descs[i], ep_thumbs[i], l_name)) # thumb_file.name

    def exit_ep_sel():
        renpy.run(Hide("ep_desc"))
        renpy.run(Return())

    def load_start(what):
        character = random.randint(0, 4)
        character_tips = tips[character]
        if character == 0:
            tip_font = "gui/fonts/calibri/Calibri Regular.ttf"
        else:
            tip_font = "gui/fonts/Rouli.ttf"
        renpy.run(Hide("ep_desc"))
        renpy.run(Show(
            "loading_screen",
            None,
            what,
            load_imgs[character],
            character_tips[random.randint(0, len(character_tips) - 1)],
            tip_font,
            tip_colors[character]
        ))
        #renpy.run(Start(l))

screen ep_select():

    tag menu

    add "gui/ep select/ep_select_bg.png"

    side ("c b"):
        area (25,400,1230,300)
        viewport id "ep_list":
            draggable True
            hbox:
                spacing 10

                for i in range(persistent.episode_fin+1):
                    imagebutton auto "gui/ep select/ep buttons/" + str(i+1) + "_%s.PNG":
                        hover_sound "audio/ui/menu_hover.ogg"
                        activate_sound "audio/ui/menu_activate.ogg"

                        action Function(show_ep_desc, i)
                        at select_options

        bar value XScrollValue("ep_list")

    imagebutton auto "gui/x_%s.png":
        xpos 17
        ypos 17
        hover_sound "audio/ui/menu_hover.ogg"
        activate_sound "audio/ui/menu_activate.ogg"

        action Function(exit_ep_sel)

screen ep_desc(title, desc, thumb, l):
    vbox:
        xpos 600
        ypos 35
        spacing 5

        text title font "gui/fonts/BigJohnPRO-Bold.otf" xsize 630 size 40
        text desc font "gui/fonts/Rouli.ttf" xsize 650 size 30
    add thumb xpos 100 ypos 40 zoom 0.35
    imagebutton auto "gui/main menu/start_%s.png":
        action Function(load_start, Start(l))
        xpos 100
        ypos 300
        hover_sound "audio/ui/menu_hover.ogg"
        activate_sound "audio/ui/epstart_menu_activate.ogg"


################################################################################
## Loading screen
###

init python:
    def renpy_music_stop_action():
        renpy.music.stop(channel="music", fadeout=None)


#TODO: LOADING NOISE

screen loading_screen(what, img, tip, tip_font, tip_color):
    on 'show' action SetMute('music/asd.mp3', True)

    python:
        renpy.music.stop(channel="blip", fadeout=None)
        renpy.music.stop(channel="sound", fadeout=None)
        renpy.music.stop(channel="voice", fadeout=None)

    $ renpy.music.play("audio/ui/loading.ogg", channel="music", loop=True)

    key "ctrl_shift_K_q" action renpy.quit

    zorder 300
    modal True

    tag menu

    add img

    add "gui/loading/loading_icon.png" at loading_anim xpos 1070 ypos 520

    $ randomterribleload = renpy.random.randint(1,100)

    if randomterribleload == 88:
        timer 30.0 action what, Function(renpy_music_stop_action)
        text "Did you know that the game has a 1 in 100 chance of the game taking 30 seconds to load!" font tip_font xalign 0.5 ypos 400 text_align 0.5 xsize 1000 size 40 color tip_color
    else:
        $ randomtime = renpy.random.random() + 3.0
        timer randomtime action what, Function(renpy_music_stop_action)

        text tip font tip_font xalign 0.5 ypos 400 text_align 0.5 xsize 1000 size 40 color tip_color

################################################################################
## MM Settings screen
###

init python:
    def heat_death_action():
        deletefiles()
        persistent._clear(progress=True)
        renpy.quit()

    def heat_death():
        yes_five = Show("confirm", transition=None, message="Last one. You sure?", yes_action = Function(heat_death_action), no_action=Hide("confirm"))
        yes_four = Show("confirm", transition=None, message="LOL I'M GONNA REVERSE YES AND NO. CLICK YES TO NOT PROCEED.", yes_action=Hide("confirm"), no_action=yes_five)
        yes_three = Show("confirm", transition=None, message="YOU WILL COMPLETELY DESTROY ALL TIMELINES!", yes_action=yes_four, no_action=Hide("confirm"))
        yes_two = Show("confirm", transition=None, message="REALLY??? ALL YOUR SAVES, YOUR FRIENDS, YOUR THINGS???", yes_action=yes_three, no_action=Hide("confirm"))
        yes_one = Show("confirm", transition=None, message="ARE YOU SURE MAN???", yes_action=yes_two, no_action=Hide("confirm"))


        renpy.run(Show("confirm", transition=None, message="DELETE ALL DATA FOREVER???", yes_action=yes_one, no_action=Hide("confirm")))


screen mm_preferences():

    tag menu

    frame:
        style "mm_preferences_bg"

        vbox:
            xpos 100
            ypos 15

            hbox:
                box_wrap True
                spacing 27

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "check"
                        label _("skip unseen text?")
                        textbutton _("no") action Preference("skip", "seen") hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"
                        textbutton _("yeah") action Preference("skip", "all") hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"

                    vbox:
                        style_prefix "check"
                        label _("confirm saving/loading?")
                        textbutton _("yeah") action SetField(persistent, "confirm_saveload", True) hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"
                        textbutton _("n o") action SetField(persistent, "confirm_saveload", False) hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"

                    vbox:
                        style_prefix "radio"
                        label _("display type?")
                        textbutton _("window") action Preference("display", "window") hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"
                        textbutton _("fullscreen") action Preference("display", "fullscreen") hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"

                    vbox:
                        style_prefix "check"
                        label _("tato heat death")
                        textbutton _(":(") action Function(heat_death) hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"

            null height (0.1 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                spacing 24
                box_wrap True

                vbox:

                    if config.has_music:
                        label _("music volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("sound volume")

                        hbox:
                            bar value Preference("sound volume")

                            # if config.sample_sound:
                            #     textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("voice volume")

                        hbox:
                            bar value Preference("voice volume")

                            # #if config.sample_voice:
                            #     textbutton _("Test") action Play("voice", config.sample_voice)

                    label _("blip volume")

                    hbox:
                        bar value Preference("blip volume")

                        # if config.sample_blip:
                        #     textbutton _("Test") action Play("blip", config.sample_blip)


                vbox:
                    style_prefix "radio"
                    label _("text speed")
                    textbutton _("chill :)") action Preference("text speed", 20) hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"
                    textbutton _("default steve") action Preference("text speed", 40) hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"
                    textbutton _("SPEEEEEED") action Preference("text speed", 60) hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"

                    text ("") size 23

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("mute all"):
                            action Preference("all mute", "toggle")
                            hover_sound "audio/ui/menu_hover.ogg"
                            activate_sound "audio/ui/settings_menu_activate.ogg"
                            style "mute_all_button"


                vbox:
                    xpos 40
                    label _("window size")
                    text "(if in fullscreen, will switch to window mode)" size 23 color "#330066" font "gui/fonts/Rouli.ttf"

                    textbutton "bite sized" action Preference("display", 0.3) hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"
                    textbutton "640 x 360" action Preference("display", 0.5) hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"
                    textbutton "960 x 540" action Preference("display", 0.75) hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"
                    textbutton "1280 x 720" action Preference("display", 1.0) hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"
                    textbutton "1920 x 1080" action Preference("display", 1.5) hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/settings_menu_activate.ogg"



    imagebutton auto "gui/x_%s.png":
        xpos 17
        ypos 17
        hover_sound "audio/ui/menu_hover.ogg"
        activate_sound "audio/ui/menu_activate.ogg"

        action Return()

style mm_preferences_bg:
    background "gui/main menu/settings_bg.png"


################################################################################
## Continue screen
## Where you load or KILL save files

screen continue():
    tag menu

    default page_name_value = FilePageNameInputValue(pattern=_("page {}"))

    frame:

        style "continue_bg"

        ## The page name, which can be edited by clicking on a button.
        vbox:
            input:
                xpos 605
                ypos 80

                style "page_label_text"
                value page_name_value
            fixed:
                xpos 512
                ypos 550

                text "click on the file to play!" size 25 color "#330066" font "gui/fonts/jsbdoublejointed.ttf"


        ## The grid of file slots.
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xpos 310
            ypos 150

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    if FileLoadable(1, page_name_value.get_page()):
                        action Function(load_start, FileLoad(slot))
                        hover_sound "audio/ui/menu_hover.ogg"
                        activate_sound "audio/ui/epstart_menu_activate.ogg"

                    has vbox

                    add FileScreenshot(slot)

                    text FileTime(slot, format=_(""), empty=_("empty slot")):
                        style "slot_time_text"

                    text FileSaveName(slot):
                        style "slot_name_text"


        ## Buttons to access other pages.
        hbox:
            style_prefix "page"

            xpos 270
            ypos 340

            spacing gui.page_spacing

            textbutton _("<"):
                action FilePagePrevious(max=6, wrap=True, auto=False, quick=False)
                hover_sound "audio/ui/menu_hover.ogg"
                activate_sound "audio/ui/menu_activate.ogg"

            textbutton _(">"):
                action FilePageNext(max=6, wrap=True, auto=False, quick=False)
                hover_sound "audio/ui/menu_hover.ogg"
                activate_sound "audio/ui/menu_activate.ogg"


    imagebutton auto "gui/x_%s.png":
        xpos 17
        ypos 17
        hover_sound "audio/ui/menu_hover.ogg"
        activate_sound "audio/ui/menu_activate.ogg"

        action Return()

style continue_bg:
    background "gui/main menu/continue_bg.png"



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

init python:
    def replace_yes_action(yes_action_baby, message):
        print(message)
        if "main menu" in message:
            load_start(MainMenu(False))
        else:
            renpy.run(yes_action_baby)

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            # if message :
            #     hbox:
            #         xalign 0.5
            #         spacing 100
            #
            #         textbutton _("yes") action Function(load_start, MainMenu(False))
            #         textbutton _("nah") action no_action
            #
            # else:
            hbox:
                xalign 0.5
                spacing 100

                textbutton _("yes") hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/menu_activate.ogg" action Function(replace_yes_action, yes_action, message)
                textbutton _("nah") hover_sound "audio/ui/menu_hover.ogg" activate_sound "audio/ui/menu_activate.ogg" action no_action


    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")
