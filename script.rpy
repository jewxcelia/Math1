#################################################
##Images
##Images bg
image bg school = "school.jpg"
image bg wall = "wall.jpg"
image bg bedroom Alice = "alice-room.jpg"
image bg bedroom Rebecca = "rebecca-room.jpg"
image bg shelter = "shelter.jpg"

##Images of items
image mirror Alice = "mirror1.png"
image mirror Rebecca = "mirror2.png"
image mirror broken = "broken-mirror.png"

##Daytime filters
image filter morning = "morning-filter.png"
image filter evening = "evening-filter.png"
image filter night = "night-filter.png"
###################################################
##Characters
init:
    $ a = Character(u"Alice",
            color="#ffb6c1",
            who_outlines=[ (2, "#ffffff") ] )

    $ r = Character(u"Rebecca",
        color="c456c4",
        who_outlines=[ (2, "#ffffff") ] )

    $ b = Character(u"Brandon",
        color="000000",
        who_outlines=[ (2, "#ffffff") ] )

    $ c = Character(u"Caroline",
        color="f7c316",
        who_outlines=[ (2, "#ffffff") ] )



##Images of characters

#Alice
image Alice normal = "alice-normal.png"
image Alice angry = "alice-angry.png"
image Alice shocked = "alice-suprised.png"
image Alice cry = "alice-cry.png"
image Alice Rebecca-turned = "rebecca-normal.png"
image Alice Rebecca-turned-cry = "rebecca-cry.png"
image Alice pj angry = "alice-pj-angry.png"
image Alice pj sad = "alice-pj-sad.png"

#Rebecca
image Rebecca normal = "rebecca-normal.png"
image Rebecca shocked = "rebecca-shocked.png"
image Rebecca cry = "rebecca-cry.png"
image Rebecca shy1 = "rebecca-shy1.png"
image Rebecca shy2 = "rebecca-shy2.png"
image Rebecca asleep = "rebecca-asleep.png"


#Brandon
image Brandon normal = "brandon-normal.png"
image Brandon bored = "brandon-bored.png"
image Brandon shy = "brandon-shy.png"

#Caroline
image Caroline normal = "caroline-normal.png"
image Caroline shocked1 = "caroline-shocked1.png"
image Caroline shocked2 = "caroline-shocked2.png"
image Caroline sad = "caroline-sad.png"

##Start
label start:

    scene bg school
    with fade

    "All lesons were over."
    show Alice normal at right
    a "I'm so tired of school. Only a jerk can enjoy this place."
    a "At least it is not a finising school. I would die of boredom in without-boys enviroment."
    show Rebecca normal
    r "Well... I think that a school is quite nice. I love to study and I adore math."
    a "Math... Again... I hate it. It is so useless. How could it help me in life?"
    a "Will someone ask me to solve an equation before a proposal?"
    r "You know... There are some other things in the world besides boys... I think..."
    a "Maybe."
    show Brandon normal at left
    "Their classmate appeared from nowhere."
    b "Rebecca, wait."
    b "Before you go I want to ask..."
    show Brandon shy
    b "Would you like to go to the concert with me?"
    b "My sister will sing here. She is one of..."
    b "You know... Who screams instead of singing."
    b "It's her first perfomance. We are sublings and stuff. So I must to go..."
    b "Sooo... Maybe..."
    show Rebecca shy1
    r "Ok! I'm kinda interested in experemental music."
    b "It's so nice of you. It begins at six. We could walk before it..."
    r "Ok"
    show Rebecca shy2
    r "Alice, do you want to go with us?"
    show Alice angry
    a "No! Lestening to the garbage is not my definition of fun."

    scene bg wall
    "Alice ran away from Brandon and Rebecca as fast as she could."
    "She didn't tell anyone even her the closest friend Rebecca that he liked Brandon."
    "And after this scene at school her heart was broken into the infinite number of pieces."
    "She hided behind the wall and cried."
    show Alice cry at right
    a "Why don't he love me? He is the only one I need."
    a "Of course, the nerdest guy chose the nerdest girl."
    a "But she is so ugly! She doen't deserve him!"
    a "What am I saying right now and to whom?"
    show Caroline normal
    "Stranger" "Well, you say the things everybody says in despair."
    show Alice shocked
    a "Who are you?"
    c "Well... My name is Caroline. And I'm kinda..."
    c "Witch."
    c "But don't worry! I won't turn you into a frog."
    c "But I could turn you into Rebecca. It's a simple spell."
    c "You could be with Brandon instead of her."
    show Alice angry
    a "You know their names! You are a creepy stalker! Get away from me!"
    a "I will call the police!"
    show Caroline shocked1
    c "No!"
    show Caroline shocked2
    c "I just want to help you. I am not so good at witch stuff yet. But I think I could help you."
    a "I don't need your help."
    c "Ok. But just in case... Take this mirror. It could turn you into anyone. Just say \"I am the limit of Rebecca\" and you will become her."
    c "You could return after breaking the mirror"
    hide Alice
    hide Caroline
    show mirror Alice
    with fade
    "Alice took the mirror and looked at it."
    "There were strange symbols on it."
    hide mirror
    show Alice angry at right
    a "Is it a prank or what?"
    "Caroline disappeared."

    scene bg bedroom Alice
    show filter night
    with fade
    "Alice went home."
    "She couldn't sleep."
    show Alice pj angry at right behind filter
    a "What a nasty girl! What did she want from me?"
    a "Did she really believe that I would believe in Bloody Mary stuff?"
    a "But what if..."
    show Alice pj sad
    a "It's my only chance to know him better."
    a "At least to be with him for some days."
    a "Anyway I can to return everything."
    a "What am I saying? It won't work."
    hide Alice
    "She felt asleep only at 3am."
    show filter morning
    with fade
    "Alice parents went to work really early so they didn't wake their daughter up. They trusted her because she had never skipped the lessons before."
    show Alice pj angry at right behind filter
    a "What happened?"
    a "Stupid girl and her mirror..."
    a "Ok. If you want so."
    "She took the mirror."
    a "I am the limit of Rebecca."
    hide Alice
    show mirror Rebecca
    with fade
    "There were no symbols anymore."
    a "What? Is it real?"
    show Alice Rebecca-turned at right
    a "Ok."
    a "Only one chance."
