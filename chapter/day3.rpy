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
    
    call first_exam


return