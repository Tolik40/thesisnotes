# === Stage 1: Каркас модуля ===
# Project: ThesisNotes
dataclasses.py


from dataclasses import dataclass


@dataclass
class Source:
    title: str
    author: str
    year: int
    chapter: int


def demo_sources() -> list[Source]:
    sources = [
        Source("Введение в информатику", "Иванов И. И.", 2020, 1),
        Source("Методы исследований", "Петрова А. С.", 2019, 3),
        Source("Теория данных", "Сидоров К. В.", 2021, 2),
    ]
    return sources


def main() -> None:
    for source in demo_sources():
        print(source)


if __name__ == "__main__":
    main()
