label ep_5:

    $ persistent.mainmenu_img = 5

    stop music fadeout 1.0


    rt "You got any {w=0.4}uhhhhhhhhhhhhhh {w=0.2}23's?????"

    show bg bl office

    show rt happy at Position(xpos=450)

    show bl headempty at flip, Position(xpos=850)

    bl ""

    show bl nervous at flip

    bl "Kid do- {w=0.2}do you know how cards work?"

    show rt happy 2

    rt "Ahah... {w=0.2}no."

    show rt happy

    show bl headempty

    rt ""

    show rt happy 2

    rt "Uh..."

    show rt joy 2

    rt "So what did you do today, Blairic?"

    show bl o

    bl "Oh, {w=0.2}just the usual."

    bl "Climbed a mountain, {w=0.2}repaired the vat that had combusted earlier, {w=0.2}defended myself from a few.... {w=0.2}lawsuits... {w=0.2}sent some aggresively worded letters to my business rival..."

    show rt o

    rt "Woah!! {w=0.2}Cool!"

    show rt nervous

    show bl happy 2

    rt "I uhh... {w=0.2}I ate some cookie dough."

    show rt joy 2

    rt "And now I'm here!!"

    show rt joy

    bl ""

    show bl singsong

    bl "This is nice..."

    show rt happy 2

    rt "Am I winning?"

    show bl nervous

    bl ""

    bl "Well-{w=0.5}{nw}"

    show bl uncomfortable

    show rt headempty

    bl ""

    rt "Whuzzat???"

    show bl gollygee at bounce

    bl "Golly gee!"

    bl "That is the 'I Am Losing Money' alarm!!"

    bl "Quick!"

    show rt o

    rt "Ah!"

    hide bl with easeoutright

    hide rt with easeoutright


    show cg 5 investors with dissolve

    hide bg

    no "Blairic and Rocktato ran outside and saw, {w=0.2}at the building across the street, a huge crowd of people in business suits."

    bl "Oh no!!"

    rt "What is it?"

    bl "All of the investors are swarming the fish factory!!"

    bl "This is terrible!!"

    rt "What's wrong with the fish factory? {w=0.2}I like fish!"

    bl "That is the factory belonging to my BUSINESS RIVAL."

    rt "Oh- {w=0.2}OH YEeaahhh.."

    show bg parkinglot

    show rt confused at Position(xpos=450)

    show bl uncomfortable at Position(xpos=850)

    with dissolve

    rt "Wait Blairic, {w=0.2}what's an investor?"

    rt "I don't really know anything about your 'business' stuff."

    show bl o at bounce

    bl "Oh, {w=0.2}investors give me the money I need to run my meat factory."

    show bl sad

    bl "If they all pull out and start investing in fish, {w=0.2}then my whole operation is ruined!!"

    rt "Couldn't you just... {w=0.2}pay for it yourself?"

    show bl nervous

    bl "Well- {w=0.2}I mean... {w=0.2}Yes..."

    show bl sad

    bl "But they were {b}my{/b} investors..."

    show bl think

    bl "Hm.."

    bl "We may need to consider war."

    show rt o at shake(rate=0.01,strength=3,loop=7)

    rt "WAr?"

    show bl bruh 2

    bl "Shhh..."

    show rt disturbed at shake(rate=0.01,strength=0.3,loop=7)

    show bl bruh

    rt "(ARE YOU GOING TO KILL THEM?)"

    show bl bruh 2

    bl "No."

    show bl bruh

    show rt happy

    rt "(Oh okay.)"

    show bl bruh 2

    bl "Kid, I need you to do me a favor."

    show rt joy 2 at bounce

    rt "Sure thing Blairic!!"

    bl "I need you to sneak into that edifice and see what these people are oogling on about."

    show rt o

    rt "Oooh okay!"

    rt "Lucky for you, {w=0.2}I have saved a special disguise for these spying situations!"

    show rt happy

    show bl fear

    show rt 5 suit at Position(xpos=450) as rtsuit

    no "Rocktato ripped off his skin, {w=0.3}revealing his disguise."

    bl "How did you- {w=0.4}WHAT??"

    show rt 5 suit 2 as rtsuit

    show rt proud

    rt "Alright, {w=0.2}it's GO TIME!"

    show fx black with dissolve

    no "Rocktato slithered through the crowd of business nerds and made his way to the lobby."

    hide bl

    show bg bl lobby

    show rt happy at Position(xpos=200)

    show rt 5 suit at Position(xpos=200) as rtsuit

    hide fx with dissolve

    rt ""

    show rt happy 2

    rt "Why does this place look exactly like Blairic's???"

    rt "Seriously, {w=0.3}there's even a Blairic statue there lol."

    show rt o at bounce

    show rt 5 suit at bounce as rtsuit

    rt "!"

    show bg at Position(xpos=500)

    show rt at Position(xpos=50)

    show rt 5 suit as rtsuit at Position(xpos=50)

    with ease

    wiz "HEH HEERHHH!!!!"

    show wiz evil 2 at Position(xpos=600, ypos=605) with easeinbottom

    wiz "TRY THE NEW FISH STICKS... {w=0.2}ON A FISH STICK!!!"

    Character("Investor", size=30, callback=no_blip) "Isn't that just.. {w=0.4}two {w=0.4}fish st-{w=2.0}{nw}"

    show rt happy

    show wiz evil 3 with hpunch

    wiz "Hahah! {w=0.2}Shut up!"

    show wiz happy

    wiz "Ignore that, {w=0.2}you other investor. {w}Would you like to try a-"

    show bg at Position(xpos=700)

    show rt at Position(xpos=200)

    show rt 5 suit as rtsuit at Position(xpos=200)

    with ease

    wiz ""

    show wiz screaming at shake(rate=0.01,strength=3,loop=5) with hpunch

    wiz "WHA??"

    show rt o

    rt "Yo Wiz! {w}You're working at a- {w=0.2}a fish factory now????"

    show rt 5 suit 2 as rtsuit

    show rt nervous

    rt "Bit of a weird choice, {w=0.2}but I support you!"

    show wiz nervous

    wiz "I'm just uhh.... {w=0.2}trying something new!!!"

    wiz "Definitely no scheming going on!"

    wiz "Ha... {w=0.2}ha..."

    wiz "I just.. {w=0.2}{nw}"

    show wiz at shake(rate=0.01,strength=5,loop=5)

    extend "LOVE FISH MAN!!!!"

    show wiz preach

    wiz "I'm a CHIEF ADMINISTRATIVE OFFICER... {w=0.2}{nw}"

    show wiz sad 2

    extend "whatever that means."

    show wiz smug

    wiz "Cool isn't it?"

    show wiz o

    extend " Anyway, {w=0.2}what are you doing here?"

    show rt joy 2

    rt "Oh.. {w=0.2}my buddy Blairic runs the meat factory across the street. {w}Y'kno, {w=0.2}the one called The Meat Factory?"

    show rt 5 suit as rtsuit

    show rt o

    rt "Think he miiiiiight wage war against your boss... {w=0.2}so... {w=0.2}that's somethin'..."

    show wiz evil 2 at bounce

    wiz "OHOHOHOHO {w=0.2}COMPETITION???"

    wiz "Sounds SPICY!!! {w=0.2}I can't wait!!!"

    show wiz o

    wiz "This Blairic guy... {w}do you work for him??"

    show rt 5 suit 2 as rtsuit

    show rt joy 2

    rt "Oh.. {w=0.2}we're just pals."

    show rt 5 suit as rtsuit

    show rt o

    rt "But I feel like a fun adventure can spout from this."

    show rt 5 suit 2 as rtsuit

    show rt proud

    rt "So, {w=0.2}y'know what Wizpotato and the guy you work for??"

    show rt 5 suit at bounce as rtsuit

    show rt smug at bounce

    rt "Blairic and I are gonna BEAT YOUR FACES!!!"

    show rt sad 2

    rt "In.. {w=0.2}uh.. {w=0.2}business.."

    rt "Your metaphorical faces.."


    hide wiz

    show bg bl office

    show bl bruh at flip, Position(xpos=850)

    show rt joy 2 at Position(xpos=450)

    show rt 5 suit 2 at Position(xpos=450) as rtsuit

    rt "And that's what I said to Wizpotato!"

    show bl bruh 2 at flip

    bl "You- {w=0.5}*sigh*"

    bl "That does not really help us right now.."

    bl "In fact, {w=0.2}that completely removes our advantage since you told them that war was imminent."

    show rt 5 suit as rtsuit

    show rt sad 2

    rt "Woops."

    bl "They are going to start preparing now."

    bl "It is imperative that we strike NOW,{nw}"

    show bl angry at shake(rate=0.01,strength=4.3,loop=3)

    extend " {w=0.2}while they still aren't ready."

    show rt joy 2

    show rt 5 suit 2 as rtsuit

    rt "YEAH!!!"

    show bl thankful

    bl "Was that good? {w}I normally am not the type to hit tables."

    show rt proud

    rt "When you're fired up (and rich), you can hit whATEVER THE HECK YOU WANT!!"

    show rt 5 suit as rtsuit at flip, Position(xpos=200), shake(rate=0.01,strength=5,loop=5)

    show rt happy 2 at flip, Position(xpos=200), shake(rate=0.01,strength=5,loop=5)

    rt "GAHHH!!"

    show bl bruh

    bl ""

    show rt 5 suit at Position(xpos=450) as rtsuit

    show rt at Position(xpos=450)

    show bl bruh 2

    bl "Was it necessary to hit a WINDOW OF ALL THINGS?"

    bl "Out of every possible item in this room, {w=0.2}that is the hardest to repair."

    show rt sad 2

    rt "Double woops."

    show bl bruh 2 at reverse_flip

    bl "I shall go call a repairman. {w}While I do that, {w=0.2}what action do you recommend we take?"

    show rt o

    show bl bruh

    rt "Oh... {w=0.2}your asking ME for advice lol?"

    show bl bruh 2

    bl "*You're."

    show bl bruh

    rt ""

    rt "Shut up.!"

    rt "Hm.. {w=0.2}advice.."

    rt "Well, {w=0.2}when I first talked to Wiz, {w=0.2}it seemed he was offering samples of a product called 'Fish Sticks on a Fish Stick.'"

    show rt 5 suit 2 as rtsuit

    show rt confused

    rt "It's really stupid, {w=0.2}right?"

    rt "But the investors just ATE that stuff up!! {w}Literally!"

    rt "We just need to give them something new... {w=0.2}and hip!"

    show rt 5 suit as rtsuit

    show rt smug

    rt "Especially if it's just... {w=0.2}kinda useless!"

    show bl o

    bl "Ahh, {w=0.2}I see!!"

    show bl think

    bl "Hm, {w=0.2}here is a proposal.."

    bl "Instead of Meat in a Can, {w=0.2}what about..."

    show bl evil

    bl "Meat in a TRASHCAN!!"

    show rt joy 2

    show rt 5 suit 2 as rtsuit

    rt "YEAH!!!"


    hide rt

    hide rtsuit

    hide bl

    show wiz o at Position(xpos=450, ypos=605)

    wiz "Boss!"

    extend " It seems like The Meat Factory has just released a new product called... {w=0.2}{nw}"

    show wiz uncomfortable at bounce

    extend "Meat in a TRASHCAN???"

    wiz "And the people LOVE IT!"

    bw_que "Hmm.."

    show bw shady at flip, Position(xpos=850) with easeinbottom

    bw_que "It seems those fools are trying to strike before we're ready."

    bw_que "Little do they know, {w=0.2}THEY'RE the ones who are unprepared."

    show wiz o

    wiz "Is it time to realse the uhh.. {w=0.2}the thing?"

    show bw at bounce

    bw_que "Indeed it is..."


    hide wiz

    hide bw

    show bl bruh 2 at flip, Position(xpos=850)

    show rt o at Position(xpos=450)

    show rt 5 suit at Position(xpos=450) as rtsuit

    bl "Diet Fish in a Can: Fish in a Can ZERO."

    show rt confused

    show rt 5 suit 2 as rtsuit

    rt "What??? {w}And people are... {w=0.2}into that???"

    bl "Yeah..."

    show rt hurt

    show rt 5 suit as rtsuit

    with hpunch

    rt "WHO THE HECK LIKES DIET FOOD???"

    rt "Erg- {w=0.2}I think I'm gonna vomit."

    show rt disgusted

    show rt 5 suit 2 at Position(xpos=450) as rtsuit

    rt "The thought of diet food makes my stomach {nw}"

    show rt disgusted at shake(0.02, 6, 2)

    show rt 5 suit 2 at shake(0.02, 6, 2) as rtsuit

    extend "BOIL."

    show bl sad at flip

    bl "I wish I had a stomach..."

    show rt joy 2 at bounce

    show rt 5 suit 2 as rtsuit at bounce

    rt "OOOO! {w=0.2}HERE'S AN IDEA!"

    show rt o

    show rt 5 suit as rtsuit

    rt "Y'kno how there's all those burgers and meats that are actually made of vegetables???"

    rt "What about.. {w=0.2}vegetables that are actually made of meat?"

    show bl headempty

    bl ""

    show bl bruh 2

    bl "What- {w=0.2}what point does that serv-{w=0.6}{nw}"


    hide bl

    hide rt

    hide rtsuit

    show wiz sus 2 at Position(xpos=450, ypos=605)

    show bw shady at Position(xpos=850)

    wiz "Vegetables made of meat???"

    show wiz smug at bounce

    extend " Gotta hand it to 'em, {w=0.3}that's genius!!"

    show bw at flip, shake(0.02, 4)

    bw_que "Seriously?"

    show wiz bruh

    wiz "Alright, {w=0.2}alright."

    show wiz screaming at shake(0.03, 7)

    hide cg

    wiz "RELEASE THE-"


    hide wiz

    hide bw

    show bg black

    show cg 5 reactions 1 at hpunch

    rt "Fish PIZZA??!"

    rt "(MMmpph this is good,,)"


    show cg 5 reactions 2 at hpunch

    bw_que "Growable meat; {w=0.2}just add water.."

    wiz "BOSS??"

    wiz "I THINK I ADDED TOO MUCH WATER??!"

    wiz "AAAA-{w=0.2}{nw}"


    show cg 5 reactions 3 at hpunch

    bl "Fooshy chair?"

    bl "What is a fooshy..?"


    show cg 5 reactions 4 at hpunch

    bw_que "Meat vapor??"

    wiz "Why."


    show cg 5 reactions 5 at hpunch

    bl "Fish scented candles???"

    bl "I wish I had a nose."

    rt "No you don't!"

    rt "This stink is hurting my brain!"

    no "He tosses the candle into the trash."

    rt "Okayokay.. {w=0.3}y'know what?"

    bl "What?{w=0.3}{nw}"

    rt "I got a really, {w=0.2}REALLY good one!"

    rt "Ready? {w}It's {w=0.2}a-"


    hide cg

    show bg bl office

    show wiz sus 2 at Position(xpos=850, ypos=605)

    show bw shady at Position(xpos=450)

    wiz "Meat hypercube???"

    show wiz screaming

    wiz "Okay, {w=0.2}how are we going to beat MEAT HYPERCUBE??"

    show bw at bounce, flip

    bw_que "..."

    bw_que "It's time for our final contingency plan."

    show wiz uncomfortable at shake(0.05, 4)

    wiz "But b-Sir... {w=0.2}Can't we launch my new idea? {w}Fish Stick in a Fish Stick in a Fish Stick in a Fish Stick in a Fish Stick in a Fish Stick in a Fish Stick in a Fish Stick in a Fish Stick in a Fish Stick in a Fish Stick in a Fish Stick in a Fish Stick in a Fish Stick in a Fish Stick in a Fish Stick in a Fish Stick in a Fish Stick in a Fish Stick in a Fish Stick in a Fish Stick in a Fish Stick in a {nw}"

    show wiz sad

    bw_que "It's the only way.."

    show wiz sad at flip

    wiz ""

    show wiz sans at flip

    wiz "So we've really stooped this low.."


    hide wiz

    hide bw

    show bl headempty at flip, Position(xpos=850)

    show rt mad at Position(xpos=450)

    show rt 5 suit at Position(xpos=450) as rtsuit

    rt "CUTE AND CHEAP FISH MARKETABLE PLUSHIES??? {w}HOW???"

    show bl gollygee at flip, bounce

    bl "Gahh! {w=0.2}How come WE did not think of that?"

    show bl sad

    bl "Well, {w=0.2}I sure am stumped."

    show rt confused

    show rt 5 suit 2 at Position(xpos=450) as rtsuit

    rt "Yeah... {w=0.2}this is... {w=0.4}mmm..."

    rt "We can't just launch new products anymore."

    rt "The demand for useless variations of meat and fish has gone down!!"

    show bl think

    bl "Well.. {w=0.2}the company had only started booming when Wizpotato came into the picture."

    bl "What if we took him... {w=0.5}well... {w=0.5}{nw}"

    show bl takemeouttodinnerfirst at reverse_flip

    extend "out of the picture-"

    show rt waah at shake(0.02, 4.5, 4)

    show rt 5 suit as rtsuit at shake(0.02, 4.5, 4)

    rt "You want to KILL HIM???"

    show bl gollygee at flip, bounce

    bl "NO! {w}No, {w=0.3}no, {w=0.3}not at all."

    show rt bruh

    show bl nervous at flip

    bl "We could, {w}simply, {w}well,"

    show bl takemeouttodinnerfirst

    extend " kidnap him?"

    rt "Look, {w=0.2}I like being funny as much as the next guy, {w=0.2}but Wizpotato is my friend!"

    show rt mad at bounce

    show rt 5 suit as rtsuit at bounce

    rt "Kidnapping someone is mean!"

    show bl bruh 2

    bl "Fine... {w=0.2}what else can we do?"

    show rt o

    rt "Okok how about this: {w}we could try to... {w=0.2}get them to go against each other??"

    show rt joy 2 at bounce

    show rt 5 suit 2 as rtsuit at bounce

    rt "Let's emotionally manipulate them!"

    rt "That's morally better than kidnapping!"

    show bl evil

    bl "Yes! {w=0.2}I like your thinking."

    show fx black with dissolve

    space ""


    hide rt

    hide rtsuit

    hide bl

    hide fx

    wiz "HOOH... "

    show wiz evil 2 at Position(xpos=450, ypos=605) with easeinleft

    extend "it's been a loooong day at the fish factory."

    show wiz o

    no "Wizpotato noticed a letter on his desk"

    no "It was addressed to his boss; {w}it must have ended up there by mistake."

    show wiz smug

    no "But whatever. {w=0.4}Might as well take a peak, {w=0.3}he thought.."

    show wiz sus

    show bl singsong at flip, Position(xpos=600), transform_transparency with dissolve

    bl "{i}To the big bossguy of The Fish Factory:{/i}"

    show bl happy 3 at flip, bounce

    bl "{i}I am happy to say that we here at The Meat Factory accept your request to merge our companies!{/i}"

    bl "{i}As you know, {w=0.3}all of your employees will sadly be fired so that we may guarantee the best and most loyal workers!{/i}"

    show bl happy 2

    show wiz uncomfortable

    bl "{i}Thank you. {w=0.4}Sincerely, {w=0.2}Blairic.{/i}"

    show wiz sad

    show bl nervous

    bl "{i}P.S.: {w}Do you want to maybe have dinner sometime?{/i}"

    hide bl with dissolve

    show wiz sad 2

    wiz ""

    wiz "What-"


    hide wiz

    hide bl

    show bg parkinglot at center

    show bw shady at Position(xpos=600)

    bw_que "We're going to have ALL the rollercoasters. {w}ALL of them!!"

    show wiz happy at flip, Position(xpos=250, ypos=605) with easeinleft

    wiz "Hey.. {i}buu{w=0.2}dd{w=0.2}yy{w=0.2}y{w=0.2}yy{w=0.2}yy{/i},"

    show wiz angey 2

    extend " care to explain this??"

    show bw at flip

    bw_que "C'mon, kid, {w=0.3}I'm in the middle of a speech!"

    bw_que "What is this anyway?"

    bw_que "Hmm.."

    show bw at bounce

    bw_que "Would you mind if I went to dinner with him?"

    show wiz screaming at shake(0.01, 5, 3)

    wiz "SHUT UP! {w=0.3}THAT'S NOT THE PROBLem!"

    show wiz angey 2

    wiz "You're going to merge companies?? {w=0.3}WITH THE ENEMY?"

    wiz "Are you just.. {w=0.2}giving up?"

    show bw at reverse_flip

    bw_que "Alright, {w=0.3}{i}b{w=0.2}u{w=0.2}d{w=0.2}d{w=0.4}y{/i}.."

    bw_que "Clearly the farts over at the- {w=0.3}the {w=0.4}FART factory sent this fake letter just to try to cause infighting."

    bw_que "They ran out of ideas and now they're just playing dirty."

    show wiz sus 2

    wiz "How do I know you aren't just saying that, though?"

    show bw at flip, shake(0.01, 5, 1)

    bw_que "This is handwritten!!! {w}You know I don't like using hands!!!"

    bw_que "How do I know YOU'RE not messing with ME?"

    show wiz angey 2 at bounce

    wiz "I- {w=0.3}I DON'T EVEN HAVE HANDS??!"


    show cg 5 telescope with dissolve

    no "While the two continued to bicker and argue, Blairic and Rocktato were watching through a telescope."

    bl "Was asking him to dinner absolutely necessary?"

    rt "OHoh.. {w=0.3}and you doooon't want to go to dinner with him?"

    bl "That is irrelevant."

    bl "At least the plan is working; {w=0.3}they are certainly quarreling."

    rt "How do you know they aren't just arguing about... {w=0.2}something- {w=0.2}something else?"

    bl "Simple! {w=0.5}I put a tiny recording device in the letter!"

    rt "That's a bit creepy dude."

    bl "I want to get a closer look.."

    show fx black with dissolve

    show wiz screaming

    show bw shady at spinny(2)

    no "The two snuck into the crowd."

    hide cg

    hide fx

    show bl bruh at flip, Position(xpos=1250)

    show rt sad at Position(xpos=1080)

    show rt 5 suit at Position(xpos=1080) as rtsuit

    with easeinbottom

    no "At this point, {w=0.2}the argument was getting intense."

    wiz "Y'know what?"

    show wiz at shake(0.03, 9, 4)

    wiz "SCREW YOU, DUDE!!!"

    hide bw

    show bw shady at flip, Position(xpos=600)

    wiz "I'm taking this joint for MYSELF!!"

    show wiz evil

    wiz "Hehh.."

    show wiz evil 2 at shake(0.03, 5, 10)

    wiz "HEHEHEHEHHEHEHHEHERRRHHH!!!!"

    show wiz at bounce

    no "Wizpotato raised his nonexistent arm, {w=0.2}and a dark shadow cast above the area."

    no "The crowd grew restless.."

    bw_que "What..."

    show bw at flip, shake(0.03, 2, 15)

    bw_que "Wizpotato... {w=0.2}what in FISH FLAKE'S NAME are you doing?"

    show wiz preach

    wiz "Well, {w=0.2}Mr. Bossman..."

    wiz "Or.. {w=0.2}should I say... {w=0.2}{nw}"

    show wiz evil 2 at shake(0.03, 30, 4) with hpunch

    extend "MR. LOSER?!"

    show rt o

    show bl o at flip

    no "The crowd gasped!"

    show wiz angey

    wiz "Ever since I had joined this company, {w=0.2}I always had this nagging feeling."

    wiz "Something was missing."

    show wiz o at flip, Position(xpos=170) with ease

    wiz "Only now do I realize... {w=0.2}the only thing missing was ME!!!"

    wiz "Well, {w=0.2}more like my uhh.... {w}my leadership."

    show wiz fsh at flip

    wiz "Point is... {w}uh.... {w}Lemmejust.."

    wiz "MMmg"

    show cg 5 dropped 1

    no "Suddenly, {w=0.2}anOTHER FACTORY WAS DROPPED ON TOP OF THE FIRST FACTORY!!"

    show cg 5 dropped 2

    wiz "There will be NO MORE FISH FACTORY!"

    wiz "Now, {w}there is only, {w}WIZPOTATO'S SCRAMBELED EGG IN A CAN FACTORY!!!"

    wiz "There will be scrambled eggs in a can, {w=0.3}scrambled eggs in a can with sprinkles, {w=0.3}scrambled eggs in a JERRYCAN, {w=0.3}BABY scrambled eggs in a can: WITH BABIES..."

    wiz "SCRAMBLED EGGS IN A CAN IN A CAN IN A CAN IN A CAN IN A CAN IN A CAN IN A CAN IN A CAN IN A CAN IN A CAN IN A CAN IN A {nw}"

    bl "We need to get out of here.."

    rt "Agreed..."

    show fx black with dissolve

    wiz "HERRHERHHRHEHRHRHEHRERH!!!"

    hide cg

    hide wiz

    hide bw

    hide bl

    hide rt

    hide rtsuit

    hide bg

    wiz "{b}HERHEHREHRHERHEHREHRHERHEHREHREHRHHHHEHRHEHHHHHH{/b}{nw}"


    show bg bl office

    show bl disturbed at flip, Position(xpos=850)

    show rt sad at Position(xpos=450)

    show rt 5 suit at Position(xpos=450) as rtsuit

    bl "..{w=0.2}."

    bl "Well..."

    rt "Well...?"

    show rt nervous at bounce

    show rt 5 suit 2 at bounce as rtsuit

    rt "It- {w=0.2}it worked?"

    bl "Yes, but, {w=0.2}who knows what Wizpotato will do?"

    show bl gollygee at flip

    bl "He could destroy this factory next!"

    show rt bruh

    show rt 5 suit as rtsuit

    rt "He wouldn't... {w=0.2}that's too predictable."

    rt "He's bound to do something even worse."

    show rt disgusted

    show rt 5 suit 2 as rtsuit

    rt "Like... {w=0.2}{b}wet socks.{/b}"

    show bl headempty

    bl "What- {w=0.2}I- {w=0.2}ok..."

    show bl o

    bl "You know him best."

    bl "What do you think he will do?"

    show rt o at bounce

    show rt 5 suit as rtsuit at bounce

    rt "I dunno!"

    show bl bruh

    rt "Dude is super fickle."

    show rt happy

    rt "Ooo.. {w=0.2}I like that word..."

    show rt happy 2

    rt "{b}Fickle~{/b}"

    show rt o at flip, bounce

    show rt 5 suit as rtsuit at flip, bounce

    show bl o at bounce

    bw_que "I believe I may be of some assistance."

    show rt at flip, Position(xpos=800)

    show rt 5 suit at flip, Position(xpos=800) as rtsuit

    show bl at Position(xpos=1100)

    with ease

    show bw shady at Position(xpos=180) with easeinleft

    space ""

    show rt confused at flip

    show rt 5 suit 2 at flip as rtsuit

    rt "Th..."

    rt "The boss guy??"

    show bw cross with dissolve

    space ""

    bw "Eyeah"

    show rt hurt at bounce

    show rt 5 suit at bounce as rtsuit

    rt "WH- {w=0.2}HOW DID YOU GET IN HERE???"

    show bw champ

    bw_que "The window, {w=0.2}obviously. {w=0.2}It was the fastest way!"

    show bl bruh 2

    bl "You- {w=0.2}I JUST GOT THAT REPAIRED!!!"

    bl "I-{w=0.2}it is no matter."

    bl "What do you want, {w=0.2}Bowser?"

    show bl bruh

    show rt o

    rt "Bowser is your name???"

    rt "That is.. {w=0.2}spicy..."

    show bw cross

    show rt headempty

    bw "I want to help you take down that imbecile so I can get my factory back."

    show bl bruh 2

    bl "Why though?"

    bl "You have always been the biggest threat to my business operations."

    bl "Why would we want to grant you your power back?"

    show bl bruh

    show bw at flip

    bw "Really?"

    bw "Because, {w=0.2}from what you fellas were saying, {w=0.2}it seems like {b}Wizpotato{/b} is your new 'biggest threat.'"

    show bw at reverse_flip

    bw "Like you guys said, {w=0.2}there's no way to predict what he's going to do next."

    show bw hold 2

    bw "Which is why you need my help."

    bw "See, {w=0.2}there is a self-destruct system in my factory."

    bw "And, {w=0.2}since it's underneath the new establishment, {w=0.2}it's bound to blow that up too!"

    bw "We can just say it was an accident! {w}If we are sneaky enough, {w=0.2}no one will know!"

    show bl think

    bl "Hmm.."

    show bw cross

    bw "Look, {w=0.2}when this is all over, {w=0.2}I'll back down for a bit, {w=0.2}let you have your stupid investors back."

    bw "I just want to have my factory back."

    show bw up

    bw "Well, {w=0.2}it will be blown up."

    show bw cross

    bw "But I want the land to rebuild it!"

    show bw at flip

    bw "Look, {w=0.2}it hurts me to work with you as much as it hurts you..."

    show bl yeahok

    bl "No.. {w=0.2}not really."

    show bw at reverse_flip

    bw "Aw..."

    bl "Do you think this is hurting my pride or anything?"

    bl "I do not hold even a smidge of respect for you."

    bw "Jesus Christ, man."

    bl "I just needed to figure out if I could trust you.."

    show bl bruh

    bl "..."

    show bl bruh 2

    bl "I guess I will, {w=0.2}for now.."

    bl "What is your plan?"

    show bl bruh

    bw "I have something in mind.."

    show bw up at Position(xpos=400) with ease

    bw "And this friend of yours can help us."

    bw "They seem very stealthy."

    rt ""

    show rt o

    rt "Ah- {w=0.2}what?"

    rt "I wasn't paying attention."

    show bw at flip

    hide fx

    bw "Hmm.. {w=0.2}here's the run down.."


    show fx black with dissolve

    space ""

    hide rt

    hide rtsuit

    hide bg

    hide bl

    hide bw

    show bg parkinglot with dissolve

    no "The time was 9 PM."

    show rt happy at Position(xpos=400)

    show rt 5 suit as rtsuit at Position(xpos=400)

    with easeinbottom

    no "Rocktato was at the back side of Wizpotato's new factory, {w=0.2}hiding in a bush."

    no "The two business guys guided him through an earpiece."

    bw "Alright, so you just need to dig down until you find the original building."

    show rt confused at bounce

    show rt 5 suit 2 as rtsuit at bounce

    rt "What? {w=0.2}How??"

    bl "There is a button in your earpiece. {w}Press it."

    show rt headempty at bounce

    show rt 5 suit as rtsuit at bounce

    no "The earpiece summoned a shovel!"

    show rt bruh

    rt "You- {w=0.2}you coulda just given it to me in the first place."

    rt "Or, {w=0.2}better yet, {w=0.2}gave me a{nw}"

    show rt o

    extend " GUN."

    show rt bruh

    bl "For the last time, {w=0.2}you are not allowed to play with FIREARMS."

    rt "Psh {w=0.5}whatever..."

    hide rt

    hide rtsuit

    with easeoutbottom

    space ""

    show bg bl hallway ground

    no "Rocktato dug down until he fell onto a floor."

    show rt hurt at Position(xpos=400, ypos=900)

    show rt 5 suit as rtsuit at Position(xpos=400, ypos=900)

    with easeintop

    rt "OUGH!!"

    show rt confused at Position(ypos=720)

    show rt 5 suit 2 as rtsuit at Position(ypos=720)

    rt "Well, {w=0.2}I'm here."

    rt "Now what?"

    bw "We need to check something. {w}You're on Floor 20, {w=0.2}right?"

    rt "Uhh... {w=0.2}it's a little hard to see..."

    bl "You see that button on the shovel? {w}Press it."

    show rt o at bounce

    show rt 5 suit as rtsuit at bounce

    no "It summoned a flashlight."

    rt "Alright!"

    rt "Iiiiiiitt looks like{nw}"

    show rt happy 2

    extend " I am!!! {w=0.2}On Floor 20..."

    bw "Okay, {w=0.2}just keep searching for the Presidential Suite."

    show rt o at transform_easein_offset(x=650, y=0, tom=120)

    show rt 5 suit as rtsuit at transform_easein_offset(x=650, y=0, tom=120)

    rt "Whaaat..."

    bw "Yeah, {w=0.2}I built a Presidential Suite for myself.. {w}Your man's gotta stay cool and fancy, {w=0.2}so what?"

    show rt confused

    show rt 5 suit 2 as rtsuit

    rt "Trueee.. {w=0.2}but why would you put the self destruct there?"

    bw "Just {w=0.4}in {w=0.4}case?{w=0.5}?"

    show rt sad

    show rt 5 suit as rtsuit

    bw "Okay.. {w=0.2}just.. {w=0.2}you'll find a lever there that says 'self destruct' in big, bold, red text."

    bw "Easy enough, {w=0.2}right?"

    show rt sad 2

    rt "Yeah.."

    show rt sad

    bw "And, {w=0.2}if all else fails, {w=0.2}you can just set the room on fire."

    bw "It's filled with explosives that will set off the rest of 'em."

    show rt sad 2

    rt "Why?"

    show rt sad

    bw ""

    bw "Yeah..."

    show rt nervous

    show rt 5 suit 2 as rtsuit

    rt "Well, {w=0.2}I really hope it doesn't come to that."

    show rt joy 2

    rt "Other wise, {w=0.2}I'll have to use the matches in my pocket."

    bl "..."

    bl "Why do you have..."

    show rt sad

    show rt 5 suit as rtsuit

    bl "Kid, {w=0.2}we are going to have a talk later."

    show rt nervous

    show rt 5 suit 2 as rtsuit

    rt "Yeah, {w=0.2}yeah.."

    show rt o at none, Position(xpos=1050), transform_offset(x=0, y=0, speed=0.0)

    show rt 5 suit as rtsuit at none, Position(xpos=1050), transform_offset(x=-0, y=0, speed=0.0)

    with ease

    rt "Anyway, I found it, {w=0.2}but it's locked."

    rt "How do I..."

    bl "You see that button on the flashlight? {w}Pre-{w=0.5}{nw}"

    show rt bruh

    rt "Okay, {w=0.2}I get the point."

    hide fx

    no "The flashlight morphed into a key."

    show fx black with dissolve

    no "Rocktato slowly opened the door.."

    hide rt

    hide rtsuit

    show bg 5 pressuite 1

    hide fx black with dissolve

    show rt uncomfortable at Position(xpos=550)

    show rt 5 suit 2 as rtsuit at Position(xpos=550)

    with easeinleft

    rt ""

    show rt headempty at bounce

    show rt 5 suit as rtsuit at bounce

    wiz "Well, {w=0.2}well, {w=0.2}well..."

    show wiz smug at Position(xpos=1000, ypos=605) with dissolve

    space ""

    show rt waah at bounce

    show rt 5 suit as rtsuit at bounce

    rt "WIZPOTATO???"

    rt "How did... {w=0.2}HOW DID YOU KNOW ABOUT THE LEVER??"

    show wiz preach

    wiz "It's quite simple."

    wiz "I was Chief of...{w=0.2}{nw}"

    show wiz confused

    extend " SOMETHING (?){w=0.2}{nw}"

    extend " at the fish factory place thing that weirdly doesn't have a company name..."

    show wiz preach

    wiz "So, OBVIOUSLY I know the in's and out's of the place."

    wiz "And I just KNEW that you would be here."

    show wiz evil 2

    wiz "My, {w=0.2}my, {w}played you like an absolute FOOL!"

    show wiz evil 3 at bounce

    wiz "HerhHERH HERHHERHH!!"

    show wiz at bounce

    no "Wizpotato grabbed hold of the lever, {w=0.2}and BROKE IT OFF THE WALL!!"

    show rt at bounce

    show rt 5 suit as rtsuit at bounce

    rt "GASP!"

    rt "OH YOU DIDN'T!"

    show rt happy

    rt "Well.."

    rt "I guess it's come to this!"

    show rt happy 2 at bounce

    show rt 5 suit as rtsuit at bounce

    no "Rocktato grabbed a matchbox from his pockets, {w=0.2}and held it above his head."

    show wiz sus 2

    wiz "You... {w=0.2}wouldn't.."

    show rt proud

    show rt 5 suit 2 as rtsuit

    rt "Uhhuh...."

    no "Rocktato smirked while stricking the match."

    show rt headempty

    show rt 5 suit as rtsuit

    bl "Rocktato... {w=0.2}this is not a good idea-"

    show rt uncomfortable

    show rt 5 suit 2 as rtsuit

    rt ""

    rt "I've taken too many L's this week."

    show rt joy 2 at bounce

    show rt 5 suit 2 as rtsuit at bounce

    rt "YOU!!"

    show rt o at bounce

    show rt 5 suit as rtsuit at bounce

    rt "ARE NOT GETTING!!"

    show rt proud at bounce

    show rt 5 suit 2 as rtsuit at bounce

    rt "THIS FACTORY!"

    show bg 5 pressuite 2 with dissolve

    show rt at bounce

    show rt 5 suit 2 as rtsuit at bounce

    show wiz uncomfortable at bounce

    no "He dropped it, {w=0.2}setting a small part of the floor."

    wiz "OKAY, {w=0.2}I ACTUALLY WASN'T EXPECTING THAT."

    show wiz sad 2

    wiz "Well, {w=0.2}it seems I lost this one, then."

    show wiz at bounce

    no "Wizpotato flipped a lever on the floor, {w=0.2}and out his hat grew a propeller!"

    show wiz evil 2

    wiz "But, {w=0.2}LET'S SEE YOU GET OUT OF THIS! {w}HERH HERHHERHHERHHHHH!!!"

    show rt headempty

    show rt 5 suit as rtsuit

    show wiz at transform_easeout_offset(x=0, y=-1000, tom=0.4)

    no "And with that, {w=0.2}he propelled through the ceiling, {w=0.2}through the ground, {w=0.2}and into the night sky."

    show rt waah at bounce

    show rt 5 suit as rtsuit at bounce

    rt "OH JEEZ!!"

    rt "YEAH, {w=0.2}HOW AM I GONNA ESCAPE?"

    show rt troubled

    bl "Okay, {w=0.2}luckily I have prepared you for this situation."

    bl "See the button on the key-"

    show rt waah

    hide fx

    rt "YEAH, {w=0.2}YEAH, {w=0.2}THANK YOU!!"

    show fx black with dissolve

    rt "Guhh... {w=0.2}the button is so small..."

    hide rt

    hide wiz

    hide rtsuit

    space ""

    $ renpy.block_rollback()

    $ saveable = False

    $ renpy.movie_cutscene("ep images/5/vid 5 explosion.webm")

    # play audio simoultaneously with movie


    $ renpy.block_rollback()

    $ saveable = True

    space ""

    wiz "ROCKTATO!?"

    #rewrite this later

    hide fx

    show rt hurt at Position(xpos=500, ypos=800)

    show wiz uncomfortable at Position(xpos=1000, ypos=605)

    show bg 5 aftermath

    rt "WAHHHHHHHH???"

    show wiz screaming at transform_easein_offset(x=150, y=500, tom=0.3), transform_rotate(degs=30.0, speed=0.3)

    wiz "AHAHGHHGHGHGHHG!!!!??"

    wiz "OH MY GOD!!"

    show rt headempty

    no "Wizpotato fell over."

    rt "W- {w=0.2}woops.."

    rt "Sorry..."

    hide wiz

    show wiz sad 2 at bounce, Position(xpos=1000, ypos=605)

    wiz "Guhh.."

    wiz "Don't... {w=0.2}worry about it.."

    show wiz screaming at shake(0.02, 2.5, 2)

    wiz "DuDE, {w=0.3}WHAT HAPPENED?"

    show wiz uncomfortable

    wiz "Are you okay???"

    wiz "Does anything hurt?"

    rt ""



    rt "I'm.. {w=0.2}fine..."

    rt "I think I'm not... {w=0.2}too badly.. {w=0.2}injured."

    rt "That's- {w=0.2}hah.. {w=0.2}lucky."

    rt "Let's... {w=0.2}try to get out of this rubble."

    wiz "Alright."

    no "Wizpotato tried to help Rocktato up, {w=0.2}but they fell right back down again."

    rt "GAH!!"

    wiz "CRAP!!"

    wiz "What is it?"

    rt "I think my leg's broken."

    wiz "Oh..."

    wiz "Oh no..."

    rt "Well this stinks."

    rt "Ahah...."

    bl "ROCKTATO!!"

    no "Blairic and Bowser arrived at the scene."

    bl "..."

    bl "Kid..."

    space ""

    # if persistent.episode_fin == 4:
    #     $ persistent.episode_fin = 5
    #
    # $ persistent.mainmenu_img = 6


    return()
