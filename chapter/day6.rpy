label daysix:
    t "Beszéd-beszéd"
    "TESZT"
    
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

return