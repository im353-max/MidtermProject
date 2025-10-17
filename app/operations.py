from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Dict
from math import pow

class Operation(ABC):
    """Abstract base class for all operations."""
    @abstractmethod
    def execute(self, a, b):
        pass


class AddOperation(Operation):
    def execute(self, a, b):
        return a + b
    
class OperationFactory:
    """Factory class for creating operation instances."""
    @staticmethod
    def create_operation(operation_name: str):
        operations = {
            "add": AddOperation(),         
        }

        op = operations.get(operation_name.lower())
        if not op:
            raise OperationError(f"Invalid operation '{operation_name}'.")
        return op