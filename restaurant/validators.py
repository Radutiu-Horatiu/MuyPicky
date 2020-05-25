from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )

	
def validate_email(value):
	email = value
	if ".edu" in email:
		raise ValidationError("We do not accept edu emails!")

CATEGORIES = ['Mexican', 'Italian', 'Romanian', 'American', 'Mix']

def validate_category(value):
	cat = value.capitalize()
	if not cat in CATEGORIES:
		raise ValidationError(F"{cat} not valid category.")
	return cat