from pydantic import BaseModel, computed_field

class TenMinStatsModel(BaseModel):
    kills: int = 0 
    deaths: int = 0 
    assists: int = 0
    gold_earned: int = 0
    minion_kills_cs: int = 0 
    kill_participation: float = 0.0
    wards_placed: int = 0
    champion_damage_share: float = 0.0
    wards_destroyed: int = 0

    @computed_field
    @property
    def kda(self) -> str:
        return f"{self.kills}/{self.deaths}/{self.assists}"