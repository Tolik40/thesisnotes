# === Stage 5: Удаление и восстановление ===
# Project: ThesisNotes
import uuid


class SoftDeletedSource:
    """Результат мягкого удаления источника с возможностью восстановления."""

    __slots__ = ("id", "deleted_at", "restored")

    def __init__(self, source_id, deleted_at=None):
        self.id = source_id
        self.deleted_at = deleted_at
        self.restored = False

    def restore(self):
        self.restored = True
        self.deleted_at = None


class SourceRepository:
    """Хранение источников с поддержкой мягкого удаления."""

    def __init__(self):
        self._sources = {}
        self._deleted = {}

    def delete_source(self, source_id):
        """Мягкое удаление источника: переносим в корзину с меткой времени."""
        if source_id not in self._sources:
            raise KeyError(f"Источник {source_id} не найден")
        deleted_record = SoftDeletedSource(source_id, deleted_at=uuid.uuid4())
        self._deleted[deleted_record.id] = deleted_record
        del self._sources[source_id]
        return deleted_record

    def restore_source(self, deleted_id):
        """Восстанавливает удалённый источник в активный список."""
        if deleted_id not in self._deleted:
            raise KeyError(f"Удалённый источник {deleted_id} не найден")
        record = self._deleted.pop(deleted_id)
        record.restore()
        self._sources[record.id] = record
        return record

    def get_active_sources(self):
        """Возвращает только активные (неудалённые) источники."""
        return dict(self._sources)

    def get_trash(self):
        """Возвращает все источники в корзине."""
        return dict(self._deleted)

    def purge_trash(self, deleted_id):
        """Окончательно удаляет запись из корзины."""
        if deleted_id not in self._deleted:
            raise KeyError(f"Запись {deleted_id} не в корзине")
        del self._deleted[deleted_id]
