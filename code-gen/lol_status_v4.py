# generated by datamodel-codegen:
#   filename:  riot_open_api.json
#   timestamp: 2024-10-17T17:34:07+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class MaintenanceStatus(Enum):
    scheduled = 'scheduled'
    in_progress = 'in_progress'
    complete = 'complete'


class IncidentSeverity(Enum):
    info = 'info'
    warning = 'warning'
    critical = 'critical'


class Platform(Enum):
    windows = 'windows'
    macos = 'macos'
    android = 'android'
    ios = 'ios'
    ps4 = 'ps4'
    xbone = 'xbone'
    switch = 'switch'


class ContentDto(BaseModel):
    locale: str
    content: str


class PublishLocation(Enum):
    riotclient = 'riotclient'
    riotstatus = 'riotstatus'
    game = 'game'


class UpdateDto(BaseModel):
    id: int
    author: str
    publish: bool
    publish_locations: List[PublishLocation] = Field(
        ..., description='(Legal values: riotclient, riotstatus, game)'
    )
    translations: List[ContentDto]
    created_at: str
    updated_at: str


class StatusDto(BaseModel):
    id: int
    maintenance_status: Optional[MaintenanceStatus] = Field(
        None, description='(Legal values:  scheduled,  in_progress,  complete)'
    )
    incident_severity: Optional[IncidentSeverity] = Field(
        None, description='(Legal values:  info,  warning,  critical)'
    )
    titles: List[ContentDto]
    updates: List[UpdateDto]
    created_at: str
    archive_at: Optional[str] = None
    updated_at: Optional[str] = None
    platforms: List[Platform] = Field(
        ...,
        description='(Legal values: windows, macos, android, ios, ps4, xbone, switch)',
    )


class PlatformDataDto(BaseModel):
    id: str
    name: str
    locales: List[str]
    maintenances: List[StatusDto]
    incidents: List[StatusDto]
