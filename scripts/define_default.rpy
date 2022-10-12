# sounds
define confog.default_music_volume = 0.7
define confog.default_sfx_volume = 0.7
define confog.default_voice_volume = 0.7

#characters
define r = Character("Róza", color = "#FF006C")
define l = Character("Lilla", color = "#CC00FF")
define k = Character("Zoli", color = "#019900")
define t = Character("Tanár", color = "#318F8D")
define i = Character("???", color = "#2E2E2E")
define player = Character("Player")

default class_a_or_b = 0 #if not 0 your class is A, if 0 then B
default point_r = 0 #if 0 then you can't go to prom with her
default point_l = 0 #if 0 then you can't go to prom with her
default current_question_idx = 0 # define the question counter
default score = 0 # define the player's starting score at questions
default quiz = 0

#Roza
image r = "roza/roza.png"
image r talk= "roza/talk.png"
image r angry= "roza/angry.png"
image r angry shut= "roza/angry_shut.png"
image r excited= "roza/excited.png"
image r excited shut= "roza/excited_shut.png"
image r sad= "roza/sad.png"
image r sad shut= "roza/sad_shut.png"
image r shy= "roza/shy.png"
image r shy shut= "roza/shy_shut.png"
image r what= "roza/what.png"
image r what shut= "roza/what_shut.png"


#Lilla
image l = "lilla/lilla.png"
image l talk= "lilla/talk.png"
image l angry= "lilla/angry.png"
image l angry shut= "lilla/angry_shut.png"
image l excited= "lilla/excited.png"
image l excited shut= "lilla/excited_shut.png"
image l sad= "lilla/sad.png"
image l sad shut= "lilla/sad_shut.png"
image l shy= "lilla/shy.png"
image l shy shut= "lilla/shy_shut.png"
image l what= "lilla/what.png"
image l what shut= "lilla/whyt_shut.png"


#Tanár
image t = "teacher/teacher.png"
image t talk= "teacher/talk.png"
image t back= "teacher/back.png"


