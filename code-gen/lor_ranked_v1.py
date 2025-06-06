# generated by datamodel-codegen:
#   filename:  riot_open_api.json
#   timestamp: 2024-10-17T17:34:07+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class PlayerDto(BaseModel):
    name: str
    rank: int
    lp: int = Field(..., description='League points.')


class LeaderboardDto(BaseModel):
    players: List[PlayerDto] = Field(
        ..., description='A list of players in Master tier.'
    )
