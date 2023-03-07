from django.test import TestCase
#from django_batch.cake_project.accounts.forms import RegistrationForm
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User


# Create your tests here.
class RegistrationFormTestCase(TestCase):

    def get_result(self, form):
        if form.errors:
            for field in form:
                for error in field.errors:
                    print(field.label, error)

    def test_form_fields(self):
        form_data = {'first_name': 'joey', 'last_name': 'django', 'username': 'joeyd', 'email': 'joey@gmail.com',
                     'phone_number': '1234567890', 'password1': 'pass@1234', 'password2': 'pass@1234'}
        form = RegistrationForm(data=form_data)
        print('Test 1')
        self.get_result(form)
        self.assertTrue(form.is_valid())

    def test_form_columns(self):
        form_data = {'first': 'joey', 'last_name': 'django', 'username': 'joeyd', 'email': 'joey@gmail.com',
                     'phone_number': '1234567890', 'password1': 'pass@1234', 'password2': 'pass@1234'}
        form = RegistrationForm(data=form_data)
        print('Test 2')
        self.get_result(form)
        assert form.errors['first_name'][0] == 'This field is required.'

    def test_invalid_email(self):
        form_data = {'first_name': 'joey', 'last_name': 'django', 'username': 'joeyd', 'email': '',
                     'phone_number': '1234567890', 'password1': 'pass@1234', 'password2': 'pass@1234'}
        form = RegistrationForm(data=form_data)
        print('Test 3')
        self.get_result(form)
        assert form.errors['email'][0] == 'This field is required.'
        self.assertFalse(form.is_valid())

    def test_username_exists(self):
        form_data = {'first_name': 'joey', 'last_name': 'django', 'username': 'joeyd', 'email': 'joey@gmail.com',
                     'phone_number': '1234567890', 'password1': 'pass@1234', 'password2': 'pass@1234'}
        User.objects.create_user(username='joeyd',
                                 email='jd@gmailcom',
                                 password='hello1234')
        form = RegistrationForm(data=form_data)
        print('Test 4')
        self.get_result(form)
        assert form.errors['username'][0] == 'A user with that username already exists.'

    def test_blank_field(self):
        form_data = {'first_name': None, 'last_name': 'django', 'username': 'jdjango', 'email': 'joey@gmail.com',
                     'phone_number': '1234567890', 'password1': 'pass@1234', 'password2': 'pass@1234'}
        form = RegistrationForm(data=form_data)
        print('Test 5')
        self.get_result(form)
        assert form.errors['first_name'][0] == 'This field is required.'
