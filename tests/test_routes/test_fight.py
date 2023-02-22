import json

from sql_app.crud import list_fights
from tests.utils.fight import fight_arnaldor_wins
from tests.utils.fight import fight_big_brother_starts
from tests.utils.fight import fight_invalid_hit
from tests.utils.fight import fight_invalid_movement
from tests.utils.fight import fight_starts_less_button_combo_has
from tests.utils.fight import fight_starts_less_hits_has
from tests.utils.fight import fight_starts_less_movements_has
from tests.utils.fight import fight_tonyn_wins
from tests.utils.fight import fight_very_large
from tests.utils.fight import fight_without_blows
from tests.utils.fight import fight_without_winner


def test_fight_unauthorized(client):
    """
    Check if you are not logged in the app you can not play
    """
    data = {}
    response = client.post("/fight", data=json.dumps(data))
    assert response.status_code == 401


def test_fight_without_winner(
    db_session, client, normal_user_token_headers, create_default_characters
):
    """
    Check fights where there is no winner
    """
    data = fight_without_winner()
    response = client.post(
        "/fight", data=json.dumps(data), headers=normal_user_token_headers
    )
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)
    assert len(response_data) == 3
    fights = list_fights(db_session)
    assert fights[-1].winner == "No hay ganador"


def test_fight_without_blows(
    client, normal_user_token_headers, create_default_characters
):
    """
    Check fights where there is no blows, the lenght of story is 1 (only the final comment)
    """
    data = fight_without_blows()
    response = client.post(
        "/fight", data=json.dumps(data), headers=normal_user_token_headers
    )
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)
    assert len(response_data) == 1


def test_fight_tonyn_wins(
    db_session, client, normal_user_token_headers, create_default_characters
):
    """
    Check fights where tonyn wins
    """
    data = fight_tonyn_wins()
    response = client.post(
        "/fight", data=json.dumps(data), headers=normal_user_token_headers
    )
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)
    assert len(response_data) == 8
    assert "Tonyn" in response_data[-2:][0]
    fights = list_fights(db_session)
    assert fights[-1].winner == "Tonyn Stallone"


def test_fight_arnaldor_wins(
    db_session, client, normal_user_token_headers, create_default_characters
):
    """
    Check fights where arnaldor wins
    """
    data = fight_arnaldor_wins()
    response = client.post(
        "/fight", data=json.dumps(data), headers=normal_user_token_headers
    )
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)
    assert len(response_data) == 7
    assert "Arnaldor" in response_data[-2:][0]
    fights = list_fights(db_session)
    assert fights[-1].winner == "Arnaldor Shuatseneguer"


def test_fight_big_brother_starts(
    client, normal_user_token_headers, create_default_characters
):
    """
    Check fights where the older brother starts because there is a tie in the number of movements and blows
    """
    data = fight_big_brother_starts()
    response = client.post(
        "/fight", data=json.dumps(data), headers=normal_user_token_headers
    )
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)
    assert "Tonyn" in response_data[0]


def test_fight_starts_less_button_combo_has(
    client, normal_user_token_headers, create_default_characters
):
    """
    Check fights where the one with the least combination of buttons starts
    """
    data = fight_starts_less_button_combo_has()
    response = client.post(
        "/fight", data=json.dumps(data), headers=normal_user_token_headers
    )
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)
    assert "Arnaldor" in response_data[0]


def test_fight_starts_less_movements_has(
    client, normal_user_token_headers, create_default_characters
):
    """
    Check fights where the one with the fewest moves starts
    """
    data = fight_starts_less_movements_has()
    response = client.post(
        "/fight", data=json.dumps(data), headers=normal_user_token_headers
    )
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)
    assert "Arnaldor" in response_data[0]


def test_fight_starts_less_hits_has(
    client, normal_user_token_headers, create_default_characters
):
    """
    Check fights where the one with the fewest hits starts
    """
    data = fight_starts_less_hits_has()
    response = client.post(
        "/fight", data=json.dumps(data), headers=normal_user_token_headers
    )
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)
    assert "Tonyn" in response_data[0]


def test_fight_very_large(client, normal_user_token_headers, create_default_characters):
    """
    Check very long fights
    """
    data = fight_very_large()
    response = client.post(
        "/fight", data=json.dumps(data), headers=normal_user_token_headers
    )
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)
    assert len(response_data) == 31


def test_fight_invalid_movement(
    client, normal_user_token_headers, create_default_characters
):
    """
    Check fight with invalid movment, api return bad request
    """
    data = fight_invalid_movement()
    response = client.post(
        "/fight", data=json.dumps(data), headers=normal_user_token_headers
    )
    assert response.status_code == 422


def test_fight_invalid_hit(
    client, normal_user_token_headers, create_default_characters
):
    """
    Check fight with invalid hit, api return bad request
    """
    data = fight_invalid_hit()
    response = client.post(
        "/fight", data=json.dumps(data), headers=normal_user_token_headers
    )
    assert response.status_code == 422
