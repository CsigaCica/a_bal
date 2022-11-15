label dayfive: 
    # Reggel
    "Ötödik nap"
    scene black_background 
    pause 0.1
    scene szoba with fade

    "*csirip-csirip*"

    "Ideje felkelnem."
    "Ma nem szabad elkésnem, hiszen ma írjuk a második dolgozatot."
    "Magabiztos vagyok!"
    "A mai dolgozat biztos jól fog menni!"
    "Ideje is indulnom!"
    
# Iskola folyosó 
    scene folyoso 
    pause 0.4
    if class_a_or_b == 1:
        show r talk 
        r "Szia [player]!"
        show r 
        player "Szia Róza!"
        player "Felkészültél a javító dolgozatra?"
        show r excited
        r "De fel ám!"
        r "Nagyon sokat készültem, úgyhogy mna biztos jobban fog menni!"
        show r excited shut 
        player "Remélem is!"
        show r talk 
        r "Induljunk is!"
    else:
        show l talk 
        l "Szia [player]!"
        show l 
        player "Szia Lilla!"
        show l talk 
        l "Felkészültél a mai dolgozatra?"
        show l 
        player "Igen!"
        show l talk 
        l "Ennek igazán örülök!"
        l "Akkor menjünk is!"

# Második dolgozat
    scene terem
    pause 0.2
    "*CSÖRRR*"
    show t with moveinright
    pause 0.3
    show t talk
    t "Mindenki itt van, igaz?"
    t "Ahogy nézem igen."
    t "Nos, akkor kezdjük a javító dolgozatot." 
    show t 
    show t talk with fade
    t "A dolgozatírás menete ugyanaz lesz mint legutóbb."
    t "Mindenki fog kapni egy lapot, aminek a bal felső sarkába kell írnotok a neveteket."
    t "Ez után szóban fogom feltenni a kérdéseket, majd négy választ hozzá."
    t "A helyes válasz számát pedig írjátok a lapotokra."
    t "Minden kérdést csak egyszer fogok feltenni."
    t "Nem fogom megismételni, úgyhogy nagyon figyeljetek."
    t "A jó jegyért legalább négy kérdésre helyesen kell felelnetek."
    t "Akkor kezdem is."
    show t
     
    call questions from _call_questions_1
    
    show t 
    show t talk with fade
    t "Ennyi." 
    t "Remélem mindenkinek jobban ment mint az előző."
    t "Az eredményeiteket holnap tudjátok meg."
    t "Most pedig adjátok be a lapjaitokat."
    t "Viszlát."
    show t 
    "*CSÖRRR*"
    
    scene folyoso
    show r excited at left
    show l talk at right
    "[player]!"
    show r shy shut at left
    show l shy shut at right
    player "Sziasztok!"
    player "Hogy ment nektek a dolgozat?"
    show r excited at left
    r "Jól!"
    show r at left
    player "Róza, legutóbb is ezt mondtad."
    show r talk at left
    r "De most tényleg sokkal jobban ment, mint az első!"
    r "Érzem!"
    show r at left
    player "És neked, Lilla?"
    show l talk at right
    l "Nekem is jobban ment mint legutóbb!"
    l "Most tényleg mindenre jól tudtam a választ!"
    show r shy shut at left
    l "És neked hogy ment [player]?"
    show r at left
    show l at right
    menu: 
        "Elmondom az igazat":
            if answer >=10: 
                $ point_r +=1
                $ point_l +=1
                label good_grades:
                player "Mindkettő nagyon jól."
                player "Büszke is vagyok magamra!"
                show r excited at left
                show l excited shut at right
                r "Tényleg?"
                show r excited shut at left
                show l excited at right
                l "Ez nagyszerű!"
                show r talk at left
                show l at right
                r "Nagyon ügyes vagy [player]!"
                show r at left
                show l talk at right
                l "Igazán örülök, hogy ilyen jól sikerültek!"
                show r talk at left
                show l at right
                r "Én is!"
                r "Így mind elmehetünk a Bálba!"
                show r at left
                show l talk at right
                l "Bizony!"
                l "És [player], tudod már kit szeretnél elhívni?"
                show r shy shut at left
                show l shy at right
                l "M-mármint ha szabad kérdeznem...persze..."
                show r shy shut at left
                show l shy shut at right
                menu:
                    "Még nem döntöttem el":
                        player "Sajnálom lányok, még nem tudom."
                        player "El is felejtettem."
                        player "De még van idő, nem?"
                        show r shy at left
                        show l shy shut at right
                        r "De, persze!"
                        show r shy shut at left
                        show l shy at right
                        l "Cs-csak tudod, ilyenkorra már tudni szokták..."
                        l "Hiszen holnap után Bál!"
                        l "D-de persze nem sürgetni szeretnélek!"
                        show r sad at left
                        show l shy shut at right
                        r "Én most megyek..."
                        r "Szia [player], szia Lilla..."
                        hide r
                        show l sad shut at right
                        player "Mi ütött Rózába?"
                        show l sad at right
                        l "T-tudod.."
                        l "Teljesen megértem őt."
                        show l shy at right
                        l "Utána megyek beszélni vele!"
                        hide l 
                        player "Ideje eldöntenem kivel menjek..."

                    "Eldöntöttem, de még nem kérdezem meg":
                        player "Igen, már tudom kit szeretnék elhívni."
                        show r excited shut at left
                        show l excited at right
                        l "Tényleg?"
                        show r excited at left
                        show l excited shut at right
                        r "Na és kit?"
                        show r excited shut at left
                        show l excited shut at right
                        player "Sajnálom lányok, még nem állok készen, hogy megkérdezzem eljön-e velem..."
                        show r shy at left
                        show l shy shut at right
                        r "P-persze, ezt megértem."
                        show r sad shut at left
                        show l shy at right 
                        l "I-igen, én is..."
                        show r sad shut at left
                        show l talk at right 
                        l "Holnap is felkérhetsz még ám akárkit!"
                        show r sad at left
                        show l at right 
                        r "Igen, ez így van."
                        r "Én most megyek."
                        r "Szia [player], szia Lilla..."
                        hide r
                        show l sad shut at right
                        player "Mi van Rózával?"
                        show l sad at right
                        l "T-tudod.."
                        l "Teljesen megértem őt."
                        show l shy at right
                        l "Utána megyek beszélni vele!"
                        hide l 
                        player "A lányok néha furák."

                    "Eldöntöttem és meg is kérdezem":
                        player "Igen, már tudom kit szeretnék elhívni."
                        label go_to_prom_w:                        
                        show r excited shut at left
                        show l excited at right
                        l "Tényleg?"
                        show r excited at left
                        show l excited shut at right
                        r "Na és kit?"
                        show r excited shut at left
                        show l excited shut at right
                        menu:
                            "Rózát szeretném elhívni a Bálba":
                                player "Róza."
                                player "Eljönnél velem a Bálba?"
                                show r excited at left
                                show l sad shut at right 
                                r "Én?"
                                r "Komolyan?"
                                show r excited shut at left
                                player "Igen, komolyan."
                                hide l 
                                show r talk 
                                r "Nagyön örülök, hogy megkérdeztél, [player]."
                                if point_r >= 7:
                                    $ prom_w += 1
                                    r "Szívesen megyek veled a Bálba!"
                                    show r excited
                                    r "Úgy örülök!"
                                    r "Megérte ennyit tanulnom!"
                                    show r shy 
                                    r "M-mármint-"
                                    r "Nem csak ez motivált!"
                                    r "V-vagyis-"
                                    show r shy shut
                                    player "Ne aggódj, értelek."
                                    show r talk 
                                    r "Tudod [player] tényleg jól esik, hogy engem hívtál el!"
                                    r "Szívesen megyek veled a Bálba!"
                                    show r 
                                    player "Ezt örömmel hallom!"
                                    show r talk 
                                    r "Ne haragudj, de most mennem kell."
                                    r "Holnap még beszélünk!"
                                    show r 
                                    player "Rendben, addig is, szia!"
                                    show r talk 
                                    r "Szia [player]!"

                                else:
                                    $ prom_w += -1
                                    show r shy 
                                    r "De sajnos én most nem tudok válaszolni, ha nem baj..."
                                    r "M-mit szólnál, ha megvárnánk a holnapi dolgozat eredményeket, aztán visszatérnénk erre?"
                                    show r shy shut 
                                    player "Oh, rendben van."
                                    player "Sajnálom."
                                    show r shy 
                                    r "Semmi baj, köszi, hogy megérted."
                                    show r talk
                                    r "Most mennem kell."
                                    r "Holnap beszélünk."
                                    show r 
                                    player "Szia Róza."
                                    show r talk
                                    r "Szia [player]."

                            "Lillát szeretném elhívni a Bálba":
                                player "Lilla."
                                player "Eljönnél velem a Bálba?"
                                show r sad shut at left
                                show l excited at right 
                                l "Én?"
                                l "Komolyan?"
                                show l excited shut at right
                                player "Igen, komolyan."
                                hide r 
                                show l talk 
                                l "O, [player], nagyon megtisztelő, hogy rám gondoltál!"
                                if point_l >= 6: 
                                    $ prom_w += 2
                                    show l excited
                                    l "Tényleg jól esik, hogy engem hívtál el a Bálba!"
                                    l "Igazán örülök neki!"
                                    show l talk 
                                    l "És nagyon szívesen megyek veled!"
                                    show l
                                    player "Ezt örömmel hallom!"
                                    show l shy 
                                    l "Sajnos nekem most mennem kell."
                                    l "Ne haragudj."
                                    show l talk
                                    l "De holnap még beszélünk!"
                                    show l 
                                    player "Rendben, addig is, szia Lilla!"
                                    show l talk 
                                    l "Szia [player]!"

                                else:
                                    show l sad
                                    l "De sajnos most nem tudok igennel válaszolni."
                                    show l talk
                                    l "Mit szólnál ha esetleg holnap erre visszatérnénk a dolgozat eredménye után?"
                                    show l 
                                    player "Hát... rendben van."
                                    show l talk 
                                    l "Köszönöm, hogy ilyen megértő vagy."
                                    show l sad 
                                    l "Tényleg sajnálom, hogy most nem tudok mást mondani."
                                    show l sad shut 
                                    player "Semmi baj, holnap még beszélünk."
                                    show l talk 
                                    l "Így van!"
                                    l "Addig is szia [player]!"
                                    show l 
                                    player "Szia Lilla."
                                    $ prom_w += -2

            else:
                label bad_grades:
                    player "Hát azt hiszem nem mentek olyan jól mint kellett volna..."
                    show r sad at left
                    show l sad shut at right
                    r "O, sajnálom..."
                    show r sad shut at left
                    show l sad at right
                    l "Én is, [player]..."
                    l "Nagyon örültem volna, ha te is jössz a Bálba." 
                    show r shy at left
                    show l shy shut at right
                    r "És én is..."
                    r "Azért is készültem olyan nagyon..."
                    r "M-mármint-"
                    r "Mennem kell!"
                    hide r
                    show l shy shut at right
                    player "Mi ütött Rózába?"
                    show l sad at right
                    l "T-tudod.."
                    l "Teljesen megértem őt."
                    show l shy at right
                    l "Utána megyek beszélni vele!"
                    hide l 
                    player "De hát még nem is tudjuk az eredményeket..."

        "Hazudok róla":
            if answer >=8:
                jump bad_grades

            else:
                jump good_grades

    hide l 
    hide r            
    "Ideje haza mennem."
    
    scene black_background with fade
    "Ötödik nap vége"   
return