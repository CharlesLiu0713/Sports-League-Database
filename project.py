import itertools
import pymongo
from datetime import datetime
from random import randint, choice
from bson.json_util import dumps


class SportLeagueDatabase:
    def __init__(self, path, PID):
        self.conn = pymongo.MongoClient(path, PID)
        self.db = self.conn.pro_db
        self.leagues_set = self.db.leagues_set
        self.teams_set = self.db.teams_set
        self.seasons_set = self.db.seasons_set
        self.game_set = self.db.game_set
        self.ratings_set = self.db.ratings_set
        self.standings_set = self.db.standings_set

    # League data entry:
    def InputLeague(self, GET, league_name=None, ceo_name=None, ceo_SSN=None, start_time=None, end_time=None,
                    team_name=None, city=None, court=None):
        if GET == 'Enter a new league':
            teams = []
            seasons = []
            result = self._InitializeLeague(league_name, ceo_name, ceo_SSN, start_time, end_time, teams=teams,
                                            seasons=seasons)
            if result is not None:
                return result
            else:
                return None
        elif GET == 'Enter a new team':
            result = self._InitializeTeam(league_name, team_name, city, court)
            if result is not None:
                return result
            else:
                return None

    def _InitializeLeague(self, name, ceo_name, ceo_SSN, start_time, end_time, teams, seasons):
        start_year, start_month, start_day = start_time.year, start_time.month, start_time.day
        end_year, end_month, end_day = end_time.year, end_time.month, end_time.day
        if start_year > end_year:
            return None
        elif start_year == end_year:
            if start_month > end_month:
                return None
            elif start_month == end_month:
                if start_day >= end_day:
                    return None
        if start_month == 1 or end_month == 1:
            return None
        league = {
            '_id': name,
            'name': name,
            'CEO': {
                'ceo_name': ceo_name,
                'ceo_SSN': ceo_SSN
            },
            'teams': teams,
            'seasons': seasons
        }
        season_id = self._InitializeSeason(league['name'], teams, start_time, end_time)
        league['seasons'].append(season_id)
        if not self.leagues_set.find_one({'_id': league['_id']}):
            self.leagues_set.insert_one(league)
            return league['_id']
        else:
            return None

    def _InitializeSeason(self, league_name, teams, start_time, end_time):
        game_info = []
        season = {
            '_id': league_name + '_' + '1',
            'league name': league_name,
            'teams': teams,
            'start time': start_time,
            'end time': end_time,
            'game number': 0,
            'game info': game_info
        }
        if not self.seasons_set.find_one({'_id': season['_id']}):
            self.seasons_set.insert_one(season)
            return season['_id']
        else:
            return None

    def _InitializeTeam(self, league_name, team_name, city, court):
        league_info = self.leagues_set.find_one({'_id': league_name})
        if league_info is None:
            return None
        season = league_info['seasons'][-1]
        seasons = [season]
        team = {
            '_id': team_name,
            'league name': league_name,
            'team name': team_name,
            'city': city,
            'court': court,
            'seasons': seasons
        }
        if not self.teams_set.find_one({'_id': team['_id']}):
            self.teams_set.insert_one(team)
            self._InsertTeamToLeague(team['league name'], team['team name'])
            self._InitializeRating()
            return True
        else:
            return None

    def _InsertTeamToLeague(self, league_name, team_name):
        filter = {'_id': league_name}
        league_info = self.leagues_set.find_one(filter)
        league_info['teams'].append(team_name)
        newvalues = {"$set": {'teams': league_info['teams']}}
        self.leagues_set.update_one(filter, newvalues)

        # add team to current season
        league_info = self.leagues_set.find_one(filter)
        game_number = len(list(itertools.combinations(league_info['teams'], 2)))
        current_season = league_info['seasons'][-1]
        filter = {'_id': current_season}
        season_info = self.seasons_set.find_one(filter)
        season_info['teams'].append(team_name)
        newvalues = {"$set": {'teams': season_info['teams'], 'game number': game_number}}
        self.seasons_set.update_one(filter, newvalues)

    # Season set up:
    def _AddSeason(self, league_name, start_time, end_time):
        filter = {'_id': league_name}
        league_info = self.leagues_set.find_one(filter)
        if not league_info['teams']:
            self._InitializeSeason(league_name, league_info['teams'], start_time, end_time)
        else:
            new_season_number = len(league_info['seasons']) + 1
            game_number = len(list(itertools.combinations(league_info['teams'], 2)))
            game_info = []
            season = {
                '_id': league_name + '_' + str(new_season_number),
                'league name': league_name,
                'teams': league_info['teams'],
                'start time': start_time,
                'end time': end_time,
                'game number': game_number,
                'game info': game_info
            }
            if not self.seasons_set.find_one(
                    {'league name': league_name, 'start time': start_time, 'end time': end_time}):
                self.seasons_set.insert_one(season)
                league_info['seasons'].append(season['_id'])
                newvalues = {"$set": {'seasons': league_info['seasons']}}
                self.leagues_set.update_one(filter, newvalues)
                for team_name in league_info['teams']:
                    filter_team = {'_id': team_name}
                    team_info = self.teams_set.find_one(filter_team)
                    team_info['seasons'].append(season['_id'])
                    newvalues_team = {"$set": {'seasons': team_info['seasons']}}
                    self.teams_set.update_one(filter_team, newvalues_team)
                return season['_id']
            else:
                return None

    # Entering game results:
    def _AddGame(self, season_name):
        filter = {'_id': season_name}
        current_season_info = self.seasons_set.find_one(filter)
        versus_list = list(itertools.combinations(current_season_info['teams'], 2))
        current_year = current_season_info['start time'].year
        if len(current_season_info['game info']) < current_season_info['game number']:
            for i in range(current_season_info['game number']):
                game_month = randint(1, 12)
                game_day = randint(1, 28)
                date = datetime(current_year, game_month, game_day)
                location_list = []
                for j in versus_list[i]:
                    team_info = self.teams_set.find_one({'_id': j})
                    if team_info['court'] is None:
                        continue
                    else:
                        location_list.append(team_info['court'])
                # score_1 = uniform(-100.0, 100.0)
                # score_2 = uniform(-100.0, 100.0)
                score_1 = randint(0, 100)
                score_2 = randint(0, 100)
                if score_1 > score_2:
                    winner = versus_list[i][0]
                elif score_1 < score_2:
                    winner = versus_list[i][1]
                else:
                    winner = [versus_list[i][0], versus_list[i][1]]
                game = {
                    '_id': season_name + ' ' + versus_list[i][0] + ' ' + versus_list[i][1] + ' ' + str(date),
                    'season name': season_name,
                    'team 1': versus_list[i][0],
                    'team 2': versus_list[i][1],
                    'location': choice(location_list),
                    'date': date,
                    'score 1': score_1,
                    'score 2': score_2,
                    'winner': winner
                }
                if not self.game_set.find_one({'_id': game['_id']}):
                    self.game_set.insert_one(game)
                    filter = {'_id': season_name}
                    season_info = self.seasons_set.find_one(filter)
                    season_info['game info'].append(
                        {'date': date, 'team 1': versus_list[i][0], 'team 2': versus_list[i][1],
                         'location': game['location']})
                    newvalues = {"$set": {'game info': season_info['game info']}}
                    self.seasons_set.update_one(filter, newvalues)
            self._InitializeStandings(season_name)

    # Update ratings:
    def _InitializeRating(self):
        team_list = []
        for league in self.leagues_set.find():
            for team in league['teams']:
                team_list.append(team)
        for i in team_list:
            rating = {
                '_id': i,
                'team name': i,
                'rating number': randint(0, 100)
            }
            if not self.ratings_set.find_one({'_id': rating['_id']}):
                self.ratings_set.insert_one(rating)

    def UpdateRating(self, team_name, new_rating):
        team_info = self.teams_set.find_one({'_id': team_name})
        if team_info is None:
            return False
        team_info['rating number'] = new_rating
        filter = {'_id': team_name}
        newvalues = {"$set": {'rating number': team_info['rating number']}}
        self.ratings_set.update_one(filter, newvalues)

    # Update the current date
    def UpdateCurrentDate(self, league_name, new_season_date):
        league_info = self.leagues_set.find_one({'_id': league_name})
        if league_info is None:
            return False
        if new_season_date.month == 1:
            return False
        old_season_name = league_info['seasons'][-1]
        old_season_info = self.seasons_set.find_one({'_id': old_season_name})
        if new_season_date.year <= old_season_info['start time'].year:
            return False
        new_end_year = new_season_date.year
        self._AddGame(old_season_name)
        self._AddSeason(league_name=league_name, start_time=new_season_date, end_time=datetime(new_end_year, 12, 31))
        return True

    # Move teams:
    def MovingTeam(self, team_name, old_league_name, new_league_name, moving_date):
        year, month, day = moving_date.split('.')
        year, month, day = int(year), int(month), int(day)
        if month > 2 or month < 1:
            return False
        filter = {'_id': old_league_name}
        league_info = self.leagues_set.find_one(filter)
        if league_info is None:
            return False
        temp_league_info = self.leagues_set.find_one({'_id': new_league_name})
        if temp_league_info is None:
            return False
        if team_name not in league_info['teams']:
            return False

        if len(league_info['seasons']) == 1:
            season_end_year_info = self.seasons_set.find_one({'_id': league_info['seasons'][-1]})
        else:
            season_end_year_info = self.seasons_set.find_one({'_id': league_info['seasons'][-2]})
        season_end_year = season_end_year_info['end time'].year
        if year != season_end_year:
            return False

        season_end_year_info = self.seasons_set.find_one({'_id': league_info['seasons'][-1]})
        team_list = []
        for every_team in season_end_year_info['teams']:
            if every_team != team_name:
                team_list.append(every_team)

        game_number = len(list(itertools.combinations(team_list, 2)))

        filter_updated_season_team = {'_id': season_end_year_info['_id']}
        newvalues = {"$set": {'teams': team_list, 'game number': game_number}}
        self.seasons_set.update_one(filter_updated_season_team, newvalues)

        new_team_list = []
        for i in league_info['teams']:
            if i == team_name:
                continue
            else:
                new_team_list.append(i)
        league_info['teams'] = new_team_list
        newvalues = {"$set": {'teams': league_info['teams']}}
        self.leagues_set.update_one(filter, newvalues)

        filter = {'_id': new_league_name}
        league_info = self.leagues_set.find_one(filter)
        if team_name not in league_info['teams']:
            league_info['teams'].append(team_name)
            newvalues = {"$set": {'teams': league_info['teams']}}
            self.leagues_set.update_one(filter, newvalues)
            filter_team = {'_id': team_name}
            team_info = self.teams_set.find_one(filter_team)
            team_info['league name'] = new_league_name
            team_info['seasons'][-1] = league_info['seasons'][-1]
            newvalues = {"$set": {'league name': team_info['league name'], 'seasons': team_info['seasons']}}
            self.teams_set.update_one(filter_team, newvalues)
        new_league_info = self.leagues_set.find_one(filter)
        game_number = len(list(itertools.combinations(new_league_info['teams'], 2)))

        new_season_name = new_league_info['seasons'][-1]
        filter = {'_id': new_season_name}
        season_info = self.seasons_set.find_one(filter)
        if team_name not in season_info['teams']:
            season_info['teams'].append(team_name)
            newvalues = {"$set": {'teams': season_info['teams'], 'game number': game_number}}
            self.seasons_set.update_one(filter, newvalues)

        return True

    # League query:
    def LeagueQuery(self, GET, league_name):
        if GET == 1:
            league_info = self.leagues_set.find_one({'name': league_name})
            if league_info is None:
                return False
            league_info = [
                {'name': league_info['name']},
                {'commissioner': league_info['CEO']},
                {'number of seasons': len(league_info['seasons'])}
            ]
            json_data = dumps(league_info, indent=2)
            with open('league_1_info.json', 'w') as file:
                file.write(json_data)
            return league_info
        elif GET == 2:
            standing_list = self.standings_set.find({'league name': league_name})
            if standing_list is None:
                return False
            output_team_list = []
            for current_standing in standing_list:
                best_teams = []
                teams_record = []
                season_standing = current_standing['season standing']
                best_point = season_standing[0]['points']
                for i in season_standing:
                    if i['points'] >= best_point:
                        best_teams.append(i['team name'])
                        teams_record.append(
                            {'scores': i['scores'], 'wins': i['wins'], 'drawns': i['drawns'], 'loses': i['loses'],
                             'points': i['points']})
                team_info = []
                for j in range(len(best_teams)):
                    team_info.append([
                        {'champion name': best_teams[j]},
                        {'year': current_standing['season year']},
                        {'champion record': teams_record[j]}
                    ])
                output_team_list.append(team_info)
            json_data = dumps(output_team_list, indent=2)
            with open('league_2_info.json', 'w') as file:
                file.write(json_data)
            return output_team_list

    def _InitializeStandings(self, season_name):
        filter = {'_id': season_name}
        season_info = self.seasons_set.find_one(filter)
        season_year = season_info['start time'].year
        league_name, _ = season_name.split('_')
        if not self.standings_set.find_one({'_id': season_name}):
            total_standing = {
                '_id': season_name,
                'league name': league_name,
                'season name': season_name,
                'season year': season_year,
                'season standing': []
            }
            self.standings_set.insert_one(total_standing)
            standing_info = self.standings_set.find_one(filter)
            for every_game in season_info['game info']:
                filter_every_game = {
                    '_id': season_name + ' ' + every_game['team 1'] + ' ' + every_game['team 2'] + ' ' + str(
                        every_game['date'])}
                every_game_info = self.game_set.find_one(filter_every_game)

                self._TwoTeamsGamingResult('1', '2', standing_info, every_game_info)
                self._TwoTeamsGamingResult('2', '1', standing_info, every_game_info)
            standing_info['season standing'].sort(key=lambda x: x['points'], reverse=True)
            newvalues = {"$set": {'season standing': standing_info['season standing']}}
            self.standings_set.update_one(filter, newvalues)

    def _TwoTeamsGamingResult(self, team_flag_1, team_flag_2, standing_info, every_game_info):
        flag = 0
        team_1 = 'team ' + team_flag_1
        score_1 = 'score ' + team_flag_1
        score_2 = 'score ' + team_flag_2
        if len(standing_info['season standing']) != 0:
            for i in standing_info['season standing']:
                if i['team name'] == every_game_info[team_1]:
                    flag = 1
                    if every_game_info[team_1] == every_game_info['winner']:
                        i['wins'] += 1
                    elif every_game_info[team_1] in every_game_info['winner']:
                        i['drawns'] += 1
                    else:
                        i['loses'] += 1
                    i['scores'] += every_game_info[score_1]
                    i['points'] = 3 * i['wins'] + i['drawns']
                    i['opponent scores'] += every_game_info[score_2]
        if flag == 0:
            wins = 0
            drawns = 0
            loses = 0
            opponent_scores = 0
            if every_game_info[team_1] == every_game_info['winner']:
                wins += 1
            elif every_game_info[team_1] in every_game_info['winner']:
                drawns += 1
            else:
                loses += 1
            opponent_scores += every_game_info[score_2]
            standing = {
                'team name': every_game_info[team_1],
                'scores': every_game_info[score_1],
                'opponent scores': opponent_scores,
                'wins': wins,
                'drawns': drawns,
                'loses': loses,
                'points': 3 * wins + drawns
            }
            standing_info['season standing'].append(standing)

    def UpdateGameScore(self, season_name, team_1, team_2, score_1, score_2):
        game_info_list = self.seasons_set.find_one({'_id': season_name})
        if game_info_list is None:
            return False
        for game_info in game_info_list['game info']:
            if game_info['team 1'] == team_1:
                if game_info['team 2'] == team_2:
                    filter_updated_game = {
                        '_id': season_name + ' ' + team_1 + ' ' + team_2 + ' ' + str(game_info['date'])}
                    searched_game_info = self.game_set.find_one(filter_updated_game)
                    searched_game_info['score 1'] = score_1
                    searched_game_info['score 2'] = score_2
                    newvalues = {
                        "$set": {'score 1': searched_game_info['score 1'], 'score 2': searched_game_info['score 2']}}
                    self.game_set.update_one(filter_updated_game, newvalues)
                    return True

            if game_info['team 1'] == team_2:
                if game_info['team 2'] == team_1:
                    filter_updated_game = {
                        '_id': season_name + ' ' + team_2 + ' ' + team_1 + ' ' + str(game_info['date'])}
                    searched_game_info = self.game_set.find_one(filter_updated_game)
                    searched_game_info['score 1'] = score_2
                    searched_game_info['score 2'] = score_1
                    newvalues = {
                        "$set": {'score 1': searched_game_info['score 1'], 'score 2': searched_game_info['score 2']}}
                    self.game_set.update_one(filter_updated_game, newvalues)
                    return True

        return False

    # Team query:
    def TeamQuery(self, GET, team_name):
        if GET == 1:
            team_info = self.teams_set.find_one({'_id': team_name})
            if team_info is None:
                return False
            rating_info = self.ratings_set.find_one({'_id': team_name})
            team_info = [
                {'name': team_info['team name']},
                {'city': team_info['city']},
                {'home court': team_info['court']},
                {'current rating': rating_info['rating number']}
            ]
            json_data = dumps(team_info, indent=2)
            with open('team_1_info.json', 'w') as file:
                file.write(json_data)
            return team_info
        elif GET == 2:
            team_info = self.teams_set.find_one({'_id': team_name})
            if team_info is None:
                return False
            seasons_info = []
            for current_season_name in team_info['seasons']:
                standing_info = self.standings_set.find_one({'_id': current_season_name})
                if standing_info is not None:
                    for i in standing_info['season standing']:
                        if i['team name'] == team_name:
                            season_info = [
                                {'team name': team_name},
                                {'season name': current_season_name},
                                {'games played': i['wins'] + i['drawns'] + i['loses']},
                                {'number of wins': i['wins']},
                                {'number of draws': i['drawns']},
                                {'number of loses': i['loses']},
                                {'sum of scores for its games': i['scores']},
                                {'sum of its opponent scores in games': i['opponent scores']},
                                {'the total number of points': i['points']},
                            ]
                            seasons_info.append(season_info)
            json_data = dumps(seasons_info, indent=2)
            with open('team_2_info.json', 'w') as file:
                file.write(json_data)
            return seasons_info

    # Game query:
    def GameQuery(self, team_1, team_2):
        team_1_info = self.teams_set.find_one({'_id': team_1})
        if team_1_info is None:
            return False
        team_2_info = self.teams_set.find_one({'_id': team_2})
        if team_2_info is None:
            return False
        seasons_list = team_1_info['seasons']
        record_list = []
        for season in seasons_list:
            season_info = self.seasons_set.find_one({'_id': season})
            games_list = season_info['game info']
            for game in games_list:
                if game['team 1'] == team_1 or game['team 2'] == team_1:
                    if game['team 1'] == team_2 or game['team 2'] == team_2:
                        league_name, _ = season.split('_')
                        game_info = self.game_set.find_one(
                            {'season name': season, 'location': game['location'], 'date': game['date']})
                        year, month, day = game_info['date'].year, game_info['date'].month, game_info['date'].day
                        if game_info['team 1'] == team_1:
                            record = [
                                {'season name': season},
                                {'league name': league_name},
                                {'date': str(year) + '-' + str(month) + '-' + str(day)},
                                {'team 1': team_1},
                                {'team 2': team_2},
                                {'score 1': game_info['score 1']},
                                {'score 2': game_info['score 2']}
                            ]
                            record_list.append(record)
                        else:
                            record = [
                                {'season name': season},
                                {'league name': league_name},
                                {'date': str(year) + '-' + str(month) + '-' + str(day)},
                                {'team 1': team_2},
                                {'team 2': team_1},
                                {'score 1': game_info['score 1']},
                                {'score 2': game_info['score 2']}
                            ]
                            record_list.append(record)
        if len(record_list) == 0:
            return False
        json_data = dumps(record_list, indent=2)
        with open('game_info.json', 'w') as file:
            file.write(json_data)
        return record_list

    # Season query:
    def SeasonQuery(self, league_name, season_name):
        leagues_info = self.leagues_set.find_one({'_id': league_name})
        if leagues_info is None:
            return False
        standing_info = self.standings_set.find_one({'_id': season_name})
        if standing_info is None:
            return False
        teams_standing = standing_info['season standing']
        json_data = dumps(teams_standing, indent=2)
        with open('season_info.json', 'w') as file:
            file.write(json_data)
        return teams_standing


