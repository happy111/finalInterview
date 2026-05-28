# tests/test_area_serializer.py
from django.test import TestCase
from area.models import Area
from area.serializers import AreaSerializer

class AreaSerializerTestCase(TestCase):

    def setUp(self):
        self.area = Area.objects.create(name="Zone A", priority=1)

    def test_serializer_output(self):
        serializer = AreaSerializer(instance=self.area)
        data = serializer.data
        self.assertEqual(data['name'], "Zone A")
        self.assertEqual(data['priority'], 1)
        self.assertIn('id', data)  # if inherited from Common

    def test_valid_input_serialization(self):
        input_data = {
            "name": "Zone B",
            "priority": 2
        }
        serializer = AreaSerializer(data=input_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        area = serializer.save()
        self.assertEqual(area.name, "Zone B")
        self.assertEqual(area.priority, 2)

    def test_missing_name_should_fail(self):
        input_data = {
            "priority": 3
        }
        serializer = AreaSerializer(data=input_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)

    def test_unique_name_constraint(self):
        Area.objects.create(name="UniqueZone", priority=5)
        input_data = {
            "name": "UniqueZone",
            "priority": 10
        }
        serializer = AreaSerializer(data=input_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)
