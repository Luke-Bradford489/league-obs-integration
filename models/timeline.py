from pydantic import BaseModel, computed_field
from models.match_v5 import TimelineDto


class PlayerTimeline(BaseModel):
    name: str
    creep_score: int
    physical_damage: int
    magic_damage: int
    xp: int
    gold: int

    @computed_field
    @property
    def total_damage(self) -> int:
        return self.physical_damage + self.magic_damage

    def __str__(self):
        return f"""
**Creep Score:** {self.creep_score}
**Physical Damage:** {self.physical_damage}
**Magic Damage:** {self.magic_damage}
**Total Damage:** {self.total_damage}
**XP:** {self.xp}
**Gold:** {self.gold}
"""

class TimelineData(BaseModel):
    # cs, damage, xp, gold
    # diff based on role
    players: list[PlayerTimeline]
    minute: int

    def __str__(self):
        player_summaries = "\n".join([str(player) for player in self.players])
        return f"""
Statistics at {self.minute} minutes:

{player_summaries}
"""

    @staticmethod
    def from_riot_api_data(api_data: TimelineDto, minute: int):
        player_map = {player.participantId: player.puuid for player in api_data.info.participants}
        timestamp_data = api_data.info.frames[minute]
        players = [
            PlayerTimeline(
                name=player_map[int(player_id)],
                creep_score=data.minionsKilled,
                physical_damage=data.damageStats.physicalDamageDoneToChampions,
                magic_damage=data.damageStats.magicDamageDoneToChampions,
                xp=data.xp,
                gold=data.totalGold
            )
            for player_id, data in timestamp_data.participantFrames.items()
        ]

        return TimelineData(players=players, minute=minute)