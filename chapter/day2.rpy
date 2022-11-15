label daytwo:
    # Reggel
    "Második nap"
    scene black_background 
    pause 0.1
    scene szoba with fade

    "*csirip-csirip*"

    player "*sóhaj*"
    player "Ideje készülődni, hamarosan be kell érnem a suliba."

    scene folyoso 
    pause 0.4

#Róza megismerése
    if know_roza == 0:
        show r shy
        $ know_roza += 1
        i "Szia!"
        i "Tegnap egymásba botlottunk."
        r "Róza vagyok!"
        r "Megkérdezhetem, mi a neved?"
        hide r 
        show r shy shut
        menu:
            "Nem szeretnék válaszolni Rózának":
                player "Ne haragudj, de nem igazán érek rá."
                hide r 
                show r sad
                r "Oh, értem."
                r "Bocsi ha feltartottalak."
                r "Azért sok sikert a holnapi dolgozathoz..."
                hide r 

            "Elmondom neki":
                player "Szia, [player] vagyok."
                $ point_r += 1
                player "Ne haragudj ha tegnap megijesztettelek."
                hide r 
                show r talk
                r "Azért nem kellett volna úgy elrohannod."
                r "Örülök a találkozásnak!"
                hide r 
                show r what
                r "Te új diák vagy?"
                r "Még nem láttalak erre..."
                hide r 
                show r what shut
                player "Igen, nemrég költöztünk ide."
                hide r 
                show r talk
                r "Ó! Értem, akkor ezért nem voltál ismerős."
                hide r 
                show r what        
                r "Ismersz már valakit a suliból?"
                hide r 
                show r what shut

                if know_zoli == 1:
                    player "Igen, már Lillával és Zolival is találkoztam."
                else:
                    player "Igen, Lillát."

                hide r 
                show r talk
                r "Ennek örülök!"
                r "Lilla biztos tud segíteni a holnapi dolgozatra való felkészülésben!"
                call exam_prom_talk_w_roza from _call_exam_prom_talk_w_roza

#Lilla megismerése
    elif know_lilla == 0:
        show l talk
        i "Szia!"
        hide l 
        show l shy 
        i "Ne haragudj, hogy csak így leszólítottalak."
        i "Tegnap láttalak beszélgetni Rózával."
        i "És arra gondoltam, hogy..."
        hide l 
        show l shy shut
        pause 
        hide l
        show l shy
        i "Én is szívesen bemutatkoznék."
        hide l 
        show l shy shut
        pause 
        hide l 
        show l shy
        i "Ha nem bánod..."
        hide l 
        show l shy shut
        pause 
        hide l 
        show l talk
        l "Az én nevem Lilla."
        l "Téged hogy hívnak?"
        hide l
        show l what shut
        menu:
            "Nem szeretném elmondani Lillának":
                player "Ne haragudj, de nem igazán érek rá."
                show l sad
                l "Oh, értem."
                l "Bocsi ha feltartottalak."
                l "Sok sikert a holnapi dolgozathoz!"
                hide l 

            "Szívesen bemutatkozok Lillának":
                player "Szia, [player] vagyok."
                $ point_l += 1
                hide l 
                show l talk
                l "Örülök a találkozásnak, [player]!"
                hide l 
                show l what
                l "Új diák vagy, igaz?"
                l "Még nem láttalak erre..."
                hide l 
                show l what shut
                player "Igen, nemrég költöztünk ide."
                hide l 
                show l talk
                l "Akkor ezért nem voltál ismerős."
                hide l 
                show l what        
                l "Ismersz már valakit a suliból Rózán kívül?"
                hide l 
                show l what shut

                if know_zoli == 1:
                    player "Igen, már Zolival is találkoztam."
                else:
                    player "Nem, csak őt."

                hide l 
                show l talk
                l "Hát mostmár engem is megismertél."
                l "Ha segítség kell a holnapi dolgozatra való tanuláshoz, nyugodtan szólj, szívesen segítek benne!"
                hide l 
                show l 

# Dolgozat bemutatása Lillától
                menu:
                    "Dolgozat?":
                        player "Milyen dolgozat?"
                        $ point_l += 1
                        hide l 
                        show l what 
                        l "Holnap dolgozatot írunk."
                        l "Nem mondta senki?"
                        hide l 
                        show l what shut 
                        player "Nem, eddig még senki sem említette."
                        hide l what shut
                        show l talk 
                        l "Oh, ez esetben örülök, hogy említettem."
                        l "Fontos tudnod a dolgozatról, hogy mindenképp jól kell sikerülnie."
                        l "Én is sokat tanulok rá másokkal."
                        hide l talk
                        show l sad
                        l "Akinek nem sikerül a dolgozat nem tud eljönni a Bálba..."
                        hide l sad 

                    "Ezzel kapcsolatban nincs kérdésem":
                        pause 0.0
                
                hide l
                show l sad
                l "Nagyon örülnék, ha mindenki el tudna jönni a Bálba..."
                hide l sad
                show l talk 
                l "Mivel a Bál úgy a legjobb, ha mindenki ott van!"
                hide l talk 
                show l 

