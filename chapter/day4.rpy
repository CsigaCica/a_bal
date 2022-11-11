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
    player "Kíváncsi vagyok hányas lett!"

    scene udvar with fade
    pause 0.7
    scene folyoso with fade
    pause 0.7
    scene tanari with fade
    pause
    




# Első eredmény
label first_result:

    show t talk
    if answer == 8:
        "Gratulálok! Jól ment a dolgozat"
    elif answer >= 4:
        "Hát ez egy közepes.."
    else:
        t "Sajnos nem sikerült mindenkinek jól ez a dolgozat."
        t "Akiknek ez most nem ment, vagyis akik nem érték el legalább a 4 pontot, azoknak korrepetációt fogok tartani holnap után."
        t "Tudom, hogy aznap van a bál, de sajnos páran ki kell hagyjátok."
        t "Legközelebb készüljetek többet."

    pause

# Iskola után
    call after_school
    
    scene black_background with fade
    "Negyedik nap vége"

return