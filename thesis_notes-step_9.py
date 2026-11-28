# === Stage 9: Сортировка записей ===
# Project: ThesisNotes
def sort_by_name_then_created(records):
    """
    Сортирует список источников.
    Первичный ключ — название (строчный вид, без учёта регистра).
    Вторичный ключ — дата создания (epoch в секундах).
    Порядок: возрастание по названию, затем возрастание по дате.
    """
    def key(record):
        return (
            record.get("name", "").strip().lower(),
            record.get("created_at", 0),
        )
    return sorted(records, key=key)


def sort_by_created_then_name(records):
    """
    Сортировка по убыванию даты создания,
    при равенстве — по убыванию названия.
    """
    def key(record):
        return (
            -record.get("created_at", 0),
            record.get("name", "").strip().lower(),
        )
    return sorted(records, key=key)


def sort_by_name_desc_then_created(records):
    """
    Сортировка по убыванию названия,
    при равенстве — по возрастанию даты создания.
    """
    def key(record):
        return (
            -ord(record.get("name", "").strip().lower()[0]) if record.get("name", "").strip().lower() else -1,
            record.get("created_at", 0),
        )
    return sorted(records, key=key)


def sort_by_created_desc_then_name(records):
    """
    Сортировка по убыванию даты создания,
    при равенстве — по возрастанию названия.
    """
    def key(record):
        return (
            -record.get("created_at", 0),
            record.get("name", "").strip().lower(),
        )
    return sorted(records, key=key)
