# -*- coding: utf-8 -*-
# from database import get_user_profile
import sqlite3

class UserProfile():
    def __init__(self, user_id) -> None:
        # вытягиваем данные по профилю из базы
        
        try:
            con = sqlite3.connect('db_discord_bot.db')
            cursorObj = con.cursor()
            # Тут ОСТАНОВИЛСЯ
            cursorObj.execute(""" 
            SELECT u.id, u.user_name, u.rating, u.rating_value, u.role_1, u.role_2, u.role_3, u.role_4, u.role_5, u.discord_name,
            b.resone, b.             
            FROM users as u
            left join ban as b on u.id = b.id_user
            WHERE u.id = ?
            """, (user_id,))

            user = cursorObj.fetchall()

            cursorObj.execute(""" 
            SELECT t.name, t.rtk_parm,
            e.date_start, e.type, e.event_name           
            FROM users as u
            left join user_to_team as ut on u.id = ut.id_user
            left join team as t on t.id = ut.id_team
            left join event_to_team as et on t.id = et.id_team
            left join events as e on e.id = et.id_event
            WHERE u.id = ?
            """, (user_id,))
            events = cursorObj.fetchall()
            print(user)
            print(events)
        except Exception as ex:
            print(ex)
        self.user_name = user[1]
        self.rating = user[2]
        self.rating_value = user[3]
        self.role_1 = user[4]
        self.role_2 = user[5]
        self.role_3 = user[6]
        self.role_4 = user[7]
        self.role_5 = user[8]
        self.discord_name = user[9]
        self.ban = user[10]
        pass

profile = UserProfile(178963010751168512)


