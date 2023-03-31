import logging


from src.constants import (
                            MAXIMUM_FIELDS_NUMBER,
                            # WORKERS,
                            # LOCATION,
                            FIELDS,
                            NEEDED_WATER,
                            STOCK,
                            FACTORY_SOUPE,
                            FACTORY_STOCK,
                            CONTENT,
                            # POTATO,
                            # LEEK,
                            # TOMATO,
                            # ONION,
                            # ZUCCHINI,
                            VEGETABLES)

logging.basicConfig(
    filename="../aigrisculteurs.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)-8s] %(filename)20s(%(lineno)3s):%(funcName)-20s :: %(message)s",  # noqa: E501
    datefmt="%m/%d/%Y %H:%M:%S")


class Aigrisculteurs:
    vegetable_list = ["TOMATE", "PATATE", "OIGNON", "COURGETTE", "POIREAU"]

    def __init__(self: "Aigrisculteurs"):
        logging.debug('Started')
        self.game_data = None
        self.my_farm = None
        self.aigrisculteurs_commands: list[str] = []
        self.actual_number_of_workers = 0
        self.actual_number_of_tractors = 0
        self.worker_daily_task = {}
        self.number_of_fields = 0
        self.list_of_fiels = []

    def get_my_farm_json(self, my_farm_name="aigrisculteurs"):

        for farm in self.game_data["farms"]:
            if farm["name"] == my_farm_name:
                self.my_farm = farm
                break
        else:
            print("error")
            raise ValueError(f"My farm is not found ({self.username})")

    def run(self, game_data, testing=False):
        try:
            self.game_data = game_data
            self.get_my_farm_json()

            if self.game_data["day"] == 0:
                self.do_bank_loan(100000)
                self.buy_fields(5)
                self.buy_tractors(4)
                self.hiring_workers(37)

            #     self.worker_sow_vegetable_at_field(1, TOMATO[1], 1)
            #     self.worker_sow_vegetable_at_field(2, POTATO[1], 2)
            #     self.worker_sow_vegetable_at_field(3, LEEK[1], 3)
            #     self.worker_sow_vegetable_at_field(4, ZUCCHINI[1], 4)
            #     self.worker_sow_vegetable_at_field(5, ONION[1], 5)

            # if self.game_data["day"] > 7:
            #     self.buy_tactors(10)
            #     for field_id in range(1, MAXIMUM_FIELDS_NUMBER + 1):
            #         logging.debug(field_id)
            #         self.field_need_water(field_id)

            # if self.game_data["day"] == 20:
            #     # {OUVRIER} STOCKER {CHAMP} {TRACTEUR}
            #     self.add_command("10 STOCKER 5 1")

            # if self.game_data["day"] == 30:
            #     # {OUVRIER} STOCKER {CHAMP} {TRACTEUR}
            #     self.add_command("10 STOCKER 3 1")

            # # self.worker_daily_task_new_day()
            if testing is True:
                self.add_command("10 STOCKER 5 1")
                raise Exception("Test exception")
            return "Day went successfully"
        except Exception:
            return "Day crashed"
            logging.exception("Oups")

    def buy_fields(self, n_fields_to_buy):
        if (n_fields_to_buy > MAXIMUM_FIELDS_NUMBER) or \
                (self.number_of_fields + n_fields_to_buy
                    > MAXIMUM_FIELDS_NUMBER):
            n_fields_to_buy = MAXIMUM_FIELDS_NUMBER - self.number_of_fields

        while n_fields_to_buy >= 1:
            self.add_command("0 ACHETER_CHAMP")
            n_fields_to_buy -= 1
            self.number_of_fields += 1

    def buy_tractors(self, number_of_tractors_to_buy):
        while (number_of_tractors_to_buy):
            self.add_command("0 ACHETER_TRACTEUR")
            self.actual_number_of_tractors += 1
            number_of_tractors_to_buy -= 1

    def do_bank_loan(self, money):
        self.add_command(f"0 EMPRUNTER {money}")

    def get_vegetables_stock(self):
        vegatable_count = {}
        for vegatable, count in self.my_farm[FACTORY_SOUPE[0]][STOCK].items():
            logging.debug(f'Vegetable count : {vegatable} : {int(count)}')
            vegatable_count[vegatable] = int(count)
        return vegatable_count

    def get_less_stocked_vegetable(self):
        less_vegetables = min(self.get_vegetables_stock(), key=self.get_vegetables_stock().get)  # noqa: E501
        logging.debug(f"Less stocked vegetables {less_vegetables}")
        fr_less_vegetable = None
        for fr_vegetables in VEGETABLES.keys():
            if fr_vegetables == less_vegetables:
                fr_less_vegetable = VEGETABLES[fr_vegetables]
        return fr_less_vegetable

    def check_if_field_sown(self, field_id):
        bought = self.my_farm[FIELDS][field_id - 1]['bought']
        logging.debug(f"Bought state : {bought}")
        logging.debug(f"Field ID : {field_id - 1}")
        if self.my_farm[FIELDS][field_id - 1][CONTENT] != 'NONE' and bought:
            return True
        else:
            return False

    def check_if_field_need_water(self, field_id):
        need_water = self.my_farm[FIELDS][field_id - 1][NEEDED_WATER] > 0
        if need_water and self.check_if_field_sown(field_id):
            return True
        else:
            return False

    def check_if_field_collectable(self, field_id):
        if(self.check_if_field_sown(field_id) and self.check_if_field_need_water(field_id) is False):  # noqa: E501
            return True
        else:
            return False

    # place can be FACTORY_SOUPE or a field ID
    def check_worker_availability(self, worker_id):
        logging.debug(f"DAILY TASK VALUE : {self.worker_daily_task[f'worker{worker_id}']}")  # noqa: E501
        worker_availability = self.worker_daily_task.get(f'worker{worker_id}') == "None"  # noqa: E501

        if worker_availability and worker_id <= self.actual_number_of_workers:
            return True
        else:
            logging.debug(f"Prevented {worker_id} from doing multiple tasks : {self.worker_daily_task[f'worker{worker_id}']}")  # noqa: E501
            return False

    def send_worker_to_place(self, worker_id, place, tractor_id=None, field_to_collect=None):   # noqa: E501
        if place == FACTORY_SOUPE:
            self.worker_creating_soup_at_FACTORY_SOUPE(worker_id)
        elif place == FACTORY_STOCK:
            self.store_with_tractor(worker_id, tractor_id, field_to_collect)

        elif 1 <= int(place) <= 5:
            if self.check_if_field_sown(int(place)):
                self.water_field(worker_id, int(place))
            else:
                self.seed_less_stocked_vegetable(worker_id, int(place))
        else:
            logging.error("Unknown place")

    def seed_less_stocked_vegetable(self, worker_id, field_id):
        less_stocked_vegetables = self.get_less_stocked_vegetable()
        self.worker_sow_vegetable_at_field(worker_id, less_stocked_vegetables, field_id)    # noqa: E501

    def worker_sow_vegetable_at_field(self, worker_id, vegetable, field_id):
        worker_available = self.check_worker_availability(worker_id) is True

        if vegetable in self.vegetable_list and worker_available is True:
            self.add_command(f"{worker_id} SEMER {vegetable} {field_id}")
            self.worker_daily_task[f"worker{worker_id}"] = "SEMER"
        else:
            logging.error(f"{vegetable} not in vegetable list")

    def store_with_tractor(self, worker_id, tractor_id, field_id):
        worker_available = self.check_worker_availability(worker_id) is True
        tractor_available = tractor_id <= self.actual_number_of_tractors
        field_collectable = self.check_if_field_collectable(field_id)
        if worker_available and tractor_available and field_collectable:
            self.add_command(f"{worker_id} STOCKER {field_id} {tractor_id}")

    def worker_creating_soup_at_FACTORY_SOUPE(self, worker_id):
        if self.check_worker_availability(worker_id) is True:
            self.add_command(f"{worker_id} {FACTORY_SOUPE[1]}")
            self.worker_daily_task[f"worker{worker_id}"] = "CUISINER"

    def water_field(self, worker_id, field_id):
        if self.check_worker_availability(worker_id) is True:
            self.add_command(f"{worker_id} ARROSER {field_id}")
            # logging.debug(
            #     f"==> worker{worker_id} wattering field{field_id} !")
            self.worker_daily_task[f"worker{worker_id}"] = "ARROSER"

    def hiring_workers(self, numbort_of_workers_to_hire):
        for _ in range(numbort_of_workers_to_hire):
            self.add_command("0 EMPLOYER")
            self.actual_number_of_workers += 1
            self.worker_daily_task[f'worker{self.actual_number_of_workers}'] = "None"    # noqa: E501
            # logging.debug(self.worker_daily_task)

    def worker_daily_task_new_day(self, new_value="None"):
        for key in self.worker_daily_task:
            self.worker_daily_task[key] = new_value

    # def worker_daily_task_state(self) -> list[int]:
    #     workers_id_available = []
    #     for worker in range(1, self.actual_number_of_workers):
    #         if self.worker_daily_task.get(f'worker{worker}') == "None":
    #             logging.debug(f'worker{worker} ready to do his daily task !')
    #             workers_id_available.append(worker)
    #         elif self.worker_daily_task.get(f'worker{worker}') != "None":
    #             logging.debug(
    #                 f"/!\\ worker{worker} already done his daily task !")
    #     return workers_id_available

    def add_command(self, command: str) -> None:
        self.aigrisculteurs_commands.append(command)
