from pydantic import BaseModel

from models.match_v5 import MatchDto, ParticipantDto

class Player(BaseModel):
    champ: str
    name: str
    won: bool

    kills: int
    deaths: int
    assists: int
    cs: int
    vision_score: int
    level: int
    gold_earned: int

    
    magic_damage: int
    physical_damage: int
    total_damage: int



    total_damage_taken: int

    total_heal: int
    total_shielded: int
    def __str__(self):
        win_status = "🏆 **Victory**" if self.won else "❌ **Defeat**"
        return f"""
**Player Stats**
**Champion:** {self.champ}
**Player Name:** {self.name}
{win_status}

**Combat Stats**
- **Kills:** {self.kills}
- **Deaths:** {self.deaths}
- **Assists:** {self.assists}
- **CS:** {self.cs}
- **Vision Score:** {self.vision_score}
- **Level:** {self.level}
- **Gold Earned:** {self.gold_earned}

**Damage Stats**
- **Magic Damage:** {self.magic_damage}
- **Physical Damage:** {self.physical_damage}
- **Total Damage:** {self.total_damage}

**Survivability**
- **Damage Taken:** {self.total_damage_taken}
- **Total Healing:** {self.total_heal}
- **Total Shielded:** {self.total_shielded}
"""
    
    @staticmethod
    def from_participant( player: ParticipantDto):
        return Player(
        champ = player.championName,
        name = f"{player.riotIdGameName}#{player.riotIdTagline}",
        won = player.win,
        kills = player.kills,
        deaths = player.deaths,
        assists = player.assists,
        cs = player.totalMinionsKilled,
        vision_score = player.visionScore,
        level = player.champLevel,
        gold_earned = player.goldEarned,
        magic_damage = player.magicDamageDealtToChampions,
        physical_damage = player.physicalDamageDealtToChampions,
        total_damage = player.totalDamageDealtToChampions,
        total_damage_taken = player.totalDamageTaken,
        total_heal = player.totalHeal,
        total_shielded = player.totalDamageShieldedOnTeammates ,
        )
        


class MatchSummary(BaseModel):
    players: list[Player]
    game_time: int

    @staticmethod
    def from_match(match:MatchDto):
        players = [Player.from_participant(player) for player in match.info.participants]
        game_time = match.info.gameDuration
        return MatchSummary(players=players, game_time=game_time)
    
    def __str__(self):
        minutes = self.game_time // 60
        seconds = self.game_time % 60
        formatted_game_time = f"{minutes}m {seconds}s"
        
        player_summaries = "\n".join([str(player) for player in self.players])
        
        return f"""
**Match Summary**
**Game Duration:** {formatted_game_time}

**Players:**
{player_summaries}
"""