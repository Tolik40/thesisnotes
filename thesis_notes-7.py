# === Stage 7: Связи между сущностями ===
# Project: ThesisNotes
source_repository.py

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Source:
    """Источник: название, автор, год и ссылка на главу."""

    title: str
    author: str
    year: int
    chapter: Optional["Chapter"] = None


@dataclass
class Citation:
    """Цитата, принадлежащая какому-то источнику."""

    text: str
    source: Optional[Source] = None


@dataclass
class Chapter:
    """Глава диссертации с привязанными сроками."""

    title: str
    deadline: str
    citations: List[Citation] = field(default_factory=list)


def _index_citations_by_source(citations: List[Citation]) -> Dict[str, List[Citation]]:
    """Собираем список цитат по ключу id источника."""

    indexed: Dict[str, List[Citation]] = defaultdict(list)
    for citation in citations:
        key = citation.source.title if citation.source else "<без источника>"
        indexed[key].append(citation)
    return indexed


def get_citations_for_source(
    source: Source,
    citations: List[Citation],
) -> List[Citation]:
    """Возвращает все цитаты для заданного источника."""

    indexed = _index_citations_by_source(citations)
    return list(indexed.get(source.title, []))


def check_integrity(source: Source, citations: List[Citation]) -> bool:
    """Проверка целостности связи «источник — цитата».

    Цитата считается «сломанной», если у неё нет источника или он не совпадает
    с переданным объектом по названию и году.
    """

    indexed = _index_citations_by_source(citations)
    target = source.title
    target_year = source.year

    for citation in citations:
        if citation.source is None:
            return False
        if citation.source.title != target:
            return False
        if citation.source.year != target_year:
            return False
        return True

    return len(citations) == 0


def check_source_present(source: Source, citations: List[Citation]) -> bool:
    """Проверка, что у источника хотя бы одна цитата."""

    indexed = _index_citations_by_source(citations)
    return len(indexed.get(source.title, [])) > 0


def find_orphan_citations(citations: List[Citation]) -> List[Citation]:
    """Цитаты без привязанного источника."""

    return [citation for citation in citations if citation.source is None]


def find_mismatched_citations(
    source: Source,
    citations: List[Citation],
) -> List[Citation]:
    """Цитаты, чей источник не совпадает с переданным объектом."""

    indexed = _index_citations_by_source(citations)
    return list(indexed.get(source.title, []))
