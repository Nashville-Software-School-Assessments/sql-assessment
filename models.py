from dataclasses import dataclass
"""
Because these classes are being used to validate rows, there is no reason to create
complex objects with properties for foreign key types. Include all columns as properties
at the top level of the data class regardless of entity (dupe columns will be omitted
when converting to Python objects) 
"""

@dataclass
class NumberofTrianglesRow:
    NumberofTrianglers: int

@dataclass
class MusicianRow:
    MusicianId: int
    MusicianName: str

@dataclass
class InstrumentNameRow:
    InstrumentName: str

@dataclass
class InstrumentRow:
    InstrumentId: int
    InstrumentName: str
    DifficultyId: int