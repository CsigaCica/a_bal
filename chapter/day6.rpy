label daysix:
    # Reggel
    "Hatodik nap"
    scene black_background 
    pause 0.1
    scene szoba with fade

    "*csirip-csirip*"

    player "Ideje felkelni."
    player "Ma végre kiderül hányas lett a második dolgozatom!"

    if prom_w == -1:
        player "Sajnálom, hogy tegnap Róza nem tudott válaszolni."
        player "Ma megint megkérdezem, hátha igent mond!"
    elif prom_w == -2:
        player "Sajnálom, hogy tegnap Lilla nem tudott válaszolni."
        player "Ma megint megkérdezem, hátha igent mond!"
    elif prom_w == 1:
        player "Nagyon örülök, hogy Róza igent mondott tegnap, és eljön velem a Bálba!"
        player "Aranyos lány."
    elif prom_w == 2:
        player "Nagyon örülök, hogy Lilla igent mondott tegnap, és eljön velem a Bálba!"
        player "Aranyos lány."
    else:
        player "És ideje eldöntenem kivel menjek a Bálba."
        menu:
            "Rózát hívom el":
                player "Azt hiszem Rózát hívom el."
                $ prom_w += 3
            "Lillát hívom el":
                player "Azt hiszem Lillát hívom el."
                $ prom_w += 4

# Beszélgetés Zolival
    scene folyoso with fade
    pause 0.4
    if know_zoli == 0:
        show z talk 
        i "Szia [player]!"
        i "Én Zoli vagyok."
        z "Furcsa, hogy még nem is beszéltünk, hiszen osztálytársak vagyunk!"
        z "Na nem baj, jobb később, mint soha."

    else:
        z "Szia [player]!"

    z "Nem akarlak feltartani, csak azt szerettem volna kérdezni, hogy gondolkodtál-e már azon, kivel menj a Bálba?"
    z "Én már tudom kivel szeretnék menni, és óra után meg is fogom kérdezni, az biztos!"
    show z 
    menu:
        "Elmondom Zolinak":
            if prom_w == -1 or prom_w == 3:
                player "Rózával szeretnék menni a Bálba."
            elif prom_w == -2 or prom_w == 4:
                player "Lillával szeretnék menni a Bálba."
            elif prom_w == 1:
                player "Rózával megyek a Bálba."
            else:
                player "Lillával megyek a Bálba."            
            show z talk
            z "Köszi, hogy elmondtad! Jó tudni!"
            if prom_w == -1 or prom_w == 1 or prom_w == 3:     
                if point_r < 7:           
                    z "Ha már te is elmondtad, én se titkolom!"
                    z "Én is arra gondoltam, hogy Rózával megyek."
                else: 
                    z "Ha már te is elmondtad, én se titkolom!"
                    z "Én arra gondoltam, hogy Lillával megyek."
            else:
                if point_l < 6:
                    z "Ha már te is elmondtad, én se titkolom!"
                    z "Én is arra gondoltam, hogy Lillával megyek."
                else: 
                    z "Ha már te is elmondtad, én se titkolom!"
                    z "Én arra gondoltam, hogy Rózával megyek."

            z "De ideje mennünk órára! Nem kéne elkésni!"

        "Nem tartozik rá":
            player "Sajnálom, de nem hiszem, hogy el kell neked mondanom."
            show z talk 
            z "Jól van na, csak kérdeztem."
            z "Nem kell ám felkapni a vizet!"
            z "Ha nem, hát nem."
            z "Akkor menjünk órára."

# Hatodik óra
    scene terem
    "*CSÖRRR*"
    pause 0.2
    show t with moveinright
    pause 0.3
    show t talk
    t "Gyerekek!"
    t "Tudom, hogy mindenkit csak az eredménye érdekel."
    t "Ezért azokat ismét majd csak óra után fogom elmondani."
    t "Úgyhogy kezdjük is el az órát." 
    show t 
    pause 0.2
    show t talk
    t "Remélem mindenki értett mindent." with fade
    t "Ha valami nem volt világos, most kérdezzetek."
    show t 
    pause
    show t talk
    t "Úgy látom nincs kérdés."
    t "Akkor elmondom az első és második dolgozat összevont eredményét."
    t "[player] neked összesen [answer] pontod lett." with fade 
    t "A javító dolgozatnak hála sokkal jobb jegyek születtek!" with fade
    t "Örülök, hogy legalább a második dolgozatra ennyit készültetek!"
    t "Mivel az eredményeket összevontam, így a minimum pont ami szükséges, az 8."
    t "Aki ezt elérte, az mehet a Bálba!"
    t "Aki nem, azzal mint már említettem külön órát tartok."
    t "Viszlát!"
    show t 
    "*CSÖRRR*"
    hide t
    if answer == 18:
        player "De jó! Max pontos lett!"
        $ point_l += 1
        $ point_r += 1
    else:
        pass
    pause

