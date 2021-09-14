from http import HTTPStatus

import requests

from src import settings
from src.domain.httpbin_repository import HTTPBinRepository


class HTTPBinAdapter(HTTPBinRepository):

    def send_file(
        self,
        path: str,
    ) -> bool:
        with open(path, 'rb') as file:
            response = requests.post(
                url=settings.HTTPBIN_API_URL,
                files=dict(csv_file=file),
            )
        return response.status_code == HTTPStatus.OK
