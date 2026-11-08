__all__ = ("message_handler", )


def message_handler(username: str, is_premium: bool) -> str:
    if not is_premium:
        return f"Спасибо, {username}! Ваш отзыв сохранён."

    return f"Спасибо, {username}! Ваш отзыв сохранён. Ваш отзыв будет рассмотрен в приоритетном порядке."
