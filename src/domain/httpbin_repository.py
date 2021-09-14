from abc import ABC
from abc import abstractmethod


class HTTPBinRepository(ABC):

    @abstractmethod
    def send_file(
        self,
        path: str,
    ) -> bool:
        """
        Send file to HTTPBin

        :param path: path of the file to upload
        :return: True is ok
        """
        pass
