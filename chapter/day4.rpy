label dayfour:
    # Reggel
    "Negyedik nap"
    scene black_background 
    pause 0.1
    scene szoba with fade

    "*csirip-csirip*"

    player "*sóhaj*"
    player "Ideje felkelni."
    player "Ma tudjuk meg a dolgozat eredményét."
    player "Időben be kell érnem."

# Beszélgetés Rózával
    scene udvar with fade
    pause
    if class_a_or_b == 1:
        show r excited
        r "Hú [player]! Olyan kíváncsi vagyok!"
        show r excited shut
        player "Izgulsz, igaz?"
        show r excited
        r "Igen, nagyon!"
        show r excited shut
        player "Hamarosan megtudjuk."
        show r talk 
        r "Így van!"
        show r sad
        r "Remélem nem kell korrepetálásra mennem..."
        show r sad shut 
        player "Csak nem kell."
        show r talk 
        r "Remélem is!"
        r "Na menjünk."
        show r 
        pause 0.3
    else:
# Beszélgetés Lillával
        show l talk 
        l "Szia [player]!"
        show l  
        player "Szia Lilla!"
        show l talk 
        l "Neked is fúrja az oldalad a kínácsiság?"
        show l  
        player "Természetesen. Nagyon kíváncsi vagyok az eredményemre."
        show l excited
        l "Biztos jól ment!"
        show l talk 
        l "De azt hiszem nem kéne elkésnünk."
        show l 
        player "Igazad van."
        player "Induljunk is."
        pause 0.3


# Negyedik óra
    scene terem
    "*CSÖRRR*"
    pause 0.2
    show t with moveinright
    pause 0.3
    show t talk
    t "Gyerekek!"
    t "Tudom, hogy mindenki csak az eredményére kíváncsi."
    t "De azokat majd csak óra után fogom elmondani."
    t "Úgyhogy kezdjük is az órát." 
    show t 
    pause 0.2
    show t talk
    t "Remélem mindenki értett mindent." with fade
    t "Ha valami nem volt világos most kérdezzetek."
    show t 
    pause
    show t talk
    t "Úgy látom nincs kérdés."
    t "Akkor elmondom az eredményeket."
    t "[player] neked [answer] pontod lett." with fade 
    t "Mivel a dolgozatok a többségnek nem sikerültek olyan jól, mint kellett volna, úgy döntöttem, hogy holnap javító dolgozat lesz." with fade
    t "Készüljetek fel rá."
    show t 
    "*CSÖRRR*"
    hide t
    pause 

    if class_a_or_b == 1:
        show r sad
        r "Neked hány pontod lett [player]?"
        show r sad shut
        player "[answer] pontom lett."
        if answer == 8:
            $ point_r +=1
            show r excited
            r "Tényleg? Az nagyon jó!"
            r "Akkor neked max pontos lett!"
            r "De ügyes vagy!"
            show r sad
            r "Bárcsak nekem is annyi lenne..."
            r "De sajnos nekem nem sikerült jól... "
        elif answer >=4:
            $ point_r +=1
            show r talk 
            r "Hú [player]!"
            r "Akkor neked jól sikerült!"
            r "Irigyellek."
            show r sad
            r "Bárcsak nekem is ilyen jól sikerült volna..."
            r "Nekem sajnos nem ment valami jól..."
        else:
            show r sad
            r "Oh, akkor neked se sikerült valami jól."
            r "Remélem a javító mindekettőnknek jobban fog menni."
        
        show r sad shut
        menu:
            "Megvígasztalom Rózát":
                $ point_r +=1
                player "Ne szomorkodj, még nincs minden veszve."
                player "Ha a holnapi jól sikerül, elmehetsz a Bálba."
                show r sad
                r "Ez igaz..."
                r "De ha egyedül megyek, úgyis mindegy..."
                show r shy shut 
                pause 0.3
                show r shy
                r "De persze, szeretném jól megírni a holnapi dolgozatot!"
                show r shy shut
                player "Mit szólnál ha átnéznénk az anyagot?"
                show r excited 
                r "Az remek lenne!"
                show r excited shut
                player "Rendben. Akkor kezdjük." 
                show r talk 
                r "Köszi [player], hogy átnézted velem az anyagot!" with fade
                show r excited
                r "Mostmár sokkal több önbizalmam van a holnappal kapcsolatban!"
                r "Biztos jól fog menni!"
                show r talk
                r "Sok sikert a holnapi dolgozathoz!"       
                show r 
                player "Sok sikert neked is, Róza!"
                player "Szia!"
                show r talk
                r "Szia!"
                show r
                pause 0.1

            "Elindulok haza":
                player "Ne aggódj, csak tanulni kell holnapra."
                player "Én is azt fogom csinálni."
                player "Majd holnap találkozunk."
                player "Addig szia!"
                show r sad
                r "Szia [player]."
                show r sad shut
                pause 0.1

    else:
