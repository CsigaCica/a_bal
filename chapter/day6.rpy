label daysix:
    # Reggel
    "Hatodik nap"
    scene black_background 
    pause 0.1
    scene szoba with fade

    "*csirip-csirip*"

    player "Ideje felkelni."
    player "Ma végre kiderül hányas lett a második dolgozatom!"

    if prom_w == -1:
        player "Sajnálom, hogy tegnap Róza nem tudott válaszolni."
        player "Ma megint megkérdezem, hátha igent mond!"
    elif prom_w == -2:
        player "Sajnálom, hogy tegnap Lilla nem tudott válaszolni."
        player "Ma megint megkérdezem, hátha igent mond!"
    elif prom_w == 1:
        player "Nagyon örülök, hogy Róza igent mondott tegnap, és eljön velem a Bálba!"
        player "Aranyos lány."
    elif prom_w == 2:
        player "Nagyon örülök, hogy Lilla igent mondott tegnap, és eljön velem a Bálba!"
        player "Aranyos lány."
    else:
        player "Ideje eldöntenem kivel menjek a Bálba."
        menu:
            "Rózát hívom el":
                player "Azt hiszem Rózát hívom el."
            "Lillát hívom el":
                player "Azt hiszem Lillát hívom el."

    scene folyoso 
    pause 0.4

    t "Beszéd-beszéd"
    
# Második eredmény
label second_result:
    show t talk
    if answer == 16:
        "Gratulálok! Jól ment a dolgozat"
    elif answer >= 8:
        "Hát ez egy közepes.."
    else:
        t "Sajnos nem sikerült mindenkinek jól ez a dolgozat."
        t "Akiknek ez most nem ment, vagyis akik nem érték el legalább a 4 pontot, azoknak korrepetációt fogok tartani holnap után."
        t "Tudom, hogy aznap van a bál, de sajnos páran ki kell hagyjátok."
        t "Legközelebb készüljetek többet."

    pause

# Iskola után
    
    scene black_background with fade
    "Hatodik nap vége"   
return