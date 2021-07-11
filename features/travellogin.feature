Feature: PHPTRAVEL login

  Scenario Outline: Login to the PHPTRAVEL with correct credentials
    Given I launch Chrome browser
    When I open PHPTRAVEL login page
    And Enter email "<email>" and password "<pwd>"
    And Click on login button
    Then I am redirected to a page with a "<msg>" message
    Examples:
      | email                 | pwd       | msg       |
      | admin@phptravels.com  | demoadmin | Hi Admin! |

  Scenario Outline: Login to the PHPTRAVEL with wrong credentials
    Given I launch Chrome browser
    When I open PHPTRAVEL login page
    And Enter email "<email>" and password "<pwd>"
    And Click on login button
    And I make sure I am on "LOGIN PANEL"
    Then I see an error message "Invalid Login Credentials"
    Examples:
      | email                    | pwd       |
      | notadmin@phptravels.com  | demoadmin |
      | admin@phptravels.com     | 123demo   |
      | admin111@phptravels.com  | 123demo   |
