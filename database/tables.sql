-- Create Players Table
CREATE TABLE Players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    role VARCHAR(20),
    FOREIGN KEY (rank_id) REFERENCES Ranks(rank_id) ON DELETE SET NULL
    team_id INT,
    FOREIGN KEY (team_id) REFERENCES Teams(team_id) ON DELETE SET NULL
);

-- Create Teams Table
CREATE TABLE Teams (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    team_name VARCHAR(50) NOT NULL,
    division_id INT,
    FOREIGN KEY (division_id) REFERENCES Divisions(division_id) ON DELETE SET NULL
);

-- Create Divisions Table
CREATE TABLE Divisions (
    division_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    tier INT,
    tournament_id INT,
    FOREIGN KEY (tournament_id) REFERENCES Tournaments(tournament_id) ON DELETE SET NULL
);

-- Create Tournaments Table
CREATE TABLE Tournaments (
    tournament_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE
);

-- Create Standings Table
CREATE TABLE Standings (
    standing_id INT AUTO_INCREMENT PRIMARY KEY,
    team_id INT,
    tournament_id INT,
    matches_won INT DEFAULT 0,
    matches_lost INT DEFAULT 0,
    points INT DEFAULT 0,
    FOREIGN KEY (team_id) REFERENCES Teams(team_id) ON DELETE CASCADE,
    FOREIGN KEY (tournament_id) REFERENCES Tournaments(tournament_id) ON DELETE CASCADE
);

-- Create Matches Table
CREATE TABLE Matches (
    match_id INT AUTO_INCREMENT PRIMARY KEY,
    tournament_id INT,
    team1_id INT,
    team2_id INT,
    date DATE,
    winner_id INT,
    score_team1 INT DEFAULT 0,
    score_team2 INT DEFAULT 0,
    FOREIGN KEY (tournament_id) REFERENCES Tournaments(tournament_id) ON DELETE CASCADE,
    FOREIGN KEY (team1_id) REFERENCES Teams(team_id) ON DELETE SET NULL,
    FOREIGN KEY (team2_id) REFERENCES Teams(team_id) ON DELETE SET NULL,
    FOREIGN KEY (winner_id) REFERENCES Teams(team_id) ON DELETE SET NULL
);

-- Create PlayerStats Table
CREATE TABLE PlayerStats (
    stat_id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT,
    match_id INT,
    kills INT DEFAULT 0,
    deaths INT DEFAULT 0,
    assists INT DEFAULT 0,
    cs INT DEFAULT 0,
    damage INT DEFAULT 0,
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE,
    FOREIGN KEY (match_id) REFERENCES Matches(match_id) ON DELETE CASCADE
);

-- Create Awards Table
CREATE TABLE Awards (
    award_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    type ENUM('Team', 'Player') NOT NULL,
    tournament_id INT,
    recipient_id INT,
    FOREIGN KEY (tournament_id) REFERENCES Tournaments(tournament_id) ON DELETE CASCADE,
    FOREIGN KEY (recipient_id) REFERENCES Players(player_id) ON DELETE SET NULL
);


CREATE TABLE Ranks (
    rank_id INT PRIMARY KEY,
    rank_name VARCHAR(20) NOT NULL,
    tier INT NOT NULL, -- Tier will define the hierarchy of ranks for ordering
    sub_tier INT DEFAULT 4 -- Default sub-tier, which you can adjust for each rank
);