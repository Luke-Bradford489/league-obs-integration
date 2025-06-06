# generated by datamodel-codegen:
#   filename:  riot_open_api.json
#   timestamp: 2024-10-17T17:34:07+00:00

from __future__ import annotations

from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class MetadataDto(BaseModel):
    data_version: str = Field(..., description='Match data version.')
    match_id: str = Field(..., description='Match id.')
    participants: List[str] = Field(..., description='A list of participant PUUIDs.')


class GameMode(Enum):
    Constructed = 'Constructed'
    Expeditions = 'Expeditions'
    Tutorial = 'Tutorial'


class GameType(Enum):
    Ranked = 'Ranked'
    Normal = 'Normal'
    AI = 'AI'
    Tutorial = 'Tutorial'
    VanillaTrial = 'VanillaTrial'
    Singleton = 'Singleton'
    StandardGauntlet = 'StandardGauntlet'


class GameFormat(Enum):
    standard = 'standard'
    eternal = 'eternal'


class PlayerDto(BaseModel):
    puuid: str
    deck_id: str
    deck_code: str = Field(
        ...,
        description='Code for the deck played. Refer to LOR documentation for details on deck codes.',
    )
    factions: List[str]
    game_outcome: str
    order_of_play: int = Field(
        ..., description='The order in which the players took turns.'
    )


class InfoDto(BaseModel):
    game_mode: GameMode = Field(
        ..., description='(Legal values:  Constructed,  Expeditions,  Tutorial)'
    )
    game_type: GameType = Field(
        ...,
        description='(Legal values:  Ranked,  Normal,  AI,  Tutorial,  VanillaTrial,  Singleton,  StandardGauntlet)',
    )
    game_start_time_utc: str
    game_version: str
    game_format: GameFormat = Field(
        ..., description='(Legal values:  standard,  eternal)'
    )
    players: List[PlayerDto]
    total_turn_count: int = Field(..., description='Total turns taken by both players.')


class MatchDto(BaseModel):
    metadata: MetadataDto = Field(..., description='Match metadata.')
    info: InfoDto = Field(..., description='Match info.')
