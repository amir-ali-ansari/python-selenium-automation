# Created by AAA at 11/29/2022
Feature: re-write Homework lesson 3

  Scenario: logged out user sees Sign in when clicking orders
    Given open Amazon
    When click on Amazon orders
    Then Verify sign in page is open

    Scenario: Your Shopping Cart is empty
      Given open Amazon
      When Click on cart
      Then Verity cart is empty