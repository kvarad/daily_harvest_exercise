from daily_harvest import get_ingredient_name_by_id, find_foods_by_ingredient

import pytest
import unittest

class TestDailyHarvestSearch(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestDailyHarvestSearch, self).__init__(*args, **kwargs)
        self.ingredient_id = 3

        self.ingredients = [
        {
            "id": 1,
            "name": "Organic Acai Berry",
            "is_allergen": False
        },
        {
            "id": 2,
            "name": "Organic Cherry",
            "is_allergen": False
        },
        {
            "id": 3,
            "name": "Organic Banana",
            "is_allergen": False
        }
        ]

    def test_get_ingredient_name_by_id(self):
        ingredient_name = get_ingredient_name_by_id(self.ingredient_id,
                                                    self.ingredients)

        self.assertEquals("Organic Banana", ingredient_name)

    def test_find_foods_by_ingredient(self):
        expected_output = ["Cinnamon + Banana", "Ginger + Greens",
                           "Chocolate + Blueberry", "Acai + Cherry"]
        products = find_foods_by_ingredient(self.ingredient_id)

        self.assertEquals(sorted(expected_output), sorted(products))
