"""
authentication app tests
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from .forms import User

#helper functions

def create_user(email, password):
    credentials = {
            'email': email,
            'password': password
        }
    user = User.objects.create_user(**credentials)
    return user
     

class UsersManagersTests(TestCase):
    """
    user manager tests
    """
    def test_create_user(self):
        """
        test create user function
        """
        user_model = get_user_model()
        user = user_model.objects.create_user(email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertIsNone(user.username)
    
            
        with self.assertRaises(TypeError):
            user_model.objects.create_user()
        with self.assertRaises(TypeError):
            user_model.objects.create_user(email='')
        with self.assertRaises(ValueError):
            user_model.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
        """
        test create superuser function
        """
        user_model = get_user_model()
        admin_user = user_model.objects.create_superuser('super@user.com', 'foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertIsNone(admin_user.username)

        with self.assertRaises(ValueError):
            user_model.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)


class TestRegisterView(TestCase):
    """
    test case for testing register view 
    """

    def test_to_see_if_registration_form_is_provided(self):
        """
        rest function
        """
        response = self.client.get(reverse("register"))
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context['form'])

    
    def test_form_fields_with_empty_input_fields(self):
        """
        test all form fields with empty input fields
        """
        expected_required_field_error = "This field is required."
        response = self.client.post(reverse("register"),)
    

        self.assertFormError(response, 'form', 'email', [expected_required_field_error,])
        self.assertFormError(response, 'form', 'password1', [expected_required_field_error])
        self.assertFormError(response, 'form', 'password2', [expected_required_field_error,])
    
    def test_email_input_with_invalid_email(self):
        """
        test email input field with an invalid email
        """
        response = self.client.post(reverse("register"), {"email":"bernard@"})
        self.assertFormError(response, "form", "email", ['Enter a valid email address.',])
    
    def test_password_input_fields(self):
        """
        test password fields with passwords that do not match
        """
        response = self.client.post(reverse("register"), {"password1":"passwordOne",
                                                         "password2":"passwordTwo"})

        self.assertFormError(response, "form", 'password2', ["The two password fields didn't match."])


class TestProfileView(TestCase):
    """
    testing profile view
    """
    def test_profile_view_when_user_isnt_logged_in(self):
        """
        test profile view when user isnt logged in
        """
        response = self.client.get(reverse("profile", args=(1,)))

        #check to see if user is redirected to login page if not logged in
        self.assertEqual(302, response.status_code)
    
    def test_profile_view_when_user_is_logged_in(self):
        """
        test profile view with logged in user
        """
        user = create_user("user@gmail.com", "password123")

        #login user
        self.client.post(reverse('login'), {"username":"user@gmail.com",  
                                                       "password":"password123"})
        
        response = self.client.get(reverse("profile", args=(user.id,)))

        self.assertEqual(200, response.status_code)

        #check if correct user is the one making the request
        self.assertEqual("user@gmail.com", response.context['user'].email)
        


class TestEmailView(TestCase):
    """
    test email view
    """
    def test_email_view_with_unauthenticated_user(self):
        """
        testing edit email view with user that is not logged in
        """
        response = self.client.get(reverse("edit_email"))

        #making sure user is redirected to login page
        self.assertEqual(302, response.status_code)
    
    def test_email_view_with_authenticated_user(self):
        """
        test email view with user that is logged in
        """
        #create a new user
        create_user("user@gmail.com", "password123")

        #log the user in
        self.client.post(reverse('login'), {"username":"user@gmail.com",  
                                                       "password":"password123"})

        response = self.client.get(reverse("edit_email"))

        self.assertEqual(200, response.status_code)

        #checking if a form is provided
        self.assertTrue(response.context['form'])

