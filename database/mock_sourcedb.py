from abc import ABC, abstractmethod


class MockScoreDB(ABC):
    @abstractmethod
    def write_score_db(self, word: str, score: float):
        pass
