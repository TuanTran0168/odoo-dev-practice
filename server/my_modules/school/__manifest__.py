# File này dùng để tạo thông tin cho module của mình

{
    'name': 'School Management',
    'version': '1.0',
    'author': 'Tran Dang Tuan',
    'summary': 'Used for school management',
    'description': 'Used for school management',
    'depends': [
        # "class" # Nếu mở cái này ra thì sẽ dính cái lỗi ở dưới, trông như bị đệ quy 2 cái depends giữa 2 models
        # Vì bên models của class cũng có depend school
        # ERROR odoo-db odoo.modules.loading:
        # Some modules have inconsistent states, some dependencies may be missing: ['class', 'school', 'student']
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/school_information_views.xml',
        # 'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
}