# Beszélgetés a Bálról a kiválasztott lánnyal
    scene folyoso
    if answer >= 8:
# Róza elhívása a Bálba (másodszor)
        if prom_w == -1:
            show r 
            player "Szia, ne haragudj!"
            show r shy shut 
            player "Tegnap nem válaszoltál, hogy eljössz-e velem a Bálba."
            if point_r >= 7:
                show r talk 
                r "Jól van [player]."
                r "Elmegyek veled a Bálba!"
                show r 
                player "Tényleg? Ez szuper!"
                show r talk 
                r "Tudod [player] tényleg jól esik, hogy engem hívtál el!"
                r "Szívesen megyek veled a Bálba!"
                show r 
                player "Ezt örömmel hallom!"
                show r talk 
                r "Ne haragudj, de most mennem kell."
                r "Holnap még beszélünk!"
                show r 
                player "Rendben, addig is, szia!"
                show r talk 
                r "Szia [player]!"

            else:
                show r shy 
                r "Sajnálom, de Zoli is pont most kérdezte meg, és már igent mondtam neki."
                r "Ne haragudj [player]."
                hide r

# Lilla elhívása a Bálba (másodszor)
        elif prom_w == -2:
            show l 
            player "Szia, ne haragudj!"
            show l shy shut 
            player "Tegnap nem válaszoltál, hogy eljössz-e velem a Bálba."
            if point_l >= 6:
                show l talk 
                l "Jól van [player]."
                l "Elmegyek veled a Bálba!"
                show l 
                player "Tényleg? Ez szuper!"
                show l talk 
                l "Tudod [player] tényleg jól esik, hogy engem hívtál el!"
                l "Szívesen megyek veled a Bálba!"
                show l 
                player "Ezt örömmel hallom!"
                show l talk 
                l "Ne haragudj, de most mennem kell."
                l "Holnap még beszélünk!"
                show l 
                player "Rendben, addig is, szia!"
                show l talk 
                l "Szia [player]!"

            else:
                show l shy 
                l "Sajnálom, de Zoli is pont most kérdezte meg, és már igent mondtam neki."
                l "Ne haragudj [player]."
                hide l 

# Beszélgetés Rózával a Bálról
        elif prom_w == 1:
            show r 
            player "Szia, ne haragudj!"
            show r 
            player "Tegnap beszélgettünk, hogy eljönnél-e velem a Bálba."
            player "Ugye nem gondoltad meg magad?"
            show r talk 
            r "Jaj [player], ne butáskodj, dehogy gondoltam meg magam!"
            r "Szívesen megyek veled a Bálba! Még mindig!"
            r "De szépen öltözz ám fel!"
            show r 
            player "Mindenképp!"
            show r talk 
            r "Tudod, még mindig nagyon boldoggá tesz, hogy együtt megyünk!"
            show r shy 
            r "M-mármint..."
            r "Hát... érted..."
            show r shy shut 
            player "Értem én, ne izgulj."
            show r talk 
            r "Most rohannom kell, de már nagyon várom a holnapot!"
            show r 
            player "Rendben, szia Róza."
            show r talk
            r "Szia [player]."

# Beszélgetés Lillával a Bálról
        elif prom_w == 2:
            show l 
            player "Szia, ne haragudj!"
            show l 
            player "Tegnap beszélgettünk, hogy eljönnél-e velem a Bálba."
            player "Ugye nem gondoltad meg magad?"
            show l talk 
            l "Jaj [player], ne butáskodj, dehogy gondoltam meg magam!"
            l "Szívesen megyek veled a Bálba! Még mindig!"
            l "De szépen öltözz ám fel!"
            show l 
            player "Mindenképp!"
            show l talk 
            l "Tudod, még mindig nagyon boldoggá tesz, hogy együtt megyünk!"
            show l shy 
            l "M-mármint..."
            l "Hát... érted..."
            show l shy shut 
            player "Értem én, ne izgulj."
            show l talk 
            l "Most rohannom kell, de már nagyon várom a holnapot!"
            show l 
            player "Rendben, szia Lilla."
            show l talk
            l "Szia [player]."

