label ep_2:

    $ persistent.mainmenu_img = 2
    $ persistent.saveepisode_img = 2
    $ failed = False

    image getreadytext:
        "gui/text/get ready.png"

    stop music fadeout 1.0

    ph "so, what'dya need me for again?"

    show bg beegcity

    show ph o at Position(xpos=450)

    show rt happy at Position(xpos=850)

    space ""

    ph "and can we hurry this up?"

    ph "i have a busy day today."

    ph "i'm gonna do a bunch of {w=0.3}nonexsiting."

    show rt joy 2 at bounce

    rt "Actually, I just wanted you to get outside of your lil' swamp for a bit."

    show ph bruh

    ph "i should've known."

    show rt o

    rt "Also! {w=0.3}We're looking for a bell!"

    rt "Mr. Rock is really quiet and it gets hard to remember he exists!"

    show ph tired 2

    ph "bro doesn't even have a dialouge sound."

    show rt happy 2

    show ph bruh

    rt "Yeah! {w=0.3}That!"

    show ph bruh 2

    ph "uh... {w=0.3}are we sure he isn't here right now?"

    show ph bruh

    show rt o at bounce

    no "Rocktato looks around."

    show rt happy

    rt "Probably."

    show ph happy

    ph "k cool just making sure."

    ph "i'm not going through that again."

    show ph o

    ph "so where are we going?"

    show ph o 2

    show rt o

    rt "Oh.."

    rt "I don't know."

    rt "Huh..."

    show rt confused at bounce

    rt "Where the heck {i}ARE{/i} you supposed to get a bell??"

    ph "..."

    show ph o 3

    ph "hey i'm hungry wanna get cookie dough?"

    show rt happy 2 at shake(rate=0.01,strength=1,loop=3)

    rt "OOOooooooooh! Heck yeah!"

    show bg cookiedoughshop

    hide rt

    hide ph

    space ""

    show rt happy at Position(xpos=500) with easeinleft

    show ph happy at Position(xpos=200) with easeinleft

    space ""

    show ph o 2

    ph "wait a second..."

    show ph at phrog_goes_in_and_out_a_door

    pause 4.0

    show chef neutral at transform_easein_pos(1400, 1000, 10.0), flip

    pause 4.0

    chef "Uh… {w=0.3}Can I help you?"

    show ph o at Position(xpos=200)

    ph "o sorry i was just..."

    ph "..."

    ph "uh..."

    show chef polite at Position(xpos=1000)

    chef "You alright?"

    show rt happy 2

    rt "Oh, don't mind Phrog."

    rt "She just.... {w=0.3}"

    show rt confused

    extend "really likes doors...{w=0.3}?"

    show rt happy

    show chef neutral

    chef "Okay..."

    show chef joy

    chef "What can I get for you today, Rocktato?"

    chef "Just the usual?"

    chef "A tub of the good ol' regular flavored cookie dough?"

    show rt joy 2 at bounce

    rt "Make it three please!"

    chef "Alrighty!"

    no "She pulls two tubs of cookie dough out of her pockets and sets them on the counter."

    chef "Here you go! {w=0.3}That'll be 6 monies."

    show rt happy at bounce

    rt "Oh just put it on my tab."

    show chef neutral

    chef "Okay..."

    show chef uncomfortable

    chef "Rocktato, {w=0.3}I've been meaning to ask..."

    chef "When do you intend on paying all this back?"

    chef "You owe us at least...{w=0.3}{nw}"

    show chef what

    extend " JESUS 1 MILLION MONIES."

    rt "Wait what."

    chef "You..."

    show chef

    chef "You intend on paying all this back, right?"

    show rt confused

    rt "I thought it was free."

    show ph bruh

    ph "you idiot."

    show rt at shake(rate=0.01,strength=3,loop=7)

    rt "Isn't that what a tab is??"

    show chef uncomfortable

    chef "Okay, {w=0.3}I'm going to kindly ask you to leave and come back once you decide to pay this back."

    show rt nervous at bounce

    rt "Aha..."

    rt "Well the thing is... {w=0.3}I don't have money."

    show rt happy 2 at bounce

    rt "I'm a child!"

    chef "Uh... {w=0.3}don't you have parents or a guardian or something?"

    show rt joy 2

    rt "No!"

    show chef neutral

    chef "Wait..."

    chef "Really?"

    chef "Dang..."

    rt "Oh don't worry about it! {w=0.3}Parents are disgusting."

    show ph smug 2

    ph "facts."

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

    extend ""

    show chef joy

    chef "Maybe a day is a bit cruel, {w=0.3}but it's sure to make some funny shenanigans..."

    rt "Cool, bye!"

    show chef angry

    chef "Oh c'mon... {w=0.3}Wait!!{nw}"


    show ph at Position(xpos=450)

    show rt at Position(xpos=850)

    play sound "audio/fx/woosh.ogg"

    show bg beegcity

    hide chef

    rt "MmmPhh… {w=0.3}I don’t know how, {w=0.3}but they just keep tasting better and better!"

    show ph bruh

    ph "do you even {i}intend{/i} on paying her back?"

    show rt nervous

    rt "Uh... {w=0.5}y{w=0.1}e{w=0.1}e{w=0.1}e{w=0.1}e{w=0.1}e{w=0.1}s{w=0.1}.{w=1.5}.{w=1.5}.{w=5.0}."

    ph "seriously, {w=0.3}you gotta pay her back."

    rt "Yeah.... {w=0.3}I know, {w=0.3}I know."

    ph "you heard her, {w=0.3}you're gonna b banned."

    show rt happy 2

    rt "I wouldn't worry about it, {w=0.3}I'm cute!"

    rt "Look, {w=0.3}I'll even walk back in to prove it!"

    hide rt with easeoutleft

    space ""

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

    play sound "audio/fx/woosh.ogg"

    bl "No."

    play sound "audio/fx/punch.ogg"

    show rt cry 2 with hpunch

    rt "What??"

    show bl uncomfortable

    bl "How the hell does one spend one million on cookie dough!?"

    bl "How?"

    show ph bruh 2

    ph "to b fair, {w=0.3}he had the tab open for like, {w=0.3}three years?"

    ph "the fact that he got away without paying for three years is more impressive, tbh."

    bl "Okay, {w=0.3}I am sorry Rocktato but I am not paying this."

    show rt at shake(rate=0.01,strength=5,loop=5)

    rt "Why not???"

    bl "Believe it or not, {w=0.3}I'm not as rich as you think I am."

    show ph o

    ph "wait srs?"

    ph "what's your net worth."

    bl "I'm not-{w=0.3}{nw}"

    show ph bruh 2

    ph "wow, {w=0.3}thought so."

    show ph smug 2

    ph "he's lying, rocktato."

    show bl bruh 2

    bl "Put a sock in it, Phrog."

    bl "Okay, {w=0.3}fine."

    bl "I shall pay for-{w=0.15}{nw}"

    show rt joy 2 at shake(rate=0.01,strength=20,loop=6)

    rt "YEAHHHHH!!!"

    bl "99.9999\% of it."

    bl "You have to pay one hundred dollars."

    show rt cry

    rt "WHAAAT??"

    show rt cry 2 with hpunch

    rt "THAT'S SO MUCH MONEYYYYY THo..."

    show ph bruh 2

    ph "well, {w=0.3}ya gotta learn."

    ph "nothin's free in life, kid."

    show bl happy 3 at bounce

    bl "Good luck!"

    bl "I shall attend to my job now."

    hide bl with easeoutright

    space ""


    show bg beegcity

    show ph bruh at Position(xpos=450)

    show rt at Position(xpos=850)

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

    ph "k cool."

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

    show ph bruh at Position(xpos=450) with easeinbottom

    ph "alright, {w=0.3}alright, {w=0.5}fine."

    show ph at shake(rate=0.005,strength=0.5,loop=20)

    no "Phrog ruffles through her refridgerator/microwave."

    no "It was a combo appliance!"

    no "Now on sale at your local dealership!"

    ph "Nope."

    ph "Don't do that."

    rt "What?{w=0.2}{nw}"

    no "Okay, {w=0.3}jeez."

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

    no "A giant gun came out of the side of the tub."

    show ph o

    ph "what."

    show rt disturbed

    Character("Tub", size=25, callback=no_blip) "UNAUTHORIZED CONSUMER DETECTED."

    Character("Tub", size=25, callback=no_blip) "DEPLOYING LASERS."


    show bg at fast_shaking

    show rt at fast_shaking

    show ph at fast_shaking

    Character("Tub", size=25, callback=no_blip) "*BZZZZZZZTTTTTTTT*"

    no "It starts firing towards Rocktato."

    show rt hurt

    show ph scared

    no "Phrog dropped the tub on the ground and hid under a pillow."

    rt "WAAAAAAAAHHHH."

    hide rt with easeoutleft

    no "Rocktato runs out of the house to hide."

    show ph scared 2

    ph "WHAT? {w=0.3}DON'T LEAVE ME IN HERE ALONE WITH THIS THING."

    show bg at none

    show ph o at none

    Character("Tub", size=25, callback=no_blip) "No unfunnies detected!"

    Character("Tub", size=25, callback=no_blip) "Thanks! {w=0.3}And have a great day!"

    ph ""

    show rt disturbed at transform_easein_pos(-500, 850, 5.0)

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

    ph "buh. {w=0.3}probly smth like that."

    ph "well... {w=0.7}it's too late to back out now."

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

    ph "if it doesn't, {w=0.3}we can just rollback."

    show rt confused

    rt "What does that mean?"

    ph "again, {w=0.3}dw about it."

    ph "So, {w=0.3}Rocktato, {w=0.3}you chose! {w=0.5}How do you wanna enter?"

    $ choice_screen_type = "choice"

    # Oh my god I have to set ALL THE VARIABLES this is gonna SUCK
    $ ep2_choice1_back = False
    $ ep2_choice1_walk = False
    $ ep2_choice1_roof = False

    $ ep2_choice2_disguise = False

    $ ep2_choice2_bomb = False

    $ ep2_choice3_hack = False

    $ ep2_choice4_recipe = False
    $ ep2_choice4_storage = False
    $ ep2_choice4_restroom = False

    $ fail_skip = False


    menu:
        "Back Door":
            $ ep2_choice1_back = True

            ph "smart."

            jump ep2_seg1_back


        "Just Walk in LOL":
            $ ep2_choice1_walk = True

            show rt smug 2

            rt "If anyone is in there, {w=0.3}they'll be so intimidated by our sheer audacity."

            show ph o

            hide rt with easeoutright

            ph "wait what-{w=0.1}{nw}"

            show bg cookiedoughshop

            show ph bruh at Position(xpos=200)

            show chef what at right, flip

            show rt smug 2 at Position(xpos=500) with easeinleft

            rt "Hey hey hey! {w=0.5}What's a poppin'?{w=1.0}{nw}"

            rt "I'm definitely not coming here for any malicious intentions!{w=1.0}{nw}"

            rt "Don't mind me!!"

            chef "."

            jump ep2_seg_end


        "Enter Thru Roof Like SPY":
            $ ep2_choice1_roof = True

            ph "i mean... {w=0.3}that could work."

            show rt confused

            rt "How do we get up there tho..."

            show ph smug

            ph "i got this."

            show ph at bounce

            no "Phrog picked up Rocktato bridal style and they jumped to the top of the roof."

            show rt o at bounce

            rt "Woah! {w=0.3}Nice!"

            show rt joy

            rt "Y'know, {w=0.3}sometimes I forget you have those frog powers n' all."

            jump ep2_seg1_roof


    label ep2_seg1_back:
        show rt o at bounce

        show ph at bounce

        no "The two kids skiddered around the building to the back."

        no "There was indeed a back door; {w=0.5}however when Phrog pulled on the handle, {w=0.3}it wouldn't budge."

        show ph bruh

        ph "locked. {w=0.3}figures."

        rt "Don't worry! {w=0.3}We'll use a-"

        $ ep2_choice2_disguise = False

        $ fail_skip = False

        menu:
            "Disguise!":
                $ ep2_choice2_disguise = True

                space ""

                ph ""

                ph "y'kno what."

                show ph smug

                ph "just go for it. {w=0.3}i wanna see what happens."

                rt "No c'mon this is gonna be super smart, {w=0.3}watch."

                show rt at bounce

                no "He knocks on the door."

                rt "EY EY. {w=0.3}It's the garbage man!!! {w=0.3}Here to eat your garbage!!!"

                show ph at Position(xpos=200)

                show rt at Position(xpos=500)

                with ease

                show chef bruh at right, flip with easeinright

                space ""

                chef "What the hell."

                $ fail_skip = True

                jump ep2_seg_end


            "Paperclip!":
                show rt smug at bounce

                no "He pulls out a paper clip."

                show rt at shake(rate=0.01,strength=2,loop=7)

                no "He jams it into the keyhole."

                no ""

                no "He just... {w=0.3}leaves it in there."

                no ""

                rt ""

                rt "Yeah, {w=0.3}I don't know how to do this lol."

                ph ""

                show img 2 fail

                $ _skipping = False

                space "Rollback to pick a different choice! (Press/hold backspace.)"

                $ renpy.pause(hard=True)


            "Gun!":
                show ph shock

                ph "what-{w=0.2}{nw}"

                show ph scared 2

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

                jump ep2_seg2_sneak


    label ep2_seg1_roof:
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

        if ep2_choice2_bomb == False:
            $ ep2_choice2_bomb = False
        else:
            $ ep2_choice2_bomb = True

        menu:
            "A Laser Cutter":
                show ph bruh

                show rt smug 2 at shake(rate=0.01,strength=5,loop=5)

                rt "EeeheheeheeeyeaAAAAHH."

                no "He slaps some wack lookin' device on the roof and it lasers a medium-size circular hole."

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

                ph "how are we getting- {w=0.4}{nw}"

                ph "oh he already jumped down."

                show ph bruh 2

                ph "welp."

                hide ph with easeoutbottom

                hide rt

                space ""

                jump ep2_seg2_office

            "A Fricken' Saw":
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

                show rt sad at shake(rate=1.00,strength=0,loop=1) with hpunch

                no "The saw snaps in half."

                rt "o"

                show img 2 fail

                $ _skipping = False

                space "Rollback to pick a different choice! (Press/hold backspace.)"

                $ renpy.pause(hard=True)

            "Bomb":
                $ ep2_choice2_bomb = True

                show rt joy at shake(rate=0.01,strength=1,loop=3)

                show ph bruh

                no "Rocktato drops a bomb at his feet."

                no ""

                no "It isn't lit."

                show ph bruh 2

                ph "it isn't lit, idiot."

                show ph bruh

                rt "Don't worry!"

                show rt happy at bounce

                no "He lights it with a match."

                ph ""

                show ph shock

                ph "wait, {w=0.3}this is a real bomb.."

                show rt happy 2 at bounce

                rt "Yeah!"

                ph ""

                rt ""

                show ph scared 2 with hpunch

                ph "shOULDN'T WE GET OUTTA HERE?"

                rt "Mm."

                show rt joy 2 at bounce

                rt "Nah."

                show ph scared

                ph "but..."

                ph "it says nuke on the side."

                show rt o

                rt "Oh-{w=0.1}{nw}"

                $ renpy.quit()


    label ep2_seg2_sneak:
        no "The two entered the door and found themselves in the kitchen."

        show ph o 2

        ph ""

        ph "holy cannoli it smells delicious in here."

        show rt o

        rt "Woah, {w=0.3}yeah-{w=0.3}{nw}"

        ph "psst get down."

        show ph at transform_easeout_offset(y=1280)

        show rt at transform_easeout_offset(y=1280)

        no "They ducked behind the counters and what nots."

        chef "What was that noise?"

        show chef neutral at right, flip with easeinright

        chef ""

        show chef think

        chef "Eh, {w=0.3}whatever."

        hide chef with easeoutright

        no "She leaves."

        ph ""

        show rt smug at transform_easein_offset(y=120)

        rt "Lol that worked?"

        show rt nervous

        chef "Actually..."

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

        ph "but you gotta be quick!"

        ph "if you don't do it in time or you select the wrong one, you'll get caught!"

        ph "but if you don't have the reflexes for this one, {w=0.3}that's okay!"

        ph "do you wanna skip this segment?"

        menu:
            "Yes":
                show ph joy at bounce

                ph "cool!"

                ph "i'll teleport you to the future in three... {w=1.0}two... {w=1.0}one...{nw}"

                jump ep2_seg2_aftersneak

            "No":
                show ph smug

                ph "ok then. {w=0.3}it's gaming time."

                rt "What."

            # TODO SNEAK SEG




        $ fail_skip = False

        label ep2_seg2_aftersneak:
            ph "let's gooo"

            # TODO AFTERSNEAK DIALOUGE


            menu:
                "{i}Sneak a Taste{/i}":
                    show rt nervous

                    rt ""

                    no "He dips his finger into the mixture and licks it."

                    show rt o

                    rt ""

                    show rt o at shake(rate=0.01,strength=3,loop=5),shake(rate=0.01,strength=6,loop=7), shake(rate=0.01,strength=20,loop=9)

                    no "He vaccuums the whole pot."

                    show ph bruh

                    ph "hey pipe down there c'mon-"

                    ph ""

                    show ph bruh 2

                    ph "seriously."

                    show rt exasperated

                    rt "Okay, c'mon. {w=0.3}It's so good."

                    ph "do you know how loud that was?"

                    ph "i'd be suprised if we didn't get-"

                    show ph o 2

                    ph ""

                    show ph o

                    ph "caught."

                    $ fail_skip = True

                    jump ep2_seg_end


                "{i}Don't{/i}":
                    rt ""

                    no "He exits the kitchen."

        jump ep2_seg3_hall


    label ep2_seg2_office:
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

        $ ep2_choice3_hack = False

        $ fail_skip = False

        menu:

            "Hack Computer Like SPY!":
                $ ep2_choice3_hack = True

                show rt proud at shake(rate=0.01,strength=5,loop="")

                rt "EHEHEEHE!"

                show ph scared

                no "He hops into the spinny chair and starts smashing the keyboard with his face."

                chef "What the hELL."

                $ fail_skip = True

                jump ep2_seg_end


            "Leave.":
                show rt sad

                rt "You're prolly right."

                show ph o 2 at phrog_goes_in_and_out_a_door(loop=1, where=450, otherwhere=1600)

                no "Phrog opened the door {w=0.7}and then quickly closed it."

                show rt bruh

                rt "What."

                show ph o

                ph "she's coming."

                show rt confused

                show ph at Position(xpos=450)

                rt "Wha-{w=0.1}{nw}"

                show ph at transform_easeout_offset(y=1280)

                show rt at transform_easeout_offset(y=1280)

                no "Phrog dragged Rocktato into a box."

                hide rt

                hide ph

                show chef happy at right, flip with easeinright

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

                ph "don't talk, {w=0.2}don't move, {w=0.2}don't do any of your classic adhd brain rocktato things."

                show ph think

                ph "can you do that?"

                show rt happy

                rt "Yeeeeeeeeeesssssssss.............."

                show ph o 2

                ph "not very reassuring but ok."

                ph "here we go."

                show getreadytext at truecenter, shake(rate=0.05,strength=1,loop=2) with dissolve

                pause 1.0

                hide getreadytext with dissolve

                no "" 

                # TODO OTHER SNEAKS EG

                jump ep2_seg3_hall


    label ep2_seg3_hall:
        hide chef

        hide rt

        hide ph

        show ph o 2 at Position(xpos=800) with easeinright

        show rt o at Position(xpos=1100) with easeinright

        no "The two found themselves in a hallway."

        if ep2_choice1_roof == True:
            no "describe hall"

        else:
            no "describe hall"

        show ph o 3

        ph "which door do we enter?"

        $ ep2_choice4_recipe = False
        $ ep2_choice4_storage = False
        $ ep2_choice4_restroom = False

        menu:
            "GO TO BATHROOM":
                $ ep2_choice4_restroom = True

                show rt smug

                show ph bruh

                rt ""

                ph ""

                rt ""

                ph ""

                ph "no"

                show img 2 fail

                $ _skipping = False

                space "Rollback to pick a different choice! (Press/hold backspace.)"

                $ renpy.pause(hard=True)


            "Storage Room":
                $ ep2_choice4_storage = True

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

                show ph bruh at Position(xpos=200) with easeinright

                show rt o at Position(xpos=500) with easeinright

                no "They walked into the storage room."

                no "I mean, {w=0.3}where else would they walk into?"

                no "It was just some shelves holding cookie dough or ingredients for cookie dough."

                rt "It could be in a corner or something. {w=0.3}Look around!"

                show rt at bounce

                show ph at bounce

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

                ph "WHEN BEAR GORGANGAS GOT TRAPPED IN A FREEZER WHAT DID HE DO?"

                rt "Phrog..."

                rt "He..."

                show chef bruh at Position(xpos=1100)

                rt "He started eating raw eggs..."

                show ph scared 2 at shake(rate=0.02,strength=50,loop=5) with hpunch

                show chef bruh at transform_easein_pos(xstart=2000, xend=1100, time=5.0), flip

                ph "OH GOD NOOO WE'RE GONNA HAVE TO START EATING RAW EGGS."

                ph "NOOOOOo"

                chef ""

                show chef bruh at right with ease

                chef "You kids alright?"

                ph "OH THANK YOU {nw}"

                show ph shock

                extend "Oh."

                jump ep2_seg_end


            "Lol Secret Recipe":
                $ ep2_choice4_recipe = True

                ph "o true."

                ph "makes the most sense, lol."

                hide rt

                hide ph

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

                show rt sad

                no "WRONG PASSCODE."

                show ph bruh 2

                ph "lol seriously."

                ph "here let me try."

                show ph smug

                ph "8...{w=0.5}0...{w=0.5}0...{w=0.5}8-{nw}"

                show rt mad with hpunch

                rt "PHROOOOOG!!!"

                rt "That's ina- {w=0.5}inappropRIATE!!!!"

                show ph bruh

                ph "clearly it is cus it didn't work."

                no "WRONG PASSCODE."

                no "1 TRY LEFT."

                show rt confused

                rt "One try left until what?"

                show rt joy

                rt "Ooo! {w=0.3}I hope the building explodes!"

                show ph bruh 2

                ph "what."

                rt "Let me do the last one!"


                $ ep2_a_in_pass = False

                $ ep2_passcode = renpy.input("{b}Guess the passcode:{/b}",  length=4, allow="1234567890b")

                if "bbbb" in ep2_passcode:
                    show ph shock

                    ph ""

                    ph "how the heck did you do that?"

                    ph "wh.."

                    ph "what???"

                    ph "it's just b's,,,,,"

                    ph ""

                elif ep2_passcode == "b":
                    show ph shock

                    ph ""

                    ph "what does this mean..."

                    ph "it's just b,,,"


                elif "b" in ep2_passcode:
                    show ph o

                    ph "how the heck did you get a b in there?"

                    ph "it's.."

                    ph "it's a number pad..."

                elif "8008" in ep2_passcode:
                    show ph bruh

                    ph "srsly. {w=0.3}you stole my joke?"

                    ph "uncool.."

                elif "1234" in ep2_passcode:
                    show ph with hpunch

                    ph "you seRIOUSLY THINK-"

                elif "6969" in ep2_passcode:
                    show rt smug

                    rt ""

                    show ph smug

                    ph ""

                    ph "yeahhh now that's what i'm talking about."

                elif ep2_passcode == "":
                    rt ""

                    show ph bruh

                    ph ""

                    rt ""

                    ph ""

                    show ph think 2

                    ph "are you going to type anything?"

                    rt ""

                elif len(ep2_passcode) < 4:
                    ph "not 4 digits but ok."

                    show ph joy at bounce

                    ph "you tried!"

                    ph "not all of us can count and that's ok!"

                else:
                    no ""



                no "WRONG PASSCODE."

                show ph o 2

                show rt o

                no "BEEEEP {w=0.5}BEEEEP {w=0.5}BEEEEP!!"

                no "WAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHH!!"

                no "The place started flashing red and not red."

                no "The alarm was going beep beep, wahhh, and other stuff like that!"

                show chef angry at right, flip with easeinright

                chef "WHAT THE HELL IS GOIN' ON HERE-"

                jump ep2_seg_end


    label ep2_seg_end:
        show ph o 2 at Position(xpos=200)

        if ep2_choice2_disguise == False:
            show rt sad at Position(xpos=500)
        else:
            show rt at Position(xpos=500)

        show chef bruh at right, flip

        with ease

        chef ""

        chef "Rocktato."

        chef "And the frog kid."

        rt "You..."

        rt ""

        if ep2_choice2_disguise == False:
            show rt nervous at bounce

        rt "What's your name again?"

        chef ""

        show chef bruh 2

        chef "What are you doing here."

        if ep2_choice2_disguise == True:
            chef "And why are you dressed in the garbage man's outfit."

            chef "There hasn't been a garbage man since the... {w=1.0}incident."

            chef "That's disrespectful."

            rt "Oh. Sorry."

            rt "I'll just..."

            show rt sad

            no ""

            jump ep2_seg_fail_skip


        if ep2_choice3_hack == True:
            show chef what

            chef "And why are you..."

            chef "Why..."

            chef "Are you okay????"

        show chef bruh

        rt ""

        ph ""

        label ep2_seg_fail_skip:
            if ep2_choice1_walk == True or fail_skip == True:
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

        if ep2_choice3_hack == True:
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


        show ph at Position(xpos=450)

        show rt at Position(xpos=850)

        hide chef

        show bg beegcity night

        ph "well..."

        ph "i think we can both can say..."

        ph "that was a day that happened..."

        if ep2_choice2_bomb == True:
            show ph o at bounce

            ph "i think i died!"

            show ph joy

            ph "lol"

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

        ph ""

        show ph tired

        ph ""

        show ph tired 2

        ph "man.."

        ph "i'm stupid."

        rt ""

        rt "Yeah, {w=0.3}but,"

        show rt nervous

        rt "like... {w=0.3}I'm stupid too!"

        rt "And... {w=0.3}I guess..."

        show rt joy 2 at bounce

        rt "we can be better!"

        show rt nervous

        rt "And try to be... {w=0.3}like... {w=0.3}less... {w=0.3}stupid??{w=0.3}?"

        show ph o 2

        ph ""

        show ph thankful 2

        ph "yeah, {w=0.3}somethin' like that."

        show ph bruh 2

        ph "we gotta find you a new favorite food to eat tho."

        show rt cry 2 at shake(rate=0.01,strength=5,loop=8) with hpunch

        rt "Oh noooOOOOO!!!"

        if persistent.episode_fin == 1:
            $ persistent.episode_fin = 2

        $ persistent.mainmenu_img = 3
