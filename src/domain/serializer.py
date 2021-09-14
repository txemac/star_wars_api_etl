from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Dict
from typing import List


class Serializer(ABC):
    @classmethod
    @abstractmethod
    def serialize(
        cls,
        item: Any,
    ) -> Dict:
        pass

    @classmethod
    def serialize_list(
        cls,
        item_list: List,
    ) -> List[Dict]:
        return [cls.serialize(item) for item in item_list]
