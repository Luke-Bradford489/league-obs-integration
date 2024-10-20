from pydantic import BaseModel

from constants.team_side_enum import TeamSide
from models.match_v5 import MatchDto, ParticipantDto

class DamageGraphRequest(BaseModel):
    blue_side_list: list[ParticipantDto]
    red_side_list: list[ParticipantDto]


    @staticmethod 
    def from_match(match: MatchDto):
        blue_list, red_list = [
            player for player in match.info.participants if TeamSide.from_value(player.teamId) == TeamSide.BLUE_SIDE
        ], [player for player in match.info.participants if TeamSide.from_value(player.teamId) == TeamSide.RED_SIDE]
        return DamageGraphRequest(blue_side_list=blue_list, red_side_list=red_list)