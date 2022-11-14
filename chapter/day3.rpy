label daythree:

    # Reggel
    "Harmadik nap"
    scene black_background 
    pause 0.1
    scene szoba with fade

    "*csirip-csirip*"

    "Ideje felkelnem."
    "Ma nem szabad elkésnem, hiszen ma írjuk az első dolgozatot."
    menu:
        "Izgulok miatta":
            "Nagyon ideges vagyok miatta."
            "Készültem rá, de vajon az elég lesz?"
            "Kíváncsi vagyok mit fog kérdezni a tanárnő."

        "Egyáltalán nem izgulok miatta":
            "Nem vagyok ideges miatta."
            "Sokat készültem rá."
            "Nem tud olyat kérdezni, amire ne tudnám a választ."
    
    "De ideje indulnom!"
    
# Iskola udvar 
    scene udvar
    show l talk 
    l "Szia [player]!"
    l "Csak sok sikert szerettem volna kívánni a dolgozathoz!"
    l "Biztos jól fog menni!"

    scene folyoso
    show r shy 
    r "Szia [player]..."
    r "Te is úgy izgulsz a dolgozat miatt, mint én?"
    r "Sokat készültem rá tegnap és tegnap előtt is, de nem vagyok valami magabiztos."
    show r shy shut 
    player "Biztos menni fog!"
    show r talk 
    r "Tudod mit?"
    r "Igazad van!"
    r "Menni fog!"

# Első dolgozat
    scene terem
    pause 0.2
    "*CSÖRRR*"
    show t with moveinright
    pause 0.3
    show t talk
    t "Mindenki itt van?"
    t "Úgy látom igen."
    t "Nos, akkor kezdjük a dolgozatot." 
    show t 
    show t talk with fade
    t "Kezdésnek felvázolnom a dolgozatírás menetét." 
    t "Mindenki fog kapni egy lapot, aminek a bal felső sarkába kell írnotok a neveteket."
    t "Ez után szóban fogom feltenni a kérdéseket, majd négy választ hozzá."
    t "A helyes válasz számát pedig írjátok a lapotokra."
    t "Minden kérdést csak egyszer fogok feltenni."
    t "Nem fogom megismételni, úgyhogy nagyon figyeljetek."
    t "A jó jegyért legalább négy kérdésre helyesen kell felelnetek."
    t "Akkor kezdem is."
    show t
     
    call questions from _call_questions
    
    show t 
    show t talk with fade
    t "Ennyi." 
    t "Remélem mindenkinek jól ment."
    t "Az eredményeteket holnap tudjátok meg."
    t "Most pedig adjátok be a lapjaitokat."
    t "Viszlát."
    show t 
    "*CSÖRRR*"
    
    scene folyoso
    

# Beszélgetés Rózával 
    if class_a_or_b == 1:
        label talk_w_roza_exam:
        show r excited
        r "[player]! Úgy örülök, hogy végre túl vagyunk a dolgozaton!"
        r "Nagyon jó megérzésem van ezzel kapcsolatban!"
        r "Biztos max pontosra írtam!"
        show r talk 
        r "Remélem mindenkinek jól ment!"
        r "Neked hogy ment?"
        show r   
        menu: 
            "Jól ment a dolgozat":
                $ point_r +=1
                player "Szerintem nekem is max pontos lesz."
                player "Magabiztos vagyok az eredményemet illetően!"
                show r excited 
                r "De jó!"
                show r talk
                r "Örlük hogy neked is jól ment a dolgozat!"

            "Nem ment valami jól a dolgozat":
                player "Örülök, hogy neked jól ment, Róza."
                show r what shut 
                player "Sajnos nekem lehetett volna jobb is."
                show r sad  
                r "Jaj [player]..."
                show r talk 
                r "Csak nem ment olyan rosszul!"
                r "Sokat készültél rá te is!"
                r "Lehet, hogy úgy érzed nem ment, de igazából mindent jól tudtál!"
                r "Velem is volt már ilyen!"
                show r sad
                r "Nagyon örlünék ha jó jegyet kapnál..."
                show r talk

        r "Az azt jelentené, hogy el tudunk menni a Bálba!"
        show r shy 
        r "Mármint..."
        show r shy shut
        pause 0.3
        show r shy 
        r "Ne haragudj [player], nekem most mennem kell!" 
        show r shy shut
        pause 0.1