# Beszélgetés Lillával
        show l sad
        l "Hogy ment a dolgozat [player]?"
        show l sad shut
        player "[answer] pontom lett. Neked?"
        if answer == 8:
            $ point_l +=1
            show l excited
            l "Tényleg? Az nagyon jó!"
            l "Akkor neked max pontos lett!"
            l "De ügyes vagy!"
            l "Nem hiába tanultál annyit!"
            show l sad
            l "Sajnos én egyet elrontottam."
            l "Pedig olyan sokat tanultam rá..."
        elif answer >=4:
            $ point_l +=1
            show l talk 
            l "Hú [player]!"
            l "Akkor neked jól sikerült!"
            l "Nagyon ügyes vagy!"
            l "Nem hiába tanultál annyit!"
            show l sad
            if answer == 7:
                l "Sajnos egyet és is elrontottam."
            else:
                l "Sajnos én egyet elrontottam."           
            l "Pedig olyan sokat tanultam rá..."
        else:
            show l sad
            l "Oh sajnálom."
            show l talk 
            l "De holnap javíthatsz rajta!"
            show l sad
            l "Nekem is javítanom kell..."
            l "Sajnos egyet elrontottam."
            l "Pedig olyan sokat tanultunk rá..."
        
        show l sad shut
        menu:
            "Megvígasztalom Lillát":
                $ point_l +=1
                player "Ne szomorkodj, még nincs minden veszve."
                player "Így is elmehetsz a Bálba."
                show l sad
                l "Ez igaz..."
                l "De ha egyedül megyek, úgyis mindegy..."
                show l shy shut 
                pause 0.3
                show l shy
                l "De persze, szeretném ennél is jobbra megírni a holnapi dolgozatot!"
                show l shy shut
                player "Mit szólnál ha átnéznénk az anyagot?"
                show l excited 
                l "Az remek lenne!"
                show l excited shut
                player "Rendben. Akkor kezdjük." 
                show l talk 
                l "Örülök, hogy átnéztük az anyagot, [player]." with fade
                l "Köszönöm, hogy rám szántad az időd."
                show l
                player "Ugyan, nincs mit!"
                show l talk
                l "Sok sikert a holnapi dolgozathoz!"       
                show l 
                player "Sok sikert neked is, Lilla!"
                player "Szia!"
                show l talk
                l "Szia!"
                show l
                pause 0.1

            "Elindulok haza":
                player "Ne aggódj, csak tanulni kell holnapra."
                player "Én is azt fogom csinálni."
                player "Majd holnap találkozunk."
                player "Addig szia!"
                show l sad
                l "Szia [player]."
                show l sad shut
                pause 0.1
        
# Óra után Lillával
    scene udvar
    if class_a_or_b == 1:
        "Ott van Lilla."
        menu: 
            "Odamegyek hozzá":
                $ point_l +=1
                show l sad shut
                player "Szia Lilla!"
                player "Mi a baj?"
                show l sad 
                l "Nem lett olyan jó a dolgozatom eredménye, mint szerettem volna."
                l "Pedig olyan sokat készültem rá."
                show l what
                l "Ti is írtatok, igaz?"
                l "Neked hány pontos lett?"
                show l what shut
                if answer == 8:
                    $ point_l +=1
                    player "Nekem max pontos lett."
                    show l excited
                    l "Tényleg?"
                    l "Ez nagyszerű [player]!"
                    l "Nagyon ügyes vagy!"
                    show l sad 
                    l "Bár nekem is annyi lett volna..."
                    l "Egyet sajnos elrontottam."
                else:
                    player "Lehetett volna jobb is."
                    player "[answer] pontom lett."
                    show l sad 
                    l "Megértem."
                    l "Sajnálom [player]."
                    if answer == 7:
                        l "Én is egyet rontottam el."
                    else:
                        l "Egyet én is elrontottam."                                       
                show l sad shut
                player "Ne szomorkodj, még nincs minden veszve."
                player "Így is elmehetsz a Bálba."
                show l sad
                l "Ez igaz..."
                l "De ha egyedül megyek, úgyis mindegy..."
                show l shy shut 
                pause 0.3
                show l shy
                l "De persze, szeretném ennél is jobbra megírni a holnapi dolgozatot!"
                show l shy shut
                player "Megértem."
                show l talk 
                l "Ideje mennem [player]."
                l "Még készülnöm kell holnapra."
                l "Örülök, hogy beszéltünk!"
                show l
                player "Sok sikert a holnapi dolgozathoz!"
                show l talk
                l "Sok sikert neked is!"       
                show l 
                player "Szia!"
                show l talk
                l "Szia!"
                show l
                pause 0.1
            "Nem szeretném zavarni":
                "Inkább csak hazamegyek."
    else:
# Óra után Rózával
        "Ott van Róza."
        menu: 
            "Odamegyek hozzá":
                $ point_r +=1
                show r sad shut
                player "Szia Róza!"
                player "Mi a baj?"
                show r sad 
                r "Nem sikerült valami jól a dolgozatom..."
                show r what
                r "Ti is írtatok, igaz?"
                r "Neked hány pontos lett [player]?"
                show r what shut
                if answer == 8:
                    $ point_r +=1
                    player "Nekem max pontos lett."
                    show r excited
                    r "Tényleg?"
                    r "Ez nagyszerű [player]!"
                    r "Nagyon ügyes vagy!"
                    show r sad 
                    r "Bár nekem is ilyen jól ment volna..."
                else:
                    player "Lehetett volna jobb is."
                    show r sad 
                    r "Megértem."
                    r "Sajnálom [player]."
                    r "Nekem se ment valami jól..."
                show r sad shut
                player "Ne szomorkodj, még nincs minden veszve."
                player "Még elmehetsz a Bálba."
                show r sad
                r "Ez igaz..."
                r "De ha egyedül megyek, úgyis mindegy..."
                show r shy shut 
                pause 0.3
                show r shy
                r "De persze, szeretném jóra megírni a holnapi dolgozatot!"
                show r shy shut
                player "Megértem."
                show r talk 
                r "Ideje mennem [player]."
                r "Még készülnöm kell holnapra."
                r "Örülök, hogy beszéltünk!"
                show r
                player "Sok sikert a holnapi dolgozathoz!"
                show r talk
                r "Sok sikert neked is!"       
                show r 
                player "Szia!"
                show r talk
                r "Szia!"
                show r
                pause 0.1

            "Nem szeretném zavarni":
                "Inkább csak hazamegyek."

    scene black_background with fade
    "Negyedik nap vége"

return