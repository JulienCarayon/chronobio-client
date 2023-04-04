import argparse
from typing import NoReturn

from chronobio.network.client import Client
from src.best_startegy_ever import Aigrisculteurs


class PlayerGameClient(Client):
    def __init__(
        self: "PlayerGameClient", server_addr: str, port: int, username: str
    ) -> None:
        super().__init__(server_addr, port, username, spectator=False)
        self._commands: list[str] = []
        self.aigrisculteurs = Aigrisculteurs()

    def run(self: "PlayerGameClient") -> NoReturn:
        while True:
            game_data = self.read_json()
            self.aigrisculteurs.run(game_data)
            # for farm in game_data["farms"]:
            #     if farm["name"] == self.username:
            #         my_farm = farm
            #         break
            # else:
            #     print("error")
            #     raise ValueError(f"My farm is not found ({self.username})")
            # print(my_farm)

            self.send_commands()

    def add_command(self: "PlayerGameClient", command: str) -> None:
        self._commands.append(command)

    def send_commands(self: "PlayerGameClient") -> None:
        data = {"commands": self.aigrisculteurs.aigrisculteurs_commands}
        print("sending", data)
        self.send_json(data)
        self.aigrisculteurs.aigrisculteurs_commands.clear()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Game client.")
    parser.add_argument(
        "-a",
        "--address",
        type=str,
        help="name of server on the network",
        default="localhost",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        help="location where server listens",
        default=16210,
    )
    parser.add_argument(
        "-u",
        "--username",
        type=str,
        help="name of the user",
        default="unknown",
        required=True,
    )
    args = parser.parse_args()

    client: PlayerGameClient = PlayerGameClient(
        args.address, args.port, args.username
    ).run()
