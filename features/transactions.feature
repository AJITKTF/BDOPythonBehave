Feature: Validate transaction search page

  Scenario Outline: User validates transaction details page
    Given User launches BDO application and enters username"<user>",password"<password>"
    And User clicks on SignIn button
    Then User validates succesfull login and clicks on continue button
    And User navigates to transactions lookup page
    When User enters search fields "<start>" and "<end>" and "<card>"
    And User clicks on Search button in transaction lookup page
    And User searches and validates transcation "<trn>" searched in the grid
    Then User validates POS data in transaction details page "<posentrymode>" and "<posdata>" and "<posconditioncode>" and "<generalresponsecode>"
   # Then User validates Other data in transaction details page


    Examples:
      | user         | password   | start      | end        | card             | trn                  | posentrymode | posdata      | posconditioncode | generalresponsecode |
      | AJITKULKARNI | test123456 | 27/06/2025 | 27/06/2025 | 5452750275538769 | 3121528251009827.615 | 0022         | 000001000030 | 00               | 00                  |
      | AJITKULKARNI | test123456 | 27/06/2025 | 27/06/2025 | 5210690277706274 | 3141551551010262.764 | 0052         | 000001000030 | 00               | 00                  |
      | AJITKULKARNI | test123456 | 27/06/2025 | 27/06/2025 | 5489240000046004 | 3141551551010774.543 | 0072         | 000001000030 | 00               | 00                  |
      | AJITKULKARNI | test123456 | 27/06/2025 | 27/06/2025 | 5489240000046004 | 3141551551019579.166 | 0912         | 000001000030 | 00               | 00                  |