def fight_without_winner():
    return {
        "player1": {"movimientos": ["S"], "golpes": ["P"]},
        "player2": {"movimientos": ["D"], "golpes": ["K"]},
    }


def fight_without_blows():
    return {
        "player1": {"movimientos": [], "golpes": []},
        "player2": {"movimientos": [], "golpes": []},
    }


def fight_tonyn_wins():
    return {
        "player1": {
            "movimientos": ["SDD", "DSD", "SA", "DSD"],
            "golpes": ["K", "P", "K", "P"],
        },
        "player2": {
            "movimientos": ["DSD", "WSAW", "ASA", "", "ASA", "SA"],
            "golpes": ["P", "K", "K", "K", "P", "k"],
        },
    }


def fight_arnaldor_wins():
    return {
        "player1": {
            "movimientos": ["D", "DSD", "S", "DSD", "SD"],
            "golpes": ["K", "P", "", "K", "P"],
        },
        "player2": {
            "movimientos": ["SA", "SA", "SA", "ASA", "SA"],
            "golpes": ["K", "", "K", "P", "P"],
        },
    }


def fight_big_brother_starts():
    return {
        "player1": {"movimientos": ["D", "S", ""], "golpes": ["K", "", "P"]},
        "player2": {"movimientos": ["S", "", "A"], "golpes": ["", "K", "K"]},
    }


def fight_starts_less_button_combo_has():
    return {
        "player1": {"movimientos": ["DWA", "SD", "AS"], "golpes": ["K", "", "P"]},
        "player2": {"movimientos": ["S", "", "A"], "golpes": ["P", "K", "K"]},
    }


def fight_starts_less_movements_has():
    return {
        "player1": {"movimientos": ["D", "SD", "A"], "golpes": ["K", "", "P"]},
        "player2": {"movimientos": ["S", "W", "A"], "golpes": ["P", "K", "K"]},
    }


def fight_starts_less_hits_has():
    return {
        "player1": {"movimientos": ["A", "S", ""], "golpes": ["K", "", "P"]},
        "player2": {"movimientos": ["S", "", "A"], "golpes": ["P", "K", "K"]},
    }


def fight_invalid_hit():
    return {
        "player1": {"movimientos": ["A", "S", ""], "golpes": ["Z", "", "P"]},
        "player2": {"movimientos": ["S", "", "A"], "golpes": ["P", "K", "K"]},
    }


def fight_invalid_movement():
    return {
        "player1": {"movimientos": ["A", "H", ""], "golpes": ["K", "", "P"]},
        "player2": {"movimientos": ["S", "", "A"], "golpes": ["P", "K", "K"]},
    }


def fight_very_large():
    return {
        "player1": {
            "movimientos": [
                "A",
                "S",
                "",
                "A",
                "S",
                "",
                "A",
                "S",
                "",
                "A",
                "S",
                "",
                "A",
                "S",
                "",
            ],
            "golpes": ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        },
        "player2": {
            "movimientos": [
                "S",
                "",
                "A",
                "S",
                "",
                "A",
                "S",
                "",
                "A",
                "S",
                "",
                "A",
                "S",
                "",
                "A",
            ],
            "golpes": ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        },
    }
