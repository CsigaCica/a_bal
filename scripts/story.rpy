# The game starts here.

label start:
    
    # if you want to block rollback, use the next line:
    # $ renpy.block_rollback()

    scene black_background 

    # "Let's begin the game:"
    
    # call dayone

    # "Róza pont: [point_r]"
    # "Lilla pont: [point_l]"

    # call daytwo 

    # "Róza pont: [point_r]"
    # "Lilla pont: [point_l]"

    call daythree
    
    
    
    "Vége"
   
return