#!/usr/bin/python3
from abc import ABC, abstractmethod

class DatabaseFetcher(ABC):
    @abstractmethod
    def get(location):
        return None
    @abstractmethod
    def check(location):
        return None

class DatabaseUploader(ABC):
    @abstractmethod
    def push(data, location):
        return None
