label first_exam:

    scene black_background 
    pause 0.1
    scene terem with fade

    "*CSÖRRR*"
    show t talk 
    t "Nos, ideje felvázolnom a dolgozatírás menetét."
    t "Mindenki fog kapni egy lapot, aminek a bal felső sarkába kell írnotok a neveteket."
    t "Ez után szóban fogom feltenni a kérdéseket, majd négy választ hozzá."
    t "A helyes válasz számát pedig írjátok a lapotokra."
    t "Minden kérdést csak egyszer fogok feltenni."
    t "Nem fogom megismételni, úgyhogy nagyon figyeljetek."
    t "A jó jegyért legalább négy kérdésre helyesen kell felelnetek."
    t "Akkor kezdem is."

    show t 
    pause

    show t talk
    t "Az első kérdés:"
    t "Irodalom."


# Kérdések:

    # Történelem
    label history:

    t "Miről volt nevezetes az ókorban Delphoi?"
    show t
    menu:
        "Első válasz: a jósdájáról.":
            "1"
            $ answer += 1
        "Második válasz: az ételeiről.":
            "2"
        "Harmadik válasz: a színházáról":
            "3"
        "Negyedik válasz: a törvényeiről":
            "4"

    t "Kinek az áldásával indult el az I. keresztes háború?"
    show t
    menu:
        "Első válasz: II. Orbán pápa":
            "1"
            $ answer += 1
        "Második válasz: II. Henrik":
            "2"
        "Harmadik válasz: II. János Pál":
            "3"
        "Negyedik válasz: II. Lajos":
            "4"
    
    t "Melyik szigeten halt meg száműzetését követően I. Napóleon?"
    show t
    menu:
        "Első válasz: Szent Ilona":
            "1"
            $ answer += 1
        "Második válasz: Korzika":
            "2"
        "Harmadik válasz: Szicília":
            "3"
        "Negyedik válasz: Baleár":
            "4"


# Irodalom
    label literature:

    t "Mely alkotás készült hexameterekben?"
    show t
    menu:
        "Első válasz: Odüsszeia":
            "1"
            $ answer += 1
        "Második válasz: Biblia":
            "2"
        "Harmadik válasz: Kalevala":
            "3"
        "Negyedik válasz: Az arany ember":
            "4"

    t "Kinek a műve az „Egy katonaének” c. lírai költemény?"
    show t
    menu:
        "Első válasz: Balassi Bálint":
            "1"
            $ answer += 1
        "Második válasz: Bornemissza Péter":
            "2"
        "Harmadik válasz: Tinódi Lantos Sebestyén":
            "3"
        "Negyedik válasz: Kosztolányi Dezső":
            "4"
    
    t "Ki volt Petőfi Sándor felesége?"
    show t
    menu:
        "Első válasz: Szendrey Júlia":
            "1"
            $ answer += 1
        "Második válasz: Prielle Kornélia":
            "2"
        "Harmadik válasz: Boncza Berta":
            "3"
        "Negyedik válasz: Harmos Ilona":
            "4"


# Nyelvtan
    label grammar:

    t "Mi a szófaja a „valami” szónak?"
    show t
    menu:
        "Első válasz: Határozatlan névmás":
            "1"
            $ answer += 1
        "Második válasz: Határozatlan névelő":
            "2"
        "Harmadik válasz: Határozott névmás":
            "3"
        "Negyedik válasz: Határozott névelő":
            "4"

    t "Melyik a helyes mondat?"
    show t
    menu:
        "Első válasz: Hétfőn választjuk a diákvezetőt.":
            "1"
            $ answer += 1
        "Második válasz: Szívesen rajzolnák valamit":
            "2"
        "Harmadik válasz: Bárkire nem oszhassuk ezt feladatot.":
            "3"
        "Negyedik válasz: Ennák fagylaltot, ha hagynák.":
            "4"
    
    t "Hogy nevezzük a rokon értelmű szavakat?"
    show t
    menu:
        "Első válasz: Szinoníma":
            "1"
            $ answer += 1
        "Második válasz: Alliteráció":
            "2"
        "Harmadik válasz: Metonímia":
            "3"
        "Negyedik válasz: Metafora":
            "4"


# Matek
    label math:

    t "Hány pozitív egész osztója van a hatos számnak?"
    show t
    menu:
        "Első válasz: 4":
            "1"
            $ answer += 1
        "Második válasz: 3":
            "2"
        "Harmadik válasz: 2":
            "3"
        "Negyedik válasz: 1":
            "4"

    t "Mennyi arab számmal a következő? MMCCCXLVIII"
    show t
    menu:
        "Első válasz: 2348":
            "1"
            $ answer += 1
        "Második válasz: 2343":
            "2"
        "Harmadik válasz: 1948":
            "3"
        "Negyedik válasz: 1353":
            "4"
    
    t "340 tonna hány kg?"
    show t
    menu:
        "Első válasz: 340 000":
            "1"
            $ answer += 1
        "Második válasz: 34 000":
            "2"
        "Harmadik válasz: 34":
            "3"
        "Negyedik válasz: 3,4":
            "4"


