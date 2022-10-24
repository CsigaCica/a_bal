# The game starts here.

label start:
    
    #if you want to block rollback, use the next line:
    #$ renpy.block_rollback()

    scene szoba

    "Let's begin the game:"
    
    call dayone
    
    "Róza pont: [point_r]"
    "Lilla pont: [point_l]"

    # label intro_scene:
    # "Ma is szép napunk van."
    # "Kicsit szürke az ég, de nem baj."
    # "Ez a nap ettől szép."
    # "Remélem az új osztálytársaim kedvesek lesznek..."
    # menu:
    #     "A régi osztálytársaimmal egyáltalán nem jöttem jól ki.":
    #         "De ez egy új esély."
    #         "Remélem itt sok barátom lesz majd!"
    #     "Nagyon sok jó barátom volt az előző osztályomban.":
    #         "Szerencsére velük bármikor tudok telefonon beszélgetni."
    #         "Remélem itt is könnyen fog menni a barátkozás."

    # scene folyoso

    # show r
    # pause
    # hide r

    # show r talk
    # i "Helló!"
    # i "Az én nevem Róza!"
    # r "Téged hogy hívnak?"
    # hide r talk

    # # Custom name input
    # # label name:
    # #     show roza
    # #     $ y = renpy.input("")
    # #     $ y = y.strip()
    # #     if y == "":
    # #         "Kérlek add meg a neved!!"
    # #         jump name
    # #     hide roza

    # show r what
    # r "Biztos [player] a neved?"
    # menu:
    #     "Igen, a nevem [player]":
    #         "Igen Róza, tényleg így hívnak"
    #         jump option1
    #     "Nem, a nevem nem [player]":
    #         "Nem, nem ez a nevem"
    #         #jump option2
    # hide r what

    # label option1:
    #     hide r what
    #     show r excited
    #     r "Szia [player]! Örülök hogy megismerhetlek!"
    #     hide r excited
    #     jump after_choices

    # label option2:
    #     hide r what
    #     show r shy
    #     r "Akkor miért mondtad hogy így hívnak..."
    #     r "De ha nem ez a neved, akkor mi?"
    #     hide r shy
    #     jump name

    # label after_choices:
    #     show r talk
    #     r "Üdvözöllek a gimink utolsó évében."
    #     r "Nehéz lehetett iskolát váltani."
    #     r "De ne aggódj, itt mindenki kedves, és biztos segíteni fognak beilleszkedni."
    #     r "Ismersz itt már valakit?"
    #     "Nem, rajtad kívül senkit..."
    #     r "O, hát akkor én szívesen leszek első barátod. :D"

    # "*CSÖRRRR*"

    # show r sad at right with move
    # r "Oh, becsengettek, azt hiszem ideje menni."
    # hide r sad 
    # show r talk at right
    # r "Melyik a te osztályod?"
    # menu:
    #     "Az A osztály":
    #         y "Azt hiszem az A."
    #         jump a_class
    #     "A B osztály":
    #         y "Ha minden igaz, a B."
    #         jump b_class
    #     "Véletlenszerű":
    #         $ random_class = renpy.random.choice(['A', 'B']) 
    #         if random_class == "A":
    #             y "[random_class] osztályos vagyok"
    #             jump a_class
    #         else:
    #             y "[random_class] osztályos vagyok"
    #             jump b_class

    # label after_what_class:
    #     y "Ideje menni órára!"
    #     y "Vajon melyik lehet az osztályom?"
    #     y "Sehova se látom kiírva."
    #     y "Róza pedig eltűnt...?"

    # label door:
    # scene folyoso
    # menu:
    #     "Megpróbálom az első ajtót":
    #         y "Legyen az első ajtó"
    #         jump door1
    #     "Megpróbálom a második ajtót":
    #         y "Legyen a második ajtó"
    #         jump door2
    #     "Megpróbálom a harmadik ajtót":
    #         y "Legyen a harmadik ajtó"   
    #         jump door3
    #     "Megpróbálom a negyedik ajtót":
    #         y "Legyen a negyedik ajtó" 
    #         jump door4

    # label door1:
    #     scene terem
    #     y "Jaj! Elnézést!"
    #     y "Úgy tűnik megzavartam egy órát."
    #     y "Biztos nem az enyém, mivel nálam fiatalabbak a diákok."
    #     jump door

    # label door2:
    #     scene mosdo
    #     y "Ez a mosdó. Fura hogy nem volt kiírva az ajtóra."
    #     jump door

    # label door3:
    #     scene terem
    #     y "Jaj, elnézést! Eltévedtem, megmondaná, hogy ez melyik terem?"
    #     t "Kérem, üljön le, már vártuk."
    #     t "Épp most akartam bemutatni az osztálytársainak, de akkor át is adom a szót!"
    #     jump after_door

    # label door4:
    #     scene szertar
    #     y "O, ez a takarítószertár."
    #     jump door

    # label after_door:
    #     y "Helló! A nevem [player]! Remélem jól kijövünk majd!"

    "Első nap vége"

    # if class_a_or_b < 1:
    #     "B osztályos vagy"
    # else:
    #     "A osztályos vagy"

    call quiz

    "Vége"
   
return









# label daychange:
#     if day == 1:
#         call intro_scene
#     elif day == 2:
#         call speech
#     elif day <= 3 and day >= 11:
#         call intro_scene
#     else:
#         call prom
# return