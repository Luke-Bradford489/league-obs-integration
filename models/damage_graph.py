from pydantic import BaseModel

from models.match_v5 import MatchDto, ParticipantDto

class DamageGraphRequest(BaseModel):
    winner_list: list[ParticipantDto]
    loser_list: list[ParticipantDto]

    @staticmethod 
    def from_match(match: MatchDto):
        winner_list, loser_list = [
            player for player in match.info.participants if player.win
        ], [player for player in match.info.participants if not player.win]
        return DamageGraphRequest(winner_list=winner_list, loser_list=loser_list)