from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Dict
from typing import List


class Transform(ABC):
    @classmethod
    @abstractmethod
    def transform(
        cls,
        item: Any,
    ) -> Dict:
        pass

    @classmethod
    def transform_list(
        cls,
        item_list: List[Any],
    ) -> List[Any]:
        return [cls.transform(item) for item in item_list]
