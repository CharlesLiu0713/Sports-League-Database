from tkinter import *
from project import *

WINDOW_SIZE = '1350x800'
BORDER_WITH = 3
TEXT_WIDTH = 40
TEXT_HEIGHT = 1


class MY_GUI:
    def __init__(self, init_window_name, my_Mongodb):
        self.init_window_name = init_window_name
        self.my_Mongodb = my_Mongodb

    def set_init_window(self):
        self.New_league()
        self.New_team()
        self.Query_team()
        self.Query_team_record()
        self.Query_game_history()
        self.Move_team()
        self.Updating_team_rating()
        self.Update_current_date()
        self.Query_season()
        self.update_game()

    def New_league(self):
        self.is_submit = False
        self.selection = StringVar()
        self.team_resultText = StringVar()
        self.league_resultText = StringVar()
        self.game_resultText = StringVar()
        self.move_resultText = StringVar()
        self.Query_teamResult = StringVar()
        self.updating_resultText = StringVar()
        self.update_current_resultText = StringVar()
        self.Query_team_recordText = StringVar()
        self.league_resultText = StringVar()
        self.query_season_resultText = StringVar()
        self.Query_history_resultText = StringVar()
        self.update_game_result_text = StringVar()

        self.init_window_name.title("Sports League Database")
        self.init_window_name.geometry(WINDOW_SIZE)

        self.new_league_title_label = Label(self.init_window_name, text='New league', font=('', 15))
        self.new_league_title_label.grid(row=0, column=1)

        self.new_league_name_label = Label(self.init_window_name, text='League name')
        self.new_league_name_label.grid(row=2, column=0)
        self.new_league_name_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.new_league_name_text.grid(row=2, column=1)

        self.new_league_commissioner_label = Label(self.init_window_name, text='League Commissioner')
        self.new_league_commissioner_label.grid(row=3, column=0)
        self.new_league_commissioner_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.new_league_commissioner_text.grid(row=3, column=1)

        self.new_league_SSN_label = Label(self.init_window_name, text='Commissioner SSN')
        self.new_league_SSN_label.grid(row=4, column=0)
        self.new_league_SSN_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.new_league_SSN_text.grid(row=4, column=1)

        self.new_league_start_label = Label(self.init_window_name, text='First season start time')
        self.new_league_start_label.grid(row=5, column=0)
        self.new_league_start_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.new_league_start_text.grid(row=5, column=1)

        self.new_league_end_label = Label(self.init_window_name, text='First season end time')
        self.new_league_end_label.grid(row=6, column=0)
        self.new_league_end_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.new_league_end_text.grid(row=6, column=1)

        self.league_result_label = Label(self.init_window_name, textvariable=self.league_resultText, fg='red')
        self.league_result_label.grid(row=7, column=0)
        self.new_league_submit_button = Button(self.init_window_name, text='Submit league', width=15,
                                               command=self.submitLeague)
        self.new_league_submit_button.grid(row=7, column=1)
        self.new_league_clear_button = Button(self.init_window_name, text='Clear', width=9, command=self.clear1)
        self.new_league_clear_button.grid(row=7, column=2)

    def New_team(self):
        self.new_team_title_label = Label(self.init_window_name, text='New Team', font=('', 15))
        self.new_team_title_label.grid(row=9, column=1)

        self.new_team_name_label = Label(self.init_window_name, text='Team Name')
        self.new_team_name_label.grid(row=10, column=0)
        self.new_team_name_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.new_team_name_text.grid(row=10, column=1)

        self.new_team_city_label = Label(self.init_window_name, text='Team City')
        self.new_team_city_label.grid(row=11, column=0)
        self.new_team_city_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.new_team_city_text.grid(row=11, column=1)

        self.new_team_court_label = Label(self.init_window_name, text='Home court')
        self.new_team_court_label.grid(row=12, column=0)
        self.new_team_court_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.new_team_court_text.grid(row=12, column=1)

        self.new_team_league_label = Label(self.init_window_name, text='Team Belongs To')
        self.new_team_league_label.grid(row=13, column=0)
        self.new_team_league_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.new_team_league_text.grid(row=13, column=1)

        self.team_result_label = Label(self.init_window_name, textvariable=self.team_resultText, fg='red')
        self.team_result_label.grid(row=14, column=0)
        self.new_team_submit_button = Button(self.init_window_name, text='Submit Team', width=15,
                                             command=self.submitTeam)
        self.new_team_submit_button.grid(row=14, column=1)

        self.new_team_clear_button = Button(self.init_window_name, text='Clear', width=9, command=self.clear2)
        self.new_team_clear_button.grid(row=14, column=2)

    def Query_team(self):
        self.query_team_label = Label(self.init_window_name, text='Query team information', font=('', 15))
        self.query_team_label.grid(row=16, column=1)
        self.query_team_title_label = Label(self.init_window_name, text='Team Name')
        self.query_team_title_label.grid(row=17, column=0)
        self.query_team_name_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.query_team_name_text.grid(row=17, column=1)
        self.query_team_button = Button(self.init_window_name, text='Query team', width=9, command=self.query_team_information)
        self.query_team_button.grid(row=17, column=2)
        self.query_team_tip = Label(self.init_window_name, textvariable=self.Query_teamResult, fg='red')
        self.query_team_tip.grid(row=18, column=2)

        self.query_team_city_label = Label(self.init_window_name, text='Team City')
        self.query_team_city_label.grid(row=18, column=0)
        self.query_home_court_label = Label(self.init_window_name, text='Home Court')
        self.query_home_court_label.grid(row=19, column=0)
        self.query_team_rating_label = Label(self.init_window_name, text='Team Current Season Rating')
        self.query_team_rating_label.grid(row=20, column=0)
        self.query_team_city_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.query_team_city_text.grid(row=18, column=1)
        self.query_home_court_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.query_home_court_text.grid(row=19, column=1)
        self.query_team_rating_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.query_team_rating_text.grid(row=20, column=1)

    def Query_team_record(self):
        self.team_record_label = Label(self.init_window_name, text='Query team record', font=('', 15))
        self.team_record_label.grid(row=25, column=1)

        self.team_record_name_label = Label(self.init_window_name, text='Team Name')
        self.team_record_name_label.grid(row=26, column=0)
        self.team_record_name_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.team_record_name_text.grid(row=26, column=1)
        self.query_team_record_button = Button(self.init_window_name, text='Query team', width=15,
                                               command=self.query_record)
        self.query_team_record_button.grid(row=28, column=1)
        self.query_team_tip = Label(self.init_window_name, textvariable=self.Query_team_recordText, fg='red')
        self.query_team_tip.grid(row=28, column=0)
        self.team_record_season_label = Label(self.init_window_name, text='Team Record')
        self.team_record_season_label.grid(row=29, column=0)
        self.team_record_season_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT * 13)
        self.team_record_season_text.grid(row=29, column=1)
        self.change_query_league_button = Button(self.init_window_name, text='Change league', width=15,
                                                 command=self.change_query_league)
        self.change_query_league_button.grid(row=30, column=0)
        self.change_champion_query_button = Button(self.init_window_name, text='Change champion', width=15,
                                                   command=self.change_champion_query)
        self.change_champion_query_button.grid(row=30, column=1)
        self.change_team_record_button = Button(self.init_window_name, text='Change team', width=9,
                                                command=self.change_team_record)
        self.change_team_record_button.grid(row=30, column=2)

    def Query_game_history(self):
        self.game_history_label = Label(self.init_window_name, text='Query game history', font=('', 15))
        self.game_history_label.grid(row=25, column=6)

        self.game_history_name1_label = Label(self.init_window_name, text='Team1 Name')
        self.game_history_name1_label.grid(row=26, column=5)
        self.game_history_name1_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.game_history_name1_text.grid(row=26, column=6)

        self.game_history_name2_label = Label(self.init_window_name, text='Team2 Name')
        self.game_history_name2_label.grid(row=27, column=5)
        self.game_history_name2_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.game_history_name2_text.grid(row=27, column=6)
        self.query_team_tip = Label(self.init_window_name, textvariable=self.Query_history_resultText, fg='red')
        self.query_team_tip.grid(row=28, column=5)
        self.game_history_button = Button(self.init_window_name, text='Query Game', width=15, command=self.query_game_history)
        self.game_history_button.grid(row=28, column=6)

        self.game_history_result_label = Label(self.init_window_name, text='Game History')
        self.game_history_result_label.grid(row=29, column=5)
        self.game_history_result_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT * 13)
        self.game_history_result_text.grid(row=29, column=6)

    def Move_team(self):
        self.Move_team_label = Label(self.init_window_name, text='Move team', font=('', 15))
        self.Move_team_label.grid(row=0, column=4)
        self.Move_team_name_label = Label(self.init_window_name, text='Team Name')
        self.Move_team_name_label.grid(row=2, column=3)
        self.Move_team_name_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.Move_team_name_text.grid(row=2, column=4)

        self.current_team_League_label = Label(self.init_window_name, text='Current League')
        self.current_team_League_label.grid(row=3, column=3)
        self.current_team_League_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.current_team_League_text.grid(row=3, column=4)

        self.Move_team_League_label = Label(self.init_window_name, text='Move To League')
        self.Move_team_League_label.grid(row=4, column=3)
        self.Move_team_League_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.Move_team_League_text.grid(row=4, column=4)

        self.Move_team_date_label = Label(self.init_window_name, text='Move date')
        self.Move_team_date_label.grid(row=5, column=3)
        self.Move_team_date_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.Move_team_date_text.grid(row=5, column=4)

        self.move_result_label = Label(self.init_window_name, textvariable=self.move_resultText, fg='red')
        self.move_result_label.grid(row=6, column=3)
        self.Move_team_button = Button(self.init_window_name, text='Move team', width=15, command=self.moveTeam)
        self.Move_team_button.grid(row=6, column=4)

    def Updating_team_rating(self):
        self.updating_team_rating_label = Label(self.init_window_name, text='Updating Team Rating', font=('', 15))
        self.updating_team_rating_label.grid(row=9, column=4)

        self.updating_team_label = Label(self.init_window_name, text='Team Name')
        self.updating_team_label.grid(row=10, column=3)
        self.updating_team_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.updating_team_text.grid(row=10, column=4)

        self.updating_rating_label = Label(self.init_window_name, text='New Rating')
        self.updating_rating_label.grid(row=11, column=3)
        self.updating_rating_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.updating_rating_text.grid(row=11, column=4)

        self.updating_result_label = Label(self.init_window_name, textvariable=self.updating_resultText, fg='red')
        self.updating_result_label.grid(row=12, column=3)
        self.updating_rating_button = Button(self.init_window_name, text='Update', width=15, command=self.Update)
        self.updating_rating_button.grid(row=12, column=4)

        self.updating_rating_button = Button(self.init_window_name, text='All Clear', width=15, command=self.All_clear)
        self.updating_rating_button.grid(row=12, column=6)

    def Update_current_date(self):
        self.update_current_date_label = Label(self.init_window_name, text='Updating Current date', font=('', 15))
        self.update_current_date_label.grid(row=16, column=4)

        self.update_current_league_label = Label(self.init_window_name, text='League Name')
        self.update_current_league_label.grid(row=17, column=3)
        self.update_current_league_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.update_current_league_text.grid(row=17, column=4)

        self.update_current_season_label = Label(self.init_window_name, text='New Season Date')
        self.update_current_season_label.grid(row=18, column=3)
        self.update_current_season_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.update_current_season_text.grid(row=18, column=4)

        self.update_current_label = Label(self.init_window_name, textvariable=self.update_current_resultText, fg='red')
        self.update_current_label.grid(row=19, column=3)
        self.update_current_button = Button(self.init_window_name, text='Update', width=15, command=self.Update_current)
        self.update_current_button.grid(row=19, column=4)

    def Query_season(self):
        self.query_season_label = Label(self.init_window_name, text='Query season information', font=('', 15))
        self.query_season_label.grid(row=25, column=4)

        self.query_leaseason_name_label = Label(self.init_window_name, text='League Name')
        self.query_leaseason_name_label.grid(row=26, column=3)
        self.query_leaseason_name_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.query_leaseason_name_text.grid(row=26, column=4)

        self.query_season_name_label = Label(self.init_window_name, text='Season Name')
        self.query_season_name_label.grid(row=27, column=3)
        self.query_season_name_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.query_season_name_text.grid(row=27, column=4)
        self.update_current_label = Label(self.init_window_name, textvariable=self.query_season_resultText, fg='red')
        self.update_current_label.grid(row=28, column=3)
        self.query_season_button = Button(self.init_window_name, text='Query Season', width=15,
                                          command=self.query_season)
        self.query_season_button.grid(row=28, column=4)

        self.query_season_result_label = Label(self.init_window_name, text='Standing Of Teams')
        self.query_season_result_label.grid(row=29, column=3)
        self.query_season_reault_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT * 13)
        self.query_season_reault_text.grid(row=29, column=4)

    def update_game(self):
        self.update_game_label = Label(self.init_window_name, text='Update game score', font=('', 15))
        self.update_game_label.grid(row=0, column=6)
        self.update_game_season_label = Label(self.init_window_name, text='Season Name')
        self.update_game_season_label.grid(row=2, column=5)
        self.update_game_season_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.update_game_season_text.grid(row=2, column=6)

        self.update_team1_label = Label(self.init_window_name, text='Team1 Name')
        self.update_team1_label.grid(row=3, column=5)
        self.update_team1_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.update_team1_text.grid(row=3, column=6)

        self.update_team2_label = Label(self.init_window_name, text='Team2 Name')
        self.update_team2_label.grid(row=4, column=5)
        self.update_team2_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.update_team2_text.grid(row=4, column=6)

        self.update_score1_label = Label(self.init_window_name, text='Team1 Score')
        self.update_score1_label.grid(row=5, column=5)
        self.update_score1_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.update_score1_text.grid(row=5, column=6)

        self.update_score2_label = Label(self.init_window_name, text='Team2 Score')
        self.update_score2_label.grid(row=6, column=5)
        self.update_score2_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.update_score2_text.grid(row=6, column=6)

        self.update_game_result_label = Label(self.init_window_name, textvariable=self.update_game_result_text,
                                              fg='red')
        self.update_game_result_label.grid(row=7, column=5)
        self.update_game_button = Button(self.init_window_name, text='Update game', width=15, command=self.Update_game)
        self.update_game_button.grid(row=7, column=6)

    # click submitLeague league button
    def submitLeague(self):
        if not self.is_submit:
            league_name = self.new_league_name_text.get(1.0, END)
            if league_name.isspace():
                self.showNotice5()
                return
            league_name = league_name.replace("\n", "")

            self.showNotice3()

            league_commissioner = self.new_league_commissioner_text.get(1.0, END)
            league_commissioner = league_commissioner.replace("\n", "")

            commissioner_SSN = self.new_league_SSN_text.get(1.0, END)
            commissioner_SSN = commissioner_SSN.replace("\n", "")

            Fseason_start = self.new_league_start_text.get(1.0, END)
            Fseason_end = self.new_league_end_text.get(1.0, END)

            print("SubmitLeague")
            year_start, month_start, day_start = Fseason_start.split('.')
            year_end, month_end, day_end = Fseason_end.split('.')
            year_start, month_start, day_start = int(year_start), int(month_start), int(day_start)
            year_end, month_end, day_end = int(year_end), int(month_end), int(day_end)

            result = self.my_Mongodb.InputLeague(GET='Enter a new league', league_name=league_name,
                                                 ceo_name=league_commissioner, ceo_SSN=commissioner_SSN,
                                                 start_time=datetime(year_start, month_start, day_start),
                                                 end_time=datetime(year_end, month_end, day_end))

            if result != None:
                self.league_resultText.set("Success")
                self.is_submit = True
            else:
                self.league_resultText.set("Fault")
        else:
            self.league_resultText.set("Please Clear")

    # click submit team button
    def submitTeam(self):
        if not self.is_submit:
            team_name = self.new_team_name_text.get(1.0, END)
            if team_name.isspace():
                self.showNotice6()
                return
            team_name = team_name.replace("\n", "")

            team_city = self.new_team_city_text.get(1.0, END)
            team_city = team_city.replace("\n", "")

            home_court = self.new_team_court_text.get(1.0, END)
            home_court = home_court.replace("\n", "")

            team_league = self.new_team_league_text.get(1.0, END)
            team_league = team_league.replace("\n", "")
            print("SubmitTeam")
            result = self.my_Mongodb.InputLeague(GET='Enter a new team', team_name=team_name, league_name=team_league,
                                                 city=team_city, court=home_court)

            if result != None:
                self.team_resultText.set("Success")
                self.is_submit = True
            else:
                self.team_resultText.set("Fault")
        else:
            self.team_resultText.set("Please Clear")

    # click clear1 button
    def clear1(self):
        self.new_league_commissioner_text.delete(1.0, END)
        self.new_league_SSN_text.delete(1.0, END)
        self.new_league_name_text.delete(1.0, END)
        self.new_league_start_text.delete(1.0, END)
        self.new_league_end_text.delete(1.0, END)
        self.league_resultText.set(" ")

        self.is_submit = False

        print("Clear")

    # click clear2 button
    def clear2(self):
        self.new_team_name_text.delete(1.0, END)
        self.new_team_city_text.delete(1.0, END)
        self.new_team_court_text.delete(1.0, END)
        self.new_team_league_text.delete(1.0, END)
        self.team_resultText.set(" ")
        self.is_submit = False

        print("Clear")

    def All_clear(self):
        self.new_league_commissioner_text.delete(1.0, END)
        self.new_league_SSN_text.delete(1.0, END)
        self.new_league_name_text.delete(1.0, END)
        self.new_league_start_text.delete(1.0, END)
        self.new_league_end_text.delete(1.0, END)
        self.new_team_name_text.delete(1.0, END)
        self.new_team_city_text.delete(1.0, END)
        self.new_team_court_text.delete(1.0, END)
        self.new_team_league_text.delete(1.0, END)

        self.query_team_name_text.delete(1.0, END)
        self.query_team_city_text.delete(1.0, END)
        self.query_home_court_text.delete(1.0, END)
        self.query_team_rating_text.delete(1.0, END)

        self.team_record_name_text.delete(1.0, END)
        self.team_record_season_text.delete(1.0, END)

        self.Move_team_name_text.delete(1.0, END)
        self.current_team_League_text.delete(1.0, END)
        self.Move_team_League_text.delete(1.0, END)
        self.Move_team_date_text.delete(1.0, END)

        self.updating_team_text.delete(1.0, END)
        self.updating_rating_text.delete(1.0, END)

        self.update_current_league_text.delete(1.0, END)
        self.update_current_season_text.delete(1.0, END)

        self.query_leaseason_name_text.delete(1.0, END)
        self.query_season_name_text.delete(1.0, END)
        self.query_season_reault_text.delete(1.0, END)

        self.game_history_name1_text.delete(1.0, END)
        self.game_history_name2_text.delete(1.0, END)
        self.game_history_result_text.delete(1.0, END)

        self.update_game_season_text.delete(1.0, END)
        self.update_team1_text.delete(1.0, END)
        self.update_team2_text.delete(1.0, END)
        self.update_score1_text.delete(1.0, END)
        self.update_score2_text.delete(1.0, END)
        self.update_game_season_text.delete(1.0, END)

        self.showNotice3()
        self.is_submit = False

        print("All Clear")

    # click Query1 button
    def query_team_information(self):
        team_name = self.query_team_name_text.get(1.0, END)
        team_name = team_name.replace('\n', '')

        result = self.my_Mongodb.TeamQuery(GET=1, team_name=team_name)
        if not result:
            self.Query_team_recordText.set("Fault")
        else:
            self.showNotice3()
            # show result to result text field
            self.query_team_city_text.delete(1.0, END)
            self.query_home_court_text.delete(1.0, END)
            self.query_team_rating_text.delete(1.0, END)
            self.query_team_city_text.insert(1.0, result[1]['city'])
            self.query_home_court_text.insert(1.0, result[2]['home court'])
            self.query_team_rating_text.insert(1.0, result[3]['current rating'])
            self.Query_team_recordText.set("Success")

    # click query_record button
    def query_record(self):
        team_name = self.team_record_name_text.get(1.0, END)
        if team_name.isspace():
            self.showNotice4()
            return
        team_name = team_name.replace('\n', '')
        result = self.my_Mongodb.TeamQuery(GET=2, team_name=team_name)
        if not result:
            self.Query_team_recordText.set("Fault")
            return False
        self.team_record_season_text.delete(1.0, END)
        self.showNotice3()
        for every_season in result:
            self.team_record_season_text.insert(1.0, '\n\n')
            self.team_record_season_text.insert(1.0, every_season[8]['the total number of points'])
            self.team_record_season_text.insert(1.0, 'the total number of points: ')

            self.team_record_season_text.insert(1.0, '\n')
            self.team_record_season_text.insert(1.0, every_season[7]['sum of its opponent scores in games'])
            self.team_record_season_text.insert(1.0, 'sum of its opponent scores in games: ')

            self.team_record_season_text.insert(1.0, '\n')
            self.team_record_season_text.insert(1.0, every_season[6]['sum of scores for its games'])
            self.team_record_season_text.insert(1.0, 'sum of scores for its games: ')

            self.team_record_season_text.insert(1.0, '\n')
            self.team_record_season_text.insert(1.0, every_season[5]['number of loses'])
            self.team_record_season_text.insert(1.0, 'number of loses: ')

            self.team_record_season_text.insert(1.0, '\n')
            self.team_record_season_text.insert(1.0, every_season[4]['number of draws'])
            self.team_record_season_text.insert(1.0, 'number of draws: ')

            self.team_record_season_text.insert(1.0, '\n')
            self.team_record_season_text.insert(1.0, every_season[3]['number of wins'])
            self.team_record_season_text.insert(1.0, 'number of wins: ')

            self.team_record_season_text.insert(1.0, '\n')
            self.team_record_season_text.insert(1.0, every_season[2]['games played'])
            self.team_record_season_text.insert(1.0, 'games played: ')

            self.team_record_season_text.insert(1.0, '\n')
            self.team_record_season_text.insert(1.0, every_season[1]['season name'])
            self.team_record_season_text.insert(1.0, 'season name: ')

            self.team_record_season_text.insert(1.0, '\n')
            self.team_record_season_text.insert(1.0, every_season[0]['team name'])
            self.team_record_season_text.insert(1.0, 'team name: ')

        self.Query_team_recordText.set("Success")
        print("query_team_record")

    # click query_league button
    def query_league(self):
        league_name = self.team_record_name_text.get(1.0, END)
        league_name = league_name.replace('\n', '')
        result = self.my_Mongodb.LeagueQuery(GET=1, league_name=league_name)
        if not result:
            self.Query_team_recordText.set("Fault")
        else:
            self.team_record_season_text.insert(1.0, '\n')
            self.team_record_season_text.insert(1.0, result[2]['number of seasons'])
            self.team_record_season_text.insert(1.0, 'number of seasons: ')

            self.team_record_season_text.insert(1.0, '\n')
            self.team_record_season_text.insert(1.0, result[1]['commissioner']['ceo_SSN'])
            self.team_record_season_text.insert(1.0, 'ceo_SSN: ')

            self.team_record_season_text.insert(1.0, '\n')
            self.team_record_season_text.insert(1.0, result[1]['commissioner']['ceo_name'])
            self.team_record_season_text.insert(1.0, 'ceo_name: ')

            self.team_record_season_text.insert(1.0, '\n')
            self.team_record_season_text.insert(1.0, result[0]['name'])
            self.team_record_season_text.insert(1.0, 'name: ')

            self.Query_team_recordText.set("Success")

    # click query_champion button
    def query_champion(self):
        league_name = self.team_record_name_text.get(1.0, END)
        league_name = league_name.replace('\n', '')
        result = self.my_Mongodb.LeagueQuery(GET=2, league_name=league_name)
        if not result:
            self.Query_team_recordText.set("Fault")
        else:
            for index, every_season in enumerate(result):
                self.team_record_season_text.insert(1.0, '\n')
                for every_champion in every_season:
                    self.team_record_season_text.insert(1.0, '\n\n')
                    self.team_record_season_text.insert(1.0, every_champion[2]['champion record']['points'])
                    self.team_record_season_text.insert(1.0, 'points: ')

                    self.team_record_season_text.insert(1.0, '\n')
                    self.team_record_season_text.insert(1.0, every_champion[2]['champion record']['loses'])
                    self.team_record_season_text.insert(1.0, 'loses: ')

                    self.team_record_season_text.insert(1.0, '\n')
                    self.team_record_season_text.insert(1.0, every_champion[2]['champion record']['drawns'])
                    self.team_record_season_text.insert(1.0, 'drawns: ')

                    self.team_record_season_text.insert(1.0, '\n')
                    self.team_record_season_text.insert(1.0, every_champion[2]['champion record']['wins'])
                    self.team_record_season_text.insert(1.0, 'wins: ')

                    self.team_record_season_text.insert(1.0, '\n')
                    self.team_record_season_text.insert(1.0, every_champion[2]['champion record']['scores'])
                    self.team_record_season_text.insert(1.0, 'scores: ')

                    self.team_record_season_text.insert(1.0, '\n')
                    self.team_record_season_text.insert(1.0, every_champion[1]['year'])
                    self.team_record_season_text.insert(1.0, 'year: ')

                    self.team_record_season_text.insert(1.0, '\n')
                    self.team_record_season_text.insert(1.0, every_champion[0]['champion name'])
                    self.team_record_season_text.insert(1.0, 'champion name: ')
                self.team_record_season_text.insert(1.0, '\n\n')
                season_name = 'season ' + str(index + 1) + ':'
                self.team_record_season_text.insert(1.0, season_name)

            self.Query_team_recordText.set("Success")

    # click Query2 button
    def query_game_history(self):
        Team1 = self.game_history_name1_text.get(1.0, END)
        if Team1.isspace():
            self.showNotice11()
            return
        Team1 = Team1.replace('\n', '')

        Team2 = self.game_history_name2_text.get(1.0, END)
        if Team2.isspace():
            self.showNotice11()
            return
        Team2 = Team2.replace('\n', '')

        result = self.my_Mongodb.GameQuery(team_1=Team1, team_2=Team2)
        if not result:
            self.Query_history_resultText.set("False")
        else:
            self.showNotice3()
            self.game_history_result_text.delete(1.0, END)
            # show result to result text field
            for index, every_game in enumerate(result):
                self.game_history_result_text.insert(1.0, '\n\n')
                self.game_history_result_text.insert(1.0, every_game[6]['score 2'])
                self.game_history_result_text.insert(1.0, 'score 2: ')

                self.game_history_result_text.insert(1.0, '\n')
                self.game_history_result_text.insert(1.0, every_game[5]['score 1'])
                self.game_history_result_text.insert(1.0, 'score 1: ')

                self.game_history_result_text.insert(1.0, '\n')
                self.game_history_result_text.insert(1.0, every_game[4]['team 2'])
                self.game_history_result_text.insert(1.0, 'team 2: ')

                self.game_history_result_text.insert(1.0, '\n')
                self.game_history_result_text.insert(1.0, every_game[3]['team 1'])
                self.game_history_result_text.insert(1.0, 'team 1: ')

                self.game_history_result_text.insert(1.0, '\n')
                self.game_history_result_text.insert(1.0, every_game[2]['date'])
                self.game_history_result_text.insert(1.0, 'date: ')

                self.game_history_result_text.insert(1.0, '\n')
                self.game_history_result_text.insert(1.0, every_game[1]['league name'])
                self.game_history_result_text.insert(1.0, 'league name: ')

                self.game_history_result_text.insert(1.0, '\n')
                self.game_history_result_text.insert(1.0, every_game[0]['season name'])
                self.game_history_result_text.insert(1.0, 'season name: ')

                index = index + 1
                current_game_name = 'game_' + str(index)
                self.game_history_result_text.insert(1.0, '\n')
                self.game_history_result_text.insert(1.0, current_game_name)

            self.Query_history_resultText.set("Success")
            print("Query2")

    # click moveTeam button
    def moveTeam(self):
        if not self.is_submit:
            team_name = self.Move_team_name_text.get(1.0, END)
            if team_name.isspace():
                self.showNotice7()
                return
            team_name = team_name.replace('\n', '')

            old_league_name = self.current_team_League_text.get(1.0, END)
            if old_league_name.isspace():
                self.showNotice7()
                return
            old_league_name = old_league_name.replace('\n', '')

            new_league_name = self.Move_team_League_text.get(1.0, END)
            if new_league_name.isspace():
                self.showNotice7()
                return
            new_league_name = new_league_name.replace('\n', '')

            # for example: '2017.01.01'
            moving_date = self.Move_team_date_text.get(1.0, END)
            if moving_date.isspace():
                self.showNotice7()
                return
            moving_date = moving_date.replace('\n', '')

            result = self.my_Mongodb.MovingTeam(team_name=team_name, old_league_name=old_league_name,
                                                new_league_name=new_league_name, moving_date=moving_date)
            self.showNotice3()
            print("SubmitMove")
            if result == True:
                self.move_resultText.set("Move Success")
                self.is_submit = True
            else:
                self.move_resultText.set("Move Fault")

            self.is_submit = True
        else:
            self.move_resultText.set("Please Clear")

    # click Update button
    def Update(self):
        if not self.is_submit:
            team_name = self.updating_team_text.get(1.0, END)
            if team_name.isspace():
                self.showNotice8()
                return
            team_name = team_name.replace('\n', '')

            new_rating = self.updating_rating_text.get(1.0, END)
            if team_name.isspace():
                self.showNotice8()
                return
            new_rating = new_rating.replace('\n', '')
            if not new_rating.isdecimal():
                self.updating_resultText.set("False")
                return
            new_rating = int(new_rating)

            result = self.my_Mongodb.UpdateRating(team_name=team_name, new_rating=new_rating)
            if result is False:
                self.updating_resultText.set("False")
                return
            else:
                self.showNotice3()
                print("Update rating")
                self.updating_resultText.set("Update Success")
                self.is_submit = True
        else:
            self.updating_resultText.set("False")

    def Update_current(self):
        league_name = self.update_current_league_text.get(1.0, END)
        if league_name.isspace():
            self.showNotice9()
            return
        league_name = league_name.replace('\n', '')
        new_season_name = self.update_current_season_text.get(1.0, END)
        if new_season_name.isspace():
            self.showNotice9()
            return
        new_season_name = new_season_name.replace('\n', '')

        year, month, day = new_season_name.split('.')
        year, month, day = int(year), int(month), int(day)
        year += 1
        result = self.my_Mongodb.UpdateCurrentDate(league_name=league_name, new_season_date=datetime(year, month, day))
        if not result:
            self.update_current_resultText.set("False")
        else:
            self.showNotice3()
            self.update_current_resultText.set("Update Success")

    # click query_season button
    def query_season(self):
        league_name = self.query_leaseason_name_text.get(1.0, END)
        if league_name.isspace():
            self.showNotice10()
            return
        league_name = league_name.replace('\n', '')

        season_name = self.query_season_name_text.get(1.0, END)
        if season_name.isspace():
            self.showNotice10()
            return
        season_name = season_name.replace('\n', '')
        result = self.my_Mongodb.SeasonQuery(league_name=league_name, season_name=season_name)
        if not result:
            self.query_season_resultText.set("False")
        else:
            self.showNotice3()
            self.query_season_reault_text.delete(1.0, END)
            for every_team in result:
                self.query_season_reault_text.insert(1.0, '\n\n')
                self.query_season_reault_text.insert(1.0, every_team['points'])
                self.query_season_reault_text.insert(1.0, 'points: ')

                self.query_season_reault_text.insert(1.0, '\n')
                self.query_season_reault_text.insert(1.0, every_team['loses'])
                self.query_season_reault_text.insert(1.0, 'loses: ')

                self.query_season_reault_text.insert(1.0, '\n')
                self.query_season_reault_text.insert(1.0, every_team['drawns'])
                self.query_season_reault_text.insert(1.0, 'drawns: ')

                self.query_season_reault_text.insert(1.0, '\n')
                self.query_season_reault_text.insert(1.0, every_team['wins'])
                self.query_season_reault_text.insert(1.0, 'wins: ')

                self.query_season_reault_text.insert(1.0, '\n')
                self.query_season_reault_text.insert(1.0, every_team['opponent scores'])
                self.query_season_reault_text.insert(1.0, 'opponent scores: ')

                self.query_season_reault_text.insert(1.0, '\n')
                self.query_season_reault_text.insert(1.0, every_team['scores'])
                self.query_season_reault_text.insert(1.0, 'scores: ')

                self.query_season_reault_text.insert(1.0, '\n')
                self.query_season_reault_text.insert(1.0, every_team['team name'])
                self.query_season_reault_text.insert(1.0, 'team name: ')

            self.query_season_resultText.set("Success")

    def Update_game(self):
        season_name = self.update_game_season_text.get(1.0, END)
        season_name = season_name.replace('\n', '')

        team_1_name = self.update_team1_text.get(1.0, END)
        team_1_name = team_1_name.replace('\n', '')

        team_2_name = self.update_team2_text.get(1.0, END)
        team_2_name = team_2_name.replace('\n', '')

        team_1_score = self.update_score1_text.get(1.0, END)
        team_1_score = team_1_score.replace('\n', '')
        if not team_1_score.isdecimal():
            self.update_game_result_text.set("False")
            return False

        team_2_score = self.update_score2_text.get(1.0, END)
        team_2_score = team_2_score.replace('\n', '')
        if not team_2_score.isdecimal():
            self.update_game_result_text.set("False")
            return False

        result = self.my_Mongodb.UpdateGameScore(season_name=season_name, team_1=team_1_name, team_2=team_2_name,
                                                 score_1=team_1_score, score_2=team_2_score)
        if result:
            self.update_game_result_text.set("Success")
        else:
            self.update_game_result_text.set("Fault")

    # show notice
    def showNotice(self):
        self.Query_teamResult.set("Input Team Name")

    def showNotice2(self):
        self.Query_teamResult.set("Please Input Team1 and Team2 Name")

    def showNotice3(self):
        self.Query_teamResult.set(" ")
        self.Query_team_recordText.set(" ")
        self.league_resultText.set(" ")
        self.team_resultText.set(" ")
        self.move_resultText.set(" ")
        self.updating_resultText.set(" ")
        self.update_current_resultText.set(" ")
        self.query_season_resultText.set(" ")
        self.Query_history_resultText.set(" ")
        self.update_game_result_text.set(" ")

    def change_query_league(self):
        self.team_record_label.configure(text="League basic information")
        self.team_record_name_label.configure(text="League Name")
        self.team_record_season_label.configure(text="Basic Information")
        self.query_team_record_button.configure(text="Query League", command=self.query_league)

    def change_champion_query(self):
        self.team_record_label.configure(text="Champion information")
        self.team_record_name_label.configure(text="League Name")
        self.team_record_season_label.configure(text="Champion")
        self.query_team_record_button.configure(text="Query Champion", command=self.query_champion)

    def change_team_record(self):
        self.team_record_label.configure(text="Query team record")
        self.team_record_name_label.configure(text="Team Name")
        self.team_record_season_label.configure(text="Team Record")
        self.query_team_record_button.configure(text="Query team", command=self.query_record)

    def showNotice4(self):
        self.Query_team_recordText.set("Input Team Name")

    def showNotice5(self):
        self.league_resultText.set("Input League Name")

    def showNotice6(self):
        self.team_resultText.set("Input Team Name")

    def showNotice7(self):
        self.move_resultText.set("Incomplete data")

    def showNotice8(self):
        self.updating_resultText.set("Incomplete data")

    def showNotice9(self):
        self.update_current_resultText.set("Incomplete data")

    def showNotice10(self):
        self.query_season_resultText.set("Incomplete data")

    def showNotice11(self):
        self.Query_history_resultText.set("Incomplete data")


if __name__ == '__main__':
    my_Mongodb = SportLeagueDatabase(path='localhost', PID=27017)
    init_window = Tk()
    PORTAL = MY_GUI(init_window, my_Mongodb)
    PORTAL.set_init_window()
    init_window.mainloop()
