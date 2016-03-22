class Scenario(object):
    '''
    this class is used for store variable dialogue and scenario
    example scenario:
    variable  = (
                ({'str_name1': 'str_dialogue1'}, {'str_name1':('str_gesture1', 'str_animation1)}, str_background),
                ({'str_name2': 'str_dialogue2'}, {'str_name2':('str_gesture2', 'str_animation2)}, str_background)
                )

    variable1 = (
                ({'str_name1': 'str_dialogue1'}, {'str_name1':('str_gesture1', 'str_animation1)}, str_background),
                ({'str_name2': 'str_dialogue2'}, {'str_name2':('str_gesture2', 'str_animation2)}, str_background)
                )
    '''
    intro = (
        ({'me': "Where am I?"}, None, 'geo'),
        ({'me': "What is this place?"},),
        ({'me': "HELLLOOOO!!"},),
        ({'me': "Anyone can hear me!"},),
        ({'self': "It looks like there's nobody here"},),
        ({'self': "Why I ended up in this place?"},),
        ({'me': "Damn!"},),
        ({'me': "I need to get out of here"},),
        ({'self': "I looking around, but there's nothing, only geo space"},),
        ({'me': "I think, I see someone"},),
        ({'me': "Huh? A girl?"},),
        ({'self': "A girl? In place like this?"},),
        ({'self': "Maybe it's my imagination but she's looks real"},),
        'ask0',
    )

    ignore = (
        ({'me': "Maybe just my imagination"},),
        ({'me': "I should go somewhere find the way out"},),
        ({'me': "I tried to run far away"},),
        ({'me': "But there's noting around"},),
        ({'me': "I stuck in here"},),
        {'ending': 'bad'}
    )

    approach = (
        ({'me': "Hey do you know what is this place?"},),
        ({'girl': "Yeah"}, None, 'meet_stigma'),
        ({'me': "can you show me the escape please?"},),
        ({'girl': "Escape? Oh you must be that guy"},),
        ({'me': "Um excuse me?"}, None, 'geo'),
        ({'self': "What is she said?"}, {'stigma': ('usual', 'blink')}),
        ({'self': "Did she know me?"},),
        ({'me': "Did we've met before?"},),
        ({'girl': "No, we didn't"}, {'stigma': ('talk',)}),
        ({'self': "She act like she's know me"},),
        ({'girl': "My name is Stigma"},),
        ({'self': "Now She's introduce herself?"},),
        ({'me': "Oh yeah stigma, that's weird name for a girl"},),
        ({'me': "Okay stigma I have several question for you"}, {'stigma': ('usual',)}),
        'ask1'
    )

    place = (
        ({'me': "What is this place?"},),
        ({'stigma': "This is a demo game application"}, {'stigma': ('talk',)},),
        ({'stigma': "It's written in Python and me"},),
        ({'self': "Huh?"},),
        ({'me': "What do you mean?"},),
        ({'stigma': "I'm framework application, used to ease development application"},),
        ({'me': "A framework?"},),
        ({'stigma': "Yep, I help the developer to create any application they wanted"},),
        ({'me': "Are you some kind of AI like j*rvis or somtthing?"},),
        ({'stigma': "No I'm just humanized character"},),
        ({'me': "Okaaaayyy"},),
        ({'self': "I don't understand what she's said"},),
        ({'self': "Well..."}, {'stigma': ('usual',)},),
        'ask1'
    )

    stigma = (
        ({'me': "Who are you?"},),
        ({'stigma': "I'm framework application, used to ease development application"}, {'stigma': ('talk', 'blink')},),
        ({'me': "Kay you're framework application, but you know framework isn't a girl like you"},
         {'stigma': ('usual',)},),
        ({'me': "framework is structured code"},),
        ({'self': "I know it because I read w*kipedia"},),
        ({'me': "and beside I never heard about you before"},),
        ({'stigma': "I just developed in february 2016, and currently in alpha version"}, {'stigma': ('talk',)},),
        ({'stigma': "Founded by someone called kzul"},),
        ({'self': "Oh well ..."},),
        'ask1'
    )

    enough = (
        ({'self': "Well, I should not interrogate her?"}, {'stigma': ('usual',)},),
        ({'me': "Okay stigma, can you create something aside this demo game"},),
        ({'guy': "Of course she can!"},),
        ({'self': "Who's that?"},),
        ({'stigma': "kzul you're here"}, {'stigma': ('smile',)},),
        ({'self': "kzul?"},),
        ({'me': "Are you kzul?"},),
        ({'kzul': "Nice to meet you"}, {'stigma': ('smile',), 'teacher': ('talk', 'join')},),
        ({'me': "Nice to meet you too kzul I thought you're little taller"},),
        ({'kzul': "It just my avatar dude, purpose to attract some girl they love cute guy ya know hahaha!"},
         {'teacher': ('smile',)},),
        ({'self': "No good he's a retard"},),
        ({'me': "So kzul ..."},),
        'ask2'
    )

    framework = (
        ({'me': "Why you created framework?"},),
        ({'kzul': "I mean you know there's ton of application framework, engine, tools"},
         {'teacher': ('talk', 'blink')}),
        ({'me': "Why invented one ?"},),
        ({'kzul': "Why eh? because I just love code and share it to people"},),
        ({'me': "That's it?"},),
        ({
             'kzul': "Um well, stigma isn't pure framework she was invented with another frameworks \n and libraries like kivy"},),
        ({'kzul': "I still use some of them to create what common need"},),
        ({'me': "Okay, Why you invented python framework?"},),
        ({'kzul': "Why python? "},),
        ({'kzul': "I think python is most used programming language, I was used PHP, java and C"},),
        ({'kzul': "But any of it I thought python is most used by common developer"},),
        ({'self': "Okay ..."},),
        'ask2'
    )

    demo = (
        ({'me': "Are you gonna make new application demo?"},),
        ({'me': "Yeah"},),
        ({'me': "What's it?"},),
        ({'me': "Secret"},),
        ({'me': "Ugh this guy"},),
        ({'me': "Okay it's a secret huh?"},),
        ({'me': "Just kidding man I was still planning what I should present for next demo"},),
        ({'me': "Okay"},),
        ({'me': "okay next ..."},),
        'ask2'
    )

    escape = (
        ({'me': "Can you tell how to escape from here?"},),
        ({'me': "Of course but before that"},),
        ({'me': "Would you like to take her source code and give me some feedback?"},
                {'stigma': ('shy', 'join'), 'teacher': ('talk',)}),
        ({'me': "What!?"},),
        ({'me': "Kzul! but the source code is still too raw"},),
        ({'me': "Is not raw Is called alpha"},),
        ({'me': "Don't worry about her boy she'll take care of your project"},),
        'ask3'
    )

    okay = (
        ({'me': "Thank you, the escape will appear soon"},),
        ({'me': "Well anyway thanks for playing this demo, see ya"},
                {'stigma' : ('shy',), 'teacher' : ('smile', 'leave')}),
        ({'me': "Kzul disappear after that"}, {'stigma' : ('shy',)}),
        ({'me': "Now what?"},),
        ({'me': "Ho-How about c-c-c-create some project!?"},),
        ({'me': "Sounds good"}, {'stigma' : ('smile',)}),
        ({'me': "After that, I create some project and application with stigma"},),
        ({'me': "And share it to people"},),
        ({'me': "Fin"},),
        {'ending': 'good'}
    )

    cannot = (
        ({'me': "Thank you, the escape will appear soon"},),
        ({'me': "Well anyway thanks for playing this demo, see ya"},),
        ({'me': "Kzul disappear after that"},),
        ({'me': "Now what?"},),
        ({'me': "Ho-How about c-c-c-create some project!?"},),
        ({'me': "Sounds good"},),
        ({'me': "After that, I create some project and application with stigma"},),
        ({'me': "And share it to people"},),
        ({'me': "Fin"},),
        {'ending': 'bad'}
    )
