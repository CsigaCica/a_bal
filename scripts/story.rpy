# The game starts here.

label start:
    
    #if you want to block rollback, use the next line:
    #$ renpy.block_rollback()

    scene kert

    "Let's begin the game:"

    call intro_scene
    
    if story < 1:
        "B osztályos vagy"
    else:
        "A osztályos vagy"
    
    "Vége"


return
