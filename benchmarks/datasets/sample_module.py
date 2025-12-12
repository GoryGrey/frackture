"""Sample Python module for benchmarking"""

import math
from typing import List, Optional


def calculate_statistics(data: List[float]) -> dict:
    """Calculate basic statistics for a list of numbers."""
    if not data:
        return {}
    
    sorted_data = sorted(data)
    n = len(data)
    
    return {
        'mean': sum(data) / n,
        'median': sorted_data[n // 2],
        'min': sorted_data[0],
        'max': sorted_data[-1],
        'stddev': math.sqrt(sum((x - sum(data) / n) ** 2 for x in data) / n)
    }


class DataValidator:
    """Validate and sanitize input data."""
    
    def __init__(self, strict: bool = False):
        self.strict = strict
        self.errors: List[str] = []
    
    def validate_email(self, email: str) -> bool:
        """Validate email format."""
        if '@' not in email or '.' not in email.split('@')[-1]:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True
    
    def validate_positive(self, value: float) -> bool:
        """Ensure value is positive."""
        if value <= 0:
            self.errors.append(f"Value must be positive: {value}")
            return False
        return True
