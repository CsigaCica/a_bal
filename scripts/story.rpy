# The game starts here.

label start:
    
    #if you want to block rollback, use the next line:
    #$ renpy.block_rollback()

    scene kert

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
#     elif day == 3:
#         call intro_scene
#     elif day == 4:
#         call intro_scene
#     elif day == 5:
#         call intro_scene
#     elif day == 6:
#         call intro_scene
#     elif day == 7:
#         call intro_scene
#     elif day == 8:
#         call intro_scene
#     elif day == 9:
#         call intro_scene
#     elif day == 10:
#         call intro_scene
#     elif day == 11:
#         call intro_scene
#     else:
#         call prom
# return