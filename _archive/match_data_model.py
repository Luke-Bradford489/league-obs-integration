from typing import List, Optional
from pydantic import BaseModel


class PerkStyleSelectionDto(BaseModel):
    perk: int
    var1: int
    var2: int
    var3: int


class PerkStyleDto(BaseModel):
    description: str
    selections: List[PerkStyleSelectionDto]
    style: int


class PerkStatsDto(BaseModel):
    defense: int
    flex: int
    offense: int


class PerksDto(BaseModel):
    statPerks: PerkStatsDto
    styles: List[PerkStyleDto]


class MissionsDto(BaseModel):
    playerScore0: int
    playerScore1: int
    playerScore2: int
    playerScore3: int
    playerScore4: int
    playerScore5: int
    playerScore6: int
    playerScore7: int
    playerScore8: int
    playerScore9: int
    playerScore10: int
    playerScore11: int


# class ChallengesDto(BaseModel):
#     baronBuffGoldAdvantageOverThreshold: Optional[int]
#     controlWardTimeCoverageInRiverOrEnemyHalf: Optional[float]
#     earliestBaron: Optional[int]
#     earliestDragonTakedown: Optional[int]
#     legendaryItemUsed: Optional[List[int]]
    # Add any other fields as needed


class ParticipantDto(BaseModel):
    allInPings: Optional[int]
    assistMePings: Optional[int]
    assists: Optional[int]
    baronKills: Optional[int]
    bountyLevel: Optional[int]
    champExperience: Optional[int]
    champLevel: Optional[int]
    championId: Optional[int]
    championName: Optional[str]
    championTransform: Optional[int]
    challenges: Optional[dict]
    consumablesPurchased: Optional[int]
    damageDealtToBuildings: Optional[int]
    damageDealtToObjectives: Optional[int]
    damageDealtToTurrets: Optional[int]
    damageSelfMitigated: Optional[int]
    deaths: Optional[int]
    detectorWardsPlaced: Optional[int]
    doubleKills: Optional[int]
    dragonKills: Optional[int]
    eligibleForProgression: Optional[bool]
    enemyMissingPings: Optional[int]
    enemyVisionPings: Optional[int]
    firstBloodAssist: Optional[bool]
    firstBloodKill: Optional[bool]
    firstTowerAssist: Optional[bool]
    firstTowerKill: Optional[bool]
    gameEndedInEarlySurrender: Optional[bool]
    gameEndedInSurrender: Optional[bool]
    goldEarned: Optional[int]
    goldSpent: Optional[int]
    individualPosition: Optional[str]
    inhibitorKills: Optional[int]
    inhibitorTakedowns: Optional[int]
    inhibitorsLost: Optional[int]
    item0: Optional[int]
    item1: Optional[int]
    item2: Optional[int]
    item3: Optional[int]
    item4: Optional[int]
    item5: Optional[int]
    item6: Optional[int]
    itemsPurchased: Optional[int]
    kills: Optional[int]
    perks: Optional[PerksDto]
    puuid: Optional[str]
    win: Optional[bool]
    # Add other fields as needed


class ObjectivesDto(BaseModel):
    first: bool
    kills: int


class BanDto(BaseModel):
    championId: int
    pickTurn: int


class TeamDto(BaseModel):
    bans: List[BanDto]
    objectives: ObjectivesDto
    teamId: int
    win: bool


class InfoDto(BaseModel):
    endOfGameResult: str
    gameCreation: int
    gameDuration: int
    gameEndTimestamp: int
    gameId: int
    gameMode: str
    gameName: str
    gameStartTimestamp: int
    gameType: str
    gameVersion: str
    mapId: int
    participants: List[ParticipantDto]
    platformId: str
    queueId: int
    teams: List[TeamDto]
    tournamentCode: Optional[str]


class MetadataDto(BaseModel):
    dataVersion: str
    matchId: str
    participants: List[str]


class MatchDto(BaseModel):
    metadata: MetadataDto
    info: InfoDto