# Földrajz
    label geography:

    t "A Föld felszínének hány százalékát borítja víz?"
    show t
    menu:
        "Első válasz: 71":
            "1"
            $ answer += 1
        "Második válasz: 81":
            "2"
        "Harmadik válasz: 61":
            "3"
        "Negyedik válasz: 91":
            "4"

    t "Izrael fővárosa?"
    show t
    menu:
        "Első válasz: Jeruzsálem":
            "1"
            $ answer += 1
        "Második válasz: Tel Aviv":
            "2"
        "Harmadik válasz: Názáret":
            "3"
        "Negyedik válasz: Dimona":
            "4"
    
    t "Hány éves a Föld?"
    show t
    menu:
        "Első válasz: 4,5 milliárd éves":
            "1"
            $ answer += 1
        "Második válasz: 15 ezer éves":
            "2"
        "Harmadik válasz: 600 millió éves":
            "3"
        "Negyedik válasz: 2022 éves":
            "4"


# Kémia
    label chemistry:

    t "Mi az arany vegyjele?"
    show t
    menu:
        "Első válasz: Au ":
            "1"
            $ answer += 1
        "Második válasz: Ag":
            "2"
        "Harmadik válasz: As":
            "3"
        "Negyedik válasz: Ar":
            "4"

    t "Minek a vegyjele a P?"
    show t
    menu:
        "Első válasz: Foszfor ":
            "1"
            $ answer += 1
        "Második válasz: Vas":
            "2"
        "Harmadik válasz: Platina":
            "3"
        "Negyedik válasz: Kén":
            "4"
    
    t "Minek a vegyjele a Cl?"
    show t
    menu:
        "Első válasz: Klór":
            "1"
            $ answer += 1
        "Második válasz: Kálium":
            "2"
        "Harmadik válasz: Kalcium":
            "3"
        "Negyedik válasz: Szén":
            "4"


# Fizika
    label physics:

    t "Milyen jellemzői vannak az egyenes vonalú egyenletes mozgásnak?"
    show t
    menu:
        "Első válasz: Egyenes útszakaszon egyenletes sebességgel halad a test":
            "1"
            $ answer += 1
        "Második válasz: A test egy köríven halad azonos sebességgel":
            "2"
        "Harmadik válasz: Változik a mozgás során a sebesség értéke, de az útirány nem":
            "3"
        "Negyedik válasz: A test egy egyenes pályán halad gyorsuló mozgással":
            "4"

    t "Melyik mozgásra jellemző az alábbi definíció: a test egyenes pályán halad és sebessége időegységről időegységre ugyanannyival változik."
    show t
    menu:
        "Első válasz: Egyenes vonalú egyenletesen változó mozgás":
            "1"
            $ answer += 1
        "Második válasz: Egyenes vonalú egyenletes mozgás":
            "2"
        "Harmadik válasz: Pillanatnyi sebesség":
            "3"
        "Negyedik válasz: Átlagsebesség":
            "4"
    
    t "Mi az erő jele?"
    show t
    menu:
        "Első válasz: F":
            "1"
            $ answer += 1
        "Második válasz: J":
            "2"
        "Harmadik válasz: E":
            "3"
        "Negyedik válasz: R":
            "4"


# Biológia
    label biology:

    t "Milyen vércsoportúnak adhat vért, akinek 0-s a vércsoportja?"
    show t
    menu:
        "Első válasz: Minden csoportnak":
            "1"
            $ answer += 1
        "Második válasz: Csak 0-snak":
            "2"
        "Harmadik válasz: B-snek":
            "3"
        "Negyedik válasz: A-snak":
            "4"

    t "Hány sejtje van egy papucsállatkának?"
    show t
    menu:
        "Első válasz: 1":
            "1"
            $ answer += 1
        "Második válasz: 0":
            "2"
        "Harmadik válasz: sok millió":
            "3"
        "Negyedik válasz: 4":
            "4"
    
    t "Mit jelent az, ha valakinek egy X és egy Y kromoszómája van?"
    show t
    menu:
        "Első válasz: Az illető férfi":
            "1"
            $ answer += 1
        "Második válasz: Az illető nő":
            "2"
        "Harmadik válasz: Azt, hogy nem lehet gyereke":
            "3"
        "Negyedik válasz: Az illető genetikai betegségben szenved":
            "4"


# Eredmény

    if answer == 24:
        "Gratulálok! Jól ment a dolgozat"
    elif answer >= 11:
        "Hát ez egy közepes.."
    else:
        "Megbuktál"

    pause


return