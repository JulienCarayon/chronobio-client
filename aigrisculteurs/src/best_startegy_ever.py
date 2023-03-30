import logging


from src.constants import MAXIMUM_FIELDS_NUMBER, LOCATION, FIELDS, NEEDED_WATER, WORKERS

logging.basicConfig(
    filename="../aigrisculteurs.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)-8s] %(filename)20s(%(lineno)3s):%(funcName)-20s :: %(message)s",  # noqa: E501
    datefmt="%m/%d/%Y %H:%M:%S")


class Aigrisculteurs:
    vegetable_list = ["TOMATE", "PATATE", "OIGNON", "COURGETTE", "POIREAU"]

    def __init__(self: "Aigrisculteurs"):
        logging.info('Started')
        self.game_data = None
        self.my_farm = None
        self.aigrisculteurs_commands: list[str] = []
        self.actual_number_of_workers = 0
        self.actual_number_of_tractors = 0
        self.worker_daily_task = {}
        self.number_of_fields = 0
        self.list_of_fiels = []

    def get_my_farm_json(self, my_farm_name="aigrisculteurs"):
        logging.info('get_my_farm_json')
        for farm in self.game_data["farms"]:
            if farm["name"] == my_farm_name:
                self.my_farm = farm
                break
            else:
                print("error")
                raise ValueError(f"My farm is not found ({self.username})")

    def run(self, game_data):
        logging.info('run')
        self.game_data = game_data
        self.get_my_farm_json()

        if self.game_data["day"] == 0:
            self.do_bank_loan(100000)
            self.buy_fields(5)
            self.buy_tactors(2)
            self.hiring_workers(24)
            self.worker_sow_vegetable_at_field(1, "TOMATE", 1)
            self.worker_sow_vegetable_at_field(2, "PATATE", 2)
            self.worker_sow_vegetable_at_field(3, "COURGETTE", 3)
            self.worker_sow_vegetable_at_field(4, "OIGNON", 4)
            self.worker_sow_vegetable_at_field(5, "POIREAU", 5)

        if self.game_data["day"] > 7:
            self.buy_tactors(10)
            for field_id in range(1, MAXIMUM_FIELDS_NUMBER + 1):
                logging.info(field_id)
                self.field_need_water(field_id)

        if self.game_data["day"] == 20:
            # {OUVRIER} STOCKER {CHAMP} {TRACTEUR}
            self.add_command("10 STOCKER 5 1")

        if self.game_data["day"] == 30:
            # {OUVRIER} STOCKER {CHAMP} {TRACTEUR}
            self.add_command("10 STOCKER 3 1")

        # self.worker_daily_task_new_day()

    def buy_fields(self, number_of_fields_to_buy):
        if (number_of_fields_to_buy > MAXIMUM_FIELDS_NUMBER) or \
                (self.number_of_fields + number_of_fields_to_buy
                    > MAXIMUM_FIELDS_NUMBER):
            number_of_fields_to_buy = MAXIMUM_FIELDS_NUMBER - self.number_of_fields

        while number_of_fields_to_buy >= 1:
            self.add_command("0 ACHETER_CHAMP")
            number_of_fields_to_buy -= 1
            self.number_of_fields += 1

    def buy_tactors(self, number_of_tractors_to_buy):
        while (number_of_tractors_to_buy):
            self.add_command("0 ACHETER_TRACTEUR")
            self.actual_number_of_tractors += 1
            number_of_tractors_to_buy -= 1

    def do_bank_loan(self, money):
        self.add_command(f"0 EMPRUNTER {money}")

    def hiring_workers(self, numbort_of_workers_to_hire):
        for _ in range(numbort_of_workers_to_hire):
            self.add_command("0 EMPLOYER")
            self.actual_number_of_workers += 1
            self.add_value_to_dict(
                f'worker{self.actual_number_of_workers}', "None", str())
            logging.info(self.worker_daily_task)

    def worker_daily_task_new_day(self, new_value="None"):
        for key in self.worker_daily_task:
            self.worker_daily_task[key] = new_value

    def worker_sow_vegetable_at_field(self, worker_id, vegetable, field_id):
        if vegetable in self.vegetable_list:
            self.add_command(f"{worker_id} SEMER {vegetable} {field_id}")

    def check_workers_number(self, actual_worker_number):
        return actual_worker_number < 10

    def worker_daily_task_state(self) -> list[int]:
        workers_id_available = []
        for worker in range(1, self.actual_number_of_workers):
            if self.worker_daily_task.get(f'worker{worker}') == "None":
                logging.info(f'worker{worker} ready to do his daily task !')
                workers_id_available.append(worker)
            elif self.worker_daily_task.get(f'worker{worker}') != "None":
                logging.info(
                    f"/!\\ worker{worker} already done his daily task !")
        return workers_id_available

    def field_need_water(self, field_id):
        workers_id_available = []
        logging.info(self.my_farm[FIELDS][field_id - 1])
        if self.my_farm[FIELDS][field_id - 1][NEEDED_WATER] != 0:
            workers_id_available = self.worker_daily_task_state()
            for worker_id in workers_id_available:
                if self.my_farm[WORKERS][worker_id - 1][LOCATION] == self.my_farm[FIELDS][field_id - 1][LOCATION]:  # noqa: E501
                    logging.info(
                        f"worker {self.my_farm[WORKERS][worker_id]['id']}  at  {self.my_farm[WORKERS][worker_id][LOCATION]}")   # noqa: E501
                    logging.info(
                        f"field : {self.my_farm[FIELDS][field_id - 1][LOCATION]}")
                    self.water_field(worker_id, field_id)
                    break

    def water_field(self, worker_id, field_id):
        self.add_command(f"{worker_id} ARROSER {field_id}")
        logging.info(
            f"==> worker{worker_id} wattering field{field_id} !")

    def worker_location_to_field(self):
        pass

    def add_value_to_dict(self, dict_key, dict_value, type_value):
        # dict_key = key - self.worker_daily_task = dict - dict_value = value - i = type value  # noqa: E501
        # si le dictionnaire 'self.worker_daily_task' contient la clé 'dict_key'    # noqa: E501
        # on récupère la valeur
        if dict_key in self.worker_daily_task:
            type_value = self.worker_daily_task[dict_key]

        # détermination du type de la valeur
        if isinstance(type_value, set):
            type_value.add(dict_value)
        elif isinstance(type_value, list):
            type_value.append(dict_value)
        elif isinstance(type_value, str):
            type_value += str(dict_value)
        elif isinstance(type_value, int):
            type_value += int(dict_value)
        elif isinstance(type_value, float):
            type_value += float(dict_value)

        # on met à jour l'objet 'type_value' pour la clé 'dict_key' dans le dictionnaire 'self.worker_daily_task' # noqa: E501
        self.worker_daily_task[dict_key] = type_value

    def add_command(self, command: str) -> None:
        self.aigrisculteurs_commands.append(command)
