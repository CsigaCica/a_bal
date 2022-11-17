## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        if renpy.get_screen("main_menu"):
            xalign 0.5
            yalign 0.2
            style_prefix "custom_start_button"
            
            textbutton _("Start") action Start()

    vbox:

        style_prefix "navigation"

        if renpy.get_screen("main_menu"):
            xalign 0.5
            yalign 0.7
        else:
            xalign 0.05
            yalign 0.5
        
        spacing gui.navigation_spacing

        if renpy.get_screen("main_menu"):
            
            pass

        else:

            textbutton _("Történet") action ShowMenu("history")

            textbutton _("Mentés") action ShowMenu("save")

        textbutton _("Betöltés") action ShowMenu("load")

        textbutton _("Beállítás") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Újrajátszás Vége") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Főmenü") action MainMenu()

        #textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Segítség") action ShowMenu("help")

        if renpy.variant("pc"):
            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Kilépés") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 0.5

