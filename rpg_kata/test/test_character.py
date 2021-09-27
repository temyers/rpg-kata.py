from rpg_kata.character import Character
import unittest

class TestCharacter(unittest.TestCase):

    def test_should_create_a_living_character(self):
        character = Character()
        self.assertEqual(character.isAlive(), True)

    def test_should_create_a_level1_character(self):
        character = Character()
        self.assertEqual(character.level, 1)

    def test_should_create_a_health1000_character(self):
        character = Character()
        self.assertEqual(character.health, 1000)

if __name__ == '__main__':
    unittest.main()