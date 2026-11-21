# === Stage 6: Связанная сущность ===
# Project: ThesisNotes
import os
from pathlib import Path

THESIS_NOTES_DIR = Path(__file__).resolve().parent
SOURCE_FILE = THESIS_NOTES_DIR / "thesis_notes_sources.json"
CITATION_FILE = THESIS_NOTES_DIR / "thesis_notes_citations.json"


class Citation:
    def __init__(self, id, text, source_id, page=None):
        self.id = id
        self.text = text
        self.source_id = source_id
        self.page = page

    def to_dict(self):
        data = {"id": self.id, "text": self.text, "source_id": self.source_id}
        if self.page is not None:
            data["page"] = self.page
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            text=data["text"],
            source_id=data["source_id"],
            page=data.get("page"),
        )


class CitationStore:
    def __init__(self, filename=CITATION_FILE):
        self.filename = filename
        self.citations = self._load()

    def _load(self):
        citations = []
        if self.filename.exists():
            with open(self.filename, "r", encoding="utf-8") as file:
                citations = [
                    Citation.from_dict(item)
                    for item in json.load(file)
                ]
        return citations

    def _save(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                [citation.to_dict() for citation in self.citations],
                file,
                ensure_ascii=False,
                indent=2,
            )

    def add_citation(self, text, source_id, page=None):
        if source_id not in self._get_source_ids():
            raise ValueError(f"Источник {source_id} не найден")
        citation = Citation(
            id=self._generate_id(),
            text=text,
            source_id=source_id,
            page=page,
        )
        self.citations.append(citation)
        self._save()
        return citation

    def _generate_id(self):
        new_id = 1
        while any(
            citation.id == new_id for citation in self.citations
        ):
            new_id += 1
        return new_id

    def _get_source_ids(self):
        source_ids = []
        if SOURCE_FILE.exists():
            with open(SOURCE_FILE, "r", encoding="utf-8") as file:
                source_ids = [
                    item["id"]
                    for item in json.load(file)
                ]
        return source_ids


import json
