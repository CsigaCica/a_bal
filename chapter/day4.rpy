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

        call questions

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
        player "[answer]. Neked?"
        if answer == 8:
            show r excited
            r "Tényleg? Az nagyon jó!"
            r "Akkor neked max pontos lett!"
            r "De ügyes vagy!"
            show r sad
            r "Bárcsak nekem is annyi lenne..."
            r "De sajnos nekem nem sikerült jól... "
        elif answer >=4:
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
            show r talk
            r "Remélem a javító mindekettőnknek jobban fog menni."


    else:
# Beszélgetés Lillával
        show l 
        

# Iskola után
    call after_school
    
    scene black_background with fade
    "Negyedik nap vége"

return