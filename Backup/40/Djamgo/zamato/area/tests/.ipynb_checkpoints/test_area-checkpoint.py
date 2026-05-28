# from unittest.mock import patch, MagicMock
# from rest_framework import status
# from rest_framework.test import APITestCase
# from django.urls import reverse

# class AreaCreationViewMockTest(APITestCase):
#     def setUp(self):
#         self.url = reverse('area-create')

#     @patch('area.views.AreaSerializer')  # 👈 Make sure this matches your import style
#     def test_area_creation_success(self, mock_serializer_class):
#         # Create a mock serializer instance
#         mock_serializer = MagicMock()
#         mock_serializer.is_valid.return_value = True
#         mock_serializer.save.return_value = MagicMock()
#         mock_serializer.data = {"id": 1, "name": "Test Area", "priority": 1}

#         # Set the return value of the serializer class
#         mock_serializer_class.return_value = mock_serializer

#         # Prepare the payload
#         payload = {
#             "name": "Test Area",
#             "priority": 1
#         }

#         # Call the API
#         response = self.client.post(self.url, payload, format='json')

#         # Assertions
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(response.data['name'], "Test Area")
#         self.assertEqual(response.data['priority'], 1)

#         # Less strict check (since DRF uses get_serializer internally)
#         mock_serializer_class.assert_called()  # ✅
