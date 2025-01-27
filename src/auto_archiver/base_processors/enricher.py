"""
Enrichers are modular components that enhance archived content by adding
context, metadata, or additional processing.

These add additional information to the context, such as screenshots, hashes, and metadata.
They are designed to work within the archiving pipeline, operating on `Metadata` objects after
the archiving step and before storage or formatting.

Enrichers are optional but highly useful for making the archived data more powerful.
"""
from __future__ import annotations
from dataclasses import dataclass
from abc import abstractmethod, ABC
from auto_archiver.core import Metadata, Step

@dataclass
class Enricher(Step, ABC):
    """Base classes and utilities for enrichers in the Auto-Archiver system."""
    name = "enricher"

    @abstractmethod
    def enrich(self, to_enrich: Metadata) -> None: pass