# Bál bemutatása Lillától
                menu:
                    "Milyen Bál?":
                        player "Milyen Bál?"
                        $ point_l += 1
                        hide l 
                        show l what 
                        l "Hát A Bál."
                        l "Amire mindenki készül."
                        hide l what 
                        show l talk
                        l "Azoknak a diákoknak szervezik, akik jól tanulnak."
                        l "Minden évben megtartják, és mindenki nagyon jól szokta érzeni magát!"
                        l "Szokás lett, hogy a diákok általában párban mennek a Bálba."
                        hide l talk
                        show l shy 
                        l "Kíváncsi vagyok ki fog idén elhívni engem."
                        hide l shy 

                    "Nincs több kérdésem":
                        pause 0.0

                show l talk
                l "De hamarosan becsengetnek úgyhogy ideje indulnunk órára."
                hide l talk

# Ha mindkét lánnyal megvolt a találkozás, Rózával jön egy beszélgetés
    else:
        show r talk
        r "Szia!"
        r "Milyen volt a tegnapi óra?"
        hide r 
        show r 
        menu:
            "Jó volt":
                if know_zoli == 1:
                    player "Jó volt, összebarátkoztam Lillával és Zolival is."
                else:
                    player "Jó volt, összebarátkoztam Lillával."
                hide r 
                show r talk
                r "Ezt örömmel hallom!"
                r "Akkor biztos jól fog sikerülni a holnapi dolgozat!"

            "Nem tetszett":
                player "Egyáltalán nem volt jó."
                hide r 
                show r sad
                r "O, sajnálom."
                hide r 
                show r talk
                r "De ne búsulj, ma még tudsz készülni a holnapi dolgozatra!"
                
        hide r 
        show r
# Dolgozat bemutatása Rózától
        label exam_prom_talk_w_roza:
        menu:
            "Holnapi dolgozat?":
                player "Holnap dolgozatot írunk?"
                $ point_r += 1
                hide r 
                show r what 
                r "Igen, holnap dolgozat."
                r "Senki nem mondta?"
                hide r 
                show r what shut
                player "Nem, még eddig még nem."
                hide r 
                show r talk
                r "Hát legalább mostmár tudod."

            "Nincs ezzel kapcsolatban kérdésem.":
                pause 0.0

        show r talk
        r "Én is jó sokat tanulok rá!"    
        hide r 
        show r sad
        r "Remélem jól fog sikerülni."
        hide r 
        show r excited
# Bál bemutatása Rózától
        r "Akkor el tudok benni a Bálba!"
        r "Már nagyon várom!"
        hide r 
        show r shy
        r "Kíváncsi vagyok ki fog elhívni..."
        hide r 
        show r sad
        r "Nem szeretnék egyedül menni."
        hide r 
        show r talk
        r "De ez még úgyis odébb van, addig meg csak tanulni kell!"
        hide r 
        show r       

        menu:
            "Bál?":
                player "Várj, milyen bál?"
                $ point_r += 1
                hide r 
                show r what
                r "Tényleg nem tudod?"
                r "A Bál."
                r "Mindenki erre készül."
                r "De ahhoz, hogy el tudj menni, jól kell sikerüliük a dolgozatoknak."

            "Nincs több kérdésem":
                player "Remélem nekem is jól fog sikerülni a dolgozat."

        hide r 
        show r talk 
        r "Viszont hamarosan becsengetnek, úgyhogy ideje lassan indulnunk."
        hide r


# Második óra 
    scene terem
    "*CSÖRRR*"
    "Le is ülök a helyemre, mielőtt ideér a tanárnő."
    pause 0.2
    show t with moveinright
    pause 0.3
    show t talk
    t "Gyerekek!"
    t "Ideje kezdeni az órát!" 
    t "Remélem mindenki értette az anyagot." with fade
    t "Mint tudjátok, holnap írjátok az első dolgozatot."
    t "Remélem mindenki készül rá."
    show t 
    "*CSÖRRR*"
    hide t
    pause 
    
