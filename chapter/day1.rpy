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
        r "Mi a neved?"
        hide r talk

    #Custom name input
    label name:
        show r
        $ player = renpy.input("")
        $ player = player.strip()
        if player == "":
            "Kérlek add meg a neved!!"
            jump name
        hide roza

    show r what
    r "Biztos [player] a neved?"
    hide r what 
    show r what shut
    menu:
        "Igen, a nevem [player]":
            "Igen Róza, tényleg így hívnak"
            jump player_name_right
        "Nem, a nevem nem [player]":
            "Nem, nem ez a nevem"
            jump player_name_wrong
    hide r what shut

    label player_name_wrong:
        hide r what
        show r shy
        r "Akkor miért mondtad hogy így hívnak..."
        hide r shy
        show r what
        r "De ha nem ez a neved, akkor mi?"
        hide r what
        jump name

    label player_name_right:
        hide r what
        show r excited
        r "Szia [player]! Örülök hogy megismerhetlek!"
        hide r excited

        show r what
        r "Milyen osztályos vagy?"
        hide r what
        show r what shut
        menu:
            "A osztályos":
                player "Azt hiszem az A osztályos."
                label class_a:
                hide r what shut 
                show r excited
                r "Tényleg? Én is oda járok!"
                r "Ezek szerint osztálytársak vagyunk!"
                $ class_a_or_b +=1
                $ point_r +=1
                hide r excited 

            "B osztályos":
                player "Ha minden igaz, B."
                label class_b:
                hide r what shut
                show r sad
                r "Oh, én A osztályos vagyok..."
                r "Remélem azért szünetben még találkozunk!"
                hide r sad 

            "Véletlenszerű":
                $ random_class = renpy.random.choice(['A', 'B']) 
                if random_class == "A":
                    player "[random_class] osztályos vagyok"
                    call class_a
                else:
                    player "[random_class] osztályos vagyok"
                    call class_b


        show r what
        r "Akkor még nem is ismersz senkit, igaz?"
        hide r what
        show r what shut

        menu:
            "Elmondom az igazat":
                $ point_r +=1
                player "Igaz, még nem sikerült senkivel se összebarátkoznom."
                player "De még rengeteg időm lesz rá."
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
                        player "Megtisztelnél vele!"
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
                                player "Igen, az jó lenne!"
                                hide r 
                                show r excited
                                r "Remek!"
                                hide r excited
                                show r talk
                                r "Akkor kérlek kövess"
                                jump around_with_roza

                            "Nem szeretném, hogy Róza körbevezessen":
                                player "Nem kell, köszi. Felfedezem egyedül."
                                hide r
                                show r sad
                                r "Oh, oké."
                                r "Azért majd ne késs el az órádról."
                                hide r sad
                                show r talk
                                r "Szia!"
                                jump alone_to_class

                    "Inkább valaki mással barátkoznék össze elsőre":
                        player "Nem köszi, először szeretnék még másokkal is összeismerkedni."
                        hide r 
                        show r sad
                        r "Oh, rendben van"
                        r "Akkor szia..."

            "Hazudok róla":
                player "De igen, már több barátot is szereztem!"
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

    "Ideje mennem órára!"
    "Vajon melyik lehet az osztályom?"
    "Sehova se látom kiírva."

    label door:
        scene folyoso
        menu:
            "Megpróbálom az első ajtót":
                "Legyen az első ajtó"
                jump door1
            "Megpróbálom a második ajtót":
                "Legyen a második ajtó"
                jump door2
            "Megpróbálom a harmadik ajtót":
                "Legyen a harmadik ajtó"   
                jump door3
            "Megpróbálom a negyedik ajtót":
                "Legyen a negyedik ajtó" 
                jump door4

        label door1:
            scene tanari
            show t back 
            pause
            hide t back
            show t 
            pause
            hide t 
            show t talk
            t "Jó napot!"
            t "Maga az új diák, igaz?"
            t "Miben segíthetek?"
            hide t talk
            show t
            player "Elnézést, az osztályom keresem."
            hide t 
            show t talk
            t "Nem vezette körbe senki?"
            t "Sajnálom, nekem erre most nincs időm, a harmadik ajtó a maga terme."
            t "Igyekezzen, mert hamarosan kezdődik az óra!"
            hide t talk
            jump door

        label door2:
            scene mosdo
            "Ez a mosdó. Fura hogy nem volt kiírva az ajtóra."
            jump door

        label door3:
            jump class_start
            

        label door4:
            scene szertar
            "O, ez a takarítószertár."
            jump door


        
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
        hide r shy at right
        show r shy shut at right
        hide t at left
        show t talk at left 
        t "Rendben, de hamarosan kezdődik az óra, ne késsenek el róla!"

        scene folyoso
        show r talk
        r "A második ajtó a mosdóhoz vezet"
        scene mosdo 
        pause

        scene folyoso
        show r talk
        r "A harmadik ajtó mögött van a termed"
        scene terem
        pause
        show r talk
        r "Itt lesznek majd az óráid"

        scene folyoso
        show r talk
        r "A negyedik ajtó pedig a takarítószertár"
        scene szertar
        pause

        scene folyoso
        show r talk
        r "Igazából ennyi, a többi ajtó mögött más osztálytermek vannak"
        hide r talk
        show r 
        menu:
            "Megköszönöm Rózának, hogy körbevezetett":
                player "Köszi Róza, hogy körbevezettél!"
                player "Rendes volt tőled!"
                hide r 
                show r shy
                r "Igazán nincs mit, én ajánlottam fel"
                hide r shy
                show r talk
                r "De ideje mennünk órára!"
                $ point_r += 1
            "Felesleges megköszönnöm":
                player "Remek, akkor mehetünk is órára!"
                hide r talk
                show r sad shut
                pause
                hide r sad shut
                show r talk
                "Igazad van, menjünk!"

    label class_start:
    scene terem
    pause
    "*CSÖRRR*"
    "Épp időben vagyok! Most csengettek be."
    "Vajon melyik az én helyem?"
    if class_a_or_b == 1:
        show r
        player "Ne haragudj, megmondanád, hogy melyik az én helyem?"
        hide r 
        show r talk
        r "Persze!"
        r "Ez lesz itt mellettem."
        r "Nyugodtan ülj le, a tanárnő hamarosan ideér."
        hide r talk
        show r shy
        r "És mindig nagyon mérges, ha nem vagyunk a helyünkön mire ideér."
        hide r shy
    else:
        show l
        pause
        hide l
        show l talk
        i "Szia!" 
        hide l talk
        show l
        player "Szia!"
        hide l 
        show l talk 
        i "Te vagy [player], igaz?"
        i "Én vagyok az osztályelnök ezért a tanárnő megkért, hogy segítsek neked beilleszkedni."
        hide l talk
        show l shy
        i "Ne haragudj, még be se mutatkoztam."
        hide l shy
        show l talk
        l "Az én nevem Lilla!"
        l "Ez lesz pedig a te helyed."
        l "A tanárnő pár perc múlva ide is ér, addig nyugodtan ülj le."
        hide l talk

    pause
    show t 
    pause
    hide t 
    show t talk
    t "Na gyerekek!"
    t "Kezdődhet az óra!" 
    with fade
    t "Remélem mindenkinek minden világos volt."
    hide t talk 
    
    if class_a_or_b == 1:
        show r
        pause
        hide r
    else:
        show l 
        pause
        hide l

    


return