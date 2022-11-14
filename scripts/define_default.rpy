# sounds
define confog.default_music_volume = 0.7
define confog.default_sfx_volume = 0.7
define confog.default_voice_volume = 0.7

#screen
# Fade to black and back (out_time, hold_time, in_time, *, color="#000000")
define fade = Fade(0.5, 0.3, 0.5, color = "#2E2E2E")
image black_background = "#2E2E2E"

#characters
define r = Character("Róza", color = "#FF006C")
define l = Character("Lilla", color = "#CC00FF")
define z = Character("Zoli", color = "#019900")
define t = Character("Tanár", color = "#318F8D")
define i = Character("???", color = "#2E2E2E")
define player = Character("az új diák")

default class_a_or_b = 0 #if not 0 your class is A, if 0 then B
default point_r = 0 #if 0 then you can't go to prom with her Max point: 22 TODO
default point_l = 0 #if 0 then you can't go to prom with her Max point: 19 TODO
default prom_w = 0 #go to prom with: if it's 1 it means Roza, if it's 2 it means Lilla, if 0 then nobody, if -1 then Roza said no, if -2 Lilla said no
default answer = 0
default have_a_name = 0
default know_roza = 0
default know_lilla = 0
default know_zoli = 0

#Róza
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
image l what shut= "lilla/what_shut.png"

#Zoli
image z = "zoli/zoli.png"
image z talk= "zoli/talk.png"

#Tanár
image t = "teacher/teacher.png"
image t talk= "teacher/talk.png"
image t back= "teacher/back.png"


