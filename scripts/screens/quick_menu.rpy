## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Vissza") action Rollback()
            textbutton _("Beállítások") action ShowMenu('history')
            #textbutton _("Átlépés") action Skip() alternate Skip(fast=True, confirm=True)
            #textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Mentés") action ShowMenu('save')
            #textbutton _("Gyors Mentés") action QuickSave()
            #textbutton _("Gyors Betöltés") action QuickLoad()
            #textbutton _("Beállítás") action ShowMenu('preferences') 


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")
