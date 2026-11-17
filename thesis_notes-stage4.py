# === Stage 4: Редактирование записей ===
# Project: ThesisNotes
def edit_source(source_id, changes, allowed_fields=("title", "author", "year", "chapter")):
    """Редактирует источник по идентификатору, меняя только допустимые поля."""
    if not isinstance(changes, dict):
        raise TypeError("Изменения должны быть словарём")

    unknown = set(changes.keys()) - set(allowed_fields)
    if unknown:
        raise ValueError(
            "Недопустимые поля для изменения: " + ", ".join(sorted(unknown))
        )

    sources = _load_sources()
    for index, source in enumerate(sources):
        if source.get("id") == source_id:
            for field in changes:
                if field not in allowed_fields:
                    raise ValueError(
                        "Недопустимое поле для изменения: " + field
                    )
                sources[index][field] = changes[field]
            _save_sources(sources)
            return sources[index]

    raise KeyError("Источник с идентификатором '" + str(source_id) + "' не найден")


def _load_sources():
    """Загружает список источников из хранилища проекта."""
    try:
        with open("thesis_notes/sources.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def _save_sources(sources):
    """Сохраняет список источников в хранилище проекта."""
    with open("thesis_notes/sources.json", "w", encoding="utf-8") as f:
        json.dump(sources, f, ensure_ascii=False, indent=2)
