Feature: Select Section

  Scenario:
    Given I launch Chrome browser
    When I open PHPTRAVEL login page
    And Enter email "admin@phptravels.com" and password "demoadmin"
    And Click on login button
    And Open the "TP HOTELS" menu
    And Click on "SETTINGS" section
    Then I must see the "TRAVELPAYOUTS" page
