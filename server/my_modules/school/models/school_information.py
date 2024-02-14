from odoo import models, fields


# Model bên này trông cũng giống Django kha khá à :v
class SchoolInformation(models.Model):
    # Mấy cái có dấu gạch đằng trước này là thông tin của bảng
    # Chưa phải là 1 field trong bảng dữ liệu
    _name = "school.information"
    _description = "School Information Tuan Tran"

    # Đây mới là các fields của bảng nè
    name = fields.Char(string="Tên trường học")
    type = fields.Selection([
        # (value, option),
        ("private", "Dân lập"),
        ("public", "Công lập")
    ], default="public", string="Loại trường")
    email = fields.Text(string="Email")
    address = fields.Text(string="Địa chỉ")

    # CÒN 1 VÀI AUTOMATIC FIELDS TRÊN DOCUMENTS NỮA (nó sẽ TỰ ĐỘNG tạo cho mình)
    # Không ưng thì tắt mà chưa biết tắt sao :)))
    # id (Id)
    # The unique identifier for a record of the model.
    #
    # create_date (Datetime)
    # Creation date of the record.
    #
    # create_uid (Many2one)
    # User who created the record.
    #
    # write_date (Datetime)
    # Last modification date of the record.
    #
    # write_uid (Many2one)
    # User who last modified the record.
