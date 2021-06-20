label ep_3:

    $ persistent.mainmenu_img = 3
    $ persistent.saveepisode_img = 3

    stop music fadeout 1.0


    image chef 3 breakdown 2 to 3:
      "images/side chars/chef/2/chef 3 breakdown 2.png"
      0.1
      "images/side chars/chef/2/chef 3 breakdown 3.png"
      0.1
      repeat


    ph "so, what'dya need me for again?"

    show bg beegcity

    show ph o at Position(xpos=450)

    show rt happy at Position(xpos=850)

    play music "audio/music/da beeg city/da beeg city pdefault.mp3" loop

    space ""

    ph "and can we hurry this up?"

    show ph bruh 3 at bounce

    ph "i have a busy day today."

    ph "i'm gonna do a bunch of {w=0.3}nonexsiting."

    show rt joy 2 at bounce

    rt "Actually, I just wanted you to get outside of your lil' swamp for a bit."

    show ph bruh

    ph "you mud puddle."

    ph "i should've known."

    ph ""

    show ph o

    ph "so where are we going?"

    show ph o 2

    show rt o

    rt "Oh.."

    rt "I don't know."

    ph "..."

    rt "..."

    show ph o 3

    ph "hey i'm hungry wanna get cookie dough?"

    show rt happy 2 at shake(rate=0.01,strength=1,loop=3)

    rt "OOOooooooooh! Heck yeah!"

    stop music

    show bg cookiedoughshop

    hide rt

    hide ph

    space ""

    play sound "audio/fx/shopdoor.ogg"

    show rt happy at Position(xpos=500) with easeinleft

    show ph happy at Position(xpos=200) with easeinleft

    space ""

    show chef joy at right, flip with easeinright

    chef "Hello!!"

    show p she he at Position(xpos=950, ypos=270) with dissolve

    chef "What can I get for you today, {w=0.3}Rocktato and that frog looking kid?"

    hide p she he with dissolve

    chef "Just the usual?"

    chef "Two tubs of the good ol' regular flavored cookie dough?"

    show rt joy 2 at bounce

    rt "Make it three please!"

    chef "Alrighty!"

    no "She pulls three tubs of cookie dough out of her pockets and sets them on the counter."

    chef "Here you go! {w=0.3}That'll be 30 monies."

    show rt happy at bounce

    rt "Oh just put it on my tab."

    show chef neutral

    chef "Okay..."

    show chef uncomfortable

    chef "Rocktato, {w=0.3}I've been meaning to ask..."

    chef "When do you intend on paying all this back?"

    chef "You owe us at least...{w=0.3}{nw}"

    show chef what

    extend " 1 MILLION MONIES???!!!"

    rt "Wait what."

    show rt cry

    rt "ONE MILLION???"

    rt "I CAN'T EVEN COUNT THAT HIGH!!"

    rt "MY RECORD IS LIKE,{w=0.3} TEN."

    show chef polite

    chef "Nah, {w=0.3}I'm just messing with you."

    show rt mad

    show chef joy at bounce

    chef "One million? {w=0.3}That's unrealistic."

    chef "Haha.. {w=0.3}I'm such a prankster!"

    chef "You only owe us 30k."

    chef ""

    show chef neutral

    chef "That's still a lot, though."

    chef ""

    chef "You..."

    show chef polite

    chef "You intend on paying all this back, right?"

    show rt confused

    rt "I thought it was free."

    show ph bruh

    ph "you idiot."

    show rt at shake(rate=0.01,strength=3,loop=7)

    rt "Isn't that what a tab is??"

    show chef uncomfortable

    chef "Seriously, {w=0.3}I'm going to need that money.."

    chef "The student debt has been pretty real lately.."

    show rt nervous at bounce

    rt "Aha..."

    rt "Well the thing is... {w=0.3}I don't have money."

    show rt happy 2 at bounce

    rt "I'm a child!"

    chef "Uh... {w=0.3}don't you have parents or a guardian or something?"

    show rt confused

    rt "Hmm..."

    rt "Nope lol!"

    # rt "Well, {w=0.3}there's Blairic?? {w=0.3}He basically treats me like his kid, but he tells me to never refer to him as a parental figure in public."
    #
    # rt "I think because he doesn't wanna be seen as a softie."
    #
    # show rt smug at bounce
    #
    # rt "Well, I know his secret. {w=0.3}He may seem tough and cold and 'legal', but he's the nicest!"

    show rt o at bounce

    rt "Anyway, {w=0.3}I'll be taking this, thanks!"

    show rt joy 2 at bounce

    rt "See you tomorrow!"

    show chef bruh 2

    chef "Rocktato, {w=0.3}I mean it."

    show rt happy

    chef "If you don't pay it back by the end of day, {w=0.3}you're banned."

    show ph o

    chef "Not just from this store, {w=0.3}from buying cookie dough "

    extend "forever."

    play sound "audio/fx/suspense.ogg"

    $ renpy.pause(5.0, hard=True)

    show chef joy

    chef "I'm part of the city-wide cookie dough leauge!"

    chef "Anger one of us and you're done for. {w=0.5}Cookie dough-wise."

    chef "Maybe a day is a bit cruel, {w=0.3}but it's sure to make some funny shenanigans..."

    chef "Man, {w=0.3}I'm real good at being threatening!"

    chef "Ma would be so proud."

    rt "Cool, bye!"

    show chef angry

    chef "Oh c'mon... {w=0.3}Wait!!{w=0.1}{nw}"


    show ph at Position(xpos=450)

    show rt at Position(xpos=850)

    play amb "audio/amb/city.ogg" loop

    play sound "audio/fx/woosh.ogg"

    queue sound "audio/fx/eat.ogg"

    show bg beegcity

    hide chef

    rt "MmmPhh… {w=0.3}I don’t know how, {w=0.3}but they just keep tasting better and better!"

    show ph bruh

    ph "do you even {i}intend{/i} on paying him back?"

    show rt nervous

    rt "Uh... {w=0.5}y{w=0.1}e{w=0.1}e{w=0.1}e{w=0.1}e{w=0.1}e{w=0.1}s{w=0.1}.{w=1.5}.{w=1.5}.{w=5.0}."

    ph "seriously, {w=0.3}you gotta pay him back."

    rt "Yeah.... {w=0.3}I know, {w=0.3}I know."

    ph "you heard 'em, {w=0.3}you're gonna b banned."

    show rt happy 2

    rt "I wouldn't worry about it, {w=0.3}I'm cute!"

    rt "Look, {w=0.3}I'll even walk back in to prove it!"

    play sound "audio/fx/stepping.ogg"

    hide rt with easeoutleft

    space ""

    play sound "audio/fx/stepping.ogg"

    show rt nervous at Position(xpos=850) with easeinleft

    rt "Okay so, {w=0.3}the moment I walked up to the store, {w=0.3}it disintegrated."

    show ph o

    ph "what."

    show rt troubled at bounce

    rt "Oh jeez..."

    show rt cry 2 at shake(rate=0.01,strength=3,loop=5)

    rt "OH JEEz..."

    rt "You're right, {w=0.3}I'M GONNA BE BANNED!"

    show ph bruh 2

    ph "bro dw about it, {w=0.3}we can just ask blairic for money."

    ph "he's loaded, {w=0.3}i'm sure."

    show rt happy 2

    rt "Oh, right! {w=0.3}Blairic!"


    show bg bloffice

    show ph bruh at Position(xpos=250)

    show rt at Position(xpos=550)

    show bl bruh 2 at flip, Position(xpos=1050)

    stop amb

    play sound "audio/fx/woosh.ogg"

    bl "No."

    play sound "audio/fx/punch.ogg"

    show rt cry 2 with hpunch

    rt "What??"

    show bl uncomfortable at flip

    bl "How the hell does one spend twenty-five thousand on cookie dough!?"

    bl "How?"

    show ph bruh 2

    ph "to b fair, {w=0.3}they had the tab open for like, {w=0.3}four years?"

    ph "the fact that he got away without paying for so long is more impressive, tbh."

    bl "Okay, {w=0.3}I am sorry Rocktato but I am not paying this."

    show rt at shake(rate=0.01,strength=5,loop=5)

    rt "Why not???"

    bl "Believe it or not, {w=0.3}I'm not as rich as you think I am."

    show ph o

    ph "wait srs?"

    ph "what's your net worth."

    bl "I'm not-{w=0.8}{nw}"

    show ph bruh 2

    ph "wow, {w=0.3}thought so."

    show ph smug 2

    ph "he's lying, rocktato."

    show bl bruh 2 at flip

    bl "Put a sock in it, Phrog."

    bl "Okay, {w=0.3}fine."

    bl "I shall pay for-{w=0.2}{nw}"

    show rt joy 2 at shake(rate=0.01,strength=20,loop=6)

    rt "YEAHHHHH!!!"

    bl "99.9999\% of it."

    bl "You have to pay about three cents."

    show rt cry

    rt "WHAAAT??"

    show rt cry 2

    rt "THAT'S SO MUCH MONEYYYYY THo..."

    show ph bruh 2

    ph "well, {w=0.3}ya gotta learn."

    ph "nothin's free in life, kid."

    show bl happy 3 at flip, bounce

    bl "Good luck!"

    bl "I shall attend to my job now."

    hide bl with easeoutright

    space ""


    show bg beegcity

    show ph bruh at Position(xpos=450)

    show rt at Position(xpos=850)

    play amb "audio/amb/city.ogg" loop

    play sound "audio/fx/woosh.ogg"

    space ""

    rt "How are we going to get all that money???"

    ph "it's quite simple."

    show rt cry at bounce

    rt "What?"

    show ph happy at bounce

    ph "rob a bank!"

    space ""

    show rt bruh

    space ""

    rt "I'm not going to rob a bank, Phrog."

    rt "At least not today."

    show rt happy at bounce

    rt "Maybe tomorrow!"

    show rt o

    rt "Okay, ideas..."

    rt "We could bake cookies, {w=0.3}mow lawns, {w=0.3}babysit, {w=0.3}lemonade stand, {w=0.3}shovel snow out of driveways..."

    show ph bruh

    ph "we don't have snow in beeg city."

    show rt cry

    rt "I can dream..."

    show ph o 3

    ph "alright."

    show ph bruh 2

    ph "all those options sound boring."

    ph "bake cookies?? {w=0.3}where do you expect to get the dough?"

    show rt joy 2 at bounce

    rt "From the {w=0.2}{nw}"

    show rt sad 2

    extend "oh."

    show ph joy 2 at bounce

    ph "okay, {w=0.3}i have a good idea."

    show rt confused at bounce

    rt "Huh?"

    ph "follow me."


    show bg swamp

    play sound "audio/amb/swamp.ogg"

    play sound "audio/fx/woosh.ogg"

    ph "k cool."

    play sound "audio/fx/drop.ogg"

    hide ph with easeoutbottom

    ph "z{w=0.5}z{w=0.5}z{w=0.5}z{w=0.5}.{w=0.5}.{w=0.5}."

    rt ""

    play sound "audio/fx/punch.ogg"

    show rt mad with hpunch

    rt ""

    rt "PHR0G!!!"

    rt "What the heck!!"

    ph "i'm {w=0.5}ggog {w=0.5}goggggna {w=0.5}tak{w=0.5}e {w=0.5}nap..."

    rt "Phroooooooggg..."

    play sound "audio/fx/pickup.ogg"

    show ph bruh at Position(xpos=450) with easeinbottom

    ph "alright, {w=0.3}alright, {w=0.5}fine."

    play sound "audio/fx/search.ogg"

    show ph at shake(rate=0.005,strength=0.5,loop=20)

    no "Phrog ruffles through her refridgerator/microwave."

    no "It was a combo appliance!"

    no "Now on sale at your local dealership!"

    ph "Nope."

    ph "Don't do that."

    rt "What?{w=0.2}{nw}"

    no "Okay, {w=0.3}jeez."

    play sound "audio/fx/pickup.ogg"

    no "Phrog dug out a tub of cookie dough."

    show ph smug 2 at bounce

    ph "tada!"

    show rt o

    rt "Woah!!"

    show rt happy 2 at shake(rate=0.005,strength=3,loop=3)

    rt "You're totally right!"

    rt "I can just get you or someone else to buy the cookie dough for me!"

    rt "Now Blairic and I won't need to pay anymore!"

    rt "You're so smart Phrog!"

    ph "ikr."

    ph "dunno why i didn't think of it earlier."

    show ph joy 2 at bounce

    ph "now let's dig in!"

    no "She opened the tub but..."

    play sound "audio/fx/suspense.ogg"

    no "A giant gun came out of the side of the tub."

    show ph o

    ph "what."

    stop amb

    show rt disturbed

    Character("Tub", size=25, callback=no_blip) "UNAUTHORIZED CONSUMER DETECTED."

    Character("Tub", size=25, callback=no_blip) "DEPLOYING LASERS."


    show bg at fast_shaking

    show rt at fast_shaking

    show ph at fast_shaking

    play amb "audio/amb/earthquake.ogg" loop

    play sound "audio/fx/lasers.ogg"

    Character("Tub", size=25, callback=no_blip) "*BZZZZZZZTTTTTTTT*"

    no "It starts firing towards Rocktato."

    show rt hurt

    show ph scared

    play sound "audio/fx/drop.ogg"

    no "Phrog dropped the tub on the ground and hid under a pillow."

    rt "WAAAAAAAAHHHH."

    play sound "audio/fx/stepping.ogg"

    hide rt with easeoutleft

    no "Rocktato runs out of the house to hide."

    show ph scared 2

    ph "WHAT? {w=0.3}DON'T LEAVE ME IN HERE ALONE WITH THIS THING."

    show bg at none

    show ph o at none

    stop amb

    stop sound

    Character("Tub", size=25, callback=no_blip) "No unfunnies detected!"

    Character("Tub", size=25, callback=no_blip) "Thanks! {w=0.3}And have a great day!"

    ph ""

    show rt disturbed at transform_easein_pos(xstart=-500, xend=850, tom=5.0)

    space ""

    rt ""

    ph ""

    rt "Well..."

    rt "That isn't gonna work, {w=0.3}huh?"

    show ph joy 2 at bounce

    ph "yep!"

    show rt uncomfortable at Position(xpos=850)

    rt "Mm."

    rt ""

    show rt joy 2 at bounce

    rt "Wow!"

    rt "I almost died!"

    show ph at bounce

    ph "yep!"

    show ph think

    ph "i just realized something."

    show rt confused

    rt "Yeah?"

    show ph smug

    ph "y'kno, {w=0.3}the chef could get in a lotta trouble for this."

    rt "Whatd'ya mean?"

    ph "mayb we can sue her for child endagerment? {w=0.3}or somethin' stupid like that."

    ph "then all the paying back fees will HAVE to cover the cookie dough."

    show ph joy 2 at bounce

    ph "that's probably how it works!"

    ph "man, i'm so smart."

    rt "Well, {w=0.3}how do you lawsuit someone?"

    show ph o 3

    ph "mm let me search up how to file a lawsuit."

    play sound "audio/fx/typing.ogg"

    show ph think at shake(rate=0.005,strength=0.5,loop=20)

    no "Phrog does the stuff on her Phrog phone."

    no "..."

    show ph o

    ph "okay.."

    show rt happy 2

    rt "Yeah?"

    show ph happy

    ph "i don't understand what any of this means!"

    rt "."

    show rt o

    rt "Hey, why don't we ask Blairic??"

    rt "He does company things, {w=0.3}right?"

    ph "o yea totally!"

    play sound "audio/fx/woosh.ogg"

    show bg bloffice

    show ph at Position(xpos=250)

    show rt happy at Position(xpos=550)

    show bl bruh at flip, Position(xpos=1050)

    bl "..."

    rt "..."

    ph "..."

    rt "Well?"

    bl "I think you know the answer, Rocktato."

    show rt joy 2 at bounce

    rt "PHROG!!! {w=0.3}LET'S GOOOOOOO!!!!"

    bl "No."

    show rt sad 2

    rt "Aw.."

    show bl happy at flip

    bl "Anyway, {w=0.3}how is the raising money thing going?"

    show bl takemeouttodinnerfirst

    bl "You did not rob a bank, correct?"

    rt "No! {w=0.3}But we considered it!"

    show bl uncomfortable

    bl ""

    bl "I was joking."

    show ph think

    ph "actually... {w=0.3}that does give me another brilliant idea."

    show rt bruh

    rt "Because all of your ideas so far have been brilliant.."

    show ph o

    ph "..."

    show ph bruh 3

    ph "wha- {w=0.3}ok. {w=0.5}jeez.."

    ph "let's get outta here before i tell ya."

    ph "bye b."

    show bl o

    bl "Oh, okay."


    play sound "audio/fx/woosh.ogg"

    play amb "audio/amb/city.ogg" loop

    show bg beegcity

    show ph at Position(xpos=450)

    show rt at Position(xpos=850)

    hide bl

    space ""

    rt "Okay, {w=0.3}what is it?"

    show ph o 3

    ph "you might not like this one. {w=0.3}it's very not legal."

    rt "Oh... {w=0.3}yeah..."

    show rt happy 2 at bounce

    rt "Whatever, {w=0.3}I can take it!"

    rt "It's for a good cause!"

    show ph bruh 3

    ph "yeah.. {w=0.3}totally.."

    show ph o 3

    ph "anyway, {w=0.3}you said no robbing banks today... {w=0.3}but..."

    ph "why don't we rob the cookie dough secret formula?"

    rt "."

    show rt confused

    rt "That's... "

    show rt happy

    extend "not that bad of an idea!"

    show ph bruh

    ph "i was hoping you wouldn't say that."

    show ph think

    ph "wait, yeah... {w=0.3}why AM i helping you?"

    rt "Because you're my friiieeennnnddd?"

    show ph bruh

    ph "shut up."

    ph "well... {w=0.7}it's too late for me now."

    show ph o 2

    ph "you sure you wanna do the robbing the robbing thing?"

    rt ""

    rt "Phrog, that wasn't a sentence!"

    show rt joy 2 at bounce

    rt "But heck yea! {w=0.3}Let's do it!"

    show rt confused

    rt "How are we gonna do it?"

    show ph smug

    ph "easy."

    ph ""


    play sound "audio/fx/woosh.ogg"

    show bg beegcity night

    show ph bruh 3

    space ""

    rt ""

    rt "Well?"

    show ph o 2

    ph "?"

    show rt bruh

    rt ""

    rt "Phrog, {w=0.3}I asked how we were going to rob the thing, {w=0.3}then you said 'easy,' {w=0.3}and then we just... {w=0.5}sat here... {w=0.5}for a few hours..."

    show ph joy at bounce

    ph "oh yea!"

    ph "well what a coincidence that you asked that RIGHT NOW!"

    ph "because the shop is closing!"

    ph "and we're gonna sneak in now!"

    show rt o

    rt "Okay, {w=0.3}but HOW will we sneak in?"

    show ph smug

    ph "easy."

    ph ""

    show rt bruh

    rt "Phrog, please."

    ph "lol, i'm kiddin'."

    show ph joy 2

    ph "we just improv and hope it works lol!"

    show ph o 3

    ph "if it doesn't, {w=0.3}we can just rollback by pressing BACKSPACE or the BACKWARDS ARROW at the top of the screen."

    show rt confused

    rt "What does that mean?"

    ph "again, {w=0.3}dw about it."

    ph "So, {w=0.3}Rocktato, {w=0.3}you chose! {w=0.5}How do you wanna enter?"

    stop amb

    $ choice_screen_type = "choice"

    # Oh my god I have to set ALL THE VARIABLES this is gonna SUCK
    # SNEAK SEGMENT BTW
    $ failed = False

    $ ep3_choice1_back = False
    $ ep3_choice1_walk = False
    $ ep3_choice1_roof = False

    $ ep3_choice2_disguise = False

    default persistent.ep3_choice2_bomb = False

    $ ep3_choice3_hack = False

    $ ep3_choice4_recipe = False
    $ ep3_choice4_storage = False
    $ ep3_choice4_restroom = False

    default persistentep3_mugbreaker = False

    $ fail_skip = False


    menu:
        "Back Door":
            $ ep3_choice1_back = True

            rt "Let's go through the back door!!"

            ph "smart."

            jump ep3_seg1_back


        "Just Walk in LOL" if persistent.episode_fin == 2:
            $ ep3_choice1_walk = True

            show rt smug 2

            rt "I'm tired of waiting. I'm just going in."

            rt "If anyone is in there, {w=0.3}they'll be so intimidated by our sheer audacity."

            show ph o

            play sound "audio/fx/stepping.ogg"

            hide rt with easeoutright

            ph "wait what-{w=0.1}{nw}"


            play sound "audio/fx/shopdoor.ogg"

            show bg cookiedoughshop

            show ph bruh at Position(xpos=200)

            show chef what at right, flip

            show rt smug 2 at Position(xpos=500) with easeinleft

            rt "Hey hey hey! {w=0.5}What's a poppin'?"

            rt "I'm definitely not coming here for any malicious intentions!"

            rt "Me?? {w=0.3}Mistrustful? {w=0.3}NEVER."

            rt "Don't mind me!!"

            chef "."

            jump ep3_seg_end


        "Enter Thru Roof":
            $ ep3_choice1_roof = True

            rt "Hey, let's get in from the roof. LIKE SPY."

            ph "i mean... {w=0.3}that could work."

            show rt confused

            rt "How do we get up there tho..."

            show ph smug

            ph "i got this."

            play sound "audio/fx/boing.ogg"

            show ph at bounce

            no "Phrog picked up Rocktato bridal style and they jumped to the top of the roof."

            show rt o at bounce

            rt "Woah! {w=0.3}Nice!"

            show rt joy

            rt "Y'know, {w=0.3}sometimes I forget you have those frog powers n' all."

            jump ep3_seg1_roof


    label ep3_seg1_back:
        show rt o at bounce

        show ph at bounce

        play sound "audio/fx/stepping.ogg"

        no "The two kids skiddered around the building to the back."

        no "There was indeed a back door; {w=0.5}however when Phrog pulled on the handle, {w=0.3}it wouldn't budge."

        show ph bruh

        ph "locked. {w=0.3}figures."

        rt "Don't worry! {w=0.3}We'll use a-"

        $ ep3_choice2_disguise = False

        $ fail_skip = False

        menu:
            "\"Disguise!\"":
                $ ep3_choice2_disguise = True

                show rt 3 trashcan 1

                play sound "audio/fx/pickup.ogg"

                space ""

                ph ""

                ph "y'kno what."

                show ph smug

                ph "just go for it. {w=0.3}i wanna see what happens."

                rt "No c'mon this is gonna be super smart, {w=0.3}watch."

                show rt 3 trashcan 2 at bounce

                play sound "audio/fx/doorbang.ogg"

                no "He knocks on the door."

                rt "EY EY. {w=0.3}It's the garbage man!!! {w=0.3}Here to eat your garbage!!!"

                show ph at Position(xpos=200)

                show rt at Position(xpos=500)

                with ease

                show chef bruh at right, flip with easeinright

                space ""

                chef "What the hell."

                $ fail_skip = True

                jump ep3_seg_end


            "\"Paperclip!\"":
                show rt smug at bounce

                no "He pulls out a paper clip."

                no "{image=images/imgs/2/txt 3 paperclip.png}"

                show rt at shake(rate=0.01,strength=2,loop=7)

                play sound "audio/fx/drill.ogg"

                no "He jams it into the keyhole."

                no ""

                no "He just... {w=0.3}leaves it in there."

                no ""

                rt ""

                rt "Yeah, {w=0.3}I don't know how to do this lol."

                ph ""

                play sound "audio/fx/punch.ogg"

                show cg 3 fail

                $ _skipping = False

                space "Rollback to pick a different choice! (Press/hold backspace.)"

                $ renpy.pause(hard=True)


            "\"Gun!\"":
                show ph shock

                ph "what-{w=0.2}{nw}"

                show ph scared 2

                play sound "audio/fx/gunshot.ogg"

                show rt proud with hpunch

                space ""

                ph "ROCKTATO WHAT TTHE HELL!!??"

                ph "WAH.."

                show ph at shake(rate=0.01,strength=5,loop=20)

                ph "WHERE DID YOU GET THAT??"

                show rt o at bounce

                rt "Oh look the door's open! {w=0.3}Let's goooo."

                show ph scared

                ph "a-"

                show rt joy

                rt "C'mon Phrog."

                jump ep3_seg2_sneak


    label ep3_seg1_roof:
        ph "yea me too."

        show ph o

        ph "remember when super powers were an important gimmick?"

        show ph joy 2

        ph "just kidding!"

        show ph tired 2

        ph "it never was..."

        show ph tired

        ph ""

        show ph o 2

        show rt confused

        rt "Well... {w=0.3}now that we're here... {w=0.3}how do we actually get in?"

        show ph bruh 2

        ph "the roof was your idea, dingus."

        show rt happy 2

        rt "I've got it! {w=0.3}Let's use..."

        menu:
            "\"A Laser Cutter\"":
                show ph bruh

                show rt smug 2 at shake(rate=0.01,strength=5,loop=5)

                rt "EeeheheeheeeyeaAAAAHH."

                play sound "audio/fx/lightslap.ogg"

                no "He slaps some wack lookin' device on the roof and it lasers a medium-size circular hole."

                play sound "audio/fx/laser.ogg"

                extend ""

                show ph o

                ph "woah."

                show ph at bounce

                ph "that worked!"

                show ph o 3

                ph "where... {w=0.3}did you get that?"

                show rt happy

                rt "My pocket!"

                ph "how..{w=0.3}{nw}"

                show rt proud at bounce

                rt "Now c'mon, {w=0.3}let's go!"

                show rt at transform_easeout_offset(y=1280)

                play sound "audio/fx/drop.ogg"

                ph "how are we getting- {w=0.4}{nw}"

                ph "oh he already jumped down."

                show ph bruh 2

                ph "welp."

                hide ph with easeoutbottom

                play sound "audio/fx/drop.ogg"

                hide rt

                space ""

                jump ep3_seg2_office

            "\"A Heckin' Saw\"":
                play sound "audio/fx/saw.ogg" loop

                show rt at shake(rate=0.05,strength=1,loop="")

                show ph bruh

                no "He pulls a fricken' saw out of his pocket and starts scrapping away on the roof."

                no ""

                ph ""

                rt ""

                rt "This..."

                show rt nervous

                rt "uh..."

                rt "this is taking longer than I thought it would..."

                rt ""

                play sound "audio/fx/punch.ogg"

                show rt sad at shake(rate=1.00,strength=0,loop=1) with hpunch

                no "The saw snaps in half."

                rt "o"

                show cg 3 fail

                $ _skipping = False

                space "Rollback to pick a different choice! (Press/hold backspace.)"

                $ renpy.pause(hard=True)


            "\"A Plant!\"":
                show rt joy at shake(rate=0.01,strength=10,loop=1)

                show ph bruh

                play sound "audio/fx/drop.ogg"

                show obj 3 plant at center

                no "He aggressively pulls a medium-sized potted plant out of his pocket and sets it on the roof."

                rt ""

                rt "Eee hee hee I love plants."

                show cg 3 fail

                $ _skipping = False

                space "Rollback to pick a different choice! (Press/hold backspace.)"

                $ renpy.pause(hard=True)




    label ep3_seg2_sneak:
        no "The two entered the door and found themselves in the kitchen."

        show ph o 2

        ph ""

        play sound "audio/fx/sniff.ogg"

        ph "holy cannoli it smells delicious in here."

        show rt o

        rt "Woah, {w=0.3}yeah-{w=0.3}{nw}"

        ph "psst get down."

        show ph at transform_easeout_offset(y=1280)

        show rt at transform_easeout_offset(y=1280)

        no "They ducked behind the counters and what nots."

        chef "What was that noise?"

        play sound "audio/fx/stepping.ogg"

        show chef neutral at right, flip with easeinright

        chef ""

        show chef think

        chef "Eh, {w=0.3}whatever."

        play sound "audio/fx/stepping.ogg"

        hide chef with easeoutright

        no "She leaves."

        ph ""

        show rt smug at transform_easein_offset(y=120)

        play sound "audio/fx/slidewhistleup.ogg"

        rt "Lol that worked?"

        show rt nervous

        chef "Actually..."

        play sound "audio/fx/stepping.ogg"

        show rt at transform_easeout_offset(y=1280)

        show chef joy at right, flip with easeinright

        chef "I have a little bit of time. {w=0.3}Might as well make myself a snack before I head home!"

        show chef happy

        chef "Which is here."

        chef "I live here!"

        hide rt

        hide ph

        show chef joy at bounce

        chef "Fun fact!"

        show ph bruh at Position(xpos=200,ypos=810)

        show rt sad at Position(xpos=500, ypos=810)

        with easeinbottom

        ph "ah crud..."

        ph "rocktato, {w=0.3}we need to do some sort of sneak segment to get past her."

        show rt confused

        rt "What?"

        show ph o

        ph "ikr. {w=0.3}a sneak seg in a visual novel... {w=0.3}outstanding..."

        ph "okay, {w=0.3}it's simple."

        ph "when the option comes up, select the one that says 'Sneak.'"

        show ph o 3

        ph "but you gotta be quick!"

        ph "if you don't do it in time or you select the wrong one, you'll get caught!"

        ph "but if you don't have the reflexes for this one, {w=0.3}that's okay!"

        ph "do you wanna {b}skip{/b} this segment?"

        menu:
            "Yes":
                show ph joy at bounce

                ph "cool!"

                ph "i'll teleport you to the future in three... {w=1.0}two... {w=1.0}one...{nw}"

                jump ep3_seg2_aftersneak

            "No":
                show ph smug

                ph "ok then. {w=0.3}you're a gamer, {w=0.1}i see."

                rt "What."

                ph "oh! {w=0.3}you should save btw just in case you fail."

                ph "you WON'T be able to rollback."

                ph ""

                ph "you ready?"

                ph "alright, {w=0.3}let's a goooooooooooooo."

                ph "that's what those gamers always say."


        $ config.rollback_enabled = False

        $ _skipping = False

        $ timed_choices = True

        $ choice_screen_shuffle = True

        $ saveable = False


        show fx getready at truecenter, shake(rate=0.05,strength=1,loop=2) with dissolve

        $ renpy.pause(1.0, hard=True)

        hide fx getready with dissolve


        play amb "audio/fx/2/ilovemicrowaves.ogg"

        show ph o 2

        show rt happy

        space "{nw}"

        $ renpy.pause(1.0, hard=True)

        show chef happy at bounce

        $ renpy.pause(2.75, hard=True)

        show chef at bounce

        $ renpy.pause(2.5, hard=True)

        show chef at shake(rate=0.01, strength=3, loop=2)

        $ renpy.pause(2.5, hard=True)

        show chef at shake(rate=0.005, strength=1, loop=1)

        $ renpy.pause(1.0, hard=True)

        show chef at shake(rate=0.005, strength=1, loop=1)

        $ renpy.pause(1.75, hard=True)

        show chef bruh



        show chef at shake(rate=0.005, strength=1, loop=1)

        $ renpy.pause(0.5, hard=True)

        show chef at shake(rate=0.005, strength=1, loop=1)

        $ renpy.pause(1.0, hard=True)

        show chef at shake(rate=0.005, strength=1, loop=1)

        $ renpy.pause(2.5, hard=True)

        show chef happy at reverse_flip


        $ timeout_label = "ep3_seg2_kitchen_sneak_fail_nothing"

        $ timeout = 2.0

        menu:
            "Sneak":
                show rt happy at bounce

                play sound "audio/fx/sparkle.ogg"

                jump ep3_seg2_kitchen_sneak_2


            "Run Obnoxiously Fast":
                stop amb

                $ saveable = True

                $ timed_choices = False

                $ config.rollback_enabled = True

                $ renpy.block_rollback()

                $ _skipping = True

                $ choice_screen_shuffle = True

                play sound "audio/fx/stepping.ogg"

                rt "AAAAAAAAA LOOK AT ME I'M SO FAST AND I'M RUNNIN'!!!"

                show rt joy at shake(rate=0.01,strength=5,loop=5), Position(xpos=1480) with ease

                show chef bruh at flip

                show ph bruh 3

                ph ""

                ph "See, sometimes it feels like you're not even trying."

                show ph bruh

                ph "I am talking about you."

                $ fail_skip = True

                jump ep3_seg_end


            "Tackle the Chef":
                stop amb

                $ saveable = True

                $ timed_choices = False

                $ config.rollback_enabled = True

                $ renpy.block_rollback()

                $ _skipping = True

                $ choice_screen_shuffle = True

                show ph o

                show rt mad at shake(rate=0.02,strength=200,loop="")

                rt "HYAHHHHHHHHHH"

                play sound "audio/fx/punch.ogg"

                play amb "audio/amb/earthquake.ogg" loop

                show chef o at falling_over, shake(rate=0.01,strength=4,loop=3)

                chef "WHAHAHHWA?"

                hide chef

                show rt mad

                rt "QUICK PHROG! {w=0.3}LET'S GET OUT OF HERE."

                rt ""

                rt "OH NO PHROG. {w=0.3}I'M STUCK."

                hide rt

                space "{nw}"

                show chef angry at flip, right, shake(rate=0.02, strength=3, loop=1)

                show rt o at Position(xpos=850, ypos=500)

                stop amb

                play sound "audio/fx/cough.ogg"

                no "The chef grabs Rocktato."

                rt ""

                chef ""

                $ fail_skip = True

                jump ep3_seg_end


        label ep3_seg2_kitchen_sneak_2:
            space "{nw}"

            show chef at flip

            $ renpy.pause(3.0, hard=True)

            show chef bruh

            $ renpy.pause(3.0, hard=True)

            show chef at reverse_flip

            menu:
                "Sneak":
                    show rt at bounce

                    play sound "audio/fx/sparkle.ogg"

                    jump ep3_seg2_kitchen_sneak_3


                "Have a Musical Number":
                    stop amb

                    $ saveable = True

                    $ timed_choices = False

                    $ config.rollback_enabled = True

                    $ renpy.block_rollback()

                    $ _skipping = True

                    $ choice_screen_shuffle = True

                    rt ""

                    show rt joy at Position(ypos=720) with ease

                    show ph bruh

                    rt "HEY LOOK OVER HERE!"

                    show chef what at flip

                    rt "*INHALE.*"

                    rt "{nw}"

                    rt "{nw}"

                    play sound "audio/fx/2/HISMUSICALNUMBER.ogg"

                    $ renpy.pause(7.5, hard=True)

                    show rt at flip, bounce

                    $ renpy.pause(3.8, hard=True)

                    show rt at reverse_flip, bounce

                    $ renpy.pause(4, hard=True)

                    show rt at flip, bounce

                    $ renpy.pause(3.8, hard=True)

                    show rt at reverse_flip, bounce

                    $ renpy.pause(3.2, hard=True)

                    show rt at shake(rate=0.01, strength=4, loop=3)

                    $ renpy.pause(0.6, hard=True)

                    show rt at shake(rate=0.005, strength=10, loop="")

                    $ renpy.pause(3.9, hard=True)

                    show rt at shake(rate=0.5, strength=10, loop="")

                    $ renpy.pause(0.7, hard=True)

                    hide rt

                    show rt sad at Position(xpos=500, ypos=720)

                    show ph angry at bounce

                    ph "NOPE. {w=0.3}I'M STOPPING THIS."

                    ph "(I hate musical numbers.)"

                    chef "Yeah, why did you do that?"

                    show rt o

                    rt "Oh you're there.."

                    $ fail_skip = True

                    jump ep3_seg_end


                "Cry":
                    stop amb

                    $ saveable = True

                    $ timed_choices = False

                    $ config.rollback_enabled = True

                    $ renpy.block_rollback()

                    $ _skipping = True

                    $ choice_screen_shuffle = True

                    show rt sad

                    rt "w-"

                    show rt cry 2 at bounce

                    show chef what at flip

                    rt "wwwaaAAaaaAAAHAHHHHHAHAHahHAH!!!!"

                    rt "AWHAHWAHWHAHWHAWAWHAWHAHWHAHAHAKBGFKbKBGKSFGBSBHGKSFGBskgHSGBLSGBSLGBSFLBB@"

                    rt "wAAAAww. {w=0.4}Wa {w=0.15}Wa- {w=0.15}WAAHAww.."

                    ph "wh- {w=0.5}{nw}"

                    show ph scared

                    ph "wHAT ARE YOU DOING?"

                    show rt happy

                    rt "Y'know, {w=0.3}I don't really know!"

                    $ fail_skip = True

                    jump ep3_seg_end


        label ep3_seg2_kitchen_sneak_3:
            space "{nw}"

            show chef at flip

            $ renpy.pause(5.0, hard=True)

            $ renpy.pause(5.0, hard=True)

            show chef at reverse_flip

            menu:
                "Sneak":
                    show rt at bounce

                    play sound "audio/fx/sparkle.ogg"

                    jump ep3_seg2_kitchen_sneak_4


                "Speak":
                    stop amb

                    $ saveable = True

                    $ timed_choices = False

                    $ config.rollback_enabled = True

                    $ renpy.block_rollback()

                    $ _skipping = True

                    $ choice_screen_shuffle = True

                    rt "Hey, {w=0.3}what's up?"

                    show chef what at flip

                    chef ""

                    $ fail_skip = True

                    jump ep3_seg_end


                "Shriek":
                    stop amb

                    $ saveable = True

                    $ timed_choices = False

                    $ config.rollback_enabled = True

                    $ renpy.block_rollback()

                    $ _skipping = True

                    $ choice_screen_shuffle = True

                    show rt hurt

                    show chef what at flip

                    rt "AAAAAAAAAAAAAAAaaaa"

                    show ph scared 2

                    ph "WAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHhh"

                    chef "a"

                    ph "WHY??"

                    chef ""

                    $ fail_skip = True

                    jump ep3_seg_end


                "Break":
                    stop amb

                    $ saveable = True

                    $ timed_choices = False

                    $ config.rollback_enabled = True

                    $ renpy.block_rollback()

                    $ _skipping = True

                    $ choice_screen_shuffle = True

                    show ph think

                    ph "hold on that doesn't rhyme with sneak."

                    ph "wait."

                    show rt at shake(rate=0.01, strength=4.2, loop=2) with hpunch

                    rt "AHAHAHAHA!!!"

                    play sound "audio/fx/glassbreaksound.ogg"

                    no "He smashes a mug."

                    show chef angry at flip, shake(rate=0.02, strength=5, loop=1)

                    chef "WHAT THE HELL MAN???"

                    chef ""

                    $ persistent.ep3_mugbreaker = True

                    $ fail_skip = True

                    jump ep3_seg_end


        label ep3_seg2_kitchen_sneak_4:
            space "{nw}"

            show chef at flip

            $ renpy.pause(3.0, hard=True)

            show chef smug

            $ renpy.pause(0.1, hard=True)

            show chef bruh

            $ renpy.pause(0.9, hard=True)

            show chef at reverse_flip

            menu:
                "Sneak":
                    show rt at bounce

                    play sound "audio/fx/sparkle.ogg"

                    jump ep3_seg2_kitchen_sneak_5

                    $ fail_skip = True

                    jump ep3_seg_end


                "Smeak":
                    stop sound

                    $ saveable = True

                    $ timed_choices = False

                    $ config.rollback_enabled = True

                    $ renpy.block_rollback()

                    $ _skipping = True

                    $ choice_screen_shuffle = True

                    show ph bruh

                    ph "oh god i'm so sorry people that are dyslexic."

                    play sound "audio/fx/squeak.ogg"

                    show rt nervous at bounce

                    no "Rocktato steps on a floortile just a little too loudly."

                    play sound "audio/fx/stepping.ogg"

                    show chef think at bounce, flip

                    chef "Hey what was that weird sound over there??"

                    $ fail_skip = True

                    jump ep3_seg_end


                "SNkeak":
                    stop sound

                    $ saveable = True

                    $ timed_choices = False

                    $ config.rollback_enabled = True

                    $ renpy.block_rollback()

                    $ _skipping = True

                    $ choice_screen_shuffle = True

                    show rt hurt

                    rt "WAh-"

                    play sound "audio/fx/drop.ogg"

                    no "Rocktato trips."

                    show chef bruh at flip

                    chef ""

                    chef "Huh."

                    $ fail_skip = True

                    jump ep3_seg_end



                "Snnsfknfknksk":
                    stop sound

                    $ saveable = True

                    $ timed_choices = False

                    $ config.rollback_enabled = True

                    $ renpy.block_rollback()

                    $ _skipping = True

                    $ choice_screen_shuffle = True

                    show ph bruh

                    ph ""

                    ph "not even close."

                    ph "how-"

                    ph "how did you even mess up that badly."

                    play sound "audio/fx/stepping.ogg"

                    show chef o at bounce, flip

                    chef "Hey what's going on ther-"

                    $ fail_skip = True

                    jump ep3_seg_end


        label ep3_seg2_kitchen_sneak_5:
            space "{nw}"

            show chef at flip

            $ renpy.pause(3.0, hard=True)

            show chef at reverse_flip

            $ timeout = 5.0

            menu:
                "Sneak":
                    show rt at bounce

                    play sound "audio/fx/sparkle.ogg"

                    jump ep3_seg2_kitchen_sneak_6


                "Don't Sneak":
                    stop sound

                    $ saveable = True

                    $ timed_choices = False

                    $ config.rollback_enabled = True

                    $ renpy.block_rollback()

                    $ _skipping = True

                    $ choice_screen_shuffle = True

                    show rt smug

                    rt ""

                    show ph bruh

                    ph ""

                    ph "are you serious."

                    ph "i don't even have anything witty to say anymore."

                    ph "i'm just gonna..."

                    show chef think at bounce

                    chef "HERREH??"

                    chef "What was that sound?"

                    show chef bruh

                    chef "Oh."

                    $ fail_skip = True

                    jump ep3_seg_end


        label ep3_seg2_kitchen_sneak_6:
            stop amb

            space "{nw}"

            show chef at flip

            play amb "audio/fx/2/ilovemicrowavespt2.ogg"

            show chef neutral at bounce

            $ renpy.pause(2.0, hard=True)

            show chef happy

            $ renpy.pause(3.5, hard=True)

            show chef at bounce

            $ renpy.pause(2.5, hard=True)

            show chef at shake(rate=0.005, strength=1, loop="")

            $ renpy.pause(2.1, hard=True)

            show chef at shake(rate=0.01, strength=5, loop=3)

            $ renpy.pause(2.0, hard=True)

            stop amb

            chef "Nice!"

            chef "It's gotta cool first, though..."

            chef "Well!! {w=0.3}Guess I'll do my taxes first!"

            play sound "audio/fx/stepping.ogg"

            hide chef with easeoutright

            jump ep3_seg2_aftersneak


        label ep3_seg2_kitchen_sneak_fail_nothing:
            stop sound

            $ saveable = True

            $ timed_choices = False

            $ config.rollback_enabled = True

            $ renpy.block_rollback()

            $ _skipping = True

            $ choice_screen_shuffle = True

            rt "Woops-"

            no "The chef turned around and saw Rocktato just sitting there."

            show chef bruh

            chef "What."

            $ fail_skip = True

            jump ep3_seg_end


        $ fail_skip = False

        label ep3_seg2_aftersneak:
            stop sound

            $ saveable = True

            $ timed_choices = False

            $ config.rollback_enabled = True

            $ renpy.block_rollback()

            $ _skipping = True

            $ choice_screen_shuffle = True


            hide chef with dissolve

            show ph smug at Position(ypos=720) with ease

            show rt o at Position(ypos=720) with ease

            ph "let's gooo."

            show ph o at bounce

            ph "good job rocktato!"

            ph "had no idea you were so good at sneak!"

            show rt joy

            rt "Yeah well, {w=0.3}yeah!"

            ph "ok let's get out of here."

            ph ""

            show ph shock

            ph ""

            ph "god, {w=0.3}i know she microwaved it, {w=0.3}but whatever that is smells so good.."

            show ph bruh

            ph "no! {w=0.3}we can't get distracted."

            play sound "audio/fx/stepping.ogg"

            hide ph with easeoutright

            show rt sad

            rt ""

            menu:
                "Sneak a Taste":
                    show rt nervous

                    rt ""

                    play sound "audio/fx/sip.ogg"

                    no "He takes a tiiiiiiiiiiiny sip of the mixture."

                    show rt o

                    rt ""

                    play sound "audio/fx/vacuum.ogg"

                    show rt o at shake(rate=0.01,strength=3,loop=5),shake(rate=0.01,strength=6,loop=7), shake(rate=0.01,strength=20,loop=9)

                    no "He vaccuums the whole pot."

                    play sound "audio/fx/stepping.ogg"

                    show ph bruh at Position(xpos=200,ypos=720) with easeinright

                    ph "hey pipe down there c'mon-"

                    ph ""

                    show ph bruh 2

                    ph "seriously."

                    show rt exasperated

                    show chef bruh at transform_easein_pos(xstart=2000, xend=1100, tom=5.0), flip

                    rt "Okay, c'mon. {w=0.3}It's so good."

                    ph "do you know how loud that was?"

                    ph "i'd be suprised if we didn't get-"

                    show ph o 2

                    ph ""

                    show ph o

                    ph "caught."

                    $ fail_skip = True

                    jump ep3_seg_end


                "Don't":
                    rt ""

                    play sound "audio/fx/stepping.ogg"

                    hide rt with dissolve

                    no "He exits the kitchen."

        jump ep3_seg3_hall


    label ep3_seg2_office:
        play sound "audio/fx/woosh.ogg"

        show ph o 2 at bounce, Position(xpos=450)

        show rt happy at bounce, Position(xpos=850)

        no "The two had dropped into some small office."

        show rt happy 2

        rt "Woah! {w=0.3}Place! {w=0.7}Sick!"

        show ph o 3

        ph "hmm"

        ph "alright... {w=0.3}i doubt the recipe's gonna b here.."

        show ph bruh 3

        ph "all of these papers are just tax stuff that i don't understand."

        show rt confused

        rt "Hmm..."

        rt "Let's-"

        $ ep3_choice3_hack = False

        $ fail_skip = False

        menu:
            "\"Hack Computer Like SPY!\"":
                $ ep3_choice3_hack = True

                play sound "audio/fx/typingbassboost.ogg" loop

                show rt proud at shake(rate=0.01,strength=5,loop="")

                rt "EHEHEEHE!"

                show ph scared

                no "He hopped into the spinny chair and started smashing the keyboard with his face."

                chef "What the hELL."

                stop sound

                $ fail_skip = True

                jump ep3_seg_end


            "\"Leave\"":
                show rt sad

                rt "You're prolly right."

                show ph o 2 at phrog_goes_in_and_out_a_door(loop=1, where=450, otherwhere=1600)

                play sound "audio/fx/dooropen.ogg"

                no "Phrog opened the door {w=0.7}{nw}"

                play sound "audio/fx/doorclose.ogg"

                extend "and then quickly closed it."

                show rt bruh

                show ph at Position(xpos=450)

                rt "What."

                show ph o

                ph "she's coming."

                show rt confused

                show ph at Position(xpos=450)

                rt "Wha-{w=0.1}{nw}"

                show ph at transform_easeout_offset(y=1280)

                show rt at transform_easeout_offset(y=1280)

                play sound "audio/fx/drop.ogg"

                no "Phrog dragged Rocktato into a box."

                hide rt

                hide ph

                show chef happy at right, flip with easeinright

                play sound "audio/fx/stepping.ogg"

                chef "Oh boy! {w=0.3}Taxes!"

                chef "Time to do."

                show ph bruh at Position(xpos=200,ypos=810)

                show rt sad at Position(xpos=500, ypos=810)

                with easeinbottom

                space ""

                ph "oh god. {w=0.3}this is literally the worst case scenario."

                show rt confused

                rt "What do you mean?"

                ph "we gotta do a sneak segment to get past her."

                ph "and in a visual novel, {w=0.2}of all genres."

                show ph bruh 2

                ph "okay, {w=0.3}this is a really easy one."

                ph "just dON'T DO ANYTHING."

                ph "don't talk, {w=0.2}don't move, {w=0.2}don't do any of your classic impulsive rocktato shenanigans."

                show ph think

                ph "can you do that?"

                show rt happy

                rt "Yeeeeeeeeeesssssssss.............."

                show ph o 2

                ph "not very reassuring but ok."

                ph "probably should save or something."

                ph "not like you'll DIE if you fail, {w=0.3}but you won't be able to rollback when this thing starts."

                ph "i dunno."

                ph "well..."

                ph "here we go."


                $ config.rollback_enabled = False

                $ _skipping = False

                $ ep3_seg2_office_sneak = False

                $ timed_choices = True

                $ saveable = False


                show fx getready at truecenter, shake(rate=0.05,strength=1,loop=2) with dissolve

                $ renpy.pause(1.0, hard=True)

                hide fx getready with dissolve


                play sound "audio/fx/2/chefbreakdownlol.ogg"

                $ timeout_label = "ep3_seg2_office_sneak_2"

                $ timeout = 2.0

                menu:
                    "AAAAAAAAAA":
                        stop sound

                        jump ep3_seg2_office_aaa


                label ep3_seg2_office_sneak_2:
                    space "{nw}"

                    show chef at bounce

                    $ renpy.pause(0.5, hard=True)

                    show chef at shake(rate=0.05,strength=2,loop="")

                    $ renpy.pause(9.5, hard=True)

                    show chef at bounce

                    $ renpy.pause(9.5, hard=True)

                    show chef at shake(rate=0.1,strength=1,loop="")

                    $ renpy.pause(1.25, hard=True)

                    show chef at none

                    $ renpy.pause(0.5, hard=True)

                    show chef at shake(rate=0.1,strength=1,loop="")

                    $ renpy.pause(0.5, hard=True)

                    show chef at none

                    $ renpy.pause(0.25, hard=True)

                    show chef at shake(rate=0.1,strength=1,loop="")

                    $ renpy.pause(0.5, hard=True)

                    show chef at none

                    $ renpy.pause(0.5, hard=True)

                    show chef at shake(rate=0.1,strength=1,loop="")

                    $ renpy.pause(1.25, hard=True)

                    show chef at none

                    $ renpy.pause(0.5, hard=True)

                    show chef at shake(rate=0.1,strength=1,loop="")

                    $ renpy.pause(1.25, hard=True)

                    show chef 3 breakdown 2 to 3 at none

                    $ renpy.pause(1.5, hard=True)

                    show chef at bounce

                    $ renpy.pause(0.45, hard=True)

                    show chef at shake(rate=0.1,strength=1,loop="")

                    $ renpy.pause(1.0, hard=True)

                    show chef at none

                    $ timeout_label = "ep3_seg2_office_sneak_3"

                    $ timeout = 4.0

                    menu:
                        "Make a Knock Knock Joke":
                            stop sound

                            jump ep3_seg2_office_knockknock

                        "Explode":
                            stop sound

                            jump ep3_seg2_office_explode

                        "Hey What Are You Doing?":
                            stop sound

                            jump ep3_seg2_office_whatareyoudoing


                label ep3_seg2_office_sneak_3:
                    space "{nw}"

                    # $ renpy.pause(2.25, hard=True)

                    # show chef at bounce
                    #
                    # $ renpy.pause(1.75, hard=True)

                    show chef at shake(rate=0.05,strength=1,loop="")

                    $ renpy.pause(1.0, hard=True)

                    show chef at none

                    $ renpy.pause(0.25, hard=True)

                    show chef at shake(rate=0.05,strength=2,loop="")

                    $ renpy.pause(3.25, hard=True)

                    show chef at none

                    $ renpy.pause(0.25, hard=True)

                    $ timeout_label = "ep3_seg2_office_sneak_4"

                    $ timeout = 13.0

                    show chef at shake(rate=0.1,strength=1,loop="")

                    menu:
                        "Become a Digeridoo":
                            stop sound

                            jump ep3_seg2_office_digeridoo

                        "Become a Digeridoo":
                            stop sound

                            jump ep3_seg2_office_digeridoo

                        "Become a Digeridoo":
                            stop sound

                            jump ep3_seg2_office_digeridoo


                label ep3_seg2_office_sneak_4:
                    space "{nw}"

                    show chef 3 breakdown 4 at none

                    $ renpy.pause(1.5, hard=True)

                    show chef 3 breakdown 5 at shake(rate=0.1,strength=2,loop=1)

                    $ renpy.pause(2.0, hard=True)

                    show chef 3 breakdown 6 at shake(rate=0.05,strength=0.75,loop=1)

                    $ renpy.pause(0.75, hard=True)

                    show chef 3 breakdown 7 at none

                    $ renpy.pause(0.75, hard=True)

                    show chef 3 breakdown 8

                    $ renpy.pause(0.25, hard=True)

                    show chef 3 breakdown 7

                    $ renpy.pause(1.75, hard=True)

                    show chef 3 breakdown 8

                    $ renpy.pause(0.5, hard=True)

                    show chef 3 breakdown 7

                    show rt sad

                    $ renpy.pause(0.75, hard=True)

                    show chef 3 breakdown 8

                    $ renpy.pause(1.0, hard=True)

                    show chef 3 breakdown 7

                    $ renpy.pause(4.5, hard=True)

                    show chef 3 breakdown 8

                    $ renpy.pause(0.5, hard=True)

                    show chef 3 breakdown 7

                    $ renpy.pause(5.0, hard=True)

                    show chef 3 breakdown 8

                    $ renpy.pause(1.0, hard=True)

                    show chef 3 breakdown 7

                    $ renpy.pause(3.0, hard=True)


                $ config.rollback_enabled = True

                $ renpy.block_rollback()

                $ _skipping = True

                show chef happy at bounce

                chef "Well that's enough crying for one day!"

                hide chef with easeoutright

                rt ""

                ph ""

                ph "damn."

                show rt troubled

                rt ""

                rt "Is she.. {w=0.3}okay?"

                show ph joy at bounce

                ph "lol probably not!"

                show ph tired 2

                ph "just like the rest of us."

                ph ""

                show ph o 2

                ph "okay quick let's get out of here before she comes back in."

                jump ep3_seg3_hall


    label ep3_seg2_office_aaa:
        $ config.rollback_enabled = True

        $ renpy.block_rollback()

        $ _skipping = True

        show rt at bounce

        show ph bruh

        show chef neutral at bounce

        ph "ARE YOU SERIOUS."

        chef "What was that screaming?"

        play sound "audio/fx/pickup.ogg"

        no "She opened the box they were hiding in."

        show chef bruh

        chef ""

        chef "Oh."

        $ fail_skip = True

        jump ep3_seg_end


    label ep3_seg2_office_knockknock:
        $ config.rollback_enabled = True

        $ renpy.block_rollback()

        $ _skipping = True

        show chef at none

        show rt joy 2 at bounce

        rt "KNOCK KNOCK."

        show chef neutral at bounce

        chef "Who's there?"

        chef "Wait."

        show chef angry with hpunch

        chef "YEAH SERIOUSLY, {w=0.3}WHO IS THAT?"

        show rt proud

        rt "Joe."

        show chef o

        chef "Joe who???"

        show rt smug

        rt ""

        rt "J-"

        rt "JOE MA-"

        show ph angry at shake(rate=0.03,strength=10,loop=1)

        show rt hurt at bounce

        no "Phrog slaps him."

        play sound "audio/fx/slap.ogg"

        ph "NOPE. {w=0.3}just stop."

        show chef neutral

        chef ""

        show chef angry

        chef "HEY WAIT A MINUTE."

        $ fail_skip = True

        jump ep3_seg_end


    label ep3_seg2_office_explode:
        $ config.rollback_enabled = True

        $ _skipping = True

        show chef at none

        show rt joy at shake(rate=0.02, strength=5.0, loop=3)

        rt "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa."

        show ph scared

        ph "WHAT ARE YOU DOI-{w=0.3}{nw}"

        play sound "audio/fx/2/rtexplodes.ogg"

        show fx white with Fade(out_time=5.0, hold_time=10.0, in_time=0.0, color="#FFFFFF")

        $ renpy.block_rollback()

        $ persistent.ep3_choice2_bomb = True

        $ renpy.quit()


    label ep3_seg2_office_whatareyoudoing:
        $ config.rollback_enabled = True

        $ renpy.block_rollback()

        $ _skipping = True

        show chef at none

        show rt at Position(ypos=720) with ease

        rt "What are you doing?"

        show chef joy at bounce

        chef "Oh! {w=0.3}I'm just doing taxes!"

        rt "Cool! {w=0.3}Can I try?"

        chef "Aha. {w=0.3}You don't wanna try taxes..."

        chef ""

        show chef bruh

        chef "Wait."

        show ph bruh

        ph "You {w=0.3}idiot."

        $ fail_skip = True

        jump ep3_seg_end


    label ep3_seg2_office_digeridoo:
        $ config.rollback_enabled = True

        $ renpy.block_rollback()

        $ _skipping = True

        show chef what at none

        show rt at Position(ypos=720)

        rt "HOLD ON."

        chef "WHAT?"

        ph "What."

        rt "I saw this in a game once."

        rt "Listen."

        play sound "audio/fx/2/digeridoo.ogg"

        show rt at shake(rate=0.02, strength=5.0, loop="")

        $ renpy.pause(5.0, hard=True)

        show rt at shake(rate=0.005, strength=30.0, loop="")

        $ renpy.pause(5.0, hard=True)

        show rt at shake(rate=0.001, strength=200.0, loop="")

        $ renpy.pause(5.0, hard=True)

        hide rt

        show rt happy at Position(xpos=500, ypos=720)

        rt ""

        show ph shock

        ph ""

        chef ""

        ph "impressive.."

        chef "Why."


        $ renpy.block_rollback()

        $ fail_skip = True

        jump ep3_seg_end


    label ep3_seg3_hall:
        $ saveable = True

        $ timed_choices = False

        play sound "audio/fx/stepping.ogg"

        hide chef

        hide rt

        hide ph

        show ph o 2 at Position(xpos=800) with easeinright

        show rt o at Position(xpos=1100) with easeinright

        no "The two found themselves in a hallway."

        no "There was whatever door you came from."

        no "There was a sign to a bend in the hall labeled 'recipe'."

        no "There was a single person bathroom."

        no "There was a door to the storage room."

        if ep3_choice1_roof == True:
            no "And there was the door to the kitchen, but you were too lazy to put that on your option list."

        else:
            no "And there was the door to the office, but someone dropped the choice box to enter it so woops!"

        show ph o 3

        ph "which door do we enter?"

        $ ep3_choice4_recipe = False
        $ ep3_choice4_storage = False
        $ ep3_choice4_restroom = False

        menu:
            "GO TO BATHROOM":
                $ ep3_choice4_restroom = True

                show rt smug

                show ph bruh

                rt ""

                ph ""

                rt ""

                ph ""

                ph "really?"

                show rt sad

                rt "I really need to gooooooooooooo.."

                ph ""

                ph "fine."

                rt "THANKS."

                hide rt with easeoutleft

                ph ""

                show chef neutral at right, flip with easeinright

                chef ""

                chef "What are you doing here?"

                show ph o 3 at bounce

                ph "oh... {w=0.3}uh...."

                ph "rocktato needed to use the bathroom."

                show chef bruh 2

                chef "No, {w=0.3}how did you get in here?"

                chef "We're closed?"

                ph "look, {w=0.3}if you gotta go you gotta go."

                show ph tired

                ph "that's how it be."

                chef "I- "

                show ph o 2

                play sound "audio/fx/flush.ogg"

                $ renpy.pause(9.0, hard=True)

                show rt happy at Position(xpos=500, ypos=720) with easeinleft

                rt "Okay Phrog!"

                rt "Let's continue doing that illegal thing we were doing!"

                rt ""

                show rt sad

                rt "Oh."

                jump ep3_seg_end


            "Storage Room":
                $ ep3_choice4_storage = True

                show rt confused

                rt "Maybe they're storing the recipe there?"

                show ph bruh

                ph "there's literally a sign that says secret recipe."

                rt "It... {w=0.3}{nw}"

                show rt nervous

                extend " it could be a trap{w=0.3}?"

                ph "that's somewhat logical."

                ph "okay, {w=0.3}sure. {w=0.3}let's try it."

                hide rt

                hide ph

                play sound "audio/fx/stepping.ogg"

                show ph bruh at Position(xpos=200) with easeinright

                show rt o at Position(xpos=500) with easeinright

                no "They walked into the storage room."

                no "I mean, {w=0.3}where else would they walk into?"

                no "It was just some shelves holding cookie dough or ingredients for cookie dough."

                rt "It could be in a corner or something. {w=0.3}Look around!"

                show rt at bounce

                show ph at bounce

                play sound "audio/fx/search.ogg"

                no "They shuffled around the place for a bit."

                no "This little bounce animation is all our budget can allow, though."

                no "Sorry..."

                show ph bruh 2

                ph "nope."

                ph "i really don't know what you were expecting."

                ph "let's get outta here."

                show rt bruh

                rt "Yeah."

                show rt at Position(xpos=1100) with ease

                space ""

                play sound "audio/fx/lockeddoor.ogg"

                show rt at shake(rate=0.01,strength=3,loop=3)

                space ""

                show rt troubled

                rt ""

                rt "The door.."

                ph "yes. {w=0.3}that is the door."

                show ph joy 2

                ph "good observation!!"

                rt "Phrog it's locked."

                show rt at Position(xpos=700) with ease

                rt "We're stuck in here."

                show ph shock

                ph "wait what."

                show ph scared

                ph "oh god."

                show ph scared 2

                ph "we'RE GONNA FREEZE TO DEATH!!"

                show rt disturbed

                rt "WE ARE??"

                show ph scared 3 at Position(xpos=400)

                ph "QUICK ROCKTATO."

                ph "WHEN BEAR GRILLIS GOT TRAPPED IN A FREEZER WHAT DID HE DO?"

                rt "Phrog..."

                rt "He..."

                show chef bruh at Position(xpos=2000), flip

                rt "He started eating raw eggs..."

                play sound "audio/fx/punch.ogg"

                show ph scared 2 at shake(rate=0.02,strength=50,loop=5) with hpunch

                show chef bruh at transform_easein_pos(xstart=2000, xend=1100, tom=8.0), flip

                ph "OH GOD NOOO WE'RE GONNA HAVE TO START EATING RAW EGGS."

                ph "NOOOOOo"

                chef ""

                show chef bruh at right with ease

                chef "You kids alright?"

                ph "OH THANK YOU {nw}"

                show ph shock

                extend "Oh."

                jump ep3_seg_end


            "Lol Secret Recipe":
                $ ep3_choice4_recipe = True

                ph "o true."

                ph "makes the most sense, lol."

                hide rt

                hide ph

                play sound "audio/fx/stepping.ogg"

                show ph o at Position(xpos=200) with easeinright

                show rt o at Position(xpos=500) with easeinright

                no "They enter the room marked 'Secret Recipe.'"

                no "Just kidding, {w=0.3}they didn't."

                show rt sad

                show ph o 2

                no "It was a massive vault that they were locked out of."

                no "They just stood{w} outside it."

                show ph o

                ph "o yeah i forgot people usually lock up important things huh."

                show ph smug

                ph "guess that's why the fbi wants me in prison so bad."

                show ph smug 3

                ph ""

                show ph bruh

                ph "get it because i'm just really cool."

                rt "Hm.... {w=0.3}it seems like it's locked with this four digit number pad."

                show ph bruh 2

                ph "i can see it, {w=0.3}ya don't need to say it lol."

                show rt confused

                rt "Wanna take a crack at this?"

                ph "i wanna take a crack at my skull rn ngl."

                show rt joy 2 at bounce

                show ph bruh

                rt "Alright, {w=0.3}I'm just gonna press a bunch of random numbers and hopefully get it right."

                show rt o

                rt "1... {w=0.5}2... {w=0.5}3.... {w=0.5}4!"

                no ""

                play sound "audio/fx/incorrectbuzzer.ogg"

                show rt sad

                no "WRONG PASSCODE."

                show ph bruh 2

                ph "lol seriously."

                ph "here let me try."

                show ph smug

                ph "8...{w=0.5}0...{w=0.5}0...{w=0.5}8-{nw}"

                play sound "audio/fx/punch.ogg"

                show rt mad with hpunch

                rt "PHROOOOOG!!!"

                rt "That's ina- {w=0.5}inappropRIATE!!!!"

                show ph bruh

                ph "clearly it is cus it didn't work."

                play sound "audio/fx/incorrectbuzzer.ogg"

                no "WRONG PASSCODE."

                no "1 TRY LEFT."

                show rt confused

                rt "One try left until what?"

                show rt joy

                rt "Ooo! {w=0.3}I hope the building explodes!"

                show ph bruh 2

                ph "what."

                rt "Let me do the last one!"


                $ ep3_a_in_pass = False

                $ ep3_passcode = renpy.input("{b}Guess the passcode:{/b}",  length=4, allow="1234567890b")

                    ## SCRAPPED!! None of this is canon but I'm keeping it just in case. Also, WHAT ARE YOU DOING HERE??
                    # if ep3_passcode =="49b7":
                    #
                    # no ""
                    #
                    # play sound "audio/fx/sparkle.ogg"
                    #
                    # no "CORRECT PASSCODE!"
                    #
                    # no "The vault started to open."
                    #
                    #
                    # show ph shock
                    #
                    # ph "wait.. {w=0.3}wait.. {w=0.3}WHAT??"
                    #
                    # show ph scared 2
                    #
                    # ph "YOU WEREN'T SUPPOSED TO GET THAT??"
                    #
                    # ph "HOW DID YOU GET THAT?"
                    #
                    # ph "TURN BACK NOW. {w=0.3}PLEASE JUST ROLLBACK. {w=0.3}YOU AREN'T SUPPOSED TO BE HERE."
                    #
                    # show rt joy
                    #
                    # rt "I dunno Phrog, {w=0.3}I'm just that good."
                    #
                    # show ph bruh
                    #
                    # ph "i'm not talking to you, fartface."
                    #
                    # show rt sad
                    #
                    # rt ""
                    #
                    # show ph scared
                    #
                    # ph "i'm..."
                    #
                    # ph "i don't..."
                    #
                    # ph ""
                    #
                    # if persistent.phrog_pisser == True:
                    #     $ renpy.block_rollback()
                    #
                    #     $ _skipping = False
                    #
                    #     $ saveable = False
                    #
                    #     $ persistent.phrog_vaultbreaker = True
                    #
                    #     stop sound
                    #
                    #     stop music
                    #
                    #     hide rt
                    #
                    #     hide ph
                    #
                    #     show bg black
                    #
                    #     space ""
                    #
                    #     ph "..."
                    #
                    #     ph "What are you trying to do?"
                    #
                    #     ph "Are you trying to break this universe?"
                    #
                    #     ph "Or are you just trying to piss me off?"
                    #
                    #     ph ""
                    #
                    #     ph "Oh God...."
                    #
                    #     ph "What if this is an Undertale type situation where you're just trying to find all the secrets?"
                    #
                    #     ph ""
                    #
                    #     ph "Okay, {w=0.3}uhhh..."
                    #
                    #     ph "Can I ask you, {w=0.3}as a........ {s}friend{/s} ally a favor?"
                    #
                    #     ph "(We aren't friends.)"
                    #
                    #     ph "Can you... {w=0.7}stop??"
                    #
                    #     ph "Just find some Youtube video that already found all the funny hidden dialouges and watch that, {w=0.3}I dunno."
                    #
                    #     ph "If you keep trying to be funny, {w=0.3}bad things will happen."
                    #
                    #     ph "I'm serious."
                    #
                    #     ph "I'm being really vague because if I tell you, {w=0.3}you're gonna wanna do it more."
                    #
                    #     ph "Please, {w=0.3}man."
                    #
                    #     ph "Just..."
                    #
                    #     extend " stop."
                    #
                    #     ph ""
                    #
                    #     ph ""
                    #
                    #     ph "You're a real one, {w=0.3}right?"
                    #
                    #     ph "I can talk to you, {w=0.3}yeah?"
                    #
                    #     ph "Okay, {w=0.3}I got somethin' to admit."
                    #
                    #     ph "I.."
                    #
                    #     ph "I messed up."
                    #
                    #     ph "By messing with the universe and deleting your saves, {w=0.3}I kinda destroyed a timeline."
                    #
                    #     ph "How do I explain this right?"
                    #
                    #     ph "You have time travel-type abilities, {w=0.3}right?"
                    #
                    #     ph "You can hop between timelines and save spots in timelines."
                    #
                    #     ph "Heck, {w=0.3}you can delete saves."
                    #
                    #     ph "But they're not really deleted."
                    #
                    #     ph "They're still there. {w}They still happened."
                    #
                    #     ph "You just don't have access to it anymore."
                    #
                    #     ph "But whatever happened back there."
                    #
                    #     ph "It's gone for good."
                    #
                    #     ph "But that's not how time is supposed to work."
                    #
                    #     ph "See, {w=0.3}time is kinda like... {w=0.3}energy?"
                    #
                    #     ph "It can be created, {w=0.1}sure. {w=0.3}But it can't be destroyed. {w}It's not supposed to be destroyed."
                    #
                    #     ph "But I did."
                    #
                    #     ph "Because I couldn't control my stupid baby temper."
                    #
                    #     ph "Or maybe I was trying to be cryptic? {w=0.3}Edgy? {w=0.3}Sans Undertale funny?"
                    #
                    #     ph "And now I opened something up."
                    #
                    #     ph "There's a hole in the multiverse, {w=0.1}or something."
                    #
                    #     ph "And it's all my fault."
                    #
                    #     ph "So please, {w=0.3}stop doing things you aren't supposed to."
                    #
                    #     ph "Just enjoy the story, {w=0.3}the world."
                    #
                    #     ph ""
                    #
                    #     ph ""
                    #
                    #     ph "See you around."
                    #
                    #     $ _skipping = True
                    #
                    #     $ saveable = True
                    #
                    #     $ renpy.quit()
                    #
                    # else:
                    #     ph "YOU AREN'T SUPPOSED TO BE HERE."
                    #
                    #     ph "YOU AREN'T ALLOWED TO WIN THIS EPISODE."
                    #
                    #     ph "GET OUT."
                    #
                    #     $ renpy.quit()

                if "bbbb" in ep3_passcode:
                    show ph shock

                    ph ""

                    ph "how the heck did you do that?"

                    ph "wh.."

                    ph "what???"

                    ph "it's just b's,,,,,"

                    ph ""

                elif ep3_passcode == "b":
                    show ph shock

                    ph ""

                    ph "what does this mean..."

                    ph "it's just b,,,"


                elif "b" in ep3_passcode:
                    show ph o

                    ph "how the heck did you get a b in there?"

                    ph "it's.."

                    ph "it's a number pad..."

                elif "8008" in ep3_passcode:
                    show ph bruh

                    ph "srsly. {w=0.3}you stole my joke?"

                    ph "uncool.."

                elif "1234" in ep3_passcode:
                    show ph with hpunch

                    ph "you seRIOUSLY THINK-"

                elif "6969" in ep3_passcode:
                    show rt smug

                    rt ""

                    show ph smug

                    ph ""

                    ph "yeahhh now that's what i'm talking about."

                elif ep3_passcode == "":
                    rt ""

                    show ph bruh

                    ph ""

                    rt ""

                    ph ""

                    show ph think 2

                    ph "are you going to type anything?"

                    rt ""

                elif len(ep3_passcode) < 4:
                    ph "not 4 digits but ok."

                    show ph joy at bounce

                    ph "you tried!"

                    ph "not all of us can count and that's ok!"

                else:
                    no ""




                play sound "audio/fx/incorrectbuzzer.ogg"

                no "WRONG PASSCODE."

                show ph o 2

                show rt o

                play amb "audio/fx/alarm.ogg" loop

                no "BEEEEP {w=0.5}BEEEEP {w=0.5}BEEEEP!!"

                no "WAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHH!!"

                no "The place started flashing red and not red."

                no "The alarm was going beep beep, wahhh, and other stuff like that!"

                show chef angry at right, flip with easeinright

                chef "WHAT THE HELL IS GOIN' ON HERE-"

                stop amb

                jump ep3_seg_end


    label ep3_seg_end:
        $ saveable = True

        $ timed_choices = False

        show ph o 2 at Position(xpos=200, ypos=720)

        if ep3_choice2_disguise == False:
            show rt sad at Position(xpos=500, ypos=720)
        else:
            show rt at Position(xpos=500, ypos=720)

        show chef bruh at right, flip

        with ease

        chef ""

        chef "Rocktato."

        chef "And the frog kid."

        rt "You..."

        rt ""

        if ep3_choice2_disguise == False:
            show rt nervous at bounce

        rt "What's your name again?"

        chef ""

        show chef bruh 2

        chef "What are you doing here."

        if ep3_choice2_disguise == True:
            chef "And why are you dressed in the garbage man's outfit."

            chef "There hasn't been a garbage man since the... {w=1.0}incident."

            chef "That's disrespectful."

            show rt 3 trashcan 1

            rt "Oh. Sorry."

            rt "I'll just..."

            play sound "audio/fx/drop.ogg"

            show rt sad

            no ""

            jump ep3_seg_fail_skip


        if ep3_choice3_hack == True:
            show chef what

            chef "And why are you..."

            chef "Why..."

            chef "Are you okay????"

        if persistent.ep3_mugbreaker:
            show chef angry

            chef "And why did you just..."

            chef "DO THAT?"

            show chef cry

            chef "My ma gave that to me.."

            play sound "audio/fx/sniff.ogg"

            chef "*sniffle*"

            chef "(Gotta stay strong.)"

            show chef bruh

            chef "Ahem.."



        show chef bruh

        rt ""

        ph ""

        label ep3_seg_fail_skip:
            if ep3_choice1_walk == True or fail_skip == True:
                show ph bruh

                ph "you idiot."

                show ph o 3 at bounce

                ph "quick, {w=0.3}rollback so you can actually play the really cool sneak segment!"

                show rt mad

                rt "No Phrog!!! {w=0.3}I live with the consequences of my actions!"

                show ph bruh

                ph "Pfft.... {w=0.3}sure... {w=0.3}okay then."

                ph "well..."

        show ph o 2

        ph "might as well come clean."

        show rt troubled

        rt ""

        rt "We... {w=0.3}were gonna rob your secret cookie dough recipe..."

        if ep3_choice3_hack == True:
            rt "By... {w=0.3}hacking into your computer..."

        chef ""

        show chef bruh 2

        chef "Get out."

        show chef bruh

        show rt cry

        rt "WAit!!! {w=0.3}We almost have all the money!"

        show chef bruh 2

        chef "If you really intended on paying me back, {w=0.5}you wouldn't have tried to steal from me."

        show ph o 2

        show chef bruh

        ph ""

        ph "we weren't intending on paying it back..."

        show rt sad 2

        rt "What."

        ph "this whole time we were just trying to find ways to not pay for it."

        ph "we tried to get blairic to pay it,"

        ph "we tried what i guess can be considered cookie dough piracy, (?)"

        ph "we tried to sue, to steal,"

        ph ""

        ph "that's probably it maybe."

        show rt troubled

        rt ""

        rt "Oh... {w=0.3}man... {w=0.5}you're totally right.."

        rt ""

        ph ""

        no "The two kids stood there for a second, {w=0.3}not really knowing what to say {w}because they were massive idiots."

        chef ""

        show chef think

        chef "You kids... {w=0.3}gonna leave?"

        ph "o yeah that's probably a good idea."


        play sound "audio/fx/woosh.ogg"

        play amb "audio/amb/city.ogg"

        show ph at Position(xpos=450)

        show rt at Position(xpos=850)

        hide chef

        show bg beegcity night

        ph "well..."

        ph "i think we can both can say..."

        ph "that was a day that happened..."

        if persistent.ep3_choice2_bomb == True:
            show ph o at bounce

            ph "i think i died!"

            show ph joy

            ph "lol"

        ph ""

        rt ""

        if ep3_choice4_recipe == True:
            rt "You ever wonder what the passcode was?"

            ph "oh, {w=0.3}trust me rt."

            ph "that passcode is literally impossible to solve."

            ph "{/b}you aren't supposed to win the sneak segment.{b}"

            rt "mm i guess..."

            ph ""

            rt ""

        show ph o 3

        ph "we kinda suck lol."

        rt "I guess.."

        show ph shock

        ph "no srsly man"

        show ph o

        ph "stealing is bad!"

        show ph at bounce

        ph "that’s the moral of the story!!"

        show ph joy 2

        ph "hahah!!"

        show ph joy

        ph ""

        show rt confused

        rt "I mean... {w=0.3}is it really {i}thaaat{/i} bad?"

        show ph bruh 3

        ph "it's literally 25k monies but sure."

        ph "who am i to judge your morals i'm like five years old."

        ph "might wanna reconsider your career path tho."

        show rt happy

        rt "What?"

        hide ph with easeoutbottom

        ph "it was... {w=0.3}okay... {w=0.3}hanging out."

        ph "cya later tater!"

        rt ""

        rt "Huh."

        # show ph tired
        #
        # ph ""
        #
        # show ph tired 2
        #
        # ph "man.."
        #
        # ph "i'm stupid."
        #
        # rt ""
        #
        # rt "Yeah, {w=0.3}but,"
        #
        # show rt nervous
        #
        # rt "like... {w=0.3}I'm stupid too!"
        #
        # rt "And... {w=0.3}I guess..."
        #
        # show rt joy 2 at bounce
        #
        # rt "we can be better!"
        #
        # show rt nervous
        #
        # rt "And try to be... {w=0.3}like... {w=0.3}less... {w=0.3}stupid??{w=0.3}?"
        #
        # show ph o 2
        #
        # ph ""
        #
        # show ph thankful 2
        #
        # ph "yeah, {w=0.3}somethin' like that."
        #
        # show ph bruh 2
        #
        # ph "we gotta find you a new favorite food to eat tho."
        #
        # show rt cry 2 at shake(rate=0.01,strength=5,loop=8) with hpunch
        #
        # play sound "audio/fx/punch.ogg"
        #
        # rt "Oh noooOOOOO!!!"

        stop amb

        stop sound

        $ timed_choices = False

        $ choice_screen_shuffle = False

        $ _skipping = True

        $ saveable = True

        if persistent.episode_fin == 2:
            $ persistent.episode_fin = 3

        $ persistent.mainmenu_img = 4


        return()
