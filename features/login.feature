Feature: validate user login

  Scenario Outline: validate valid user login

    Given User launches BDO application and enters username"<user>",password"<password>"
    And User clicks on SignIn button
    Then User validates succesfull login and clicks on continue button
    Then User clicks on Logout
    Examples:
      | user            | password   |
      | AJITKULKARNI    | test123456 |
      | TESTAUTOMATION1 | test123456 |



