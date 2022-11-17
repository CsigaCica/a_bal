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
        menu:
            "Ideges vagyok miatta":
                player "Izgulok, hogy vajon milyen lesz a mai nap!"
                player "Biztos jó lesz!"
                player "Már várom."

            "Egyáltalán nem izgulok ":
                player "Nem igazán izgat, hogy mi lesz ma."
                player "Csak sodródok az árral."

    else:
        player "Nem szabad elkésnem."
        player "Időben be kell érnem a korrepetálásra."
        menu:
            "Ideges vagyok miatta":
                player "Izgulok, hogy vajon milyen lesz a mai nap!"

            "Egyáltalán nem izgulok ":
                player "Nem igazán izgat, hogy mi lesz ma."
    
    "Ideje végre indulnom!"

# BÁL
    if answer >= 8: 
        scene bal with fade
        if prom_w == 1 or prom_w == -1 or prom_w == 3:
            label prom_w_roza:
            if point_r >= 7:
                show r prom 
                player "Hú Róza!"
                player "Nagyon csinos vagy!"
                show r prom talk 
                r "Köszönöm [player]! Te is Jól nézel ki!"
                show r prom 
                player "Felkérhetlek egy táncra?"
                show r prom talk
                r "Azt hittem sose kérdezed meg!" 
                show r prom               
            else:
                label prom_alone:
                show r prom at left 
                show l prom at right
                player "Hú lányok, nagyon csinosak vagytok!"
                show r prom talk at left 
                r "Köszi [player]!"
                r "Én most megyek, szia!"
                hide r 
                show l prom talk 
                l "Egyedül jöttél?"
                show l prom  
                player "Igen..."
                show l prom talk 
                l "Oh, rendben van. Viszont én is megyek. Szia!"
                scene bal
                pause
        else:
            if prom_w == 2 or prom_w == -2 or prom_w == 4:
                if point_l >= 6:
                    show l prom 
                    player "Hú Lilla!"
                    player "Nagyon csinos vagy!"
                    show l prom talk 
                    l "Köszönöm [player]! Te is Jól nézel ki!"
                    show l prom 
                    player "Felkérhetlek egy táncra?"
                    show l prom talk
                    l "Örömmel táncolok veled!" 
                    show l prom 
                else:
                    jump prom_alone              
            else:
                jump prom_alone

# KORREPETÁLÁS    
    else:
        scene korrep with fade
        player "Ideje tanulni."

    scene black_background with fade

return