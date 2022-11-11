# Itt kezdődik a játék

label start:
    
    # if you want to block rollback, use the next line:
    # $ renpy.block_rollback()

    # scene black_background 

    # "Let's begin the game:"
    
    # call dayone

    # "Róza pont: [point_r]"
    # "Lilla pont: [point_l]"

    # call daytwo 

    # "Róza pont: [point_r]"
    # "Lilla pont: [point_l]"

    call daythree

    "Róza pont: [point_r]"
    "Lilla pont: [point_l]"

    call dayfour

    "Róza pont: [point_r]"
    "Lilla pont: [point_l]"

    call dayfive

    "Róza pont: [point_r]"
    "Lilla pont: [point_l]"

    call daysix
    
    "Róza pont: [point_r]"
    "Lilla pont: [point_l]"

    call dayseven

    "Róza pont: [point_r]"
    "Lilla pont: [point_l]"

    "Vége"
   
return