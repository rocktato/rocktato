label start:

    $ persistent.mainmenu_img = 1
    $ persistent.saveepisode_img = 1

    stop music fadeout 1.0


    # play sound "audio/fx/windy.ogg" loop
    #
    # show bg lightblue
    #
    # show obj 1 rumboy at fast_shaking
    #
    # "{w=5.0}{size=-5}(LEFT CLICK or press SPACE to continue!){/size}"
    #
    # play sound "audio/fx/crash.ogg"
    #
    # show cg 1 rumboy crashed at hpunch
    #
    # hide bg lightblue
    #
    # hide obj
    #
    #
    # ""
    #
    # Character("Random Citizen 1", size=25, callback=no_blip) "OH MY GOD!!!"
    #
    # Character("Random Citizen 2", size=25, callback=no_blip) "A GIANT RUMBOY HAS FALLEN FROM THE SKY!!!"
    #
    # Character("Random Citizen 3", size=25, callback=no_blip) "MY TAX DOLLARS WENT INTO THAT FOUNTAIN NOO!!"
    #
    # Character("Random Citizen 3.5", size=23, callback=no_blip) "AHHHHHHHHHHHHHH SCREAMING!!"
    #
    # rt "No way..."
    #
    #
    # play sound "audio/fx/button.ogg"
    #
    # show cg 1 rumboy crashed freezeframe with hpunch
    #
    # rt "Well this is me."
    #
    # rt "You're probably wondering how I got into this situation."
    #
    # rt "Oh, {w=0.3}this is narration by the way."


    show bg black

    # with dissolve
    #
    # hide cg 1 rumboy crashed freezeframe

    rt_nar_que "So..."

    rt_nar_que "You're probably wondering what I'm doing here."

    rt_nar_que "Let me just start from the beginning."

    rt_nar_que "Today began just like every other morning."

    # rt "The air was crisp with whatever air has."

    rt_nar_que "I got out of bed with naive optimism, {w=0.3}wondering what adventures awaited me today."

    rt_nar_que "Then, I realized that I don't even have a bed?? {w}I just have a gigantic bean bag chair-type?? {w}That I sleep on??"

    rt_nar_que "But whatever, {w=0.3}I'm used to the back pain."

    rt_nar_que "Okay, okay, {w=0.3}fine."

    rt_nar_que "I'll stay on topic."


    play music "audio/music/gmoroning.mp3" loop

    show bg rtcave

    show rt happy 2

    with dissolve

    show p he they at Position(xpos=500, ypos=450) with dissolve

    rt_nar "This is me, {w=0.3}Rocktato!"

    rt_nar "(Don't ask where the name comes from.)"

    hide p he they with dissolve

    rt_nar "I'm a cool superhero that does things!"

    rt_nar "I think?"

    show rt troubled

    rt_nar "I don't really know how to describe myself, {w=0.2}haha."

    show rt happy

    rt_nar "So anyway, I got out of 'bed', right?"

    rt_nar "I put on this killer cape on my shoulders, {w=0.3}I brushed and floofed up my hair, {w=0.3}and I stuffed some good ol' cookie dough in my mouth for breakfast."

    show rt joy 2 at bounce

    rt_nar "Then, I went to greet my best friend, {w=0.3}Mr. Rock, good morning!"

    rt_nar "Love that guy."

    # rt "You know that guy, right? {w}What a good guy..."

    show rt joy

    # rt "I remember that one time when I greeted him good morning yesterday!"

    rt_nar "I looked at his bed, {w=0.3}yeah?"

    show rt exasperated

    play sound "audio/fx/cough.ogg"

    stop music

    rt_nar "Then I asked myself why HE got a bed but I didn't."

    show rt joy

    rt_nar "Oh yeah he was gone too."

    rt_nar "I feel like I didn't do that right, wait."


    play sound "audio/fx/punch.ogg"

    show rt o with hpunch

    rt_nar "He was GONE!!!"

    show rt cry

    rt_nar "Just poof! Vanished!!"

    rt_nar "No note or anything, {w=0.3}just a pile of uneaten rock food. {w}Which also happens to just be rocks."

    show rt o

    rt_nar "Did you know rocks are cannibals?"

    show rt joy 2 at bounce

    rt_nar "Fun fact!"

    rt_nar "Anyway, {w=0.3}I went around my cave calling out for him."

    show rt sad 2 at shake(rate=0.005,strength=1,loop=7)

    rt "MR. ROCK??? Do you hear me??? Make a noise or something!!"

    rt_nar "Those were the words that came out of my mouth."

    show rt troubled

    rt_nar "However, I got no response."

    rt_nar "So I thought that maybe... {w=0.3}he'd be out there somewhere in the city!"

    show fx black with dissolve

    rt_nar "And thus, {w=0.3}I began {w=0.5}the search for Mr. Rock!"

    hide fx black


    play sound "audio/fx/woosh.ogg"

    show bg beegcity

    queue sound "audio/fx/step.ogg" loop

    play amb "audio/amb/city.ogg" loop

    show rt joy 2 at bouncing

    rt_nar "So there I was. Walking through the streets of Beeg City."

    rt_nar "I mean you know the place right?"

    rt_nar "It's beeg!!! {w=0.3}With beeg towers and beeg money!! {w=0.3}And beeg people with awesome superpowers."

    # rt "Well, {w=0.3}some of them are beeg, {w=0.3}but not all of them. {w}I just meant beeg as in status."
    #
    # rt "They're really cool people is what I'm trying to say!"

    rt_nar "There are so many sections too!! {w=0.3}There's a little something for everyone!"

    show rt sad 2 at bouncing

    rt_nar "The bad part about that is that Mr. Rock could have been anywhere!!"

    show rt troubled

    rt_nar "I racked my brain, thinking about where he could possibly be."

    rt_nar "I have no idea what he does when I'm not around, tbh."

    rt_nar "In my defense, {w=0.3}he's really hard to talk to."

    rt_nar "I decided that I was gonna need some help with this."


    play sound "audio/fx/woosh.ogg"

    stop amb

    show bg gamerbar

    show rt happy 2 at bounce

    rt "AYO! {w=0.2}WHAT'S POPPin'?"

    rt "GIN!!!"

    gin "GASP!!!"

    show bg at Position(xpos=480)

    show rt happy 2 at Position(xpos=450)

    with ease

    show gin evil 2 at flip, Position(xpos=800) with easeinbottom

    show p she they at Position(xpos=1020, ypos=300) with dissolve

    gin "If it isn't my favorite piss baby!!!!"

    hide p she they with dissolve

    rt_nar "Meet Gin, {w=0.2}the ultimate heroic cowboy!"

    rt_nar "(Not ultimate like Danganronpa, shut up.)"

    rt_nar "They do cool stuff like saving the city from monsters with cool cowboy powers!"

    rt_nar "Or saving babies from villains!"

    rt_nar "Or saving banks from robbers!"

    show rt sad

    rt_nar "Or saving me whenever I get stuck in a tree."

    show rt joy 2 at bounce

    rt_nar "I ran up and hugged her."

    rt_nar "Her hugs are always the best."

    show gin o at flip, bounce

    gin "What're ya doin' here??"

    show rt o

    rt "OH!"

    rt "I'm looking for Mr. Rock!"

    rt "And I realized! {w=0.3}I'm really bad at looking for things!"

    show rt sad

    rt "Can you help me find him?"

    show gin evil at flip, bounce

    gin "Eyah, {w=0.3}sure thing bud!"

    gin "Lemme jus' finish this drink!"

    show gin at flip, shake(0.03, 3.4, 3)

    play sound "audio/fx/slurp.ogg"

    gin "SLRLSRPPPPPPPSPPSp"

    show rt o

    rt "Giinnn??"

    rt "Can I get some????"

    show gin bruh

    gin "Mmmm... {w=0.3} just a lil' sippy sipp."

    gin "This stuff isn't good for growin' kiddos like you."

    show rt mad at bounce

    rt "Hey! {w=0.2}Don't baby me!"

    show gin nervous

    gin "Alright, {w=0.3}alright."

    play sound "audio/fx/sip.ogg"

    show gin evil at flip, bounce

    show rt joy

    no "Gin allowed Rocktato to have a tiiiiiny sip from her can of Mountain Dew G Fuel."

    show rt joy 2 at bounce

    rt "Mmmm {w=0.3}thank youuu!!"

    show rt happy 2

    rt "Now, {w=0.3}the quest!"

    show rt sad 2

    rt "Where do we go?"

    show gin o at flip, bounce

    gin "Ah dunno, {w=0.3}where do {i}you{/i} wanna go?"

    show rt o at bounce

    rt "I dunno, {w=0.3}where do YOU wanna go?"

    show gin o at bounce

    gin "Ah dunno, {w=0.3}where do {i}you{/i} wanna go?"

    show rt o at bounce

    rt "I dunno, {w=0.3}where do YOU wanna go?"

    show gin think at flip

    gin "Eeeyeah, {w=0.2}enough of that."

    show gin happy

    gin "How about we rob a bank!"

    show rt happy at bounce

    rt "Hmmm maybe!"

    rt "Not today tho!"

    show gin think

    gin "Aight uhhh, {w=0.3}what about the central park?"

    show gin evil

    gin "That sounds like a good first place to check!"

    gin "Thats's where basically everythin' in this city happens!"

    show rt joy 2

    rt "Wow! {w=0.2}You're smart!"

    rt "Let's go!"



    play sound "audio/fx/woosh.ogg"

    play amb "audio/amb/park.ogg" loop

    show bg citypark at center

    show rt joy

    show gin evil

    rt_nar "We arrived at the center of the beloved Beeg City."

    rt_nar "There were kids eating ice cream and playing insert any sport game here."

    rt_nar "There were bird people perched on the trees screaming."

    rt_nar "And there were many heroes just going about and stuff."

    rt_nar "It's pretty hard to describe the scene, {w=0.3}you just had to see it."

    # rt_nar "The best we can do is show this crappy MS Paint background."
    #
    # rt_nar "Sorry!"

    rt_nar "I stood on top of the center fountain calling out."

    show rt hurt at bounce

    rt "Mr. Rock???"

    rt "Mr. Rock!!!"

    show rt sad 2

    rt "Ah, {w=0.3}do you see him anywhere??"

    show gin o

    gin "Nah."

    show rt o

    rt "Mmmmmaybe... {w=0.3}he's hidin' under a pebble!"

    play sound "audio/fx/search.ogg"

    show rt at Position(ypos=900), shake(0.03, 2.3, 10) with ease

    rt_nar "I proceeded to start looking under pebbles."

    show gin happy

    gin "Okayyy.. {w=0.3}there are faster ways of doin' this, buddy."

    show rt at Position(ypos=720) with ease

    gin "Check this out."

    play sound "audio/fx/summon.ogg"

    show gin at bounce

    rt_nar "She summoned out her cowboy whip {w=0.3}and..."

    gin "TORNADO!!! {w=0.2}{nw}"

    show gin evil at flipper

    play sound "audio/fx/wooshing.ogg" loop

    play sound2 "audio/fx/windy.ogg" loop

    extend "WHIP!!!"

    rt_nar "They spun around and around, creating huge gusts of wind that pushed away from them."

    rt_nar "I'm pretty sure tornadoes are supposed to suck? {w}Not... {w=0.5}un{w=0.4}suck?{w=0.4}?"

    rt_nar "But it's a pretty cool move with a pretty cool name, {w=0.3}right?"

    hide gin

    stop sound

    stop sound2

    show gin evil 2 at transform_zoom, Position(xpos=565), bounce

    gin "Booyah!"

    gin "No stone left unturned!"

    show gin wink

    gin "Literally!"

    show rt sparkle

    rt "Woa {w=0.4}that's so cool,,"

    show rt sad

    rt "But there's no Mr. Roc ,k,"

    gin "How about we try somewhere else?"

    show gin mm

    gin "Also, {w=0.2}I may've knocked over a few.. {w=0.3}kids, {w=0.5}hot dog stands..."

    show gin happy at flip

    gin "Let's get outta here before I get seen!"


    play amb "audio/amb/city.ogg" loop

    play sound "audio/fx/woosh.ogg"

    show bg beegcity

    queue sound "audio/fx/step.ogg" loop

    show rt at bouncing

    show gin at bouncing

    rt_nar "We then started kinda just.. {w=0.3}walking."

    rt_nar "I realized that even with Gin's expert hero skills {w=0.3}and my expert skill in just kinda existing, {w=0.3}we still wouldn't be able to find this guy."

    rt_nar "We needed more help."

    show rt proud

    rt_nar "So.. {w=0.3}I decided to recruit the BEEG guns on our little adventure."


    stop amb

    stop sound

    play sound "audio/fx/woosh.ogg"

    hide rt

    hide gin

    show bg bl lobby

    ""

    show gin o at Position(xpos=200)

    show rt proud at Position(xpos=500)

    with easeinbottom

    bl "Why!!!"

    show bl happy at flip, Position(xpos=1000) with easeinright

    extend " If it isn't Rocktato and Gin!!!"

    show p he him at Position(xpos=900, ypos=270) with dissolve

    bl "Pleasant seeing the two of you here!!!"

    hide p he him with dissolve

    show rt happy 2 at bounce

    rt "BLAIRIC!!!"

    show gin evil 2 at bounce

    gin "Eyy Blairic, {w=0.3}my maaaaannnnnn."

    rt_nar "This is Blairic! {w=0.3}The skeleton billionaire!"

    rt_nar "Some things about him?"

    rt_nar "He's really professional and businessmanlike... {w}uh... {w=0.3}he runs this meat factory!"

    rt_nar "I think his superpower is being rich."

    rt_nar "And being alive."

    show bl o at flip, bounce

    bl "What are you children doing here?"

    show rt o

    rt "Mr. Rock is missing and we're trying to find him!!"

    show bl happy 2

    bl "Sounds like fun, kid!"

    show bl takemeouttodinnerfirst

    bl "You did not rob a bank, right?"

    show rt joy at bounce

    rt "Nope but we considered it!!"

    show bl disturbed

    bl "Wh-"

    bl "Why?"

    show rt o

    rt "Anyway, {w=0.3}we could really use your help with this thing!!"

    show bl think

    bl "Hm..."

    bl "I am not sure if I have the time for a little escapade right now."

    show rt cry at bounce

    rt "PLeeeeeaaaase????"

    show gin thankful

    gin "Ey c'mon, {w=0.3}ya busy man."

    gin "It'll be funny!"

    # show rt o
    #
    # rt "You mean fun right?"
    #
    # show gin o
    #
    # gin "No, I mean funny."
    #
    # rt "O"

    bl "Hrmm.."

    rt_nar "The business guy thought for a bit, {w=0.3}before finally giving in."

    show bl happy 3 at flip, bounce

    bl "Okay, alright. {w=0.3}Sure!!!"

    show rt joy 2

    show gin evil

    rt "Yayy!"

    show rt o

    rt "You have any idea where he could be? {w=0.3}Or how to find him?"

    show bl happy

    bl "No!"

    show rt sad

    bl "I am a rich man, {w=0.3}not a smart man."

    bl "What would you suggest?"

    show rt o at bounce

    rt "GASP!"

    show rt happy 2 at shake(rate=0.01,strength=3,loop=7)

    rt "MCDONDALS!!!!!!"

    show bl think

    bl "Why would he be at a McDonda{w=0.1}{nw}"


    play sound "audio/fx/woosh.ogg"

    show bg mcdondals

    show bl bruh

    show rt joy

    show gin evil

    ""

    show rt joy 2

    rt "Thanks for paying Blairic!"

    rt "I don't have any money."

    rt "Haha I'm a child."

    play sound "audio/fx/vacuum.ogg"

    show rt joy 2 at shake(rate=0.01,strength=5,loop=75)

    ""

    rt "Man, {w=0.3}I'm just in love with these!!!"

    rt "If I'm ever gonna marry, {w=0.3}it's gotta be the McDondals 6 pc. Chicken Nuggets!"

    show gin evil 2 at bounce

    gin "Hey! {w=0.3}Skeleboy! {w=0.3}Ya gonna eat any?"

    show bl bruh 2 at flip, bounce

    bl "I will pass, Gin."

    bl "I do not have a digestive system."

    show bl sad

    bl "I am a skeleton."

    show gin o at bounce

    ""

    gin "O."

    gin "Right..."

    show rt sad 2 at bounce

    rt "Too bad Mr. Rock wasn't hidden in the ball pit."

    show gin smug

    gin "Yea, {w=0.3}I could've SWORN I saw him in there."

    gin "But oh well!"

    show gin evil 2

    gin "At least I got to play in a ball pit for like... {w=0.3}the first time in forever haha!!"

    show bl nervous at flip, bounce

    bl "This uh..."

    bl "This does not really feel like a proper search."

    show bl bruh 2

    bl "You kids just{w=0.3} amused yourselves in the McDonDals play place for an hour..."

    show gin happy at bounce

    gin "Aha..."

    gin "Yeah.."

    ""

    play sound "audio/fx/punch.ogg"

    play sound2 "audio/fx/foodtray.ogg"

    show rt mad with hpunch

    show gin o

    show bl o

    rt_nar "I suddenly stood up and AGGRESSIVELY threw my food tray onto the ground!"

    rt_nar "(Then I picked it up and properly put my trash and tray at the correct places.)"

    rt_nar "(Fast food workers don't get paid enough to deal with your messes.)"

    show rt mad at shake(rate=0.01,strength=5,loop=5)

    rt "For hecks sake!!!"

    rt "Blairic is right!!!"

    rt "We gotta get out there and SEARCH!!"

    show gin angey

    gin "Ey, {w=0.3}can I finish my drink first?"

    show rt at shake(0.03, 3, 7)

    rt "There's NO! {w=0.3}TIME!"

    play sound2 "audio/fx/running.ogg"

    hide rt

    with easeoutleft

    play sound "audio/fx/shopdoor.ogg"

    hide gin with easeoutleft

    gin "WAHHHHHhhhh!"

    ""


    show fx black with dissolve

    ""

    rt_nar "The last place that I went to was the swamp."

    play sound "audio/fx/woosh.ogg"

    play amb "audio/amb/swamp.ogg" loop

    hide fx

    show bg swamp

    show bl happy 2 at reverse_flip, Position(xpos=100)

    show gin o at Position(xpos=400)

    show rt happy at Position(xpos=700)

    show ph reallymad at flip, Position(xpos=1100)

    rt "Which is right here!!"

    rt "And that's!!! {w=0.3}The reason why I'm here!"

    rt "Gettin' the whole gang together yeaaaa!"

    show rt o at bounce

    rt "Have you seen Mr. Rock around-"

    ph "was it really necessary"

    show ph reallymad at flip, shake(0.03, 5, 7)

    ph "to tell me that ENTIRE STORY"

    show ph reallymad at flip, shake(0.03, 6, 8)

    ph "of you running around in a city I LITERALLY LIVE IN"

    show ph reallymad at flip, shake(0.03, 7, 9)

    ph "and meeting people that I ALREADY KNOW"

    show ph reallymad 2 at flip, shake(0.03, 8, 10)

    ph "BECAUSE WE ARE LITERALLY IN THE SAME FRIEND GROUP AND THEY'RE THE ONLY PEOPLE I'M WILLING TO TALK TO?"

    show ph reallymad 2 at flip, shake(0.03, 10, 11)

    ph "WHY DID YOU WASTE FRICKin' {w=0.3}TWO HOURS OF MY PRECIOUS TIME??"

    ph "JUST FOR A POINTLESS SEARCH???"

    ph "MR. ROCK IS LITERALLY-"

    play sound "audio/fx/explosion.ogg"

    show ph scared 2 at flip, bounce

    show bl gollygee at bounce

    show gin woah at bounce

    with hpunch

    ph "JESUS CHRIST!!"

    show rt happy 2

    rt "Silly Phrog! {w=0.3}Mr. Rock isn't whoever that is! He's Mr. Rock!"

    gin "Kiddo, {w=0.3}look."

    show rt sad 2

    rt_nar ""

    rt "Oh."


    # play sound "audio/fx/sniff.ogg"
    #
    # no "Rocktato suddenly got up and started sniffing."
    #
    # show gin o
    #
    # gin "WoAH!"
    #
    # show ph bruh 2 at bounce
    #
    # ph "ew what are you doing?"
    #
    # show rt disgusted
    #
    # rt "{i}Do you smell that????{/i}"
    #
    # ph "no{w=0.2}{nw}"
    #
    # show ph bruh
    #
    # show gin sad
    #
    # rt "{i}It's the smell of {b}villainy.{/b}{/i}"
    #
    # play sound "audio/fx/suspense.ogg"
    #
    # show rt disgusted at shake(rate=0.01,strength=15,loop=5) with hpunch
    #
    # no "Suddenly, {w=0.3}the air turned gray."
    #
    # no "Something beeg was in the sky."
    #
    # no "It casted a shadow over the whole park."
    #
    # no "All of the civilians were panicking and running away."
    #
    # no "Rocktato and the crew stood on guard."
    #
    # hide rt
    #
    # hide ph
    #
    # hide gin
    #
    # show bg lightblue
    #
    # play sound "audio/fx/windy.ogg" loop
    #
    # show obj 1 rumboy at fast_shaking
    #
    # with dissolve
    #
    # ""
    #
    # play sound "audio/fx/crash.ogg"
    #
    # show cg 1 rumboy crashed at hpunch
    #
    # hide obj
    #
    # hide bg
    #
    # ""
    #
    # Character("Random Citizen 1", size=25, callback=no_blip) "OH MY GOD!!!"
    #
    # Character("Random Citizen 2", size=25, callback=no_blip) "A GIANT RUMBOY HAS FALLEN FROM THE SKY!!!"
    #
    # Character("Random Citizen 3", size=25, callback=no_blip) "MY TAX DOLLARS WENT INTO THAT FOUNTAIN NOO!!"
    #
    # Character("Random Citizen 3.5", size=23, callback=no_blip) "AHHHHHHHHHHHHHH SCREAMING"
    #
    # rt "No way..."
    #
    # show bg 1 rumboy crashed
    #
    # hide cg 1 rumboy crashed
    #
    # hide rt
    #
    # with dissolve

    show rt waah

    rt "Wait, iS thAT-"

    hide bl

    hide gin

    hide rt

    hide ph

    with dissolve

    wiz_que "..."

    wiz_yell_que "NYEHEHEHEH..."

    play sound "audio/fx/slidewhistleup.ogg"

    show wiz evil 2 at center, Position(ypos=50) with easeinbottom

    wiz_yell_que "IT IS I, {w=0.3}WIZPOTATo!!!"

    show p he him at Position(xpos=400, ypos=270) with dissolve

    wiz_yell "WAIT CRAP!!! {w=0.3}I MISSED!!!!!"

    play sound "audio/fx/squeak.ogg"

    show wiz bruh at center, Position(ypos=200) with ease

    wiz "uhhhhhhhhh {w=0.3}wait one sec..."

    play sound "audio/fx/squeak.ogg"

    show wiz bruh at center, Position(ypos=300) with ease

    pause 1.0

    play sound "audio/fx/squeak.ogg"

    show wiz bruh at center, Position(ypos=500) with ease

    pause 1.0

    play sound "audio/fx/squeak.ogg"

    show wiz bruh at center, Position(ypos=800) with ease

    pause 0.5

    play sound "audio/fx/squeak.ogg"

    show wiz bruh at center, Position(ypos=605) with ease

    pause 1.0

    show wiz sus 2 at center, Position(ypos=605)

    wiz "okay... {w=0.3}THERE we go..."

    hide p he him with dissolve

    show wiz sad 2 at center, Position(ypos=605)

    wiz "okay uhh..."

    wiz "it is I, Wizpotato... the uh.."

    play sound "audio/fx/punch.ogg"

    show wiz evil 2 with hpunch

    wiz_yell "THE GREATEST SUPERVILLAIN TO EVER..."

    show wiz sad 2

    wiz "uh...{w=0.3}{nw}"

    play sound "audio/fx/punch.ogg"

    show wiz evil 3 with hpunch

    wiz_yell "YEAH!!!!!!!!! !!!!!!!!!!!! !!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!"

    # no "A bunch of the heroes that were there walked away, disappointed."
    #
    # show wiz bruh
    #
    # Character("Random Hero 1", size=31, callback=no_blip) "Are you kiddin' me?? {w=0.3}THIS GUY AGAIN?!"
    #
    # Character("Random Citizen 3", size=25, callback=no_blip) "MY TAX DOLLARS WERE WASTED FOR THIS????"

    rt "GASP!!!!!!"

    show wiz evil at Position(xpos=400) with ease

    show rt disgusted at Position(xpos=900) with easeinbottom

    rt "WIZPOTATO!!!!"

    rt "What are you doing here.."

    # rt "I knew it was you."
    #
    # rt "I could smell you from miles away!!!"

    show ph scared 2 at flip, Position(xpos=1200) with easeinbottom

    ph "DUDE WHAT THE HELL MY SWAMP!"

    hide ph with easeoutbottom

    # show wiz sus 2
    #
    # wiz "OKay, "
    #
    # play sound "audio/fx/punch.ogg"
    #
    # show wiz angey 2 with hpunch
    #
    # extend "WEIRD."

    show wiz evil 3 at bounce

    wiz "It is quite convenient that you are here!!!"

    show wiz evil 2 at shake(rate=0.01,strength=10,loop=2)

    wiz_yell "MY DEAR RIVAL..."

    wiz_yell "IT SEEMS IT HAS BEEN FATED FOR US TO{w=0.3}{nw}"

    play sound "audio/fx/punch.ogg"

    show rt mad at shake(rate=0.01,strength=10,loop=2) with hpunch

    rt "SHUT UP!!!!!!!!"

    show rt sad 2

    rt "We just wanted to look for Mr. Rock, man."

    show rt hurt at shake(rate=0.01,strength=10,loop=2) with hpunch

    rt "HOLD ON!!!!"

    rt "I BET YOU MUST'VE TAKEN HIM, {w=0.3}HRMM????"

    show wiz sus 2

    ""

    wiz "what"

    wiz "What are you talking about????"

    show rt mad

    rt "OH, YOU {i}KNOW{/i} WHAT I'M TALKING ABOUT!!!!"

    wiz "no????{w=0.5}?{nw}"

    show rt smug at bounce

    rt "Ooooo, {w=0.3}I'm gonna beat you up so bad!!!"

    ph "rocktato wait!"

    show rt bruh

    show ph bruh 2 at flip, Position(xpos=1150) with easeinbottom

    ph "ok first of all, {w=0.3}{nw}"

    show ph reallymad 2 at flip

    extend "SCREW YOU!!"

    show ph happy

    ph "second of all,"

    ph "if you enter battle, {w=0.1}you won't be able to save or rollback to anything before the sequence or after any decisions."

    ph "i'd recommend saving now!"

    show ph bruh at flip, Position(xpos=1140)

    ph "i mean, {w=0.3}i do realize now how your chances of dying are slim..."

    ph "but y'kno, {w=0.3}just in case..."

    show ph happy at flip, Position(xpos=1140), bounce

    ph "it's good practice!"

    show rt sad 2

    rt "Phrog, {w=0.1}what does any of that mean?"

    show ph bruh at flip, Position(xpos=1140)

    rt "What do you mean by saving and rollback???"

    show rt confused

    rt "What, are we in a GAME or something?"

    show rt joy at bounce

    rt "That's a ridiculous!"

    show ph bruh 2 at flip, Position(xpos=1140)

    ph "oKAY BATTLE STARTS NOW!"

    $ renpy.block_rollback()

    $ saveable = False


    show rt fight idle

    show wiz fight idle

    play music "audio/music/too much effort for a one off rocktato joke but whatever lol.mp3"

    show fx battlestart at truecenter, shake(rate=0.05,strength=1,loop=2) with dissolve

    pause 1.0

    hide fx battlestart with dissolve


    $ chara_healths = [ 100, 100 ]
    $ chara_maxhealths = [ 100, 100 ]
    $ chara_hppositions = [ (200, 490), (700, 490) ]
    show screen battle_health

    $ moves = 0
    $ slaps = 0
    $ stomps = 0
    $ defends = 0

    if persistent.episode_fin >= 1:
        $ choice_screen_type = "choice"

        ph "tato, you know how to fight (i mean they teach this stuff in elementary lol) but do you want a reminder anyway?"

        menu:
            "Yes please!":
                $ renpy.block_rollback()
                pass
            "Shut up Phrog!":
                $ renpy.block_rollback()

                ph "jeez ok."

                hide ph

                ""

                rt "Okay, it's go time baby!"

                $ ep1_skiptut2 = True
                jump ep1_battle1

    $ ep1_skiptut2 = False

    ph "okay tato, {w=0.3}lemme give ya a rl quick run down."

    ph "all ya gotta do is click the buttons and hope it's the correct option."

    show rt o

    rt "I don't know why you said those words at me but thanks!"

    ph "b."

    hide ph

    pause 1.0

    show rt fight idle

    rt_nar "{i}Alright, so what are my options?{/i}"

    rt_nar "{i}Italics means thinking, by the way.{/i}"

    show rt joy 2 at bounce

    rt_nar "{i}Fun fact!{/i}"

    label ep1_battle1:

        show rt fight idle

        $ choice_screen_type = "fight_choice"

        if moves == 0 and ep1_skiptut2 == False:
            rt_nar "{i}Okay, so I can either punch him, which will hurt a bunch!!!{/i}"
            rt_nar "{i}Ah, but it might hurt me too though. {w}I'm a sensitive boy :,<.{/i}"
            rt_nar "{i}I can stomp him into the ground too, which would be funny.{/i}"
            rt_nar "{i}Or... I can defend!!! {w=0.3}So I won't get too beeg of a hurt myself!{/i}"

            rt_nar "{i}GO CHOOSE,  {w=0.1}ME!{/i}"

        elif moves == 5:
            show gin evil 2 at flip, Position(xpos=1170) with easeinbottom

            gin "Hey Rocktato!!! You should use your s e c r e t move!"

            rt "Oh... YEAH!!"

            rt "Thanks Gin!!!"

            gin "JEez kid, there's barely any room in here!"

            hide gin with easeoutbottom

        elif moves == 9:
            show ph bruh at flip, Position(xpos=1140) with easeinbottom

            ph "rocktato, {w=0.1}i'm boooooored. {w=0.3}can you please transform already."

            hide ph with easeoutbottom

        elif moves == 11:
            show ph bruh at flip, Position(xpos=1140) with easeinbottom

            ph "rocktato pleaaaaseeee...."

            hide ph with easeoutbottom

        elif moves == 13:
            show ph bruh at flip, Position(xpos=1140) with easeinbottom

            ph "hughgugbgugghugbu."
            hide ph with easeoutbottom

        elif moves == 50:
            # if persistent.phrog_pisser == True and persistent.phrog_vaultbreaker:
            #     ph "I'm not going to crash the game again."
            #
            #     ph "I think.."
            #
            #     ph "Oh! {w=0.3}I'll just teleport you to the transformation sequence!"
            #
            #     ph "Problem solved!"
            #
            #     jump ep1_transform

            if persistent.phrog_pisser == True:
                ph "Yeah ok i'm not gonna give you that dialogue again or new dialogue. {w=0.3}if you don't transform, i'll kill you and rocktato again."
                rt "Wait what-{w=0.1}{nw}"

            else:
                ph "Wow."

                ph "You're a real persistent one, huh?"

        elif moves == 51:
            if persistent.phrog_pisser == True:
                $ persistent._clear(progress=True)
                $ deletefiles()
                $ persistent.phrog_pisser = True

                $ renpy.quit()

        elif moves == 53:
            ph "ya alright."

            ph "if you keep doing this."

            ph "{b}I'm gonna end you.{\b}"

            ph "not just Rocktato."

            ph "but you too."

            ph "yea, {w=0.3}it's one of THOSE visual novels."

            ph "omg!! {w=0.3}rocktato is secretly edgy!!! {w=0.3}and phrog is sans undertale???"

            ph "no way."

            show ph sans at center, Position(ypos=2400), transform_zoom(x=6.0, y=6.0)

            pause 0.2

            hide ph

        elif moves == 55:
            ph "you think you're a real funny one yea well shut up."

            ph "keep going and you won't like what happens next."

            ph "why?"

            ph "cus i'm bored lol."

            ph "and a {i}lil'{/i} bit annoyed."


        elif moves == 57:
            ph "and.. {w=0.3}to add on..."

            ph "i'll delete all your saves too!"

            ph "fun!"


        elif moves == 59:
            ph "i mean, {w=0.1}this is the first episode."

            ph "so it probably doesn't matter..."

            ph "but still..."

        elif moves == 61:
            ph "that'd kinda suck, {w=0.3}huh?"

        elif moves == 62:
            ph "well..."

        elif moves == 63:
            $ persistent._clear(progress=True)
            $ deletefiles()
            $ persistent.phrog_pisser = True
            ph "Don't say I didn't warn y{w=0.3}{nw}"
            $ renpy.quit()

        menu:
            "Slap":
                $ renpy.block_rollback()
                if moves >= 50:
                    $ moves = moves + 1
                    jump ep1_battle1

                if slaps >= 5:
                    no "Rocktato's hand hurts."
                    no "He decides to stop."
                    $ moves = moves + 1
                    jump ep1_battle1

                elif stomps >=1:
                    show rt fight slap at shake(0.05, 4)
                    rt "HYAH!!!"
                    no "Wizpotato is stuck in the ground."
                    no "Rocktato misses."
                    $ moves = moves + 1
                    jump ep1_battle1

                else:
                    show rt fight slap at shake(0.05, 4)
                    show wiz hurt at shake(0.05, 4)

                    $ chara_healths[0] = chara_healths[0] - 3
                    $ chara_healths[1] = chara_healths[1] - 3

                    play sound "audio/fx/slap.ogg"

                    rt "HYAH!!!"


                if slaps == 0:
                    rt "Ow"
                    no "Rocktato slaps Wizpotato."

                    show wiz hurt at shake(0.05, 4)

                    wiz "OW!!!!"

                elif slaps == 1:
                    show wiz angey 2 at shake(0.05, 4)

                    wiz "Can you stop???"

                    show wiz with hpunch

                    extend " SLAPPING???"

                    rt "."

                    show rt joy 2 at bounce

                    rt "No."

                elif slaps == 2:
                    show wiz hurt at shake(0.05, 4)

                    wiz "wHY??"

                elif slaps == 3:
                    show wiz sad 2

                    wiz "Okay... {w=0.3}so you're just gonna keep... {w=0.3}doing that..."
                    wiz "Ow....."

                elif slaps == 4:
                    show wiz cry at shake(0.05, 4)

                    wiz "*Sobs*"

                show wiz fight idle

                $ slaps = slaps + 1
                $ moves = moves + 1
                jump ep1_battle1

            "Stomp":
                $ renpy.block_rollback()
                if moves >= 50:
                    $ moves = moves + 1
                    jump ep1_battle1

                if stomps >= 5:
                    play sound "audio/fx/stomp.ogg"

                    show rt fight slap at shake(0.05, 4)

                    rt "STOMP!"

                    no "He cannot go any lower."
                    no "Please stop."

                    $ moves = moves + 1
                    jump ep1_battle1

                $ stomp_depth = (stomps+1) * 100

                play sound "audio/fx/stomp.ogg"
                show rt fight slap at shake(0.05, 4)
                show wiz hurt at transform_offset(0,stomp_depth, 0.04), transform_zoom(1, 0.7)

                $ chara_healths[0] = chara_healths[0] - 10

                rt "STOMP!"


                if stomps == 0:
                    wiz "AUGH!!!"

                    no "Rocktato stomps on Wizpotato, {w=0.1}burying him into the ground, {w=0.2}like a plant."

                    wiz "MMPHHH GMGMGMPHMPGGMSFPMSPGM!!!!!"

                    no "Don't ask why it looks like he's slapping him; {w=0.3}he's not."

                elif stomps == 1:
                    wiz "MMHM MGM MFMSM!!!"
                    no "The deeper he goes..."

                elif stomps == 2:
                    wiz "GMGNGSM NS < NSDHB SDFNSJFS!!!"
                    no "Please help him."

                elif stomps == 3:
                    wiz "*Muffled sobs*"
                    no "Oh..."

                elif stomps == 4:
                    no "Wizpotato has gotten to that stony part in the ground."
                    no "He cannot go any lower."
                    no "{b}You monster.{\b}"
                    $ stomps = stomps + 1
                    $ moves = moves + 1
                    jump ep1_battle1



                $ stomps = stomps + 1
                $ moves = moves + 1
                jump ep1_battle1

            "Defend":
                $ renpy.block_rollback()
                if moves >= 50:
                    $ moves = moves + 1
                    jump ep1_battle1

                if defends == 0:
                    play sound "audio/fx/sparkle.ogg"
                    play sound2 "audio/fx/snapping.ogg"
                    show rt fight defn 1

                    rt "*Snapping noises*"

                    no "Rocktato does a stupid pose."
                    no "There's no need to defend; {w=0.3}Wizpotato isn't even attacking."
                    no "(But like, would you count that as defending though?)"

                elif defends == 1:
                    play sound "audio/fx/sparkle.ogg"
                    show rt fight defn 2

                    no "Rocktato does another stupid pose."
                    no "I mean... {w=0.2}sure."
                    no "Alright."

                elif defends == 2:
                    play sound "audio/fx/sparkle.ogg"
                    play sound2 "audio/fx/meow.ogg"
                    show rt fight defn 3

                    rt "Nyah~!{w=0.2}{nw}"

                    no "NOOOOOOOOOOO!!!!"
                    no "WHYYYY???"

                elif defends == 5:
                    no "Well, {w=0.2}if you say so."

                    play sound "audio/fx/cough.ogg"
                    show rt fight defn terrible

                    pause 3.0

                elif defends >= 3:
                    no "Rocktato couldn't think of any other pose to do."
                    no "So... they didn't. {w=0.3}Pose."



                $ defends = defends + 1
                $ moves = moves + 1
                jump ep1_battle1

            "SECRET!!!" if moves >= 5:
                $ renpy.block_rollback()
                $ saveable = True
                if stomps >= 1:
                    no "Gin pulls Wizpotato out of the ground with her massive arms."

                    play sound "audio/fx/dirt.ogg"

                    show wiz cry at transform_zoom(1.0, 1.429), Position(xpos=400, ypos=605) with ease

                    wiz "WHYyyyyy????"

                    show wiz angey at transform_zoom(1.0, 1.0)
                else:
                    ""

                stop music fadeout 1.0

                hide screen battle_health with dissolve

    label ep1_transform:
        show rt happy 2 at flip

        rt "Okay are you ready for this? {w=0.3}This is gonna be mega cool; {w=0.1}it always is."

        if stomps >= 1:
            $ persistent.ep1_squished = True
        else:
            $ persistent.ep1_squished = False

    #     show rt fight idle 1 at funny_expand
    #
    #     stop music fadeout 1.0
    #
    #     play sound "audio/fx/transform.ogg"
    #
    #     show fx white with dissolve
    #
    #     ""
    #
    #     no "Rocktato started to glow."
    #
    #     hide wiz
    #
    #     hide rt
    #
    #     no "Everything turned white."
    #
    #     no "At least our FX budget can afford that."
    #
    #     rt "My true form...."
    #
    #     play sound "audio/fx/fart.ogg"
    #
    #     hide fx white
    #
    #     show rt trueform evil 3 at center, Position(ypos=605)
    #
    #     rt "BEHOLD!"
    #
    # show rt trueform happy 2 at Position(xpos=900) with ease
    #
    # show wiz angey at Position(xpos=400, ypos=605) with easeinbottom

    rt "Time to show you the power of my super cool Rocktato (TM) kick attack!!"

    play sound "audio/fx/slidewhistleup.ogg"

    queue sound "audio/fx/punch.ogg"

    show rt at super_cool_rocktato_tm_kick_attack

    show wiz angey

    pause 0.51

    show wiz hurt at super_cool_rocktato_tm_kick_attack_victim

    with hpunch

    rt "HYAAHH!!!!!!"

    wiz "WAHHHHHHHHH!!"

    ""

    hide rt

    hide wiz

    ""

    play sound "audio/fx/ta da.ogg"

    show rt happy 2 at center

    rt "Yay, I won the battle!"

    rt "That was easy!"

    show rt mad at shake(rate=0.01,strength=3,loop=4)

    rt "Now, WHERE IS HE?"

    rt "WHERE IS MR. ROCK???"

    show wiz angey 2 at Position(xpos=200, ypos=660) with easeinleft

    wiz_yell "You frickin'.... {w=0.3}he's-{w=0.3}"

    show wiz angey 2 at shake(rate=0.01,strength=3,loop=4)

    extend "he's RIGHT THERE!!"

    no "Wizpotato didn't have any arms."

    no "Nor any functional bones."

    no "I think."

    no "I'm,"

    no "I'm not sure if he even had bones to begin with."

    no "But he gestured towards below the screen where, {w=0.2}indeed, {w=0.2}the stupid little stone stood."

    play sound "audio/fx/slidewhistleup.ogg"

    show mr bellless at Position(xpos=900,ypos=580) with easeinbottom

    show p he him at Position(xpos=1120, ypos=450) with dissolve

    mr "{w=0.6}.{w=0.6}.{w=0.6}."

    hide p he him with dissolve

    wiz_yell "I KEPT TRYING TO TELL YOU!!!"

    wiz "While you were busy BEATING ME TO A PULP,"

    extend " he's just been... {w=0.2}been sitting there the whole flip flapperintime!!!!!"

    wiz "EVen while you were wandering through the city, {w=0.3}he's BEEN FOLLOWING YOU!"

    wiz "(Yeah, I was watching you, {w=0.3}so WHAT?)"

    show rt o

    rt "MR. ROCK?"

    show rt joy 2 at bounce

    rt "MR. ROCK!!!!!!!!!!!"

    rt "IT'S SO GOOD TO SEE YOU!!!!!!!"

    # show rt confused
    #
    # rt "Wait, {w=0.3}but why would you know that?"
    #
    # rt "You weren't even at our quest???"
    #
    # show wiz angey 2 at shake(rate=0.01,strength=3,loop=4) with hpunch
    #
    # wiz_yell "YOU HAD A WHOLE QUEST LOOKING FOR HIM???"
    #
    # wiz_yell "Was he... {w=0.3}THERE THE WHOLE TIME?"
    #
    # show rt sad 2
    #
    # rt "Well... {w=0.3}now that I think about it...."
    #
    # show bg white
    #
    # hide rt
    # hide wiz
    # hide mr
    #
    # with dissolve
    #
    #
    # show rt cry
    #
    # show bg rtcave
    #
    # with dissolve
    #
    # ""
    #
    # show mr at Position(xpos=900,ypos=580) with dissolve
    #
    # ""
    #
    # show bg white
    #
    # hide rt
    # hide mr
    #
    # with dissolve
    #
    # show bg swamp
    #
    # show rt sad at Position(xpos=400)
    #
    # show ph bruh at Position(xpos=900)
    #
    # with dissolve
    #
    # ""
    #
    # show mr at Position(xpos=640,ypos=580) with dissolve
    #
    # ""
    #
    # show bg white
    #
    # hide rt
    # hide mr
    # hide ph
    #
    # with dissolve
    #
    # show bg mcdondals
    #
    # show bl bruh at Position(xpos=200)
    #
    # show rt joy at Position(xpos=600)
    #
    # show ph smug at Position(xpos=1000)
    #
    # with dissolve
    #
    # ""
    #
    # show mr at Position(xpos=1250,ypos=200) with dissolve
    #
    # ""
    #
    # show bg white
    #
    # hide rt
    # hide mr
    # hide ph
    # hide bl
    #
    # with dissolve
    #
    # show bg 1 rumboy crashed
    #
    # show wiz angey at Position(xpos=200, ypos=660)
    #
    # show rt o at center
    #
    # with dissolve
    #
    # ""
    #
    # show mr at Position(xpos=900,ypos=580) with dissolve
    #
    # ""

    show rt at bounce

    no "He picks up the little stone."

    # rt "Wow, {w=0.2}to think we went on a whole quest looking for you, without seeing you!"
    #
    # rt "What a crazy, fun time..."
    #
    # show wiz sus 2
    #
    # wiz "what."
    #
    # wiz "You.."
    #
    # ph "yeah, {w=0.3}a whooooole adventure."
    #
    # show wiz angey 2 with hpunch
    #
    # wiz_yell "DID NONE OF YOU IDIOTS SAY ANYTHING TO HIM?"
    #
    # ph "nyehhhhhhhhh {w=0.3}i was too lazy to."
    #
    # gin "I jus' assumed it was like a... {w=0.3}a lil' game?"
    #
    # gin "Or somethin'.."
    #
    # bl "Apologies, {w=0.2}my friends, {w=0.2}for leaving but..."
    #
    # bl "uh..."
    #
    # bl "I am not going to touch this one."
    #
    # bl "Oh woopsie me! {w=0.3}Another phone call?"
    #
    # bl "What a coincidence!! {w=0.3}Let me just..."
    #
    # no "He escapes..."
    #
    # show rt sad at bounce
    #
    # no "Rocktato picks up Mr. Rock, {w=0.3}looking at his Sharpie-scribbled face."

    show cg 1 mr rock

    hide bg

    hide wiz

    hide rt

    hide mr

    with dissolve

    rt "Man... {w=0.3}Aaaa I'm sorry I didn't notice you."

    rt "It's just... {w=0.3}really hard since you can't talk!"

    rt "Hey, {w=0.3}how about I get you a bell or something!!"

    mr "{w=0.6}.{w=0.6}.{w=0.6}."

    rt "YEAH! {w=0.3}This way I'll notice you more!"

    mr "{w=0.6}.{w=0.6}.{w=0.6}."

    rt "Cookie dough?? {w=0.3}Heck yeah!"

    play sound "audio/fx/stepping.ogg"

    show bg black

    hide cg

    with dissolve

    rt "See you guys later!!!"

    no "The kid started walking away from the scene and waving to their friends."

    no "He was happy with his latest adventure!"

    ph "OH MY GOD THE FIRE IS SPREADING TO MY HOUSE!!"

    ph "YOU ASSHOOOOOOOOooooleee{size=15}ee{size=15}"

    if persistent.episode_fin == 0:
        $ persistent.episode_fin = 1

    $ persistent.mainmenu_img = 2


    return()
