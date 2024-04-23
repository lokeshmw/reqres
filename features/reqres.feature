Feature: Testing User API Endpoints

  Background:
    Given the base URL "https://reqres.in/api" is loaded
  @get_users
  Scenario: Get Users
    When I send a GET request to "/users"
    Then the response status code should be 200
  @get_users_by_id
  Scenario Outline: Get User by ID
    When I send a GET request to /users/user_id with "<user_id>"
    | TestCaseId   | TestCaseName     |  user_id      |
    | <TestCaseId> | <TestCaseName>   | <user_id >    |
    Then the response status code should be 200
    Examples:
      |   TestCaseId         |      TestCaseName                |user_id |
      |   Request_001        |   Fetching user data by ID       |7       |
      |   Request_002        |   Fetching user data by ID       |8      |
      |   Request_003        |   Fetching user data by ID       |9       |
      |   Request_004        |   Fetching user data by ID       |10      |

  @create_users
  Scenario Outline: Create User
    When I send a POST request to "/users" with "<name>" and "<job>"
       | TestCaseId | TestCaseName  |name|job|
    | <TestCaseId> | <TestCaseName> | <name>| <job> |
    Then the response status code should be 201
    Examples:
      | TestCaseId   |    TestCaseName       | name     | job                 |
      | Request_005  |   Creating_user       |John Doe  |Software Engineer    |
      | Request_006  |   Creating_user       |Randy     | doctor              |


  @update_users
  Scenario Outline: Updating User's data
    When I send a PUT request to "/users" with "<name>" and "<job>" by "<user_id>"
       | TestCaseId | TestCaseName     |name   |job    |
       | <TestCaseId> | <TestCaseName> | <name>| <job> |
    Then the response status code should be 200
    And The response body should contain the data
    Examples:
      | TestCaseId   |    TestCaseName       |user_id | name     | job           |
      | Request_005  |   Updating_user       | 8      |Doe       |AI Engineer    |
      | Request_006  |   Updating_user       | 9      |Ray jones | Eye doctor    |
  @delete_user
  Scenario Outline: Delete User by ID
    When I send a Delete request to /users/user_id with "<user_id>"
    | TestCaseId   | TestCaseName     |  user_id      |
    | <TestCaseId> | <TestCaseName>   | <user_id >    |
    Then the response status code should be 204
    Examples:
      |   TestCaseId         |      TestCaseName                |user_id |
      |   Request_001        |   Deleting user data by ID       |31      |
#      |   Request_002        |   Deleting user data by ID       |41      |
#      |   Request_003        |   Deleting user data by ID       |51      |
#      |   Request_004        |   Deleting user data by ID       |61      |

