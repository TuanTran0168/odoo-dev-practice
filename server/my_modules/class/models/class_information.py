from odoo import models, fields


class ClassInformation(models.Model):
    _name = "class.information"
    _description = "Class Information Tuan Tran"

    name = fields.Char(string="Tên lớp")
    grade = fields.Char(String="Khối")
    main_teacher = fields.Char(string="Giáo viên chủ nhiệm")
    school_id = fields.Many2one("school.information", string="Trường")
