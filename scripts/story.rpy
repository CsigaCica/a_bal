# The game starts here.

label start:
    
    #if you want to block rollback, use the next line:
    #$ renpy.block_rollback()

    scene szoba

    "Let's begin the game:"

    call intro_scene
    
    call speech

    if story < 1:
        "B osztályos vagy"
    else:
        "A osztályos vagy"
    
    "Vége"

return









# label daychange:
#     if day == 1:
#         call intro_scene
#     elif day == 2:
#         call speech
#     elif day <= 3 and day >= 11:
#         call intro_scene
#     else:
#         call prom
# return