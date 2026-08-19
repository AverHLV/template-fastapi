from fastapi import status


class TestResource:
    code = 'code'

    @staticmethod
    def get_url_retrieve(app, code: str) -> str:
        return app.url_path_for('resource_retrieve', code=code)

    async def test__resource_retrieve(self, app, client):
        url = self.get_url_retrieve(app, code=self.code)
        response = await client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {'code': self.code}
