label dayone:
# Reggel
    "Első nap"
    scene black_background
    pause 0.1
    scene szoba with fade


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
    
# Iskola udvar 
    scene udvar
    "*bum*"
    "Jaj!"
    "Ne haragudj, nem vettelek észre!"

# Találkozás Rózával
    show r shy 
    i "Sz-szia."
    i "Semmi baj, az én hibám."
    hide r shy
    show r shy shut
    menu:
        "Érdekel, hogy mi lehet a neve":
            "Ha már így egymásba botlottunk, megkérdezhetem mi a neved?"
            $ know_roza += 1
            jump speak_with_roza
        "Nem akarom zavarni szegényt, így is megijesztettem":
            "Ne haragudj mennem kell, mégegyszer bocsi!"
            jump alone_to_class
    hide r shy shut
        
# Beszélgetés Rózával
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

# Egyedi név megadása
    show r
    label name:
        $ have_a_name += 1
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
            "Igen Róza, tényleg így hívnak."
            jump player_name_right
        "Nem, a nevem nem [player]":
            "Nem, nem ez a nevem."
            jump player_name_wrong
    hide r what shut

    label player_name_wrong:
        hide r what
        show r shy
        r "Akkor miért mondtad hogy így hívnak..."
        hide r shy
        show r what
        r "De ha nem ez a neved, akkor mi?"
        show r what shut
        jump name

    label player_name_right:
        hide r what
        show r excited
        r "Szia [player]! Örülök hogy megismerhetlek!"
        hide r excited

# Osztály választás
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
                    player "[random_class] osztályos vagyok."
                    call class_a
                else:
                    player "[random_class] osztályos vagyok."
                    call class_b

# Barát szerzés
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
                                r "Akkor kérlek kövess."
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
                        r "Oh, rendben van."
                        r "Akkor szia..."

            "Hazudok róla":
                player "De igen, már több barátot is szereztem!"
                hide r what shut
                show r excited
                r "Tényleg?"
                r "Ez nagyszerű!"
                hide r excited
                show r talk
                r "Akkor nem tartalak fel."
                r "Szia!"
                hide r talk
                jump alone_to_class

# Beszélgetés kihagyása Rózával

    label alone_to_class:
    scene folyoso

    menu:
        "Aranyos volt":
            "Remélem máskor még összefutunk."

        "Egyáltalán nem volt szimaptikus":
            "Remélem nem fogunk sokszor találkozni."

    "Ideje mennem órára!"
    "Vajon melyik lehet az osztályom?"
    "Sehova se látom kiírva."

# Iskola felfedezése egyedül

    label door:
        scene folyoso
        menu:
            "Megpróbálom az első ajtót":
                "Legyen az első ajtó."
                jump door1
            "Megpróbálom a második ajtót":
                "Legyen a második ajtó."
                jump door2
            "Megpróbálom a harmadik ajtót":
                "Legyen a harmadik ajtó."   
                jump class_start
            "Megpróbálom a negyedik ajtót":
                "Legyen a negyedik ajtó." 
                jump door4

        label door1:
# Egyedi név megadása 2
            if have_a_name == 0:
                scene tanari
                show t back 
                pause
                hide t back
                show t 
                pause
                hide t 
                show t talk
                t "Jó napot!"
                t "Maga pedig?"
                hide t talk
                $ have_a_name += 1
                label name2:
                    show t
                    $ player = renpy.input("")
                    $ player = player.strip()
                    if player == "":
                        "Kérlek add meg a neved!!"
                        jump name2
                    hide t
                    show t talk
                    t "Szóval [player]?"
                    hide t talk
                    show t
                    menu:
                        "Igen, a nevem [player]":
                            "Igen, [player] vagyok."
                            jump player_name_right2
                        "Nem, a nevem nem [player]":
                            "Vagyis..."
                            jump player_name_wrong2
                    hide t 

                    label player_name_wrong2:
                        hide t 
                        show t talk
                        t "Sajnálom, de erre nem érek rá."
                        hide t talk 
                        jump name2

                label player_name_right2:
                    show t talk
                    t "[player]. Miben segíthetek?"
                    hide t talk
                    show t
                    player "Az osztályom keresem."
                    hide t 
                    show t talk
                    t "Nem vezette körbe senki?"
                    t "Sajnálom, nekem erre most nincs időm, a harmadik ajtó a maga terme."
                    t "Igyekezzen, mert hamarosan kezdődik az óra!"
                    hide t talk
                    jump door
            else:
                scene tanari
                show t back 
                pause
                hide t back
                show t 
                pause
                hide t 
                show t talk
                t "Jó napot!"
                t "[player]. Miben segíthetek?"
                hide t talk
                show t
                player "Az osztályom keresem."
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

        label door4:
            scene szertar
            "O, ez a takarítószertár."
            jump door

