Feature: Go Web Automation Practice
  Scenario: Basic Web Automation Practice navigation
    Given The Automation Practice Home page is displayed
    When Navigate from Home to Shopping Cart page
    Then Accept we on the  Shopping Cart page and Cart is empty
    When Navigate from Shopping Cart to Home page
    Then Navigate from Home to Login page and assrt login element