from django.core.management.base import BaseCommand
from bookstore_management.models import Inventory, Department
from django.core.mail import send_mail
from django.conf import settings


class Command(BaseCommand):
    help = 'Generate and send inventory report to department chairs'

    def handle(self, *args, **kwargs):
        # Query inventory data for each department
        departments = Department.objects.all()
        for department in departments:
            department_inventory = Inventory.objects.filter(
                DepartmentCode=department.DepartmentCode)
            # Generate inventory report
            report_lines = ['Inventory Report for Department: {}'.format(
                department.DepartmentName)]
            for inventory_item in department_inventory:
                report_line = 'Book: {}, Inventory: {}'.format(
                    inventory_item.BookID.BookTitle, inventory_item.CurrentInventory)
                report_lines.append(report_line)
            # Send report via email to department chair
            email_subject = 'Inventory Report for {}'.format(
                department.DepartmentName)
            email_body = '\n'.join(report_lines)
            send_mail(email_subject, email_body,
                      settings.DEFAULT_FROM_EMAIL, [department.ChairID.Email])
            self.stdout.write(self.style.SUCCESS(
                'Inventory report sent to {}.'.format(department.ChairID.Name)))