# Róza körbevezet
        
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
        r "A második ajtó a mosdóhoz vezet."
        scene mosdo 
        pause

        scene folyoso
        show r talk
        r "A harmadik ajtó mögött van a termed."
        scene terem
        pause
        show r talk
        r "Itt lesznek majd az óráid."

        scene folyoso
        show r talk
        r "A negyedik ajtó pedig a takarítószertár."
        scene szertar
        pause

        scene folyoso
        show r talk
        r "Igazából ennyi, a többi ajtó mögött más osztálytermek vannak."
        hide r talk
        show r 
        menu:
            "Megköszönöm Rózának, hogy körbevezetett":
                player "Köszi Róza, hogy körbevezettél!"
                player "Rendes volt tőled!"
                hide r 
                show r shy
                r "Igazán nincs mit, én ajánlottam fel."
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
                r "Igazad van, menjünk!"

# Első óra kezdés
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
        $ know_lilla += 1
        pause
        hide l
        show l talk
        i "Szia!" 
        i "Te vagy [player], igaz?"
        i "Én vagyok az osztályelnök ezért a tanárnő megkért, hogy segítsek neked beilleszkedni."
        show l shy
        i "Ne haragudj, még be se mutatkoztam."
        hide l shy
        show l talk
        l "Az én nevem Lilla!"

# Ha még nincs egyedi játékosnév
        if have_a_name == 0:
                $ have_a_name += 1

                hide l talk
                show l what 
                l "Téged hogy hívnak?"               
                hide l what 

                label name3:
                    show l what shut 
                    $ player = renpy.input("")
                    $ player = player.strip()
                    if player == "":
                        "Kérlek add meg a neved!!"
                        jump name3

                    hide l what shut
                    show l what
                    l "Tényleg [player] a neved?"
                    hide l what
                    show l what shut 
                    menu:
                        "Igen, a nevem [player]":
                            "Igen, [player] vagyok."
                            jump player_name_right3
                        "Nem, a nevem nem [player]":
                            "Igazából nem ez a nevem..."
                            jump player_name_wrong3
                    hide l what 

                    label player_name_wrong3:
                        show l shy
                        l "Akkor mi a neved?"
                        hide l shy
                        jump name3

                    label player_name_right3:
                        show l talk
                        l "Igazán örvendek [player]!"
                        l "Ez lesz a te helyed."
                        l "A tanárnő pár perc múlva ide is ér, addig nyugodtan ülj le."
                        hide l talk
        else:            
            l "Ez lesz pedig a te helyed."
            l "A tanárnő pár perc múlva ide is ér, addig nyugodtan ülj le."
            hide l talk

    pause 0.7
    show t with moveinright
    pause 0.3
    hide t 
    show t talk
    t "Na gyerekek!"
    t "Kezdődhet az óra!" 
    t "Remélem mindenkinek minden világos volt." with fade
    show t
    "*CSÖRRR*"
    hide t talk     
    
