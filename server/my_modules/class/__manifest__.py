# File này dùng để tạo thông tin cho module của mình

{
    'name': 'Class Management',
    'version': '1.0',
    'author': 'Tran Dang Tuan',
    'summary': 'Used for class management',
    'description': 'Used for class management',
    'depends': [
        # 'base',
        # 'other_module'
        "school"  # Tham chiếu khóa ngoại ở models thì khai báo ở đây, dính bug tốn hơn 30p của toi
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/class_information_views.xml',
        # 'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
}
