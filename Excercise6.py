import random

import time

from random import randint

from typing import Any


class Restaurant:
    """Restaurant name and items"""

    def __init__(self, restaurant_name, cuisine_type):
        """attributes to describe restaurant"""

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """restaurant name and cuisine type"""

        greeting = f"Welcome to {self.restaurant_name} one of our signature cuisines is {self.cuisine_type}"
        return greeting

    def open_restaurant(self):
        """State the the restaurant is open and give hours"""

        open_during =  f"{self.restaurant_name} is currently open and our store hours are Monday through Saturday from 8:00am to 12am. "
        return open_during


restaurant_details = Restaurant('Matts unknown seafood', 'Anything we can catch')
print(restaurant_details.describe_restaurant())
print(restaurant_details.open_restaurant())


class Seafoodparlor:
    """Restaurant name and items"""

    def __init__(self, parlor_name, food_type, options):
        """Initialize attributes to describe restaurant"""

        self.shop_name = parlor_name
        self.food_type = food_type
        self.options = options

    def describe_restaurant(self):
        """Print both the restaurant name and cuisine type"""

        greeting = f"\nWelcome to {self.parlor_name} one of our signature cuisines is {self.food_type}"
        return greeting

    def open_restaurant(self):
        """State the the restaurant is open and give hours"""

        open_during =  f"{self.parlor_name} is currently open and our store hours are Monday through Tuesday from 8:00am to 8:15am. "
        return open_during
    def guest_options(self):
        """Give the guest their options of choices for Seafood"""

        flavor_options = f"Here at {self.parlor_name} we have a three options of seafood items that range from {self.options}"
        return flavor_options

welcome_to_parlor = Seafoodparlor('matts unknown seafood', 'whatever we catch', 'crappy crab')
print(welcome_to_parlor.describe_restaurant())

print(welcome_to_parlor.open_restaurant())

print(welcome_to_parlor.guest_options())






class Seafood(Restaurant):
    def __init__(self,restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

    def describe_items(self,*items):
        print(f'{self.restaurant_name} has the following items:')
        for self.flavor in items:
            print(f'-{self.items}')

restaurant = Seafood('Unknown','items')
restaurant.describe_restaurant()
restaurant.describe_items('Sandy Salmon','macho mackeral', 'crappy crab',)

class User:

    def __init__(self, first_name, last_name):
        """Ask the user for their full name"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        prompt_user = f"\nYour name first name is {self.first_name} and your last name is {self.last_name}."
        return prompt_user

    def greet_user(self):
        prompt_greeting = f"Hello {self.first_name} {self.last_name} welcome to your machine."
        return prompt_greeting

welcome_user = User('Kendall', 'Davenport')

welcome_user2 = User('Elisa', 'Saul')

welcome_user3 = User('Adam', 'Sandler')
print(welcome_user.describe_user())
print(welcome_user.greet_user())

print(welcome_user2.describe_user())
print(welcome_user2.greet_user())

print(welcome_user3.describe_user())
print(welcome_user3.greet_user())


class Admin:

    def __init__(self, first_name, last_name):
        """Ask the user for their full name"""

        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        prompt_user = f"\nYour name first name is {self.first_name} and your last name is {self.last_name}."
        return prompt_user

    def greet_user(self):
        prompt_greeting = f"Hello {self.first_name} {self.last_name} welcome to your machine."
        return prompt_greeting

    def describe_permissions(self, *privileges):
        print(f"\nHello {self.first_name} {self.last_name} your  privileges are: ")
        for self.privilege in privileges:
            print(f'{self.privilege}')

welcome_user = Admin('Kendall', 'Davenport')

welcome_user2 = Admin('Elisa', 'Saul')

welcome_user3 = Admin('Adam', 'Sandler')
show_privileges = Admin.describe_permissions(welcome_user, 'will post',' delete post', 'you can ban user')

show_privileges2 = Admin.describe_permissions(welcome_user2, 'Can post','Can delete post', 'you can ban user')

show_privileges3 = Admin.describe_permissions(welcome_user3, 'Can post','Can delete post', 'you can ban user')