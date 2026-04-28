init python:
    import math

screen change_season():
    default bgs = ["_noon", "", "_night"]
    default counter = 0
    default season_timer = 0
    default max_iterations = 60
    add "bg maincastle[bgs[counter]]"

    timer 1 - season_timer * 0.085 action [If(season_timer < 10, IncrementScreenVariable("season_timer")), If(counter < 2, IncrementScreenVariable("counter"), SetScreenVariable("counter", 0)), IncrementScreenVariable("max_iterations", -1), If(max_iterations <= 0, SetScreenVariable("counter", 0))] repeat max_iterations > 0



screen calendar(current_month, current_date, target_month=None, target_day=None, speed=0.3):
    default local_current_month = current_month
    default current_day_number = target_day - 1
    default current_day_number_display = current_date - 1
    default all_months = ["Esynce", "Jinus", "Dallinus", "Vanus", "Dyalt", "Neralt", "Exalt", "Elvera", "Verabris", "Overa"]
    default months_32 = ["Jinus", "Dallinus", "Elvera"]
    default months_31 = ["Vanus", "Dyalt", "Neralt", "Verabris", "Overa"]
    default months_30 = ["Exalt"]
    default max_number_days = 0
    #default total = 31
    default radius = 1000
    default center_x = config.screen_width - 100
    default center_y = config.screen_height - 100
    default rotate_pos = current_date - 1
    default default_text_speed = 0
    default count_started = False
    default count_finished = False
    default date_text_padding = 0

    if current_month in months_32:
        $ max_number_days = 32
        $ date_text_padding = 50
    elif current_month in months_31:
        $ max_number_days = 31
        $ date_text_padding = 30
    elif current_month in months_30:
        $ max_number_days = 30
        $ date_text_padding = 10
    elif current_month == "Esynce":
        $ max_number_days = 28
        $ date_text_padding = -20
    
    add "bg/magis_hall_afternoon.png"
    frame:
        #background "bg maincastle"
        background Solid("#bbbbbb81")
        #xysize (150, 150)
        xfill True
        yfill True


        #text "current_day_number_display: " + str(current_day_number_display + 1) + " raw: " + str( current_day_number_display) + ", current_day_number: " + str(current_day_number + 1) + " raw: " + str(current_day_number) + " count_started: " + str(count_started) + " count_finished: " + str(count_finished)
        #text "local_current_month: " + str(local_current_month) + ", target_month: " + str(target_month):
        #    ypos 50
        #text "current_day_number != current_day_number_display and local_current_month != target_month: " + str(current_day_number != current_day_number_display and local_current_month != target_month):
        #    ypos 90
        #text "max_days: " + str(max_number_days):
        #        ypos 150


        frame:
            background Solid("#49494991")
            xfill True
            ysize 190
            yalign 0.32

            text "[local_current_month]":
                size 150
                xalign 0.3
                color "#000"

                if current_day_number_display == max_number_days - 1 or current_day_number_display == 0:
                    at transform:
                        linear 0.1
                        linear 0.1 alpha 0.0 xalign 0.1
                        
                        linear 0.1 alpha 1.0 xalign 0.3
    
        for i in range(max_number_days):
            
            if not count_finished:
                $ angle = 2 * math.pi * (i + 3 - rotate_pos) / max_number_days
                $ x = int(center_x - radius * math.cos(angle) + 390)
                $ y = int(center_y - radius * math.sin(angle) - date_text_padding)

            else:
                $ angle = 2 * math.pi * (i + 4 - rotate_pos) / max_number_days
                $ x = int(center_x - radius * math.cos(angle) + 390)
                $ y = int(center_y - radius * math.sin(angle) - date_text_padding)

                
            text "[i+1]":
                xpos x
                ypos y
                size 190
                
                at transform:
                    linear default_text_speed xpos x ypos y
                    zoom 0.3
                    anchor (1.0, 0.5)
                    #if i == current_day_number:
                    #    linear 0.5 zoom 1.5

                if i == current_day_number_display:
                    at transform:
                        linear 0.1
                        linear 0.2 zoom 3.5

                if i == current_day_number_display - 1:
                    at transform:
                        zoom 3.5
                        linear 0.3 zoom 1.0

                if i == max_number_days - 1 and current_day_number_display == 0:
                    at transform:
                        #zoom 4.0
                        linear 0.3 zoom 1.0
                # if i == current_day_number_display:
                #     if count_started == False:
                #         at transform:
                #             zoom 2.5
                #     else:
                #         at transform:
                #             zoom 2.5
                #             linear 0.5
                #             linear 0.5 zoom 1

                # if i == current_day_number_display and i != current_day_number or i == current_day_number_display - 1:
                #     at transform:
                #         zoom 2.5
                #         linear 1
                #         linear 0.5 zoom 1

                # if i == current_day_number_display + 1:
                #     at transform:
                #         #linear 1
                #         linear 1 zoom 2.5

                # #if i == current_day_number:
                # if current_day_number == current_day_number_display:
                #     at transform:
                #         #linear 1
                #         linear 1 zoom 2.5
                


        # button:
        #     background Solid("#a8a8a8")
        #     xysize (280, 220)
        #     xpos int(center_x - radius * math.cos(2 * math.pi * (3) / max_number_days) + 170)
        #     ypos int(center_y - radius * math.sin(2 * math.pi * (3) / max_number_days) - 70)
        #     action NullAction()
                    
        
        # text "[current_day_number_display + 1 if (count_started == False) else current_day_number_display]":
        #     size 150
        #     xalign 0.6
        #     color "#000"
                
    # timer 1 action [
    #     IncrementScreenVariable("rotate_pos"),
    #     If(current_day_number_display != current_day_number and local_current_month != target_month, [IncrementScreenVariable("current_day_number_display", 1), SetScreenVariable("count_started", True)]), 
    #     SetScreenVariable("default_text_speed", 1),
    #     If(current_day_number_display == current_day_number, SetScreenVariable("count_finished", True)),
    #     If(current_day_number_display >= max_number_days, [SetScreenVariable("current_day_number_display", 0)])
    #     ] repeat (current_day_number != current_day_number_display and local_current_month != target_month)

    timer speed action [
        IncrementScreenVariable("rotate_pos"),
        If(current_day_number_display != current_day_number or local_current_month != target_month, [IncrementScreenVariable("current_day_number_display", 1), SetScreenVariable("count_started", True)]), 
        SetScreenVariable("default_text_speed", speed),
        If(current_day_number_display == current_day_number and local_current_month == target_month, SetScreenVariable("count_finished", True)),
        If(current_day_number_display >= max_number_days - 1, [SetScreenVariable("current_day_number_display", 0), SetScreenVariable("local_current_month", all_months[all_months.index(target_month)])])
        ] repeat (current_day_number != current_day_number_display or local_current_month != target_month)

    
    key ["K_SPACE", "K_RETURN", "mouseup_1"] action [Hide(transition=dissolve), Return()]