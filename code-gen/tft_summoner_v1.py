# generated by datamodel-codegen:
#   filename:  riot_open_api.json
#   timestamp: 2024-10-17T17:34:07+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class SummonerDTO(BaseModel):
    accountId: str = Field(
        ..., description='Encrypted account ID. Max length 56 characters.'
    )
    profileIconId: int = Field(
        ..., description='ID of the summoner icon associated with the summoner.'
    )
    revisionDate: int = Field(
        ...,
        description='Date summoner was last modified specified as epoch milliseconds. The following events will update this timestamp: summoner name change, summoner level change, or profile icon change.',
    )
    id: str = Field(..., description='Encrypted summoner ID. Max length 63 characters.')
    puuid: str = Field(
        ..., description='Encrypted PUUID. Exact length of 78 characters.'
    )
    summonerLevel: int = Field(
        ..., description='Summoner level associated with the summoner.'
    )
