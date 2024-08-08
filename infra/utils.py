import random
import string
from random_username.generate import generate_username


class Utils:

    @staticmethod
    def generate_random_lowercase_string(min_length, max_length):
        """
            Generates a random string containing lowercase letters, digits.
            Args:
                min_length (int): The minimum length of the generated string.
                max_length (int): The maximum length of the generated string.
            Returns:
                str: A randomly generated string.
        """
        characters = string.ascii_lowercase + string.digits
        username = ''.join(random.choice(characters) for _ in range(random.randint(min_length, max_length)))
        return username

    @staticmethod
    def generate_random_string(min_length, max_length):
        """
            Generates a random string containing uppercase and lowercase letters, digits.
            Args:
                min_length (int): The minimum length of the generated string.
                max_length (int): The maximum length of the generated string.
            Returns:
                str: A randomly generated string.
        """
        characters = string.ascii_letters + string.digits
        username = ''.join(random.choice(characters) for _ in range(random.randint(min_length, max_length)))
        return username

    @staticmethod
    def generate_username(count):
        """
            Generates a random username
            Returns:
                str: A randomly generated username.
        """
        return generate_username(count)

    @staticmethod
    def random_number(a, b):
        """
            Get a random number in the range [a, b) or [a, b] depending on rounding.
            Args:
                a (int): The minimum of the given number.
                b (int): The maximum of the given number.
            Returns:
                int: A random number.
        """
        return str(int(random.uniform(a, b)))
