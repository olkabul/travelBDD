Feature: PHPTRAVEL login

  Scenario Outline: Login to the PHPTRAVEL with correct credentials
    Given I launch Chrome browser
    When I open PHPTRAVEL login page
    And Enter email "<email>" and password "<pwd>"
    And Click on login button
    Then I must successfully login to the Dashboard and see the "<msg>" message
    Examples:
      | email                 | pwd       | msg       |
      | admin@phptravels.com  | demoadmin | Hi Admin! |

  Scenario Outline: Login to the PHPTRAVEL with wrong credentials
    Given I launch Chrome browser
    When I open PHPTRAVEL login page
    And Enter email "<email>" and password "<pwd>"
    And Click on login button
    Then I must stay on "<pnlname>"
    Examples:
      | email                    | pwd       | pnlname                     |
      | notadmin@phptravels.com  | demoadmin | LOGIN PANEL |
      | admin@phptravels.com     | 123demo   | LOGIN PANEL |
      | admin111@phptravels.com  | 123demo   | LOGIN PANEL |