if __name__ == '__main__':
    my_Mongodb = SportLeagueDatabase(path='localhost', PID=27017)

    my_Mongodb.InputLeague(GET='Enter a new league', league_name='NBA', ceo_name='Charles', ceo_SSN='123456',
                           start_time=datetime(2018, 2, 1), end_time=datetime(2018, 12, 31))
    my_Mongodb.InputLeague(GET='Enter a new team', league_name='NBA', team_name='Houston Rockets', city='Houston',
                           court='Houston Rockets')
    my_Mongodb.InputLeague(GET='Enter a new team', league_name='NBA', team_name='Los Angeles Lakers',
                           city='Los Angeles', court='Los Angeles')
    my_Mongodb.InputLeague(GET='Enter a new team', league_name='NBA', team_name='Dallas Mavericks', city='Dallas',
                           court='Dallas')
    my_Mongodb.InputLeague(GET='Enter a new team', league_name='NBA', team_name='Phoenix Suns', city='Phoenix',
                           court='Phoenix')
    my_Mongodb.UpdateCurrentDate(league_name='NBA', new_season_date=datetime(2019, 2, 1))

    my_Mongodb.InputLeague(GET='Enter a new team', league_name='NBA', team_name='China', city='Beijin', court='Beijin')
    my_Mongodb.InputLeague(GET='Enter a new team', league_name='NBA', team_name='USA', city='New York',
                           court='New York')
    my_Mongodb.UpdateCurrentDate(league_name='NBA', new_season_date=datetime(2020, 2, 1))

    my_Mongodb.InputLeague(GET='Enter a new league', league_name='FIFA', ceo_name='Charles', ceo_SSN='123456',
                           start_time=datetime(2019, 2, 1), end_time=datetime(2019, 12, 31))
    my_Mongodb.MovingTeam(team_name='China', old_league_name='NBA', new_league_name='FIFA', moving_date='2019.01.01')
    my_Mongodb.MovingTeam(team_name='USA', old_league_name='NBA', new_league_name='FIFA', moving_date='2019.01.01')
    my_Mongodb.InputLeague(GET='Enter a new team', league_name='FIFA', team_name='Canada', city='Ottawa',
                           court='Ottawa')
    my_Mongodb.UpdateCurrentDate(league_name='FIFA', new_season_date=datetime(2020, 2, 1))

    my_Mongodb.UpdateRating(team_name='Houston Rockets', new_rating=99)

    my_Mongodb.LeagueQuery(GET=1, league_name='NBA')
    my_Mongodb.LeagueQuery(GET=2, league_name='NBA')
    my_Mongodb.TeamQuery(GET=1, team_name='Houston Rockets')
    my_Mongodb.TeamQuery(GET=2, team_name='Houston Rockets')
    my_Mongodb.GameQuery(team_1='Houston Rockets', team_2='Los Angeles Lakers')
    my_Mongodb.SeasonQuery(league_name='NBA', season_name='NBA_2')

    my_Mongodb.UpdateGameScore(season_name='NBA_2', team_1='Houston Rockets', team_2='Los Angeles Lakers', score_1=99,
                               score_2=10)
