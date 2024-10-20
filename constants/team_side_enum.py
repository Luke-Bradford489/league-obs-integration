from enum import Enum

class TeamSide(Enum):
    BLUE_SIDE = 100
    RED_SIDE = 200

    @classmethod
    def from_value(cls, value):
        if value == 100:
            return cls.BLUE_SIDE
        elif value == 200:
            return cls.RED_SIDE
        else:
            raise ValueError(f"Unknown value: {value}")

# Example usage
team = TeamSide.from_value(100)
print(team)  # Output: TeamSide.BLUE_SIDE

team = TeamSide.from_value(200)
print(team)  # Output: TeamSide.RED_SIDE
