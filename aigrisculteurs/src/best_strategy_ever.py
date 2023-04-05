import logging

from src.constants import (
    MAXIMUM_FIELDS_NUMBER,
    WORKERS,
    WORKER,
    DESTINATION,
    LOCATION,
    FIELDS,
    FARM,
    NEEDED_WATER,
    STOCK,
    FACTORY_SOUPE,
    FACTORY_STOCK,
    CONTENT,
    TRACTORS,
    # POTATO,
    # LEEK,
    # TOMATO,
    # ONION,
    # ZUCCHINI,
    VEGETABLES,
)

logging.basicConfig(
    filename="../aigrisculteurs.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s \
    [%(levelname)-8s] \
    %(filename)20s(%(lineno)3s):%(funcName)-20s :: %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
)


class Aigrisculteurs:
    fr_vegetable_list = ["TOMATE", "PATATE", "OIGNON", "COURGETTE", "POIREAU"]
    en_vegetable_list = ["TOMATO", "POTATO", "ONION", "ZUCCHINI", "LEEK"]

    def __init__(self: "Aigrisculteurs"):
        logging.debug("Started")
        self.game_data = None
        self.my_farm = None
        self.day = None
        self.aigrisculteurs_commands: list[str] = []
        self.actual_number_of_workers = 0
        self.actual_number_of_tractors = 0
        self.worker_daily_task = {}
        self.number_of_fields = 0
        self.list_of_fiels = []
        self.tractor_data = (
            []
        )  # [tractor_id]{'worker':worker_id,'location':FIELD_ID or FACTORY_STOCK, destination:FIELD_ID or FACTORY_STOCK or None if not used}   # noqa: E501
        self.testing = False
        self.field_status = []
        self.day_bool = True

    def get_my_farm_json(self, my_farm_name="aigrisculteurs"):

        for farm in self.game_data["farms"]:
            if farm["name"] == my_farm_name:
                self.my_farm = farm
                # print(self.my_farm)
                break
        else:
            # print("error")
            raise ValueError(f"My farm is not found ({self.username})")

    def run(self, game_data, testing=False, should_crash=False):    # noqa: C901
        self.testing = testing
        try:
            self.game_data = game_data
            if testing is False:
                self.get_my_farm_json()
                self.day = self.game_data["day"]

            if self.day == 0:
                self.new_day()
                self.do_bank_loan(70_000)
                self.buy_fields(5)
                self.buy_tractors(4)
                self.hiring_workers(37)

                self.send_group_to_place(
                    workers_id_start=1, workers_id_length=33, place=1
                )

            elif self.day == 1:
                self.hiring_workers(8)

                self.new_day()
                self.send_group_to_place(
                    workers_id_start=1, workers_id_length=33, place=2
                )
                self.send_group_to_place(
                    workers_id_start=38, workers_id_length=8, place=FACTORY_SOUPE   # noqa: E501
                )
                self.send_worker_to_place(
                    field_to_collect=1, worker_id=36, tractor_id=3
                )

            elif self.day == 2:
                self.new_day()
                self.worker_daily_task_new_day()
                self.send_group_to_place(
                    workers_id_start=12, workers_id_length=22, place=3
                )
                self.send_worker_to_place(
                    field_to_collect=2, worker_id=37, tractor_id=4
                )

            elif self.day == 3:
                self.new_day()
                self.send_group_to_place(
                    workers_id_start=1, workers_id_length=11, place=1
                )
                self.send_group_to_place(
                    workers_id_start=12, workers_id_length=22, place=4
                )
                self.send_worker_to_place(
                    field_to_collect=3, worker_id=34, tractor_id=1
                )

            elif self.day == 4:
                self.new_day()
                self.send_group_to_place(
                    workers_id_start=1, workers_id_length=11, place=2
                )
                self.send_group_to_place(
                    workers_id_start=12, workers_id_length=11, place=3
                )
                self.send_group_to_place(
                    workers_id_start=23, workers_id_length=11, place=5
                )
                self.send_worker_to_place(
                    field_to_collect=1, worker_id=35, tractor_id=2
                )
                self.send_worker_to_place(field_to_collect=4, tractor_id=4)

            elif self.day == 5:
                self.new_day()

                self.send_group_to_place(
                    workers_id_start=12, workers_id_length=11, place=4
                )
                self.send_worker_to_place(field_to_collect=2, tractor_id=1)
                self.send_worker_to_place(field_to_collect=3, tractor_id=3)
                self.send_worker_to_place(field_to_collect=5, tractor_id=4)

            if self.day > 5 and self.day % 2 == 0:
                self.new_day()
                self.send_group_to_place(
                    workers_id_start=12, workers_id_length=11, place=3
                )
                self.send_group_to_place(
                    workers_id_start=23, workers_id_length=11, place=5
                )
                self.send_worker_to_place(field_to_collect=4, tractor_id=3)
                if self.day > 6 and self.day % 4 != 2:
                    self.send_group_to_place(
                        workers_id_start=1, workers_id_length=11, place=2
                    )
                    self.send_worker_to_place(field_to_collect=1, tractor_id=1)

            elif self.day > 5 and self.day % 2 != 0:
                self.new_day()
                self.send_group_to_place(
                    workers_id_start=12, workers_id_length=11, place=4
                )
                self.send_worker_to_place(field_to_collect=3, tractor_id=3)
                self.send_worker_to_place(field_to_collect=5, tractor_id=4)
                if self.day_bool is True:
                    self.send_group_to_place(
                        workers_id_start=1, workers_id_length=11, place=1
                    )
                    self.day_bool = False
                else:
                    self.send_worker_to_place(field_to_collect=2, tractor_id=2)
                    self.day_bool = True

            if self.actual_number_of_workers > 37 and self.day > 6:
                self.send_group_to_place(
                    workers_id_start=38, workers_id_length=8, place=FACTORY_SOUPE   # noqa: E501
                )

            if testing is True and should_crash is True:
                self.add_command("10 STOCKER 5 1")
                raise Exception("Test exception")
            return "Day went successfully"
        except Exception:
            logging.exception("Oups")
            return "Day crashed"

    def new_day(self):
        self.worker_daily_task_new_day()
        # self.update_tractors_position()

        logging.info(f"--DAY {self.game_data['day']}--{self.game_data}")

    def buy_fields(self, n_fields_to_buy):
        if (n_fields_to_buy > MAXIMUM_FIELDS_NUMBER) or (
            self.number_of_fields + n_fields_to_buy > MAXIMUM_FIELDS_NUMBER
        ):
            n_fields_to_buy = MAXIMUM_FIELDS_NUMBER - self.number_of_fields

        while n_fields_to_buy >= 1:
            self.add_command("0 ACHETER_CHAMP")
            self.my_farm[FIELDS][n_fields_to_buy - 1]["bought"] = True
            n_fields_to_buy -= 1
            self.number_of_fields += 1

    def buy_tractors(self, number_of_tractors_to_buy):
        while number_of_tractors_to_buy:
            self.actual_number_of_tractors += (
                1  # Ignoring first list item for easy management
            )
            self.tractor_data.append(
                {"worker": None, LOCATION: FARM, "destination": "None"}
            )
            self.my_farm[TRACTORS].append(
                {"location": "FARM", "id": self.actual_number_of_tractors}
            )
            logging.debug(f"TRACTOR DATA : {self.tractor_data}")
            self.add_command("0 ACHETER_TRACTEUR")
            number_of_tractors_to_buy -= 1

    def do_bank_loan(self, money):
        self.add_command(f"0 EMPRUNTER {money}")

    def get_vegetables_stock(self):
        vegatable_count = {}
        for vegatable, count in self.my_farm[FACTORY_SOUPE[0]][STOCK].items():
            logging.debug(f"Vegetable count : {vegatable} : {int(count)}")
            vegatable_count[vegatable] = int(count)

        for field in self.my_farm[FIELDS]:

            en_vegetable = field[CONTENT]
            if en_vegetable in self.en_vegetable_list:
                vegatable_count[en_vegetable] += 2000
            logging.debug(f"Field content count : {field}")
        return vegatable_count

    def get_less_stocked_vegetable(self):
        vegetable_stock = self.get_vegetables_stock()
        less_vegetables = min(vegetable_stock, key=vegetable_stock.get)  # noqa: E501
        logging.debug(f"Less stocked vegetables {less_vegetables}")
        fr_less_vegetable = None
        for fr_vegetables in VEGETABLES.keys():
            if fr_vegetables == less_vegetables:
                fr_less_vegetable = VEGETABLES[fr_vegetables]
        return fr_less_vegetable

    def check_if_field_sown(self, field_id):
        if 1 <= field_id <= 5:
            bought = self.my_farm[FIELDS][field_id - 1].get("bought")
            if self.my_farm[FIELDS][field_id - 1].get(CONTENT) != "NONE" and bought:    # noqa: E501

                return True

            else:
                return False
        else:
            raise ValueError(f"Field not in range 1 -5 : {field_id}")

    def check_if_field_need_water(self, field_id):
        if 1 <= field_id <= 5:
            need_water = self.my_farm[FIELDS][field_id - 1].get(NEEDED_WATER) > 0   # noqa: E501
            if need_water and self.check_if_field_sown(field_id):
                return True
            else:
                return False
        else:
            raise ValueError(f"Field not in range 1 -5 : {field_id}")

    def check_if_field_collectable(self, field_id):
        is_bought = self.my_farm[FIELDS][field_id - 1].get("bought")
        if (
            (
                self.check_if_field_sown(field_id)
                and self.check_if_field_need_water(field_id) is False
            )
            and is_bought is True
            and (
                self.my_farm[FIELDS][field_id - 1].get("already_collected") is False   # noqa: E501
                or ("already_collected")
                not in self.my_farm[FIELDS][field_id - 1].items()
            )
        ):
            return True
        else:
            logging.warning(
                f"FIELD {field_id} not collectable. water status : {self.my_farm[FIELDS][field_id][NEEDED_WATER]}"   # noqa: E501
            )
            return False

    # place can be FACTORY_SOUPE or a field ID
    def check_worker_availability(self, worker_id):
        if worker_id <= self.actual_number_of_workers:
            worker_availability = (
                self.worker_daily_task.get(f"worker{worker_id}") == "None"
            )  # noqa: E501
            if worker_availability:
                logging.debug(
                    f"WORKER{worker_id} DAILY TASK VALUE : {self.worker_daily_task[f'worker{worker_id}']}"   # noqa: E501
                )  # noqa: E501
                return True
            else:
                logging.warning(
                    f"Prevented {worker_id} from doing multiple tasks : {self.worker_daily_task[f'worker{worker_id}']}"   # noqa: E501
                )  # noqa: E501
                return False
        else:
            logging.warning(f"Worker {worker_id} not hired")  # noqa: E501

    def send_worker_to_place(
        self,
        place=FACTORY_STOCK,
        worker_id=None,
        tractor_id=None,
        field_to_collect=None,
    ):  # noqa: E501

        if tractor_id is not None and worker_id is None:
            if WORKER in self.tractor_data[tractor_id - 1]:
                worker_id = self.tractor_data[tractor_id - 1].get(WORKER)
                logging.debug(f"worker{worker_id} in tractor{tractor_id}")

        if place == FACTORY_SOUPE:
            self.worker_creating_soup_at_FACTORY_SOUPE(worker_id)
            logging.debug(f"WORKER STATUS: worker{worker_id} went SOUPE")
        elif place == FACTORY_STOCK:
            logging.debug(
                f"WORKER {worker_id} ASKED TO {place} COLLECT ? {field_to_collect}"   # noqa: E501
            )
            self.store_with_tractor(worker_id, tractor_id, field_to_collect)

        elif 1 <= int(place) <= 5:
            logging.debug(
                f"WORKER {worker_id} : IS FIELD{int(place)} SOWN? {self.check_if_field_sown(int(place))}"   # noqa: E501
            )
            if self.check_if_field_sown(int(place)):
                self.water_field(worker_id, int(place))
                logging.debug(f"WORKER STATUS: worker{worker_id} watered field{place}")   # noqa: E501
            else:
                logging.debug(
                    f"WORKER STATUS: worker{worker_id} seeded {self.get_less_stocked_vegetable()} on field{place}"   # noqa: E501
                )
                self.seed_less_stocked_vegetable(worker_id, int(place))

        else:
            logging.error("Unknown place")

    def send_group_to_place(self, workers_id_start, workers_id_length, place):
        for i in range(workers_id_start, workers_id_start + workers_id_length):
            logging.debug(f"WORKER {i} ASKED TO {place}")
            self.send_worker_to_place(worker_id=i, place=place)

    def seed_less_stocked_vegetable(self, worker_id, field_id):
        less_stocked_vegetables = self.get_less_stocked_vegetable()
        self.worker_sow_vegetable_at_field(
            worker_id, less_stocked_vegetables, field_id
        )  # noqa: E501

    def worker_sow_vegetable_at_field(self, worker_id, vegetable, field_id):
        worker_available = self.check_worker_availability(worker_id) is True
        if worker_available:
            if vegetable in self.fr_vegetable_list:
                self.add_command(f"{worker_id} SEMER {vegetable} {field_id}")
                for en_vegetables in VEGETABLES.values():
                    if en_vegetables == vegetable:
                        en_vegetables = VEGETABLES.get(vegetable)
                self.my_farm[FIELDS][field_id - 1][CONTENT] = en_vegetables
                self.worker_daily_task[f"worker{worker_id}"] = "SEMER"
            else:
                logging.error(f"{vegetable} not in vegetable list")

    def store_with_tractor(self, worker_id, tractor_id, field_id):
        worker_available = self.check_worker_availability(worker_id) is True
        tractor_available = self.check_if_tractor_available(tractor_id) is True
        field_collectable = self.check_if_field_collectable(field_id)
        if worker_available:
            if tractor_available:
                if field_collectable:
                    logging.debug(f"TRACTOR {tractor_id} with worker{worker_id}")   # noqa: E501
                    if (
                        self.tractor_data[tractor_id - 1].get(WORKER) == worker_id   # noqa: E501
                        or self.tractor_data[tractor_id - 1].get(WORKER) is None   # noqa: E501
                    ):
                        logging.debug(
                            f"WORKER {worker_id} STORED {field_id} WITH {tractor_id}"   # noqa: E501
                        )
                        self.tractor_data[tractor_id - 1][DESTINATION] = FACTORY_STOCK[   # noqa: E501
                            1
                        ]
                        self.tractor_data[tractor_id - 1][WORKER] = worker_id
                        self.my_farm[FIELDS][field_id - 1]["already_collected"] = True   # noqa: E501
                        self.my_farm[FIELDS][field_id - 1][CONTENT] = "NONE"

                        self.worker_daily_task[f"worker{worker_id}"] = "STOCKER"   # noqa: E501
                        self.add_command(f"{worker_id} STOCKER {field_id} {tractor_id}")   # noqa: E501
            else:
                logging.warning(f"TRACTOR {tractor_id} not available")

    def check_if_tractor_available(self, tractor_id):
        self.update_tractors_position()
        if tractor_id <= self.actual_number_of_tractors:
            if (
                self.tractor_data[tractor_id - 1][LOCATION] == FACTORY_STOCK[1]
                or self.tractor_data[tractor_id - 1][LOCATION] == FARM
            ):
                return True
        else:
            logging.warning(
                f"TRACTOR {tractor_id } is below TRACTOR_NUMBER : {self.actual_number_of_tractors}"   # noqa: E501
            )
            return False

    def update_tractors_position(self):
        # if self.day > 0:
        logging.debug(f"tractor_data : {self.tractor_data}")
        logging.debug(f"farm_tractor_data : {self.my_farm[TRACTORS]}")
        logging.debug(f"number_of_tractors : {self.actual_number_of_tractors}")
        for tractor in range(0, self.actual_number_of_tractors):
            position = self.my_farm[TRACTORS][tractor][LOCATION]
            self.tractor_data[tractor][LOCATION] = position

    def worker_creating_soup_at_FACTORY_SOUPE(self, worker_id):
        if self.check_worker_availability(worker_id) is True:
            self.add_command(f"{worker_id} {FACTORY_SOUPE[1]}")
            self.worker_daily_task[f"worker{worker_id}"] = "CUISINER"

    def water_field(self, worker_id, field_id):
        if self.check_worker_availability(worker_id) is True:
            self.add_command(f"{worker_id} ARROSER {field_id}")
            # logging.debug(
            #     f"==> worker{worker_id} wattering field{field_id} !")
            self.my_farm[FIELDS][field_id - 1][NEEDED_WATER] -= 1
            self.worker_daily_task[f"worker{worker_id}"] = "ARROSER"

    def hiring_workers(self, numbort_of_workers_to_hire):
        for _ in range(numbort_of_workers_to_hire):
            self.add_command("0 EMPLOYER")

            self.my_farm[WORKERS].insert(
                self.actual_number_of_workers,
                {
                    "id": self.actual_number_of_workers,
                    "location": "FARM",
                    "tractor": None,
                    "salary": 1000,
                },
            )
            self.actual_number_of_workers += 1
            self.worker_daily_task[
                f"worker{self.actual_number_of_workers}"
            ] = "None"  # noqa: E501
            # logging.debug(self.worker_daily_task)

    def worker_daily_task_new_day(self, new_value="None"):
        for key in self.worker_daily_task:
            self.worker_daily_task[key] = new_value

    def add_command(self, command: str) -> None:
        self.aigrisculteurs_commands.append(command)
