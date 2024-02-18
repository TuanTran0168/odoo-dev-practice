from odoo import models, fields


class StudentInformation(models.Model):
    _name = "student.information"
    _description = "Student Management Tuan Tran"

    name = fields.Char(string="Họ và Tên", required=True)
    birthday = fields.Date(string="Ngày sinh", required=True)
    class_id = fields.Many2one("class.information", string="Lớp", required=True)


# class ClassInformation(models.Model):
#     _inherit = "class.information" # Kế thừa nè
#
#     student_set = fields.One2many(comodel_name="student.information", inverse_name="class_id", string="Danh sách học sinh")