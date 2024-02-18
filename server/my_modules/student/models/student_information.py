from odoo import models, fields


class StudentInformation(models.Model):
    _name = "student.information"
    _description = "Student Management Tuan Tran"

    name = fields.Char(string="Họ và Tên", required=True)
    birthday = fields.Date(string="Ngày sinh", required=True)
    class_id = fields.Many2one("class.information", string="Lớp", required=True)
