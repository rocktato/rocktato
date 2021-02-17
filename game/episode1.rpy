label start:

    image battlestarttext:
        "gui/text/battle start.png"

    image sky:
      "images/imgs/1/bg 1 sky.png"
      0.1
      "images/imgs/1/bg 1 sky 2.png"
      0.1
      "images/imgs/1/bg 1 sky 3.png"
      0.1
      repeat

    stop music fadeout 1.0

    show sky

    show obj 1 rumboy at fast_shaking

    space ""

    show img 1 rumboy crashed at hpunch

    hide sky

    hide obj

    space ""

    Character("Random Citizen 1", size=25, color="#ffffff",callback=no_blip) "OH MY GOD!!!"

    Character("Random Citizen 2", size=25, color="#ffffff",callback=no_blip) "A GIANT RUMBOY HAS FALLEN FROM THE SKY!!!"

    Character("Random Citizen 3", size=25, color="#ffffff",callback=no_blip) "MY TAX DOLLARS WENT INTO THAT FOUNTAIN NOO!!"

    Character("Random Citizen 3.5", size=23, color="#ffffff",callback=no_blip) "AHHHHHHHHHHHHHH SCREAMING!!"

    show rt disgusted at right

    rt "No way..."


    show img 1 rumboy crashed freezeframe with hpunch

    show rt o at bounce

    rt "Well this is me."

    rt "You're probably wondering how I got into this situation."

    rt "Oh, {w=0.3}this is narration by the way."


    show bg black

    hide rt

    with dissolve

    hide img 1 rumboy crashed freezeframe

    rt "Today started just like every other morning."

    rt "The air was crisp with whatever air has."

    rt "I got out of bed with naive optimism, {w=0.3}wondering what adventures awaited me today."

    rt "Then, I realized that I don't even have a bed?? {w}I just have a gigantic bean bag chair-type?? {w}That I sleep on??"

    rt "But whatever, {w=0.3}I'm used to the back pain."

    rt "Okay, okay, {w=0.3}fine."

    rt "I'll stay on topic."

    show bg rtcave with dissolve

    show rt happy 2 with dissolve

    rt "So anyway, I got out of bed, right?"

    show rt joy 2 at bounce

    rt "I went to greet my best friend, {w=0.3}Mr. Rock, {w=0.3}good morning."

    rt "You know that guy, right? {w}What a good guy..."

    show rt joy

    rt "I remember that one time when I greeted him good morning yesterday!"

    rt "So I looked at his bed, {w=0.3}yeah?"

    show rt exasperated

    rt "Then I asked myself why HE got a bed but I didn't."

    show rt joy

    rt "Oh yeah he was gone too."

    rt "I feel like I didn't do that right, wait."

    show rt o with hpunch

    rt "He was GONE!!!"

    show rt cry

    rt "Just poof! Vanished!!"

    rt "No note or anything, {w=0.3}just a pile of uneaten rock food. {w}Which also happens to just be rocks."

    show rt o

    rt "Did you know rocks are cannibals?"

    show rt joy 2 at bounce

    rt "Fun fact!"

    rt "Anyway, {w=0.3}I went looking around my cave calling out for him."

    show rt sad 2 at shake(rate=0.005,strength=1,loop=7)

    rt "MR. ROCK??? Do you hear me??? Make a noise or something!!"

    rt "Those were the words that came out of my mouth."

    show rt troubled

    rt "However, I got no response."

    rt "So I thought that maybe... {w=0.3}he'd be out there somewhere in the city!"

    show rt joy 2 at shake(rate=0.005,strength=1,loop=5)

    rt "Let's go!!!!!!!"

    rt "I said outloud, {w=0.3}for some reason."

    show bg beegcity

    show rt joy 2 at bouncing

    rt "So there I was. Walking through the streets of Beeg City."

    rt "I mean you know the place right?"

    rt "It's beeg!!! {w=0.3}With beeg towers and beeg money!! {w=0.3}And beeg people."

    rt "Well, {w=0.3}some of them are beeg, {w=0.3}but not all of them. {w}I just meant big as in status."

    rt "They're really cool people is what I'm trying to say!"

    rt "This place is filled with awesome superheroes with awesome superpowers!!"

    rt "The city has so many sections too!! {w=0.3}It's for everyone!!"

    show rt sad 2 at bouncing

    rt "The bad part about that is that Mr. Rock could have been anywhere!!"

    rt "So the first place I went to was the swamp."


    show bg swamp

    show rt sad 2 at center

    rt "Which is here."

    rt "I need to know if you've heard Mr. Rock come around here, Phrog."

    show rt sad at Position(xpos=400) with ease

    show ph bruh at Position(xpos=900) with easeinbottom

    ph "what."

    show ph bruh 2

    ph "why did you tell me all that????"

    ph "i literally LIVE here."

    ph "i've lived in beeg city for like fifty years or smth probably."

    ph "but.."

    show ph bruh 3 at bounce, Position(xpos=900)

    pause 1.0

    show ph bruh at bounce

    pause 1.0

    show ph bruh 2

    ph "nah... he isn't here."

    show ph o

    ph "i haven't seen the guy since yesterday..."

    show rt o

    rt "Wait you saw him yesterday??? {w=0.3}What was he doing???"

    show ph bruh

    ph ""

    ph "he was with you."

    show rt joy 2 at bounce

    rt "Oh yeah!"

    rt "Well..."

    show rt o

    rt "Will you help me look for him?"

    show ph bruh 3 at shake(rate=0.01,strength=1,loop=5)

    ph "sighs audibly."

    show ph bruh 2

    ph "fine."

    show rt confused at bounce

    rt "Why did you say sighs audbily??"

    show ph o 2

    ph "  "

    ph "  "

    show ph o 2 at shake(rate=0.01,strength=5,loop=18)

    space ""

    show ph bruh 2 at bounce

    ph "okay where we going first? {w=0.3}{i}sirrrrrrrr{/i}"

    show rt joy 2 at bounce

    rt "Wow! {w=0.3}You should use 'sir' more often!"

    rt "Makes me feel rich!!!"

    show rt o at shake(rate=0.01,strength=5,loop=2)

    rt "OOOH!"

    show rt happy 2

    rt "Maybe let's explore the rich area place thing first??"

    show ph think 2

    ph "why the frig frog would he be at the rich area place thing?"

    show rt happy at bounce

    space ""

    no "Rocktato shrugs."

    show ph bruh 2

    ph "ok."



    show bg beegcity

    show ph bruh

    show rt joy 2

    space ""

    ph "welp. we here."

    show ph bruh 2 at shake(rate=0.01,strength=1,loop=7)

    ph "i wanna take a naaaaaap..."

    show rt o

    rt "Do you see him anywhere here?"

    show ph bruh 3

    space ""

    show ph bruh 2

    ph "nyeh... {w=0.3}it doesn't look like it...."

    show ph o at bounce

    ph "guess he's dead oh nooooo"

    show rt bruh at bounce

    rt "I'm not stupid Phrog."

    show rt nervous

    rt "I..."

    show rt confused at bounce

    rt "I don't think he {b}CAN{/b} die."

    show ph o at bounce

    space ""

    ph "o."

    show ph think 2

    ph "uhhhhh what does mr. rock do in his free time?"

    ph "does he do like... {w=0.3}i dunno... "

    show ph o with hpunch

    extend "drUG DEALS???"

    show ph o 3 at bounce

    ph "maybe he's on the run from the FBI?"

    show ph tired 2

    ph "sigh..."

    ph "i know i still am :("

    show ph tired

    show rt o

    rt "Now that I think about it...."

    show rt o at shake(rate=0.01,strength=1,loop=3)

    rt "Yeah I think so!!"

    show ph smug 2

    ph "wait what actually lol"

    show rt happy 2 at bounce

    rt "I'm pretty sure Mr. Rock does drugs deals!"

    show ph o

    rt "He's probably in the middle of one right now!"

    ph "how"

    show rt o at shake(rate=0.01,strength=1,loop=3)

    rt "OOH!!!"

    rt "Let's look in that fishy alley!!"

    rt "Maybe he's in there!"

    hide rt

    hide ph

    show img 1 alley 1

    with dissolve

    no "Across from them were two buildings that had a convenient amount of space in them."

    no "A space between buildings you'd barely even pay attention to."

    no "The two kids slowly walked up to the spoooooooky alley."

    no "They quietly peeked into the corner and saw something you couldn't describe with words."
    #TODO: LIFE SCARRING SOUND EFFECT
    space ""

    space ""

    show img 1 alley 2 with hpunch

    space ""

    space ""

    hide img 1 alley 2

    show bg beegcity

    show ph scared 2 at Position(xpos=900)

    show rt disturbed at Position(xpos=400)

    ph "NOPE NOPE NOPE NOPe!!!!"

    show rt disturbed at shake(rate=0.01,strength=3,loop=7)

    rt "Those poor vegetable kids..."

    rt "They never stood a chance against that tall dealer man."

    show rt joy 2 at bounce

    rt "Now we know why we shouldn't do drugs kids!"

    show rt troubled

    show ph o 2

    rt "There goes our only lead."

    rt "Where do we go now??"

    show ph think 2

    ph "hey, {w=0.3}isn't blairic around these parts?"

    show rt o at bounce

    rt "Oh yeah!!!"

    show rt joy 2

    rt "He IS a skeleton billionaire after all."

    show rt o

    rt "But WHICH of these buildings would he be in?"

    show ph bruh 2

    ph "buhhhhhhh idk probably a bank or something."

    show rt joy 2 at bounce

    rt "Sounds good to me!"


    show bg bloffice

    show rt confused

    show ph bruh

    space ""

    rt "Is it just me or does this place look a lot like Blairic's office??"

    show ph bruh 2

    ph "that joke only works if we've seen his office already."

    rt "But we have..."

    show ph bruh 3

    ph ""

    show ph bruh 2

    ph "well..."

    ph "some people haven't..."

    show ph o 2

    bl "Why!!! {w=0.3}If it isn't Rocktato and Phrog!!!"

    show rt confused at Position(xpos=600)

    show ph o 2 at Position(xpos=1000)

    with ease

    show bl happy at Position(xpos=200) with easeinbottom

    bl "Pleasant seeing the two of you here!!!"

    show rt happy 2 at bounce

    rt "BLAIRIC!!!"

    show ph smug 2 at bounce

    ph "yo b."

    show bl o at bounce

    bl "What are you children doing in a bank of all places?"

    show rt o

    rt "We're on a search for Mr. Rock!!"

    rt "Can you help us?"

    show bl think

    bl "Hm..."

    show bl happy 3 at bounce

    bl "Alright!!! {w=0.3}Sure!!!"

    bl "I shall accompany you two on your little escapade!"

    show rt joy 2 at bounce

    rt "Heck yeah!!!"

    show ph bruh 2

    ph "should've left while you still had the chance."

    show ph bruh

    show bl o

    bl "So..."

    bl "Where will our next destination be?"

    show rt happy 2 at shake(rate=0.01,strength=3,loop=7)

    rt "MCDONDALS!!!!!!"

    show bl think

    bl "Why would he be at a McDonda{w=0.1}{nw}"


    show bg mcdondals

    show bl bruh

    show rt joy

    show ph smug

    space ""

    show rt joy 2

    rt "Thanks for paying Blairic!"

    rt "I don't have any money."

    rt "Haha I'm a child."
    #TODO add vaccum noise

    show rt joy 2 at shake(rate=0.01,strength=5,loop=10)

    space ""

    rt "Man, {w=0.3}I'm just in love with these nuggs!!!"

    show ph smug 2 at bounce

    ph "b, {w=0.3}you gonna eat any?"

    show bl bruh 2 at bounce

    bl "I will pass Phrog."

    bl "I do not have a digestive system."

    show bl sad

    bl "I am a skeleton."

    show ph o at bounce

    space ""

    ph "o."

    show ph o 3

    ph "right..."

    show rt sad 2 at bounce

    rt "Too bad Mr. Rock wasn't hidden in the ball pit."

    show ph smug 2

    ph "yea, {w=0.3}i coulda SWORN i saw him in there."

    ph "but oh well."

    show bl nervous at bounce

    bl "This uh..."

    bl "This does not really feel like a search."

    show bl bruh 2

    bl "You kids just amused yourselves in the McDonDals playplace for an hour..."

    show ph smug 2 at bounce

    ph "nah b, {w=0.3}we resting."
    #TODO SOUND EFFECT

    space ""

    show rt mad with hpunch

    no "Rocktato suddenly stood up and AGGRESSIVELY threw his food tray onto the ground!"

    no "Then he picked it up and properly put his trash and tray at the correct places."

    show rt mad at shake(rate=0.01,strength=5,loop=5)

    show ph o

    show bl heehee

    rt "For hecks sake!!!"

    rt "Blairic is right!!!"

    rt "We gotta get out there and search!!"

    show ph bruh 2 at bounce

    ph "aaaaaaaaaaaaand lametato's back."

    ph "aw man.."

    show rt bruh at bounce

    show ph bruh

    rt "Okay, {w=0.3}first off, {w=0.3}that's a bit mean Phrog."

    show rt o with hpunch

    rt "Second of all, {w=0.3}who KNOWS what's happening to Mr. Rock??"

    rt "He could be, {w=0.1}like..."

    show rt cry 2 at bounce

    rt "Hanging out with someone cooler than me!!!"

    show ph bruh 2

    ph "okay maybe that's a stretch..."

    show rt happy 2 at bounce

    rt "C'mon let's go!!!"

    show bg black

    show ph scared

    show bl uncomfortable

    space ""

    show ph scared 2 at shake(rate=0.01,strength=5,loop=5)

    ph "ROCKTATO!!!"

    show ph scared 2 at shake(rate=0.01,strength=10,loop=7)

    ph "YOU DIDN'T CHOOSE A LOCATION???"

    bl "What is this place??"

    show rt o at bounce

    rt "Oh yeah, {w=0.3}guess I didn't!"

    rt "Well, {w=0.1}since Blairic is here, {w=0.1}we might as well ask Gin for help too!"

    show bl o at bounce

    bl "She usually hangs around the gamer bar, {w=0.1}correct?"

    show rt joy 2 at bounce

    rt "YEAH!"

    show ph scared 2 at shake(rate=0.01,strength=15,loop=10)

    ph "OKAY OKAY JUST HURRY UP!!{w=0.3}{nw}"


    show bg gamerbar

    show ph scared

    show bl happy 2

    space ""

    ph ""

    show ph joy 2 at bounce

    ph "i don't like it here anymore!"

    show ph o 3

    ph "wait... {w=0.5} i can say that for real!"

    show ph bruh

    ph "i hate this place."

    show rt happy 2 at bounce

    rt "YO!!! {w=0.3}GIN!!!"

    gin "GASP!!!"

    show bl happy 2 at Position(xpos=125)

    show rt happy 2 at Position(xpos=425)

    show ph o 2 at Position(xpos=725)

    with ease

    show gin evil 2 at Position(xpos=1100) with easeinbottom

    gin "If it isn't my favorite piss babies!!!!"

    show gin o at bounce

    gin "What're y'all doin' here??"

    show bl o at bounce

    bl "We are uhh... {w=0.5}looking for Mr. Rock."

    show bl bruh 2

    bl "Also, it is now your turn to chaperone these little gremlins."

    bl "I shall take a phone call. {w=0.3}Excuse me."

    hide bl bruh with easeoutbottom

    show rt happy 2 at Position(xpos=200)

    show ph o 2 at Position(xpos=545)

    show gin o at Position(xpos=1000)

    with ease

    space ""

    gin "Yeah, that's fair."

    show gin happy

    gin "How have you kiddos been doing??"

    show rt joy 2 at bounce

    rt "I'm doing awesome!!! {w=0.3}Wait, {w=0.3}no I'm not!"

    show rt cry 2 with vpunch

    rt "Mr. Rock is still gone!!!"

    show gin bruh

    gin "Hmm... {w=0.3}that is very troublin'."

    show gin happy at bounce

    show rt happy

    gin "How about you Phrog?"

    show ph bruh 2

    ph "i wanna take a nap."

    show gin thankful

    gin "C'mon kid, {w=0.3}you haven't been on a wild adventure in a while!"

    gin "At least like, {w=0.1}{i}try{/i} to have fun."

    show gin evil 2 at bounce

    gin "It'll be good for ya!"

    show ph bruh at bounce

    ph "yea... {w=0.3}that's fair."

    show rt o

    show ph o 2

    rt "Giinnn??"

    rt "Can I get a drink????"

    show gin bruh

    gin "Mmmm... {w=0.3} just a lil' sippy sipp."

    show gin evil at bounce

    show rt joy

    no "Gin allowed Rocktato to have a tiiiiiny sip from her can of Mountain Dew G Fuel."

    show rt joy 2 at bounce

    rt "Mmmm {w=0.3}thank youuu!!"

    show rt happy 2

    rt "Now where do we head next?"

    show ph o at bounce

    ph "what about the uhhhhhhhhhh {w=1.3}yeah i'm gonna b honest, {w=0.3}i just started talking and i didn't think of anything."

    show ph joy at bounce

    ph "woops!"

    show gin o

    gin "Okay well..."

    gin "where have you guys been so far???"

    show rt happy 2 at bounce

    rt "Well... {w=0.3}we went to the swamp, {w=0.3}the rich place area thing, {w=0.3}and the McDonDals!"

    show gin happy at bounce

    gin "WOAH!!! {w=0.3}Fun!"

    show gin lecture

    gin "So you guys didn't check the city park yet???"

    show rt joy 2 at bounce

    rt "Nah."

    show gin o

    gin "Whhhhhhhhhhh... {w=0.3}why not???"

    gin "That's where literally everything interesting happens!"

    show rt o

    rt "Oh yeahhhhhh"


    show bg citypark

    show rt joy

    show ph bruh

    show gin evil

    no "We now see our protaginists standing at the center of their beloved Beeg City."

    no "There were kids eating ice cream and playing insert any sport game here."

    no "There were bird people perched on the trees screaming."

    no "And there were many heroes just going about and stuff."

    no "It's pretty hard to describe, {w=0.3}you just had to see it."

    no "The best we can do is show this background."

    no "Sorry!!!"

    no "Rocktato stood on top of the center fountain calling out for his best friend."

    show rt hurt at bounce

    rt "Mr. Rock???"

    rt "Mr. Rock!!!"

    show rt sad 2

    rt "Aw, {w=0.3}do you guys see him anywhere??"

    show gin think

    gin "Mmm, {w=0.1}he's quite the hider, {w=0.1}ain't he?"

    show ph bruh 2

    ph "yeaaaaaaaaaa {w=0.3}that..."

    rt "Man this sucks."

    show rt cry 2

    show ph bruh

    rt "It's already afternoon and he's still gone!"

    rt "How will we have our daily afternoon cookie dough eating competition now???"

    rt "How can I unfairly win again and rub it in his face while feeling better about myself???"

    show rt hurt with hpunch

    rt "AHHHHHHHHHH!!!!!"

    show rt o at bounce

    rt "..."

    no "Rocktato suddenly got up and started sniffing."

    show gin o

    gin "WoAH!"

    show ph bruh 2 at bounce

    ph "ew what are you doing?"

    show rt disgusted

    rt "{i}Do you smell that????{/i}"

    ph "no{w=0.2}{nw}"

    show ph bruh

    show gin sad

    rt "{i}It's the smell of {b}villainy.{/b}{/i}"

    show rt disgusted at shake(rate=0.01,strength=15,loop=5) with hpunch

    space ""

    no "Suddenly, {w=0.3}the air turned gray."

    no "Something beeg was in the sky."

    no "It casted a shadow over the whole park."

    no "All of the civilians were panicking and running away."

    no "Rocktato and the crew stood on guard."

    hide rt

    hide ph

    hide gin

    show sky

    show obj 1 rumboy at fast_shaking

    with dissolve

    space ""

    show img 1 rumboy crashed at hpunch

    hide obj

    hide sky

    space ""

    Character("Random Citizen 1", size=25, color="#ffffff",callback=no_blip) "OH MY GOD!!!"

    Character("Random Citizen 2", size=25, color="#ffffff",callback=no_blip) "A GIANT RUMBOY HAS FALLEN FROM THE SKY!!!"

    Character("Random Citizen 3", size=25, color="#ffffff",callback=no_blip) "MY TAX DOLLARS WENT INTO THAT FOUNTAIN NOO!!"

    Character("Random Citizen 3.5", size=23, color="#ffffff",callback=no_blip) "AHHHHHHHHHHHHHH SCREAMING"

    rt "No way..."

    show bg 1 rumboy crashed

    hide img 1 rumboy crashed

    hide rt

    with dissolve

    rt "Is thAT-"

    Character("???", color="#ffffff", size=43, what_size=70, callback=wiz_blip) "..."

    Character("???", color="#ffffff", size=43, what_size=70, callback=wiz_blip) "NYEHEHEHEH..."

    show wiz evil 2 at center, Position(ypos=50) with easeinbottom

    Character("???", color="#ffffff", size=43, what_size=70, callback=wiz_blip) "IT IS I, {w=0.3}WIZPOTATo!!!"

    wiz_yell "WAIT CRAP!!! {w=0.3}I MISSED!!!!!"

    show wiz bruh at center, Position(ypos=200) with ease

    wiz "uhhhhhhhhh {w=0.3}wait one sec..."

    show wiz bruh at center, Position(ypos=300) with ease

    pause 1.0

    show wiz bruh at center, Position(ypos=500) with ease

    pause 1.0

    show wiz bruh at center, Position(ypos=800) with ease

    pause 1.0

    show wiz bruh at center, Position(ypos=605) with ease

    pause 1.0

    show wiz sus 2 at center, Position(ypos=605)

    wiz "okay... {w=0.3}THERE we go..."

    show wiz sad 2 at center, Position(ypos=605)

    wiz "okay uhh..."

    show wiz evil 2 with hpunch

    wiz_yell "THE GREATEST SUPERVILLAIN TO EVER..."

    show wiz sad 2

    wiz "uh...{w=0.3}{nw}"

    show wiz evil 3 with hpunch

    wiz_yell "YEAH!!!!!!!!! !!!!!!!!!!!! !!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!"

    no "A bunch of the heroes that were there walked away, disappointed."

    show wiz bruh

    Character("Random Hero 1", size=31, color="#ffffff",callback=no_blip) "Are you kiddin' me?? {w=0.3}THIS GUY AGAIN?!"

    Character("Random Citizen 3", size=25, color="#ffffff",callback=no_blip) "MY TAX DOLLARS WERE WASTED FOR THIS????"

    rt "GASP!!!!!!"

    show wiz evil at Position(xpos=400) with ease

    show rt disgusted at Position(xpos=900) with easeinbottom

    rt "WIZPOTATO!!!!"

    rt "I knew it was you."

    rt "I could smell you from miles away!!!"

    show wiz sus 2

    wiz "OKay, "

    show wiz angey 2 with hpunch

    extend "WEIRD."

    show wiz evil 3 at bounce

    wiz "But, {w=0.3}it is quite convenient that you are here!!!"

    show wiz evil 2 at shake(rate=0.01,strength=10,loop=2)

    wiz_yell "MY DEAR RIVAL..."

    wiz_yell "IT SEEMS IT HAS BEEN FATED FOR US TO{w=0.3}{nw}"

    show rt mad at shake(rate=0.01,strength=10,loop=2) with hpunch

    rt "SHUT UP!!!!!!!!"

    show rt sad 2

    rt "We just wanted to look for Mr. Rock, man."

    show rt hurt at shake(rate=0.01,strength=10,loop=2) with hpunch

    rt "HOLD ON!!!!"

    rt "I BET YOU MUST'VE TAKEN HIM, {w=0.3}HRMM????"

    show wiz sus 2

    space ""

    wiz "what"

    wiz "What are you talking about????"

    show rt mad

    rt "OH YOU KNOW WHAT I'M TALKING ABOUT!!!!"

    wiz "no????{w=0.2}{nw}"

    show rt smug 2 at bounce

    rt "Ooooo, {w=0.3}I'm gonna beat you up so bad!!!"

    ph "rocktato wait!"

    show rt bruh

    show ph o at flip, Position(xpos=1200) with easeinbottom

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

    show battlestarttext at truecenter, shake(rate=0.05,strength=1,loop=2) with dissolve

    pause 1.0

    hide battlestarttext with dissolve


    #TODO: BATTLE SPRITES
    # - DECISION BOXES FIX (use parameters in choice box screen?)

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

        ph "tato, you know how to fight (i mean they teach this stuff in elementary jesus) but do you want a reminder anyway?"

        menu:
            "Yes please!":
                $ renpy.block_rollback()
                pass
            "Shut up Phrog!":
                $ renpy.block_rollback()

                ph "jeez ok."

                hide ph

                space ""

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

    rt "(Alright, so what are my options?)"

    rt "(Parentheses means thinking, by the way.)"

    show rt joy 2 at bounce

    rt "(Fun fact!)"

    label ep1_battle1:

        show rt fight idle

        $ choice_screen_type = "fight_choice"

        if moves == 0 and ep1_skiptut2 == False:
            rt "(Okay, so I can either punch him, which will hurt a bunch!!!)"
            rt "(Ah, but it might hurt me too though. {w}I'm a sensitive boy :,<.)"
            rt "(I can stomp him into the ground too, which would be funny.)"
            rt "(Or... I can defend!!! {w=0.3}So I won't get too big of a hurt myself!"
            rt ")"

            rt "(GO CHOOSE,  {w=0.1}ME!)"

        elif moves == 5:
            show gin evil 2 at Position(xpos=1170) with easeinbottom

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
            if persistent.phrog_pisser == True:
                ph "yeah ok i'm not gonna give you that dialouge again or new dialouge. {w=0.3}if you don't transform, i'll kill you and rocktato again."
                rt "Wait what-{w=0.1}{nw}"
            else:
                ph "wow."

                ph "you're a real persistent one, huh?"

        elif moves == 51:
            if persistent.phrog_pisser == True:
                $ persistent._clear(progress=True)
                $ deletefiles()
                $ persistent.phrog_pisser = True

                $ renpy.quit()

        elif moves == 53:
            ph "ya alright."

            ph "if you keep doing this."

            ph "{b}i'm gonna end you.{\b}"

            ph "not just rocktato."

            ph "but you too."

            ph "yea, {w=0.3}it's one of THOSE visual novels."

            ph "omg!! {w=0.3}rocktato is secretly edgy!!! {w=0.3}and phrog is sans undertale???"

            ph "no way"

            show ph sans at center, Position(ypos=2400), transform_zoom(x=6.0, y=6.0)

            pause 0.2

            hide ph

        elif moves == 55:
            ph "you think you're a real funny one yea well shut up."

            ph "keep going and you won't like what happens next."

            ph "why?"

            ph "cus i'm bored lol"

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
            ph "don't say i didn't warn y{w=0.3}{nw}"
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
                    show wiz fight hurt at shake(0.05, 4)

                    $ chara_healths[0] = chara_healths[0] - 3
                    $ chara_healths[1] = chara_healths[1] - 3
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
                    show wiz hurt 2 at shake(0.05, 4)

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
                    show rt fight slap at shake(0.05, 4)

                    rt "STOMP!"

                    no "He cannot go any lower."
                    no "Please stop."

                    $ moves = moves + 1
                    jump ep1_battle1

                $ stomp_depth = (stomps+1) * 100

                show rt fight slap at shake(0.05, 4)
                show wiz fight squish at transform_offset(0,stomp_depth, 0.04), transform_zoom(1, 0.7)

                $ chara_healths[0] = chara_healths[0] - 5

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
                    show rt fight defn 1

                    rt "*Snapping noises*"

                    no "Rocktato does a stupid pose."
                    no "There's no need to defend; {w=0.3}Wizpotato isn't even attacking."
                    no "(But like, would you count that as defending though?)"

                elif defends == 1:
                    show rt fight defn 2

                    no "Rocktato does another stupid pose."
                    no "I mean... {w=0.2}sure."
                    no "Alright."

                elif defends == 2:
                    show rt fight defn 3

                    rt "Nyah~!{w=0.2}{nw}"

                    no "NOOOOOOOOOOO!!!!"
                    no "WHYYYY???"

                elif defends == 5:
                    no "Well, {w=0.2}if you say so."

                    show rt fight defn terrible

                    pause 3.0

                elif defends >= 3:
                    no "Rocktato couldn't think of any other pose to do."
                    no "So... he didn't. {w=0.3}Pose."



                $ defends = defends + 1
                $ moves = moves + 1
                jump ep1_battle1

            "TRANSFORM!!!" if moves >= 5:
                $ renpy.block_rollback()
                $ saveable = True
                if stomps >= 1:
                    no "Gin pulls Wizpotato out of the ground with her massive arms."

                    show wiz hurt 2 at transform_zoom(1.0, 1.429), Position(xpos=400, ypos=605) with ease

                    wiz "WHYyyyyy????"

                    show wiz angey at transform_zoom(1.0, 1.0)

                hide screen battle_health

    show rt fight idle 1

    rt "Okay are you ready for this? {w=0.3}This is gonna be mega cool; {w=0.1}it always is."

    show rt fight idle 1 at funny_expand

    show fx white with dissolve

    no "Rocktato started to glow."

    hide wiz

    hide rt

    no "Everything turned white."

    no "At least our FX budget can afford that."

    rt "My true form...."

    hide fx white

    show rt trueform smile at center, Position(ypos=605)

    rt "BEHOLD!"

    show rt trueform happy 2 at Position(xpos=900) with ease

    show wiz angey at Position(xpos=400, ypos=605) with easeinbottom

    rt "Time to show you the power of my super cool Rocktato (TM) kick attack!!"

    show rt at super_cool_rocktato_tm_kick_attack

    show wiz angey

    pause 0.51

    show wiz hurt at super_cool_rocktato_tm_kick_attack_victim

    with hpunch

    rt "HYAAHH!!!!!!"

    wiz "WAHHHHHHHHH!!"

    space ""

    hide rt

    hide wiz

    space ""

    show rt trueform happy 2 at center, Position(ypos=605)

    rt "Yay, I won the battle!"

    show rt joy 2 at center

    space ""

    show rt mad at shake(rate=0.01,strength=3,loop=4)

    rt "Now, WHERE IS HE?"

    rt "WHERE IS MR. ROCK???"

    show wiz angey 2 at Position(xpos=200, ypos=660) with easeinleft

    wiz_yell "You frickin'.... {w=0.3}he's-{w=0.3}"

    show wiz angey 2 at shake(rate=0.01,strength=3,loop=4)

    extend "he's RIGHT THERE!!"

    no "Wizpotato didn't have any arms."

    no "Nor any functional bones."

    no "I think?"

    no "But he gestured towards behind the textbox where, {w=0.2}indeed, {w=0.2}the stupid little stone stood."

    show mr at Position(xpos=900,ypos=580) with easeinbottom

    wiz "He's been... {w=0.2}been there the whole flip flapperintime!!!!!"

    show rt o

    rt "MR. ROCK?"

    show rt joy 2 at bounce

    rt "MR. ROCK!!!!!!!!!!!"

    rt "IT'S SO GOOD TO SEE YOU!!!!!!!"

    show rt confused

    rt "Wait, {w=0.3}but why would you know that?"

    rt "You weren't even at our quest???"

    show wiz angey 2 at shake(rate=0.01,strength=3,loop=4) with hpunch

    wiz_yell "YOU HAD A WHOLE QUEST LOOKING FOR HIM???"

    wiz_yell "Was he... {w=0.3}THERE THE WHOLE TIME?"

    show rt sad 2

    rt "Well... {w=0.3}now that I think about it...."

    show bg white

    hide rt
    hide wiz
    hide mr

    with dissolve


    show rt cry

    show bg rtcave

    with dissolve

    space ""

    show mr at Position(xpos=900,ypos=580) with dissolve

    space ""

    show bg white

    hide rt
    hide mr

    with dissolve

    show bg swamp

    show rt sad at Position(xpos=400)

    show ph bruh at Position(xpos=900)

    with dissolve

    space ""

    show mr at Position(xpos=640,ypos=580) with dissolve

    space ""

    show bg white

    hide rt
    hide mr
    hide ph

    with dissolve

    show bg mcdondals

    show bl bruh at Position(xpos=200)

    show rt joy at Position(xpos=600)

    show ph smug at Position(xpos=1000)

    with dissolve

    space ""

    show mr at Position(xpos=1250,ypos=200) with dissolve

    space ""

    show bg white

    hide rt
    hide mr
    hide ph
    hide bl

    with dissolve

    show bg 1 rumboy crashed

    show wiz angey at Position(xpos=200, ypos=660)

    show rt o at center

    with dissolve

    space ""

    show mr at Position(xpos=900,ypos=580) with dissolve

    space ""

    wiz_yell "DID NONE OF YOU IDIOTS SAY ANYTHING TO HIM?"

    ph "nyehhhhhhhhh {w=0.3}i was too lazy to."

    gin "I jus' assumed it was like a... {w=0.3}a lil' game? {w=0.3}Or somethin'.."

    bl "Apologies, {w=0.2}my friends, {w=0.2}for leaving but... {w=0.3}uh..."

    bl "I'm not going to touch this one."

    bl "Oh woopsie me! {w=0.3}Another phone call?"

    bl "What a coincidence!! {w=0.3}Let me just..."

    no "He escapes..."

    show rt sad at bounce

    no "Rocktato picks up Mr. Rock, {w=0.3}looking at his Sharpie-scribbled face."

    show img 1 mr rock

    hide bg

    hide wiz

    hide rt

    hide mr

    with dissolve

    rt "You really were here this... {w=0.3}this whole time??"

    mr "{w=0.6}.{w=0.6}.{w=0.6}."

    rt "Man... {w=0.3}Aaaa I'm sorry I didn't notice you."

    rt "It's just... {w=0.3}really hard since you can't talk!"

    rt "Hey, {w=0.3}how about I get you a bell or something!!"

    mr "{w=0.6}.{w=0.6}.{w=0.6}."

    rt "YEAH! {w=0.3}This way I'll notice you more!"

    mr "{w=0.6}.{w=0.6}.{w=0.6}."

    rt "Cookie dough after?? {w=0.3}Heck yeah!"

    show bg black

    hide img

    with dissolve

    no "Rocktato started walking away from the scene and waving to his friends."

    rt "See you guys later!!!"

    space ""

    ph "that was a waste of time."

    $ persistent.episode_fin = 1
