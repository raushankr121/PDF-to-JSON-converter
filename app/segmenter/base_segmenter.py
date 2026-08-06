from abc import ABC, abstractmethod


class BaseSegmenter(ABC):

    @abstractmethod
    def segment(self, blocks):
        pass