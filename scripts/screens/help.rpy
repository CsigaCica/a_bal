## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Segítség"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Billentyűzet") action SetScreenVariable("device", "keyboard")
                textbutton _("Egér") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Kontroller") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Előrelép a párbeszédben.")

    hbox:
        label _("Szóköz")
        text _("Előrelép a párbeszédben.")

    hbox:
        label _("Nyilak")
        text _("Navigál a felhasználói felületen.")

    hbox:
        label _("Escape")
        text _("Játékmenü megnyitása.")

    hbox:
        label _("Ctrl")
        text _("Átugorja a dialógusokat.")

    hbox:
        label _("Tab")
        text _("Előregörget a legközelebbi választási lehetőségig.")

    hbox:
        label _("Page Up")
        text _("Visszagörget egy előző dialógushoz.")

    hbox:
        label _("Page Down")
        text _("Előregörget egy későbbi dialógushoz.")

    hbox:
        label "H"
        text _("A felhasználói felület elrejtése.")

    hbox:
        label "S"
        text _("Képernyőkép készítése.")

    # hbox:
    #     label "V"
    #     text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    # hbox:
    #     label "Shift+A"
    #     text _("Játékmenü megnyitása.")


screen mouse_help():

    hbox:
        label _("Bal gombnyomás")
        text _("Előrelép a párbeszédben.")

    hbox:
        label _("Görgő gombnyomás")
        text _("Párbeszéd elrejtése.")

    hbox:
        label _("Jobb gombnyomás")
        text _("Játékmenü.")

    hbox:
        label _("Felfelé görgetés")
        text _("Visszagörget egy előző dialógushoz.")

    hbox:
        label _("Lefelé görgetés")
        text _("Előregörget egy későbbi dialógushoz.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Kalibrálás") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0