# Tanulás Rózával 
    if class_a_or_b == 1:
        show r shy
        r "Jaj [player], úgy izgulok a holnap miatt!"
        r "Nagyon sokat tanultam rá, de attól tartok, hogy a tanárnő pont olyat fog kérdezni, amit nem tudok."
        show r what 
        r "Te nem vagy ideges miatta?"
        show r what shut 
        menu: 
            "Egy kicsit de":
                $ point_r +=1
                player "De, egy kicsit azért izgulok, hogy jól menjen."
                show r talk 
                r "Akkor mit szólnál hozzá ha átismételnénk, hogy biztos minden menjen."
                show r 
                menu:
                    "Szívesen átismétlen Rózával az anyagot":
                        jump study_w_roza2
                    "Nem szeretném átismételni Rózával az anyagot":
                        jump not_study_w_roza2


            "Nem, nem vagyok ideges a dolgozat miatt":
                player "Nem, egyáltalán nem vagyok ideges miatta."
                show r excited
                r "Tényleg?"
                show r shy
                r "Úgy irigyellek..."
                show r talk
                r "Segítesz nekem átvenni a mai anyagot?"
                show r 
                menu: 
                    "Szívesen átismétlen Rózával az anyagot":
                        label study_w_roza2:
                        $ point_r +=1
                        player "Persze, szívesen segítek tanulni."
                        show r excited
                        r "Tényleg? Jaj de jó!"
                        show r talk
                        r "Akkor tanuljunk!"
                        show r 
                        player "Rendben. Akkor kezdjük." 
                        show r talk 
                        r "Köszi [player], hogy tanultál velem!" with fade
                        show r excited
                        r "Mostmár sokkal több önbizalmam van a holnappal kapcsolatban!"
                        show r talk
                        r "Most mennem kell, de holnap még beszélünk!"
                        r "Sok sikert a holnapi dolgozathoz!"                        

                    "Nem szeretném átismételni Rózával az anyagot":
                        label not_study_w_roza2:
                        player "Nem szeretném, bocsi."
                        show r sad 
                        r "Oh... Rendben van [player]."
                        r "Akkor megkérek valaki mást..."
                        r "Azért sok sikert a holnapi dolgozatra való tanuláshoz!"
        show r talk              
        r "Szia!"
        show r
        pause 0.1

# Tanulás Lillával
    else:
        show l talk
        l "Szia [player]!"
        l "Értetted a tanárnőt?"
        show l 
        menu:
            "Igen, mindent":
                player "Persze, minden érthető volt."
                $ point_l += 1
                show l talk
                l "Ennek örülök!"
                l "Azért szeretnél csatlakozni hozzám átismételni az anyagot?"
                show l 
                menu:
                    "Nem szeretném átismételni az anyagot":
                        player "Nem szükséges, de azért köszi."
                        jump not_study_w_lilla2

                    "Igen, szeretnék csatlakozni":
                        player "Szívesen csatlakozok átismételni az anyagot."
                        jump study_w_lilla2

                
            "Nem, nem mindent":
                player "Nem, volt egy rész ami nem egészen tiszta..."
                show l sad
                l "Oh..."
                show l talk 
                l "Szeretnéd hogy elmagyarázzam?"
                show l 
                menu: 
                    "Igen":
                        player "Igen, annak örülnék."
                        label study_w_lilla2:
                        $ point_l += 1
                        show l excited
                        l "Szuper! Akkor tanuljunk!"
                        show l talk
                        l "Szerintem kezdjük az elején, hogy biztos minden menjen."
                        show l
                        pause 0.1
                        show l talk 
                        l "Így már mindent értesz?" with fade
                        show l 
                        player "Igen Lilla. Így már biztos jól fog menni a holnapi dolgozat!"
                        show l talk
                        l "Abban biztos vagyok!"
                        show l sad
                        l "Most mennem kell."
                        show l talk 
                        l "Sok sikert a holnapi dolgozathoz!"
                        l "Azért otthon nézd át még párszor, én is azt fogom csinálni!"
                        show l 
                        player "Oké, köszi mégegyszer. Szia."
                        show l talk 
                        l "Szia [player]."

                    "Nem":
                        player "Nem kell köszi. Menni fog egyedül is."
                        label not_study_w_lilla2:
                        show l sad
                        l "Oh, rendben."
                        show l talk
                        l "De szívesen segítek benne bármikor."
                        show l
                        player "Rendben Lilla, köszi."
                        show l talk
                        l "Nincs mit [player]."
        show l
        pause 0.1
    
    scene black_background with fade
    "Második nap vége"

return