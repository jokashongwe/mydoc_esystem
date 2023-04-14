from dataclasses import dataclass

@dataclass
class AtomicFact:
    symbol: str
    value: any
