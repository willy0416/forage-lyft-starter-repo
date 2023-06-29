from datetime import date

from battery.types.nubbin import NubbinBattery
from battery.types.spindler import SpindlerBattery
from car.car import Car
from engine.types.capulet import CapuletEngine
from engine.types.sternman import SternmanEngine
from engine.types.willoughby import WilloughbyEngine


class CarFactory:
    @staticmethod
    def create_calliope(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        return Car(
            CapuletEngine(last_service_mileage, current_mileage),
            SpindlerBattery(last_service_date, current_date),
        )

    @staticmethod
    def create_glissade(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        return Car(
            WilloughbyEngine(last_service_mileage, current_mileage),
            SpindlerBattery(last_service_date, current_date),
        )

    @staticmethod
    def create_palindrome(
        current_date: date, last_service_date: date, warning_light_on: bool
    ) -> Car:
        return Car(
            SternmanEngine(warning_light_on),
            SpindlerBattery(last_service_date, current_date),
        )

    @staticmethod
    def create_rorschach(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        return Car(
            WilloughbyEngine(last_service_mileage, current_mileage),
            NubbinBattery(last_service_date, current_date),
        )

    @staticmethod
    def create_thovex(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        return Car(
            CapuletEngine(last_service_mileage, current_mileage),
            NubbinBattery(last_service_date, current_date),
        )