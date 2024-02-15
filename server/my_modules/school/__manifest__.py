# File này dùng để tạo thông tin cho module của mình

{
    'name': 'School Management',
    'version': '1.0',
    'author': 'Tran Dang Tuan',
    'summary': 'Used for school management',
    'description': 'Used for school management',
    'depends': [
        # 'base',
        # 'other_module'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/school_information_views.xml',
        # 'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
}
