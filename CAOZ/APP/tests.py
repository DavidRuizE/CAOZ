from django.test import TestCase, Client
from django.urls import reverse
from .models import User

class UserRegistrationTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('registro')
        self.user_data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }

    def test_register_user(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, 302)  # Redirige después de registrarse
        self.assertTrue(User.objects.filter(email='testuser@example.com').exists())

class UserLoginTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = User.objects.create_user(email='testuser@example.com', password='testpassword', name='Test User')

    def test_login_user(self):
        response = self.client.post(self.login_url, {'email': 'testuser@example.com', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Redirige después de iniciar sesión
        self.assertTrue('_auth_user_id' in self.client.session)