# Beszélgetés Rózával

    if class_a_or_b == 1:
        show r excited
        r "Végre kicsengettek!"
        hide r excited
        show r what
        r "[player], te értetted az anyagot?"
        hide r what 
        show r what shut
        menu:
            "Persze, nem volt vészes":
                player "Igen, a tanárnő jól magyarázott, könnyű volt követni."
                hide r what shut
                show r talk
                r "Tényleg?"
                r "De jó neked, [player]!"
                hide r talk
                show r sad
                r "Én sajnos semmit sem értettem. Lemaradtam az elején."
                hide r sad
                show r sad shut
                menu:
                    "Felajánlom Rózának, hogy tanuljunk együtt":
                        player "Mit szónál hozzá, ha elmagyaráznám neked?" 
                        hide r sad shut
                        show r excited
                        r "Tényleg? Annak nagyon örülnék!"
                        hide r excited 
                        jump learn_with_Roza

                    "Inkább egyedül tanulok":
                        player "Sajnálom. De biztos van valaki, aki segít megérteni az anyagot."
                        jump meet_with_Zoli

            "Nem, teljesen elvesztem":
                player "Egyáltalán nem, nagyon gyorsan haladt a tanárnő, már az elején lemaradtam."
                hide r what shut
                show r talk
                r "Tényleg? Ne aggódj, én se tudtam követni."
                hide r talk
                show r shy 
                r "M-mit szólnál hozzá...ha esetleg...ömm.."
                hide r shy
                show r shy shut
                player "Igen? Mit szeretnél mondani?"
                hide r shy shut
                show r shy 
                r "T-tud-tudod...ha mi...ketten.."
                hide r shy
                show r shy shut
                player "Róza, ha nem modnod ki, nem értelek."
                hide r shy shut
                show r angry 
                r "T-tanulhahtnánk együtt!"
                hide r angry
                show r shy shut 
                menu:
                    "Szeretnék Rózával együtt tanulni":
                        player "Ez egy remek ötlet! Szívesen tanulnék veled, Róza."
                        hide r shy shut 
                        show r excited 
                        r "Tényleg? Jaj de jó!"
                        hide r excited
                        show r talk
                        r "Izgultam, hogy nem szeretnéd. De örülök, hogy megkérdeztem!"
                        hide r talk 
                        jump learn_with_Roza 

                    "Inkább nem tanulok együtt Rózával":
                        player "Sajnálom, de nem hiszem, hogy az jó ötlet lenne."
                        hide r shy shut
                        show r sad 
                        r "Oh... Persze, megértem."
                        hide r sad 
                        show r sad shut
                        player "De biztos van valaki, aki szívesen segít."
                        jump meet_with_Zoli

# Találkozás Zolival

        label meet_with_Zoli:
            $ know_zoli += 1
            hide r sad shut 
            show r sad
            r "Remélem igazad van."
            r "Jó lenne, ha valaki segítene."
            show r sad shut at right with move
            show z at left
            pause
            show z talk at left
            i "Szia Róza, ha szeretnéd én elmagyarázom."
            hide z talk
            show z at left
            hide r sad shut 
            show r excited at right
            r "Tényleg? Az nagyon jó lenne!"
            hide r excited
            show r at right
            menu:
                "Hagyom, hogy beszélgessenek":
                    hide r
                    show r talk at right
                    r "Köszi Zoli, nagyon rendes vagy!"
                    hide r talk
                    show r at right
                    hide z  
                    show z talk at left
                    z "Akkor mehetünk is."
                    hide z talk
                    show z at left
                    hide r  
                    show r talk at right
                    r "Rendben. Szia [player], majd holnap találkozunk!"
                    hide r talk 
                    show r at right
                    pause 0.1
                    jump after_school
                                        
                "Közbeszólok":                              
                    player "Szia, te ki is vagy?"
                    hide z  
                    show z talk at left
                    i "Ne haragudj, még be se mutatkoztam."
                    z "Nyugodtan hívj Zolinak. Téged hogy hívnak?"
                    hide z talk
                    show z at left
                    player "A nevem [player]."
                    show z talk at left
                    z "Üdv, [player]."
                    z "Nos, Róza, akkor mehetünk is."
                    hide z talk
                    show z at left
                    hide r  
                    show r talk at right
                    r "Rendben. Szia [player], majd holnap találkozunk!"
                    hide r talk 
                    show r at right
                    pause 0.1
                    jump after_school

        label learn_with_Roza:
            $ point_r +=1
            show r talk 
            r "Akkor szerintem kezdjük is el, amíg friss az órai anyag."
            hide r talk
            show r 
            player "Rendben. Akkor kezdjük is." 
            show r excited 
            r "Ó! Így már értem!" with fade
            hide r excited 
            show r talk
            r "Köszi [player], hogy időt szántál rám!"
            r "Mostmár biztos jól fog sikerülni a dolgozatírás!"
            hide r talk
            show r shy
            r "Viszont nagyon elszaladt az idő, úgyhogy most rohannom kell."
            hide r shy
            show r excited
            r "Mégegyszer köszi mindent [player]!"
            hide r excited
            show r talk
            r "Szia!"
            hide r talk 
            show r
            pause 0.1
            jump after_school

