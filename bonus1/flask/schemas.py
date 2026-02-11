from marshmallow import Schema, fields
from marshmallow import validates, ValidationError

class HelloSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    place = fields.Str(required=True)
    number = fields.Int(required=True)
    email = fields.Email(required=True)          # condition auto implemented i.e check for @, local part, domain ,etc

    @validates("number")
    def validate_number(self, value, **kwargs):
        value = str(value)                     # since we cannot use startswith method for integer value
        if not value.startswith(("97", "98")) or len(value) != 10:
            raise ValidationError("Only phone number starting with 97 and 98.")