from odoo import models, fields


class ClassInformation(models.Model):
    _name = "class.information"
    _description = "Class Information Tuan Tran"

    name = fields.Char(string="Tên lớp")
    grade = fields.Char(String="Khối")
    main_teacher = fields.Char(string="Giáo viên chủ nhiệm")
    school_id = fields.Many2one("school.information", string="Trường")

    # student_set = fields.One2many(comodel_name="student.information", inverse_name="class_id",
    #                               string="Danh sách học sinh")

# Khai báo bên này á thì lỗi không tìm thấy model student, do chưa có trong depends
# Mà thêm dô depends cái student rồi thì lại lỗi đệ quy
# Còn bên student khai báo lại bên class này á thì lại lỗi view không tìm thấy cái student_set
# Tùm lum tùm la luôn á trời ơi.

# class ClassInformation(models.Model):
#     _inherit = "class.information"  # Kế thừa nè
#
#     student_set = fields.One2many(comodel_name="student.information", inverse_name="class_id",
#                                   string="Danh sách học sinh")
