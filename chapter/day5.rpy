label dayfive: 
    # Reggel
    "Ötödik nap"
    scene black_background 
    pause 0.1
    scene szoba with fade

    "*csirip-csirip*"

    player " "

    scene folyoso 
    pause 0.4

    "TESZT"
    call questions


# Iskola után
    call after_school
    
    scene black_background with fade
    "Ötödik nap vége"   
return