# Róza elhívása a Bálba
        elif prom_w == 3:
            show r 
            player "Szia, ne haragudj!"
            show r shy shut 
            player "Róza, valami fontosat kell kérdeznem."
            player "Eljönnél velem a Bálba?"
            show r excited 
            r "Én?"
            r "Komolyan?"
            show r excited shut
            player "Igen, komolyan."
            show r talk 
            r "Nagyön örülök, hogy megkérdeztél, [player]."
            if point_r >= 7: 
                $ prom_w += 1
                r "Szívesen megyek veled a Bálba!"
                show r excited
                r "Úgy örülök!"
                r "Megérte ennyit tanulnom!"
                show r shy 
                r "M-mármint-"
                r "Nem csak ez motivált!"
                r "V-vagyis-"
                show r shy shut
                player "Ne aggódj, értelek."
                show r talk 
                r "Tudod [player] tényleg jól esik, hogy engem hívtál el!"
                r "Szívesen megyek veled a Bálba!"
                show r 
                player "Ezt örömmel hallom!"
                show r talk 
                r "Akkor holnap találkozunk! Szépen öltözz ám fel!"
                show r
                player "Rendben, addig is, szia!"
                show r talk 
                r "Szia [player]!"

            else:
                show r shy 
                r "Sajnálom, de Zoli is pont most kérdezte meg, és már igent mondtam neki."
                r "Ne haragudj [player]."
                hide r

# Lilla elhívása a Bálba
        else:
            show r 
            player "Szia, ne haragudj!"
            show r shy shut 
            player "Lilla, valami fontosat kell kérdeznem."
            player "Eljönnél velem a Bálba?"
            show l excited 
            l "Én?"
            l "Komolyan?"
            show l excited shut 
            player "Igen, komolyan."
            show l talk 
            l "O, [player], nagyon megtisztelő, hogy rám gondoltál!"
            if point_l >= 6: 
                $ prom_w += 2
                show l excited
                l "Tényleg jól esik, hogy engem hívtál el a Bálba!"
                l "Igazán örülök neki!"
                show l talk 
                l "És nagyon szívesen megyek veled!"
                show l
                player "Ezt örömmel hallom!"
                show l shy 
                l "Sajnos nekem most mennem kell."
                l "Ne haragudj."
                show l talk
                l "De holnap még beszélünk!"
                show l 
                player "Rendben, addig is, szia Lilla!"
                show l talk 
                l "Szia [player]!"

            else:
                show l shy 
                l "Sajnálom, de Zoli is pont most kérdezte meg, és már igent mondtam neki."
                l "Ne haragudj [player]."
                hide l 

# Beszéletés a lányokkal, hogy nem sikerült a dolgozat
    else:
        show r excited at left
        show l talk at right
        "[player]!"
        show r at left
        show l at right
        player "Sziasztok!"
        player "Hogy ment nektek a dolgozat?"
        show r excited at left
        r "Jól! Képzeljétek 10 pontom lett!"
        show l shy shut at right
        r "Nagyon büszke vagyok magamra!"
        show r excited shut at left
        show l talk at right
        l "Nekem max pontos lett."
        show r shy shut at left 
        l "És neked hogy ment [player]?"
        show r at left
        show l at right
        player "Nekem sajnos nem sikerültek jól..."
        show r what shut at left
        show l what shut at right
        player "Nem mehetek a Bálba."
        player "[answer] pontom lett."
        show r angry shut at left
        show l sad shut at right
        player "Korrepetálásra kell mennem."
        show r angry at left
        r "Micsoda? Az nem lehet! Beszélek a tanárnővel hogy nézze megint át a dolgozatod!"
        r "Valahol biztos rosszul javított!"
        r "Vagy összekeverhette valakivel a dolgozatod!"
        show r angry shut at left
        player "Sajnos nem, Róza."
        player "Tényleg nem ment jól egyik dolgozat se..."
        show r sad at left
        r "Pedig nagyon szerettem volna, hogy mindenki ott legyen a Bálon."
        show r sad shut at left
        show l sad at right
        l "Ahogy én is..."
        l "Nélküled nem lesz olyan jó, [player]."
        show l sad shut at right
        player "Sajnálom lányok."
        show l sad at right
        l "Nem te tehetsz róla."
        l "Én viszont most megyek..."
        l "Sziasztok..."
        show l sad shut at right
        player "Szia Lilla."
        hide l 
        pause
        show r sad at left
        r "Azt hiszem akkor én is megyek..."
        r "Szia [player]."
        show r sad shut at left
        player "Szia Róza."
        hide r
        pause
        player "Pedig szerettem volna elmenni a Bálba."
        player "De csak nem lesz olyan rossz az a korrepetálás..."
    pause

# Iskola után
    scene szoba
    player "Nagyon kíváncsi vagyok a holnapra."
    player "Vajon milyen lesz?"

    scene black_background with fade
    "Hatodik nap vége"   
return