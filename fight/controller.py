import random

from sqlalchemy.orm import Session

from sql_app.crud import create_fight
from sql_app.crud import get_character_by_name
from sql_app.crud import update_fight
from sql_app.models import Character
from sql_app.schemas import PlayerGame


class ControllerFight:
    comments = {
        "special": [
            "{attacker} conecta un {hit_name}",
            "{attacker} usa un {hit_name}",
            "{attacker} arremete contra {defender} con un {hit_name}",
        ],
        "common": [
            "{attacker} {movement} le da {hit_name} a {defender}",
            "{attacker} {movement} conecta {hit_name}",
            "{attacker} {movement} golpea con {hit_name}",
            "{attacker} {movement} le pega {hit_name} al pobre {defender}",
        ],
        "movement": ["{attacker} {movement}"],
        "final": [
            "{winner} gana derrotando a {loser}",
            "{winner} gana la pelea y aun le queda {energy} de energía",
            "{loser} es derrotado por {winner}",
        ],
        "zero tie": [
            "Empate entre {a} y {b}",
            "El resultado sin ganador es {a} tiene {e_a} y {b} queda con {e_b}",
        ],
    }

    hand_blows = ["un puñetazo", "un puño", "una trompada", "un castañazo"]
    legs_blows = ["un patadon", "una patada", "una patadaza", "un puntapié"]

    forward_movements = ["avanza", "se adelanta", "se mueve"]
    back_movements = ["retrocede", "recula", "se mueve"]
    up_movements = ["salta", "se eleva"]
    down_movements = ["se agacha", "se agazapa"]
    still_movements = ["se queda en el lugar"]

    def __init__(self, player1: PlayerGame, player2: PlayerGame, db: Session) -> None:
        self.db = db
        self.p1 = player1
        self.p2 = player2
        self.character1 = get_character_by_name(self.db, name="Tonyn")
        self.character2 = get_character_by_name(self.db, name="Arnaldor")
        self.energy_player1 = 6
        self.energy_player2 = 6
        self.turn_of = 1
        self.story = []

    def get_player(self, number: int) -> PlayerGame:
        """Get player attribute by number"""
        return getattr(self, f"p{number}")

    def get_character(self, number: int) -> Character:
        """Get character attribute by number"""
        return getattr(self, f"character{number}")

    def get_energy(self, number: int) -> int:
        """Get energy of character by number"""
        return getattr(self, f"energy_player{number}")

    def set_player(self, number: int, player: PlayerGame) -> None:
        """Set object player in attribute player by number"""
        return setattr(self, f"p{number}", player)

    def set_energy(self, number: int, energy: int) -> None:
        """Set object energy in attribute energy of character by number"""
        return setattr(self, f"energy_player{number}", energy)

    def get_opponent(self, number: int) -> int:
        """Get opponent_number by number"""
        return number % 2 + 1

    def next(self) -> None:
        """Increase turn_off attribute"""
        self.turn_of = self.get_opponent(self.turn_of)

    def count_movements(self, player: PlayerGame) -> int:
        """Count quantity of movements by player"""
        return sum(len(s) for s in player.movimientos)

    def count_hits(self, player: PlayerGame) -> int:
        """Count quantity of hits by player"""
        return sum(len(s) for s in player.golpes)

    def create_fight(self) -> None:
        """Inser into db a new fight object"""
        return create_fight(self.db, self.p1, self.p2)

    def update_fight(self, fight_id: int, winner: str) -> None:
        """Update in db a fight object with winner and story"""
        return update_fight(self.db, fight_id, self.story, winner)

    def is_without_hits(self) -> bool:
        """Check if fight can continue"""
        return len(self.p1.golpes) == 0 and len(self.p2.golpes) == 0

    def who_start(self):
        """Rerun which caracter start"""
        p1_movements_number = self.count_movements(self.p1)
        p1_hits_number = self.count_hits(self.p1)
        p2_movements_number = self.count_movements(self.p2)
        p2_hits_number = self.count_hits(self.p2)
        p1_all_commands_number = p1_movements_number + p1_hits_number
        p2_all_commands_number = p2_movements_number + p2_hits_number
        if p1_all_commands_number > p2_all_commands_number:
            self.turn_of = 2
        elif p1_all_commands_number < p2_all_commands_number:
            self.turn_of = 1
        elif p1_movements_number > p2_movements_number:
            self.turn_of = 2
        elif p1_movements_number < p2_movements_number:
            self.turn_of = 1
        elif p1_hits_number > p2_hits_number:
            self.turn_of = 2
        elif p1_hits_number < p2_hits_number:
            self.turn_of = 1

    def get_hit_name(self, hit: str) -> str:
        """Return blow name random"""
        hit_name = ""
        if hit == "P":
            hit_name = random.choice(self.hand_blows)
        elif hit == "K":
            hit_name = random.choice(self.legs_blows)
        return hit_name

    def get_movement_name(self, movement: str, c: Character) -> str:
        """Return movement name random"""
        movement_name = ""
        if movement == "W":
            movement_name = random.choice(self.up_movements)
        elif movement == "S":
            movement_name = random.choice(self.down_movements)
        elif (movement == "D" and c == self.character1) or (
            movement == "S" and c == self.character2
        ):
            movement_name = random.choice(self.forward_movements)
        elif (movement == "S" and c == self.character1) or (
            movement == "D" and c == self.character2
        ):
            movement_name = random.choice(self.back_movements)
        else:
            movement_name = random.choice(self.still_movements)
        return movement_name

    def get_blow(self, character: Character, movement: str, hit: str) -> int:
        """Return blow or movement in this turn"""
        damage = 0
        is_special_blow = False
        hit_name = self.get_hit_name(hit)
        movement_name = self.get_movement_name(movement[-1:], character)
        if len(hit) > 0:
            damage = 1
        for sp in character.get_superpowers(self.db):
            if movement.endswith(sp.sequence[:-1]) and hit == sp.sequence[-1]:
                damage = sp.damage
                hit_name = sp.name
                is_special_blow = True
                break
        return hit_name, movement_name, damage, is_special_blow

    def comment_turn_of_fight(
        self, hit_name: str, movement_name: str, is_special_blow: bool
    ) -> None:
        """Create and add new comment in story of fight by turn"""
        comment = ""
        if is_special_blow:
            comment = random.choice(self.comments["special"])
        elif hit_name:
            if movement_name:
                movement_name = random.choice([f"{movement_name} y", ""])
            comment = random.choice(self.comments["common"])
        else:
            comment = random.choice(self.comments["movement"])

        attacker = self.get_character(self.turn_of)
        opponent = self.get_opponent(self.turn_of)
        defender = self.get_character(opponent)

        comment = comment.format(
            hit_name=hit_name,
            movement=movement_name,
            attacker=attacker.name,
            defender=defender.name,
        )
        self.story.append(comment)

    def final_comment(self) -> str:
        """Create and add new comment in story of fight if that can't continue"""
        winner = 1
        loser = 2
        if self.energy_player2 > 0:
            winner = 2
            loser = 1
        c_winner = self.get_character(winner)
        c_loser = self.get_character(loser)
        energy_winner = self.get_energy(winner)

        winner_name = f"{c_winner.name} {c_winner.last_name}"
        if self.energy_player2 > 0 and self.energy_player1 > 0:
            energy_loser = self.get_energy(loser)
            comment = random.choice(self.comments["zero tie"])
            comment = comment.format(
                a=c_winner.name, b=c_loser.name, e_a=energy_winner, e_b=energy_loser
            )
            winner_name = "No hay ganador"
        else:
            comment = random.choice(self.comments["final"])
            comment = comment.format(
                winner=c_winner.name, loser=c_loser.name, energy=energy_winner
            )

        self.story.append(comment)
        return winner_name

    def run_turn(self):
        player = self.get_player(self.turn_of)
        character = self.get_character(self.turn_of)
        opponent = self.get_opponent(self.turn_of)
        opponents_energy = self.get_energy(opponent)
        try:
            movement = player.movimientos[0]
        except IndexError:
            movement = ""
        try:
            hit = player.golpes[0]
        except IndexError:
            hit = ""

        hit_name, movement_name, damage, is_special_blow = self.get_blow(
            character, movement, hit
        )
        self.comment_turn_of_fight(hit_name, movement_name, is_special_blow)

        player.movimientos = player.movimientos[1:]
        player.golpes = player.golpes[1:]
        self.set_player(self.turn_of, player)
        self.set_energy(opponent, opponents_energy - damage)

    def fight(self):
        """Create and realte new fight"""
        fight = self.create_fight()
        self.who_start()
        while (
            self.energy_player1 > 0
            and self.energy_player2 > 0
            and not self.is_without_hits()
        ):
            self.run_turn()
            self.next()
        winner = self.final_comment()
        self.update_fight(fight.id, winner)
