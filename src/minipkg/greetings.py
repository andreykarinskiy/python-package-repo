"""Простые функции приветствия для примера."""

from __future__ import annotations


def greet(name: str, *, excited: bool = False) -> str:
    """Вернуть персональное приветствие.

    Args:
        name: Имя пользователя.
        excited: Если True, то добавляется восклицательный знак.

    Returns:
        Строку с приветствием.
    """

    suffix = "!" if excited else "."
    normalized = name.strip() or "мир"
    return f"Привет, {normalized}{suffix}"
