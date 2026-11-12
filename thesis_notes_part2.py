# === Stage 2: Проверка полей ===
# Project: ThesisNotes
from datetime import datetime


SOURCE_ERROR_PREFIX = "Неверное значение поля источника: "


def normalize_source_name(name):
    if name is None:
        return ""
    normalized = name.strip()
    if normalized:
        normalized = normalized[0].upper() + normalized[1:].lower()
    return normalized


def normalize_source_author(author):
    if author is None:
        return ""
    normalized = author.strip()
    if normalized:
        normalized = normalized[0].upper() + normalized[1:].lower() + normalized[2:]
    return normalized


def normalize_source_year(year):
    if year is None:
        return ""
    cleaned = str(year).strip()
    if cleaned.isdigit():
        return cleaned
    return ""


def normalize_source_chapter(chapter):
    if chapter is None:
        return ""
    cleaned = str(chapter).strip()
    if cleaned.isdigit():
        return cleaned
    return ""


def validate_source(source):
    errors = []

    name = normalize_source_name(source.get("name"))
    if not name:
        errors.append(SOURCE_ERROR_PREFIX + "Название не может быть пустым.")
    source["name"] = name

    author = normalize_source_author(source.get("author"))
    if not author:
        errors.append(SOURCE_ERROR_PREFIX + "Автор не может быть пустым.")
    source["author"] = author

    year = normalize_source_year(source.get("year"))
    if not year:
        errors.append(SOURCE_ERROR_PREFIX + "Год должен быть числом.")
    source["year"] = year

    chapter = normalize_source_chapter(source.get("chapter"))
    if not chapter:
        errors.append(SOURCE_ERROR_PREFIX + "Глава должна быть числом.")
    source["chapter"] = chapter

    return errors
