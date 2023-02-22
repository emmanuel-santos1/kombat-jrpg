import json

from tests.utils.fight import fight_without_winner


def test_fight_without_winner(client):
    data = fight_without_winner()
    response = client.post("/fight", data=json.dumps(data))
    assert response.status_code == 200
    assert isinstance(response.json(), "list")
