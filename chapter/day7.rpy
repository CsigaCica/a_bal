label dayseven:
    # Reggel
    "A Bál napja"
    scene black_background 
    pause 0.1
    scene szoba with fade

    "*csirip-csirip*"

    "Ideje felkelnem."
    if answer >= 8:
        player "Ma nem szabad elkésnem, hiszen ma nagy nap lesz!"
        player "Ma lesz a Bál!"
    else:
        player "Nem szabad elkésnem."
        player "Időben be kell érnem a korrepetálásra."

    menu:
        "Ideges vagyok miatta":
            player "eddig van kész"
        "Egyáltalán nem izgulok ":
            player "eddig van kész"
    
    "Ideje végre indulnom!"
    

    scene black_background with fade
return