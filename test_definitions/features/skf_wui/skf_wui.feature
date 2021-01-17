Feature: To validate if SKF application is able to display options under select bearing type dropdown menu

Scenario: Launching SKF website and clicking on Single bearing image
    Given I launch SKF website
    When I click on Accept & Continue button
    Then I click on Rolling bearing image
    And I click on Single bearing image

Scenario Outline: Verify display options under select bearing type dropdown menu
    When I click on Select bearing type dropdown
    Then I verify option: <options> is present
    And I close the dropdown

    Examples: Select bearing type options
        |               options                 |
        |   Insert bearing (Y-bearing)          |
        |   Angular contact ball bearing        |
        |   Self-aligning ball bearing          |
        |   Cylindrical roller bearing          |
        |   Needle roller bearing               |
        |   Tapered roller bearing              |
        |   Spherical roller bearing            |
        |   CARB toroidal roller bearing        |
        |   Thrust ball bearing                 |
        |   Cylindrical roller thrust bearing   |
        |   Needle roller thrust bearing        |
        |   Spherical roller thrust bearing     |
        |   Track roller                        |
        |   Deep groove ball bearing            |

