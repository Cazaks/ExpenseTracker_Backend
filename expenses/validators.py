import re
from django.core.exceptions import ValidationError


class NoWhiteSpaceValidator:
    def validate(self, password, user=None):
        if " " in password:
            raise ValidationError("Password cannot contain spaces.",
                code="password_has_whitespace",)

    def get_help_text(self):
        return "Your password cannot contain spaces."

class SpecialCharacterValidator:
    def validate(self, password, user=None):
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-]", password):
            raise ValidationError("Password cannot contain at least one special characters.",
                                  code='password_no_cpecial_char',)

    def get_help_text(self):
        return "Your password must contain at least one special character (e.g. ! @ # $ %)."
