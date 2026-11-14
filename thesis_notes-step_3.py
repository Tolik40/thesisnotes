# === Stage 3: Хранилище в памяти ===
# Project: ThesisNotes
import uuid


class SourceError(Exception):
    """Ошибка хранения источников диссертации."""


class Source:
    __slots__ = ("id", "title", "author", "year", "chapter")

    def __init__(self, title, author, year, chapter):
        if not title.strip():
            raise SourceError("Название источника не может быть пустым")
        if not author.strip():
            raise SourceError("Автор источника не может быть пустым")
        if not str(year).strip():
            raise SourceError("Год издания не может быть пустым")
        if not str(chapter).strip():
            raise SourceError("Глава не может быть пустой")
        self.id = uuid.uuid4()
        self.title = title.strip()
        self.author = author.strip()
        self.year = str(year).strip()
        self.chapter = str(chapter).strip()

    def __repr__(self):
        return "Source(id={!r}, title={!r}, author={!r}, year={!r}, chapter={!r})".format(
            self.id, self.title, self.author, self.year, self.chapter
        )


class SourceStore:
    def __init__(self):
        self._sources = {}

    def add_source(self, source):
        if not isinstance(source, Source):
            raise SourceError("Хранилище принимает только объекты Source")
        if source.id in self._sources:
            raise SourceError("Источник с идентификатором {} уже добавлен".format(source.id))
        self._sources[source.id] = source
        return source

    def get_source(self, source_id):
        try:
            return self._sources[source_id]
        except KeyError:
            raise SourceError("Источник с идентификатором {} не найден".format(source_id))

    def list_sources(self):
        return list(self._sources.values())

    def __len__(self):
        return len(self._sources)
