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
                            VEGETABLES)

logging.basicConfig(
    filename="../aigrisculteurs.log",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)-8s] %(filename)20s(%(lineno)3s):%(funcName)-20s :: %(message)s",  # noqa: E501
    datefmt="%m/%d/%Y %H:%M:%S")


class Aigrisculteurs:
    fr_vegetable_list = ["TOMATE", "PATATE", "OIGNON", "COURGETTE", "POIREAU"]
    en_vegetable_list = ["TOMATO", "POTATO", "ONION", "ZUCCHINI", "LEEK"]
    def __init__(self: "Aigrisculteurs"):
        logging.debug('Started')
        self.game_data = None
        self.my_farm = None
        self.day = None
        self.aigrisculteurs_commands: list[str] = []
        self.actual_number_of_workers = 0
        self.actual_number_of_tractors = 0
        self.worker_daily_task = {}
        self.number_of_fields = 0
        self.list_of_fiels = []
        self.tractor_data = []  # {tractor_id]{worker:worker_id,position:FIELD_ID or FACTORY_STOCK, destination:FIELD_ID or FACTORY_STOCK or None if not used
        self.testing = False

    def get_my_farm_json(self, my_farm_name="aigrisculteurs"):

        for farm in self.game_data["farms"]:
            if farm["name"] == my_farm_name:
                self.my_farm = farm
                break
        else:
            # print("error")
            raise ValueError(f"My farm is not found ({self.username})")

    def run(self, game_data, testing=False):
        self.testing = testing
        try:
            self.game_data = game_data
            self.get_my_farm_json()
            self.day = self.game_data["day"]

            if self.day == 0:
                # self.new_day()
                self.do_bank_loan(120_000)
                self.buy_fields(5)
                self.buy_tractors(4)
                self.hiring_workers(37)
                self.sendTO(start=1, length=33, place=1)
                # self.send_group_to_place(workers_id_start = 1 , workers_id_length=33, place=1)

            elif self.day == 1:
                # self.new_day()
                self.sendTO(start=1, length=33, place=2)
                # self.send_group_to_place(workers_id_start = 1 , workers_id_length=33, place=2)
                self.send_worker_to_place(worker_id=34, place=FACTORY_STOCK, tractor_id=1, field_to_collect=1)

            elif self.day == 2:
                # self.new_day()
                self.worker_daily_task_new_day()
                self.sendTO(start=12, length=22, place=3)
                # self.send_group_to_place(workers_id_start = 12 , workers_id_length=22, place=3)
                self.send_worker_to_place(worker_id=35, place=FACTORY_STOCK, tractor_id=2, field_to_collect=2)

            elif self.day == 3:
                # self.new_day()
                self.sendTO(start=12, length=22, place=4)
                # self.send_group_to_place(workers_id_start = 12 , workers_id_length=22, place=4)
                self.send_worker_to_place(worker_id=36, place=FACTORY_STOCK, tractor_id=3, field_to_collect=3)
            
            elif self.day == 4:
                # self.new_day()
                self.sendTO(start=1, length=11, place=2)
                self.sendTO(start=23, length=11, place=5)
                # self.send_group_to_place(workers_id_start = 1 , workers_id_length=11, place=2)
                # self.send_group_to_place(workers_id_start = 23 , workers_id_length=11, place=5)


            elif self.day == 5:
                # self.new_day()
                self.sendTO(start=1, length=11, place=1)
                self.sendTO(start=12, length=11, place=3)
                self.send_worker_to_place(worker_id=35, place=FACTORY_STOCK, tractor_id=2, field_to_collect=2)
                self.send_worker_to_place(worker_id=36, place=FACTORY_STOCK, tractor_id=3, field_to_collect=5)
                self.send_worker_to_place(worker_id=37, place=FACTORY_STOCK, tractor_id=4, field_to_collect=4)

            if self.my_farm['blocked']==False:
                if self.day > 5 and self.day%2==True :
                    # self.new_day()
                    self.update_tractor_position()
                    # self.update_tractor_position()
                    self.sendTO(start=1, length=11, place=2)
                    self.sendTO(start=12, length=11, place=4)

                elif self.day > 5 and self.day%2==False :
                    # self.new_day()
                    self.update_tractor_position()
                    self.send_worker_to_place(worker_id=35, place=FACTORY_STOCK, tractor_id=2, field_to_collect=4)

                    self.sendTO(start=1, length=11, place=1)
                    self.sendTO(start=12, length=11, place=3)

            self.new_day()
            if testing is True:
                self.add_command("10 STOCKER 5 1")
                raise Exception("Test exception")
            return "Day went successfully"
        except Exception:
            # logging.exception("Oups")
            return "Day crashed"

    def new_day(self):
        self.worker_daily_task_new_day()
        self.update_tractor_position()
        logging.info(f"--DAY {self.game_data['day']}--{self.game_data}")

    def buy_fields(self, n_fields_to_buy):
        if (n_fields_to_buy > MAXIMUM_FIELDS_NUMBER) or \
                (self.number_of_fields + n_fields_to_buy
                    > MAXIMUM_FIELDS_NUMBER):
            n_fields_to_buy = MAXIMUM_FIELDS_NUMBER - self.number_of_fields

        while n_fields_to_buy >= 1:
            self.add_command("0 ACHETER_CHAMP")
            self.my_farm[FIELDS][n_fields_to_buy-1]['bought'] = True
            n_fields_to_buy -= 1
            self.number_of_fields += 1

    def buy_tractors(self, number_of_tractors_to_buy):
        while (number_of_tractors_to_buy):
            self.actual_number_of_tractors += 1 # Ignoring first list item for easy management
            self.tractor_data.insert(self.actual_number_of_tractors, {'worker': None, LOCATION: FARM, 'destination':'None'})
            logging.debug(f"TRACTOR DATA : {self.tractor_data}")
            self.add_command("0 ACHETER_TRACTEUR")
            number_of_tractors_to_buy -= 1
            
    def do_bank_loan(self, money):
        self.add_command(f"0 EMPRUNTER {money}")

    def get_vegetables_stock(self):
        vegatable_count = {}
        for vegatable, count in self.my_farm[FACTORY_SOUPE[0]][STOCK].items():
            logging.debug(f'Vegetable count : {vegatable} : {int(count)}')
            vegatable_count[vegatable] = int(count)
        
        for field in self.my_farm[FIELDS]:

            en_vegetable = field[CONTENT]
            if en_vegetable in self.en_vegetable_list:
                vegatable_count[en_vegetable] += 2000
            logging.debug(f'Field content count : {field}')
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
        if 1<= field_id <=5:
            bought = self.my_farm[FIELDS][field_id - 1].get('bought')
            if self.my_farm[FIELDS][field_id - 1].get(CONTENT) != 'NONE' and bought:

                return True
                
            else:
                return False
        else:
            raise ValueError(f"Field not in range 1 -5 : {field_id}")

    def check_if_field_need_water(self, field_id):
        if 1<= field_id <=5:
            need_water = self.my_farm[FIELDS][field_id - 1].get(NEEDED_WATER) > 0
            if need_water and self.check_if_field_sown(field_id):
                return True
            else:
                return False
        else:
            raise ValueError(f"Field not in range 1 -5 : {field_id}")

    def check_if_field_collectable(self, field_id):
        is_bought = self.my_farm[FIELDS][field_id - 1].get('bought')
        # logging.warning(f"FIELD {field_id} not collectable. water status : {self.my_farm[FIELDS][field_id][NEEDED_WATER]}")

        if(self.check_if_field_sown(field_id) and self.check_if_field_need_water(field_id) is False) and is_bought is True:  # noqa: E501
            return True
        else:
            logging.warning(f"FIELD {field_id} not collectable. water status : {self.my_farm[FIELDS][field_id][NEEDED_WATER]}")
            return False

    # place can be FACTORY_SOUPE or a field ID
    def check_worker_availability(self, worker_id):
        logging.debug(f"WORKER{worker_id} DAILY TASK VALUE : {self.worker_daily_task[f'worker{worker_id}']}")  # noqa: E501
        worker_availability = self.worker_daily_task.get(f'worker{worker_id}') == "None"  # noqa: E501

        if worker_availability and worker_id <= self.actual_number_of_workers:
            return True
        else:
            logging.warning(f"Prevented {worker_id} from doing multiple tasks : {self.worker_daily_task[f'worker{worker_id}']}")  # noqa: E501
            return False

    def send_worker_to_place(self, worker_id, place, tractor_id=None, field_to_collect=None):   # noqa: E501
        # if 34 <= worker_id <= 37:
        # logging.warning(f"WORKER {worker_id} ASKED TO {place} COLLECT ? {field_to_collect}")

        if place == FACTORY_SOUPE:
            self.worker_creating_soup_at_FACTORY_SOUPE(worker_id)
            logging.debug(f"WORKER STATUS: worker{worker_id} went SOUPE")
        elif place == FACTORY_STOCK:
            logging.warning(f"WORKER {worker_id} ASKED TO {place} COLLECT ? {field_to_collect}")
            self.store_with_tractor(worker_id, tractor_id, field_to_collect)

            
        elif 1 <= int(place) <= 5:
            logging.warning(f"WORKER {worker_id} : IS FIELD{int(place)} SOWN? {self.check_if_field_sown(int(place))}")
            if self.check_if_field_sown(int(place)):
                self.water_field(worker_id, int(place))
                logging.debug(f"WORKER STATUS: worker{worker_id} watered field{place}")
            else:
                logging.debug(f"WORKER STATUS: worker{worker_id} seeded {self.get_less_stocked_vegetable()} on field{place}")
                self.seed_less_stocked_vegetable(worker_id, int(place))

        else:
            logging.error("Unknown place")

    def sendTO(self,start,length,place):
        for i in range(start,start+length):
            self.send_worker_to_place(worker_id=i, place=place)

    def send_group_to_place(self,workers_id_start, workers_id_length, place):
        for worker in range (workers_id_start, workers_id_start + workers_id_length):
            logging.warning(f"WORKER {worker} ASKED TO {place}")
            self.send_worker_to_place(worker, place)

    def seed_less_stocked_vegetable(self, worker_id, field_id):
        less_stocked_vegetables = self.get_less_stocked_vegetable()

        key_list=list(VEGETABLES.keys())
        val_list=list(VEGETABLES.values())
        ind=val_list.index(less_stocked_vegetables)
        en_less_vegetable=key_list[ind]
        # logging.warning(f"LESS STOCKED VEGETABLE VALUE : {self.my_farm[FACTORY_SOUPE[0]][STOCK][en_less_vegetable]}")
        # self.my_farm[FACTORY_SOUPE[0]][STOCK][en_less_vegetable] += 2000
        self.worker_sow_vegetable_at_field(worker_id, less_stocked_vegetables, field_id)    # noqa: E501

    def worker_sow_vegetable_at_field(self, worker_id, vegetable, field_id):
        worker_available = self.check_worker_availability(worker_id) is True
        if worker_available:
            if vegetable in self.fr_vegetable_list:
                self.add_command(f"{worker_id} SEMER {vegetable} {field_id}")
                en_vegetable = None
                for en_vegetables in VEGETABLES.values():
                    if en_vegetables == vegetable:
                        en_less_vegetable = VEGETABLES.get(vegetable)
                                
                self.my_farm[FIELDS][field_id - 1][CONTENT] = en_vegetables
                # logging.error(f"{field_id} has {self.my_farm[FIELDS][field_id - 1][CONTENT]} sown")
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
                    logging.debug(f"TRACTOR : {tractor_id} with worker{worker_id}")
                    if self.tractor_data[tractor_id - 1].get(WORKER) == worker_id or self.tractor_data[tractor_id - 1].get(WORKER) == None:
                        logging.warning(f"WORKER {worker_id} STORED {field_id} WITH {tractor_id}")
                        self.tractor_data[tractor_id - 1][DESTINATION] = FACTORY_STOCK[1]
                        self.tractor_data[tractor_id - 1][WORKER] = worker_id
                        self.worker_daily_task[f"worker{worker_id}"] = "STOCKER"
                        self.add_command(f"{worker_id} STOCKER {field_id} {tractor_id}")
                else:
                    logging.warning(f"FIELD {field_id} not collectable")
            else:
                logging.warning(f"TRACTOR {tractor_id} not available")
        else:
            logging.warning(f"WORKER {worker_id} not available")


    def check_if_tractor_available(self,tractor_id):
        logging.debug(f"TRACTOR COUNT : {self.actual_number_of_tractors}, TRACTOR ID : {tractor_id}")
        if tractor_id <= self.actual_number_of_tractors:
            if self.tractor_data[tractor_id - 1][DESTINATION] == 'None':
                return True
        else:
            logging.warning(f"TRACTOR {tractor_id - 1} is below TRACTOR_NUMBER : {self.actual_number_of_tractors}")
            return False

    def update_tractor_position(self):
        for tractor in range (1,self.actual_number_of_tractors+1):
            position = self.my_farm[TRACTORS][tractor][LOCATION]
            self.tractor_data[tractor][LOCATION] = position
            logging.warning(f'TRACTOR {tractor} : LOCATION: {position} DESTINATION : {self.tractor_data[tractor][DESTINATION]}')
            if position == self.tractor_data[tractor][DESTINATION]:
                self.tractor_data[tractor][DESTINATION]='None'
            logging.warning(f'TRACTOR {tractor} : LOCATION: {position} DESTINATION : {self.tractor_data[tractor][DESTINATION]}')

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

    def add_command(self, command: str) -> None:
        self.aigrisculteurs_commands.append(command)
