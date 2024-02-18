# File này dùng để tạo thông tin cho module của mình

{
    'name': 'Student Management',
    'version': '1.0',
    'author': 'Tran Dang Tuan',
    'summary': 'Used for student management',
    'description': 'Used for student management',
    'depends': [
        # 'base',
        # 'other_module'
        "class"
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/student_information_views.xml',
        # 'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
}
