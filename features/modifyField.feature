Feature: modify field

  Scenario:
    Given I launch Chrome browser
    When I open PHPTRAVEL login page
    And Enter email "admin@phptravels.com" and password "demoadmin"
    And Click on login button
    And Open the "TP HOTELS" menu
    And Click on "SETTINGS" section
    And Disable the Show header/footer option
    And Submit the changes
    Then I make sure that "Show Header/Footer" option disabled indeed