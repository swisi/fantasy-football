SELECT * from nfl_team 
WHERE team_abbr NOT in ('TEN')

SELECT * FROM nfl_player 
WHERE team NOT in ('TEN')

SELECT * FROM nfl_weekly_stat 
WHERE player_id IN (
    SELECT player_id 
    FROM nfl_player 
    WHERE team != 'TEN'
);

DELETE  from nfl_team
WHERE team_abbr NOT in ('TEN')

DELETE  FROM nfl_player 
WHERE team NOT in ('TEN')

DELETE  FROM nfl_weekly_stat 
WHERE player_id NOT IN (
    SELECT player_id 
    FROM nfl_player 
);