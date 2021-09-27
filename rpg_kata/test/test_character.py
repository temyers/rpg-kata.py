from rpg_kata.character import Character
import unittest

class TestCharacter(unittest.TestCase):

    def test_should_create_a_living_character(self):
        character = Character()
        self.assertEqual(character.isAlive(), True)

    def test_should_create_a_level1_character(self):
        character = Character()
        self.assertEqual(character.level, 1)

    def test_should_create_a_health100_character(self):
        character = Character()
        self.assertEqual(character.health, 100)

    def test_should_deal_damage(self):
        character1 = Character()
        character2 = Character()

        character2.health = 100

        character1.damage(character2,10)
        self.assertEqual(character2.health,90)
        self.assertEqual(character1.health, 100)

    def test_character_should_die_from_damage(self):
        character1 = Character()
        character2 = Character()

        character2.health = 50

        character1.damage(character2, 60)
        self.assertEqual(character2.health, 0)
        self.assertEqual(character2.isAlive(), False)
        self.assertEqual(character1.health, 100)

    def test_should_be_able_to_heal_another_character(self):
        character1 = Character()
        character2 = Character()

        character2.health = 50

        character1.heal(character2, 10)
        self.assertEqual(character2.health, 60)
        self.assertEqual(character1.health, 100)

    def test_should_not_be_able_to_heal_more_than_starting_health(self):
        character1 = Character()
        character2 = Character()

        character2.health = 90

        character1.heal(character2, 20)
        self.assertEqual(character2.health, 100)
        self.assertEqual(character1.health, 100)


if __name__ == '__main__':
    unittest.main()