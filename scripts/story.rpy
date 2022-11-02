# The game starts here.

label start:
    
    #if you want to block rollback, use the next line:
    #$ renpy.block_rollback()

    scene black_background 

    # "Let's begin the game:"
    
    # call dayone

    # "Róza pont: [point_r]"
    # "Lilla pont: [point_l]"

    # call daytwo 

    # "Róza pont: [point_r]"
    # "Lilla pont: [point_l]"

    #call daythree
    call first_exam
    
    
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