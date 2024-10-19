from typing import List, Optional
from pydantic import BaseModel


class SearchMatchModel(BaseModel):
    start_time: Optional[int]
    end_time: Optional[int]
    start: Optional[int] = 0
    count: int = 10
    def toJson(self):
        return {
            "startTime" : self.start_time,
            "endTime" : self.end_time,
            "start" : self.start,
            "count" : self.count
        }
