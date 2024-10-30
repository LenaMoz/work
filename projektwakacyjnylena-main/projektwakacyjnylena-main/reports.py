import json
from orders import OrderSystem
from finances import Finance

class ReportGenerator:
    def __init__(self, users):
        self.users = users
        self.order_system = OrderSystem()
        self.finance = Finance()

    def generate_user_report(self):
        report = "Raport Użytkowników:\n"
        report += "---------------------------------\n"
        for user in self.users:
            report += f"Użytkownik: {user['username']}, Rola: {user['role']}\n"
        report += "---------------------------------\n"
        return report

    def generate_order_report(self):
        report = "Raport Zamówień:\n"
        report += "---------------------------------\n"
        for order in self.order_system.orders:
            report += f"{order}\n"
        report += "---------------------------------\n"
        return report

    def generate_finance_report(self):
        report = "Raport Finansowy:\n"
        report += "---------------------------------\n"
        report += f"Saldo: {self.finance.balance} PLN\n"
        report += "---------------------------------\n"
        return report

    def generate_full_report(self):
        full_report = "Raport Firmy:\n"
        full_report += self.generate_user_report()
        full_report += self.generate_order_report()
        full_report += self.generate_finance_report()
        return full_report

    def save_report_to_file(self, filename="report.txt"):
        full_report = self.generate_full_report()
        with open(filename, 'w') as file:
            file.write(full_report)
        print(f"Raport zapisany do pliku {filename}.")
