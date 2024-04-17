from bookstore_management.models import Inventory, Book

data = [
    (1, '9780077125363', 'MISY', 'MISY4341', '22'),
    (2, '9781292103471', 'MISY', 'MISY2312', '42'),
    (3, '9780324601190', 'SOEN', 'SOEN4371', '50'),
    (4, '978-0133023893', 'ITAP', 'ITAP3382', '12'), 
    (5, '9780357418697', 'MISY', 'MISY2311', '70'),
    (6, '9781292061184', 'MISY', 'MISY3311', '36'), 
    (7, '9780071107662', 'MISY', 'MISY3322', '10'),
    (8, '9781285860237', 'MISY', 'MISY4341', '7'),
    (9, '9780134794105', 'ITAP', 'ITAP3431', '10'),
    (10, '9780134794105', 'ITAP', 'ITAP3431', '90'),
    (11, '9780321992789', 'ITAP', 'ITAP3313', '7'),
    (12, '9780135192016', 'SOEN', 'SOEN4311', '2'),
    (13, '9780134518379', 'ITAP', 'ITAP2431', '21'),
    (14, '9780134729397', 'ACCT', 'ACCT2311', '26'),
    (15, '9780135192022', 'BUSI', 'BUSI2311', '15'),
    (16, '9780135192090', 'BUSI', 'BUSI3311', '18'),
    (17, '9780135191100', 'BUSI', 'BUSI3312', '32'),
    (18, '9780135192091', 'BUSI', 'BUSI3313', '11'),
    (19, '9780135192010', 'BUSI', 'BUSI3321', '13'),
    (20, '9780135192123', 'ACCT', 'ACCT2321', '80'),
    (21, '9780135192116', 'FINA', 'FINA3311', '77'),
    (22, '9780135192009', 'BUSI', 'BUSI4362', '45'),
]

# Insert data into the Inventory model
for item in data:
    print(item)
    try:
        book = Book.objects.get(BookID=item[1])
        inventory = Inventory.objects.create(
            InventoryID=item[0],
            BookID=book,
            DepartmentCode=item[2],
            CourseID=item[3],
            CurrentInventory=item[4]
        )
        print(f"Inventory created: {inventory}")
    except Exception as e:
        print(e)

print("Data insertion complete.")
