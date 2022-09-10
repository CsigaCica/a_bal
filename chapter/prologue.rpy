label intro_scene:
    "Ma is szép napunk van."
    "Kicsit szürke az ég, de nem baj."
    "Ez a nap ettől szép."

    show roza
    pause
    hide roza
    

    show roza talk
    k "Helló!"
    k "Az én nevem Róza!"
    r "Téged hogy hívnak?"
    hide roza talk

    label name:
        show roza
        $ y = renpy.input("")
        $ y = y.strip()
        if y == "":
            "Kérlek add meg a neved!!"
            jump name
        hide roza

    show roza what
    r "Biztos ez a neved?"
    menu:
        "Igen, a nevem [y]":
            "Igen Róza, tényleg így hívnak"
            jump option1
        "Nem, a nevem nem [y]":
            "Nem, nem ez a nevem"
            jump option2
    hide roza what

    label option1:
        hide roza what
        show roza excited
        r "Szia [y]! Örülök hogy megismerhetlek!"
        hide roza excited
        jump after_choices

    label option2:
        hide roza what
        show roza shy
        r "Akkor miért mondtad hogy így hívnak..."
        r "De ha nem ez a neved, akkor mi?"
        hide roza shy
        jump name

    label after_choices:
        show roza talk
        r "Üdvözöllek a gimink utolsó évében."
        r "Nehéz lehetett iskolát váltani. :("
        r "De ne aggódj, itt mindenki kedves, és biztos segíteni fognak beilleszkedni."
        r "Ismersz itt már valakit?"
        "Nem, rajtad kívül senkit..."
        r "O, hát akkor én szívesen leszek első barátod. :D"

    "*CSÖRRRR*"

    show roza shy at right with move
    r "Oh, becsengettek, azt hiszem ideje menni."
    hide roza shy 
    show roza talk at right
    r "Melyik a te osztályod?"
    menu:
        "Az A osztály":
            y "Azt hiszem az A."
            jump a_class
        "A B osztály":
            y "Ha minden igaz, a B."
            jump b_class

    label after_what_class:
        y "Ideje menni órára!"
        
    scene folyoso
    y "Vajon melyik lehet az osztályom?"
    y "Sehova se látom kiírva."
    y "Róza pedig eltűnt...?"

    label door:
    menu:
        "Megpróbálom az első ajtót":
            y "Legyen az első ajtó"
            jump door1
        "Megpróbálom a második ajtót":
            y "Legyen a második ajtó"
            jump door2
        "Megpróbálom a harmadik ajtót":
            y "Legyen a harmadik ajtó"   
            jump door3
        "Megpróbálom a negyedik ajtót":
            y "Legyen a negyedik ajtó" 
            jump door4

    label door1:
        y "Jaj! Elnézést!"
        y "Úgy tűnik megzavartam egy órát."
        y "Biztos nem az enyém, mivel nálam fiatalabbak a diákok."
        jump door

    label door2:
        y "Ez a mosdó. Fura hogy nem volt kiírva az ajtóra."
        jump door

    label door3:
        y "Jaj, elnézést! Eltévedtem, megmondaná, hogy ez melyik terem?"
        t "Kérem, üljön le, már vártuk."
        t "Épp most akartam bemutatni az osztálytársainak, de akkor át is adom a szót!"
        jump after_door

    label door4:
        y "O, ez a takarítószertár."
        jump door

    label after_door:
        y "Helló! A nevem [y]! Remélem jól kijövünk majd!"

return