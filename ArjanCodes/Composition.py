import abc
from abc import ABC
from dataclasses import dataclass
from typing import Optional



@dataclass
class Comission(ABC):
    """ Representa uma comissão """

    @abc.abstractmethod
    def get_payment(self) -> float:
        """ Computa a comissão a ser paga"""


@dataclass
class ContractComission(Comission):
    """ Representa uma comissão """

    comission: float = 100
    contracts_landed: float = 0

    def get_payment(self) -> float:
        """ Computa a comissão a ser paga"""
        return self.comission * self.contracts_landed


@dataclass
class Contract(ABC):
    """ Representa um contrato e seu pagamento a um empregado particular"""

    @abc.abstractmethod
    def get_payment(self) -> float:
        """ Computa o contrado a ser pago """


@dataclass
class HourlyContract(Contract):
    """ Type Contract que é pago baseado em número de horas trabalhado """

    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def get_payment(self) -> float:
        return(
            self.pay_rate * self.hours_worked
            + self.employer_cost
        )


@dataclass
class SalariedContract(Contract):
    """ Type Contract que é pago baseado em número de horas trabalhado """

    monthly_salary: float = 0
    percentage: float = 1

    def get_payment(self) -> float:
        return self.monthly_salary * self.percentage


@dataclass
class FreelancerContract(Contract):
    """ Contrat type que é pago baseado na base do freelancer """

    pay_rate: float = 0
    hours_worked: int = 0
    vat_number: str = ""

    def get_payment(self) -> float:
        """ Computa o pagamento do contrato Freelancer"""
        return self.pay_rate * self.hours_worked


@dataclass
class Employee(ABC):
    """ Representa um empregado"""
    name: str
    id: int
    contract: Contract
    comission: Optional[Comission] = None


    def compute_pay(self) -> float:
        """ Computa quanto o empregado será pago"""
        payout = self.contract.get_payment()
        if self.comission is not None:
            payout += self.comission.get_payment()
        return payout


@dataclass
class HourlyEmployee(Employee):
    pass

@dataclass
class SalariedEmployee(Employee):
    pass


@dataclass
class FreelancerEmployee(Employee):
    pass


def main() -> None:
    """ Main Function """

    henry_contract = HourlyContract(pay_rate=50, hours_worked=100)
    henry = Employee(name='Henry', id=123456, contract=henry_contract)
    print(
        f'{henry.name}, worked for {henry_contract.hours_worked} hours and earned ${henry.compute_pay()}'
    )
    """ TypeError: Can't instantiate abstract class Employee with abstract method pay """

    sarah_contract = SalariedContract(monthly_salary=5000)
    sarah_commission = ContractComission(contracts_landed=10)
    sarah_employee = Employee(
        name="Sarah", id=47832, contract=sarah_contract, comission=sarah_commission
    )
    print(
        f"{sarah_employee.name} landed {sarah_commission.contracts_landed} contracts and earned ${sarah_employee.compute_pay()}"
    )

main()
