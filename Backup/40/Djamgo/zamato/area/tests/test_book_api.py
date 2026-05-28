from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from book.models import Book

class BookCreateAPITest(APITestCase):
    def setUp(self):
        self.url = reverse('book-create')
        self.payload = {
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "published": "1988-01-01"
        }

    def test_create_book_success(self):
        response = self.client.post(self.url, self.payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.payload['title'])
        self.assertTrue(Book.objects.filter(title="The Alchemist").exists())


class BookListAPITest(APITestCase):
    def setUp(self):
        self.url = reverse('book-list')
        # create 2 books for testing
        Book.objects.create(title="Book 1", author="Author A", published="2020-01-01")
        Book.objects.create(title="Book 2", author="Author B", published="2021-01-01")

    def test_get_book_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], "Book 1")


# # books/tests/test_email_api.py
# from django.core import mail
# from rest_framework.test import APITestCase
# from django.urls import reverse
# from rest_framework import status

# class SendEmailAPITest(APITestCase):
#     def setUp(self):
#         self.url = reverse('send-email')

#     def test_send_email_success(self):
#         response = self.client.post(self.url, {"email": "user@example.com"}, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['message'], "Email sent successfully")
#         self.assertEqual(len(mail.outbox), 1)  # ✅ Email was actually "sent"
#         self.assertEqual(mail.outbox[0].subject, "Welcome to the Library")
#         self.assertEqual(mail.outbox[0].to, ["user@example.com"])

#     def test_send_email_without_email(self):
#         response = self.client.post(self.url, {}, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn("error", response.data)
