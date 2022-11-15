# Itt kezdődik a játék

label start:
    
    # if you want to block rollback, use the next line:
    # $ renpy.block_rollback()

    scene black_background 

    "Let's begin the game:"

    call dayone from _call_dayone
    call daytwo from _call_daytwo 
    call daythree from _call_daythree
    call dayfour from _call_dayfour
    call dayfive from _call_dayfive
    call daysix from _call_daysix
    call dayseven from _call_dayseven
    
    "Vége"
   
   

return