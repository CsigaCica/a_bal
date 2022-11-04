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
    hide r 

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
    
    call first_exam
    
    show t 
    show t talk with fade
    t "Ennyi." 
    t "Remélem mindenkinek jól ment."
    t "Az eredményeteket holnap tudjátok meg."
    t "Most pedig adjátok be a lapjaitokat."
    show t 
    "*CSÖRRR*"
    

    scene folyoso
# Beszélgetés Rózával 
    if class_a_or_b == 1:
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
                show r 
                r "Örlük hogy jól ment neked a dolgozat!"
                r "Az azt jelentené, hogy el tudunk menni a Bálba."
                show r shy 
                r "Mármint..."
                r "Ne haragudj [player], nekem most mennem kell!" 


            "Nem ment valami jól a dolgozat":
                player "Nem, egyáltalán nem vagyok ideges miatta."
                show r excited
                r "Tényleg?"
                show r shy
                r "Úgy irigyellek..."
                show r talk
                r "Segítesz nekem átvenni a mai anyagot?"
                show r 
                menu: 
                    "Szívesen átismétlen Rózával az anyagot":
                        label study_w_roza2:
                        $ point_r +=1
                        player "Persze, szívesen segítek tanulni."
                        show r excited
                        r "Tényleg? Jaj de jó!"
                        show r talk
                        r "Akkor tanuljunk!"
                        show r 
                        player "Rendben. Akkor kezdjük." 
                        show r talk 
                        r "Köszi [player], hogy tanultál velem!" with fade
                        show r excited
                        r "Mostmár sokkal több önbizalmam van a holnappal kapcsolatban!"
                        show r talk
                        r "Most mennem kell, de holnap még beszélünk!"
                        r "Sok sikert a holnapi dolgozathoz!"
                        

                    "Nem szeretném átismételni Rózával az anyagot":
                        label not_study_w_roza2:
                        player "Nem szeretném, bocsi."
                        show r sad 
                        r "Oh... Rendben van [player]."
                        r "Akkor megkérek valaki mást..."
                        r "Azért sok sikert a holnapi dolgozatra való tanuláshoz!"
        show r talk              
        r "Szia!"
        show r
        pause 0.1

# Tanulás Lillával
    else:
        show l talk
        l "Szia [player]!"
        l "Értetted a tanárnőt?"
        show l 
        menu:
            "Igen, mindent":
                player "Persze, minden érthető volt."
                $ point_l += 1
                show l talk
                l "Ennek örülök!"
                l "Azért szeretnél csatlakozni hozzám átismételni az anyagot?"
                show l 
                menu:
                    "Nem szeretném átismételni az anyagot":
                        player "Nem szükséges, de azért köszi."
                        jump not_study_w_lilla2

                    "Igen, szeretnék csatlakozni":
                        player "Szívesen csatlakozok átismételni az anyagot."
                        jump study_w_lilla2

                
            "Nem, nem mindent":
                player "Nem, volt egy rész ami nem egészen tiszta..."
                show l sad
                l "Oh..."
                show l talk 
                l "Szeretnéd hogy elmagyarázzam?"
                show l 
                menu: 
                    "Igen":
                        player "Igen, annak örülnék."
                        label study_w_lilla2:
                        $ point_l += 1
                        show l excited
                        l "Szuper! Akkor tanuljunk!"
                        show l talk
                        l "Szerintem kezdjük az elején, hogy biztos minden menjen."
                        show l
                        pause 0.1
                        show l talk 
                        l "Így már mindent értesz?" with fade
                        show l 
                        player "Igen Lilla. Így már biztos jól fog menni a holnapi dolgozat!"
                        show l talk
                        l "Abban biztos vagyok!"
                        show l sad
                        l "Most mennem kell."
                        show l talk 
                        l "Sok sikert a holnapi dolgozathoz!"
                        l "Azért otthon nézd át még párszor, én is azt fogom csinálni!"
                        show l 
                        player "Oké, köszi mégegyszer. Szia."
                        show l talk 
                        l "Szia [player]."

                    "Nem":
                        player "Nem kell köszi. Menni fog egyedül is."
                        label not_study_w_lilla2:
                        show l sad
                        l "Oh, rendben."
                        show l talk
                        l "De szívesen segítek benne bármikor."
                        show l
                        player "Rendben Lilla, köszi."
                        show l talk
                        l "Nincs mit [player]."

        show l
        pause 0.1

        label after_school2:
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
    "Második nap vége"


return