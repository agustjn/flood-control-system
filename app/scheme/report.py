from app.dao.report import ReportDAO
from marshmallow import Schema , fields, post_load, validate, ValidationError

def validate_coordinates(coordinates):
    if   existe_coordinates(coordinates):
        raise ValidationError(" La coordenada ingresada ya existe")

class ReportScheme(Schema):
        title = fields.Str(required=True)
        category = fields.Str(required=True,validate=validate.OneOf([1, 2, 3]))
        description = fields.Str(required=True)
        coordinates = fields.Str(required=True,validate = validate_coordinates)
        #coordinates_longitude = fields.Str()
        first_name = fields.Str(required=True)
        last_name = fields.Str(required=True)
        phone = fields.Int(required=True)
        email = fields.Email(required=True)

        @post_load
        def make_report(self, data, **kwargs):
            return self.inicializar_report(**data)

        def inicializar_report(data):
            return ReportDAO.create_report_dict(**data)

class Report_show_id(Schema):
    id = fields.Int(required = True)

    @post_load
    def make_report(self, data, **kwargs):
        return ReportDAO.show(data)

reports_scheme = ReportScheme(many = True)
report_scheme = ReportScheme()
