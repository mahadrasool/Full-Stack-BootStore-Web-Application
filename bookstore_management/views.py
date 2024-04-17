from django.shortcuts import render

# Create your views here.
from .models import Department
from django.http import JsonResponse
from .models import Inventory

def home(request):
    return render(request, 'home.html')

def inventory_report(request):
    departments = Department.objects.all()
    inventories = Inventory.objects.all()
    return render(request, 'inventory_report.html', {'departments': departments, "inventories": inventories, "selected_department": "FINA"})


def generate_report(request):
    department_code = request.GET.get('department_code')
    inventory_report = Inventory.objects.filter(DepartmentCode=department_code)

    # Build table header row
    table_header = "<tr>"
    for field_name in ["Inventory ID", 'BookTitle', 'Department Code', "Course ID", "Current Inventory"]:
        table_header += f"<th>{field_name}</th>"
    table_header += "</tr>"

    # Build table rows
    table_body = ""
    for item in inventory_report:
        table_body += f"<tr><td>{item.InventoryID}</td> <td>{item.BookID}</td> <td>{item.DepartmentCode}</td> <td>{item.CourseID}</td>  <td>{
            item.CurrentInventory}</td></tr>"

    # Combine table elements and report title
    report_html = f"""
    <h2>Inventory Report for Department: {department_code}</h2>
    <table>
      <thead>{table_header}</thead>
      <tbody>{table_body}</tbody>
    </table>
    """

    # Return JSON response with the report HTML
    return JsonResponse({'data': report_html})