# Beszélgetés Lillával
    else:
        label talk_w_lilla_exam:
        show l talk
        l "[player]! Hogy ment a dolgozat?"
        show l 
        menu:
            "Jól ment a dolgozat":
                $ point_l +=1
                player "Jól ment!"
                player "Magabiztos vagyok az eredményemet illetően."
                player "Szerintem max pontos lett!"
                show l excited 
                l "De jó!"
                l "Ennek nagyon örülök!"
                show l talk
                l "Megérte rá annyit tanulnod."

            "Nem ment valami jól a dolgozat":
                player "Sajnos mehetett volna jobban is."                
                show l what shut 
                player "Nem minden kérdésre tudtam jól a választ..."
                show l sad  
                l "Jaj [player]..."
                l "Sajnálom."
                l "Pedig sokat készültél rá."
                show l talk 
                l "Csak nem lett olyan rossz, mint ahogy azt mondod."
                l "Aki ennyit készül, az biztos jó jegyet kap."

        show l 
        menu:
            "Érdekel Lillának hogy ment a dolgozat":
                $ point_l += 1
                player "És neked, Lilla?"   
                show l talk             
                l "Nekem biztos jó lett."
                l "Sokat készültem rá, egyedül és másokkal is."
                l "Nem tudott a tanárnő olyat kérdezni, ami kifogott volna rajtam!"
                show l
                player "Azta! Ügyes vagy!" 
                show l shy
                l "K-köszi..."

            "Nem érdekel hogy ment a dolgozat Lillának":
                pause 0.1

        show l talk 
        l "De így el tudok menni a Bálba!"
        show l excited
        l "És ennek nagyon örülök!"
        l "Jó lenne ha te is el tudnál jönni."
        show l shy
        l "Mármint jó lenne, ha mindenki el tudna jönni!"
        show l shy shut 
        pause 0.5
        show l shy
        l "M-most mennem kell, holnap beszélünk [player]..."
        show l shy shut 
        pause 0.3
        

# Beszélgetés lehetősége a másik lánnyal
    label talk_w_other:
    scene udvar
    pause 0.3
    if class_a_or_b == 1:
        "Ott van Lilla."
        menu:
            "Odamegyek beszélni vele":
                "Megkérdezem neki hogy ment a dolgozat."
                $ point_l += 1
                show l talk
                l "[player]! Hogy ment a dolgozat?"
                show l 
                menu:
                    "Jól ment a dolgozat":
                        $ point_l +=1
                        player "Jól ment!"
                        player "Magabiztos vagyok az eredményemet illetően."
                        player "Szerintem max pontos lett!"
                        show l excited 
                        l "De jó!"
                        l "Ennek nagyon örülök!"
                        show l talk
                        l "Megérte rá annyit tanulnod."

                    "Nem ment valami jól a dolgozat":
                        player "Sajnos mehetett volna jobban is."                
                        show l what shut 
                        player "Nem minden kérdésre tudtam jól a választ..."
                        show l sad  
                        l "Jaj [player]..."
                        l "Sajnálom."
                        l "Pedig sokat készültél rá."
                        show l talk 
                        l "Csak nem lett olyan rossz, mint ahogy azt mondod."
                        l "Aki ennyit készül, az biztos jó jegyet kap."

                show l 
                player "És neked, Lilla?"   
                $ point_l += 1
                show l talk             
                l "Nekem biztos jó lett."
                l "Sokat készültem rá, egyedül és másokkal is."
                l "Nem tudott a tanárnő olyat kérdezni, ami kifogott volna rajtam!"
                show l
                player "Azta! Ügyes vagy!" 
                show l shy
                l "K-köszi..."
                show l talk 
                l "De így el tudok menni a Bálba!"
                show l excited
                l "És ennek nagyon örülök!"
                l "Jó lenne ha te is el tudnál jönni."
                show l shy
                l "Mármint jó lenne, ha mindenki el tudna jönni!"
                show l shy shut 
                pause 0.5
                show l shy
                l "M-most mennem kell, holnap beszélünk [player]..."
                show l shy shut 
                pause 0.3
                hide l
                "Vajon mi ütött mindenkibe?"

            "Nem szeretném zavarni":
                "Inkább hazamegyek."
    else:
        "Ott van Róza."
        menu:
            "Odamegyek beszélni vele":
                "Megkérdezem neki hogy ment a dolgozat."
                $ point_r += 1
                show r excited
                r "[player]! Úgy örülök, hogy végre túl vagyunk a dolgozaton!"
                r "Nagyon jó megérzésem van ezzel kapcsolatban!"
                r "Biztos max pontosra írtam!"
                show r talk 
                r "Remélem mindenkinek jól ment!"
                r "Neked hogy ment?"
                show r   
                menu: 
                    "Jól ment a dolgozat":
                        $ point_r +=1
                        player "Szerintem nekem is max pontos lesz."
                        player "Magabiztos vagyok az eredményemet illetően!"
                        show r excited 
                        r "De jó!"
                        show r talk
                        r "Örlük hogy neked is jól ment a dolgozat!"

                    "Nem ment valami jól a dolgozat":
                        player "Örülök, hogy neked jól ment, Róza."
                        show r what shut 
                        player "Sajnos nekem lehetett volna jobb is."
                        show r sad  
                        r "Jaj [player]..."
                        show r talk 
                        r "Csak nem ment olyan rosszul!"
                        r "Sokat készültél rá te is!"
                        r "Lehet, hogy úgy érzed nem ment, de igazából mindent jól tudtál!"
                        r "Velem is volt már ilyen!"
                        show r sad
                        r "Nagyon örlünék ha jó jegyet kapnál..."
                        show r talk

                r "Az azt jelentené, hogy el tudunk menni a Bálba!"
                show r shy 
                r "Mármint..."
                show r shy shut
                pause 0.5
                show r shy 
                r "Ne haragudj [player], nekem most mennem kell!" 
                show r shy shut
                pause 0.3
                hide r
                "Vajon mi ütött mindenkibe?"

            "Nem szeretném zavarni":
                "Inkább hazamegyek."
    
    scene black_background with fade
    "Harmadik nap vége"

return