# Beszélgetés Lillával

    else:
        show l talk
        l "[player], értetted az anyagot?"
        hide l talk 
        show l
        menu:
            "Persze, nem volt vészes":
                player "Igen, a tanárnő jól magyarázott, könnyű volt követni."
                $ point_l += 1
                $ know_zoli += 1
                hide l 
                show l talk
                l "Ezt örömmel hallom."
                l "Ha esetleg később mégis felmerülne benned egy kérdés, nyugodtan keress meg. Szívesen elmagyarázom."
                show l at right with move
                show z at left
                hide z 
                show z talk at left
                i "Sziasztok."
                i "Ne haragudj Lilla, de ráérsz kicsit? Nem egészen értek egy részt. Elmagyaráznád?"
                hide z talk 
                show z at left
                hide l 
                show l talk at right
                l "Persze Zoli, mi nem ment?"
                hide l talk
                show l at right

                menu:
                    "Maradok és csatlakozok hozzájuk":
                        player "Én is maradhatok?"
                        $ point_l += 1
                        hide l 
                        show l talk at right
                        l "Persze [player]! Az ismétés sosem árthat, igaz?" 
                        hide l talk 
                        show l at right 
                        pause 0.1
                        show l talk at right
                        l "Így már minden világos?" with fade
                        hide l talk
                        show l at right
                        hide z 
                        show z talk at left 
                        z "Igen Lilla, nagyon köszi!"
                        hide z 
                        show l talk at center with move
                        l "Örülök, hogy te is maradtál még [player]."
                        l "Együtt tanulni mindig sokkal jobb!"
                        hide l talk
                        show l sad
                        l "Nekem viszont most mennem kell."
                        hide l sad
                        show l talk
                        l "Holnap találkozunk!"

                    "Inkább elmegyek":
                        player "Én akkor megyek is."
                        hide l 
                        show l sad at right
                        l "Oh, rendben van [player]."
                        hide l sad
                        show l talk at right
                        l "Holnap találkozunk." 

            "Nem, teljesen elvesztem":
                player "Egyáltalán nem, nagyon gyorsan haladt a tanárnő, már az elején lemaradtam."
                hide l 
                show l sad 
                l "Oh, ezt sajnálattal hallom."
                hide l sad
                show l talk
                l "Szeretnéd, hogy segítsek?"
                hide l talk
                show l 
                menu:
                    "Nem szeretnék Lillával tanulni":
                        player "Nem kell, megoldom egyedül is. De azért köszi."
                        hide l 
                        show l sad
                        l "Oh, oké..."
                        hide l sad
                        show l talk
                        l "Azért ha valahol elakadnál szólj, szívesen elmagyarázom!"
                        hide l talk
                        show l
                        player "Rendben van Lilla, megjegyzem!"
                        hide l 
                        show l talk
                        l "Akkor szia [player]! Holnap találkozunk!"
                    
                    "Jó lenne Lillával együtt tanulni":
                        $ point_l += 1
                        player "Igen, az jó lenne. Köszi."
                        hide l 
                        show l excited
                        l "Igazán nincs mit!"
                        hide l excited
                        show l talk
                        l "Kezdem az elején, hogy biztos mindent érts, jó?"
                        hide l talk 
                        show l
                        pause 0.1
                        show l talk 
                        l "Így már minden világos?" with fade
                        hide l talk 
                        show l 
                        player "Igen Lilla! Köszi, hogy segítettél!"
                        hide l 
                        show l shy 
                        l "T-tényleg nincs mit."
                        hide l shy 
                        show l talk 
                        l "Nekem is jó, ha ismétlem az anyagot."
                        l "És szeretek segíteni az osztálytársaimnak." 
                        hide l talk
                        show l
                        player "Igen, nem véletlenül vagy te az osztályelnök!"
                        hide l
                        show l talk
                        l "Na igen."
                        hide l talk
                        show l sad
                        l "De nekem most mennem kell."
                        hide l sad
                        show l talk
                        l "Örülök, hogy segíthettem!"
                        l "Holnap találkozunk. Szia [player]!"

                hide l talk 
                show l
                pause 0.1
                jump after_school        
                        
# Iskola után
    label after_school:
        scene szoba with fade
        pause 0.2
        menu:
            "Ez egy jó nap volt":
                "Ma igazán jól éreztem magam."
                "Mindenki nagyon kedves volt a suliban."
                
            "Ez a nap nem volt olyan jó":
                "A mai nap azért lehetett volna jobb is."
                "De a holnap még lehet jobb."
    
    scene black_background with fade
    "Első nap vége"

return