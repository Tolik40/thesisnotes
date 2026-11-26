# === Stage 8: Генерация идентификаторов ===
# Project: ThesisNotes
def generate_id(prefix: str, counter: dict) -> str:
    """Генерирует уникальный идентификатор с префиксом и проверкой коллизий."""
    while True:
        candidate = f"{prefix}-{counter['current'] + 1}"
        counter['current'] += 1
        if candidate not in counter['used']:
            counter['used'].add(candidate)
            return candidate


def create_source_id(counter: dict) -> str:
    return generate_id("SRC", counter)


def create_quote_id(counter: dict) -> str:
    return generate_id("QT", counter)


def create_chapter_id(counter: dict) -> str:
    return generate_id("CH", counter)


def create_deadline_id(counter: dict) -> str:
    return generate_id("DL", counter)


if __name__ == "__main__":
    counter = {"current": 0, "used": set()}
    ids = [create_source_id(counter) for _ in range(3)]
    print(ids)
    assert len(set(ids)) == 3, "Дубликаты!"
    print("Уникальные идентификаторы сгенерированы без коллизий.")
