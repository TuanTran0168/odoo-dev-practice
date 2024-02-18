from odoo import models, fields


# Model bên này trông cũng giống Django kha khá à :v
class SchoolInformation(models.Model):
    # Mấy cái có dấu gạch đằng trước này là thông tin của bảng
    # Chưa phải là 1 field trong bảng dữ liệu
    _name = "school.information"
    _description = "School Information Tuan Tran"

    # Đây mới là các fields của bảng nè
    name = fields.Char(string="Tên trường học") # Cái string ở trong này là để hiển thị lên giao diện
    type = fields.Selection(selection=[
        # (value, option),
        ("private", "Dân lập"),
        ("public", "Công lập")
    ], default="public", string="Loại trường")
    email = fields.Text(string="Email")
    address = fields.Text(string="Địa chỉ")
    phone_number = fields.Char(string="Số điện thoại")
    hasOnlineClass = fields.Boolean(string="Có lớp hoạt động không?")
    rank = fields.Integer(string="Xếp hạng")
    establish_day = fields.Date(string="Ngày thành lập")
    document = fields.Binary(string="Tài liệu về trường")
    document_name = fields.Char(string="Tên tài liệu")

    # class_set = fields.One2many(comodel_name="class.information", inverse_name="school_id", string="Danh sách lớp")

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
