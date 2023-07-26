# Type hinting is a way to provide hints about the types of variables and 
# function arguments in Python code. It helps improve code readability 
# and enables static type checkers to catch potential 
# type-related errors.

from typing import List, Tuple

def add(x: int, y: int) -> int:
    return x + y

def concatenate(words: List[str]) -> str:
    return ' '.join(words)

def get_user_info() -> Tuple[str, int]:
    return "Alice", 30
