label dayone:

    scene szoba

    "*csirip-csirip*"

    "Ideje felkelni."
    "Nem szeretnék elkésni az iskolából már az első nap."
    "Eddig még nem sikerült megismerkednem senkivel, remélem ez ma megváltozik."
    menu:
        "A régi osztálytársaimmal egyáltalán nem jöttem jól ki.":
            "De ez egy új esély."
            "Remélem itt sok barátom lesz majd!"
        "Nagyon sok jó barátom volt az előző osztályomban.":
            "Szerencsére velük bármikor tudok telefonon beszélgetni."
            "Remélem itt is könnyen fog menni a barátkozás."
    
    scene udvar
    "*bum*"
    "Jaj!"
    "Ne haragudj, nem vettelek észre!"

    show r shy 
    i "Sz-szia."
    i "Semmi baj, az én hibám."
    hide r shy
    show r shy shut
    menu:
        "Érdekel, hogy mi lehet a neve":
            "Ha már így egymásba botlottunk, megkérdezhetem mi a neved?"
            jump speak_with_roza
        "Nem akarom zavarni szegényt, így is megijesztettem":
            "Ne haragudj mennem kell, mégegyszer bocsi!"
            jump alone_to_class
    hide r shy shut
        
    label speak_with_roza:
        show r 
        pause 
        hide r 
        show r talk
        i "Az én nevem Róza!"
        $ point_r +=1
        r "Örülök a találkozásnak!"
        r "Te új diák vagy?"
        r "Még nem láttalak erre..."
        hide r talk
        show r
        "Igen, most költöztünk ide."
        hide r 
        show r excited
        r "Juj de izgi!"
        hide r excited
        show r what
        r "Akkor még nem is ismersz senkit, igaz?"
        hide r what
        show r what shut

        menu:
            "Elmondom az igazat":
                $ point_r +=1
                "Igaz, még nem sikerült senkivel se összebarátkoznom."
                "De még rengeteg időm lesz rá."
                hide r what shut 
                show r excited
                r "Pontosan!"
                hide r excited
                show r talk 
                r "Milyen pozitív vagy!"
                r "Én szívesen leszek az első barátod!"
                r "Persze csak ha te is szeretnéd."
                hide r talk
                show r 

                menu:
                    "Szeretném, hogy Róza legyen az első barátom":
                        $ point_r +=1
                        "Megtisztelnél vele!"
                        hide r
                        show r excited
                        r "Hú de jó!"
                        hide r excited
                        show r talk
                        r "Szeretnéd hogy körbevezesselek?"
                        hide r talk
                        show r 

                        menu:
                            "Szeretném, hogy Róza vezessen körbe az iskola területén":
                                $ point_r +=1
                                "Igen, az jó lenne!"
                                hide r 
                                show r excited
                                r "Remek!"
                                hide r excited
                                show r talk
                                r "Akkor kérlek kövess"
                                jump around_with_roza

                            "Nem szeretném, hogy Róza körbevezessen":
                                "Nem kell, köszi. Felfedezem egyedül."
                                hide r
                                show r sad
                                r "Oh, oké."
                                r "Azért majd ne késs el az órádról."
                                hide r sad
                                show r talk
                                r "Szia!"
                                jump alone_to_class

                    "Inkább valaki mással barátkoznék össze elsőre":
                        "Nem köszi, először szeretnék még másokkal is összeismerkedni."
                        hide r 
                        show r sad
                        r "Oh, rendben van"
                        r "Akkor szia..."

            "Hazudok róla":
                "De igen, már több barátot is szereztem!"
                hide r what shut
                show r excited
                r "Tényleg?"
                r "Ez nagyszerű!"
                hide r excited
                show r talk
                r "Akkor nem tartalak fel"
                r "Szia!"
                hide r talk
                jump alone_to_class

    label alone_to_class:

        scene folyoso

        menu:
            "Aranyos volt":
                "Remélem msákor még összefutunk."

            "Egyáltalán nem volt szimaptikus":
                "Remélem nem fogunk sokszor találkozni."
        
    label around_with_roza:
        scene folyoso
        show r talk
        r "Az első ajtó a tanárok terme."
        scene tanari
        show r talk
        r "Itt bármikor megtalálod az osztályfőnököd, vagy bármelyik másik tanárt."
        show r at right with move
        show t at left
        hide r  
        show r shy shut at right
        hide t
        show t talk at left
        t "Jó napot!"
        t "Keresnek valakit?"
        hide t talk at left
        show t at left
        hide r shy shut at right
        show r shy at right
        r "Nem köszönjük, csak [player] megkért, hogy vezessem körbe."
return