from __future__ import annotations
from dataclasses import dataclass
from abc import abstractmethod, ABC
from typing import Union

from auto_archiver.core import Metadata, BaseModule


@dataclass
class Database(BaseModule):

    def started(self, item: Metadata) -> None:
        """signals the DB that the given item archival has started"""
        pass

    def failed(self, item: Metadata, reason:str) -> None:
        """update DB accordingly for failure"""
        pass

    def aborted(self, item: Metadata) -> None:
        """abort notification if user cancelled after start"""
        pass

    # @abstractmethod
    def fetch(self, item: Metadata) -> Union[Metadata, bool]:
        """check and fetch if the given item has been archived already, each database should handle its own caching, and configuration mechanisms"""
        return False

    @abstractmethod
    def done(self, item: Metadata, cached: bool=False) -> None:
        """archival result ready - should be saved to DB"""
        pass
