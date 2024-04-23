from behave import given, when, then
from selenium.common import NoSuchElementException

from features.pages.Api_functions_page import APIFunctions
from utilities.logger import logger


@given(u'the base URL "https://reqres.in/api" is loaded')
def step_impl(context):
    context.Api_testing = APIFunctions(context)
    logger.info("Base URL set to 'https://reqres.in/api'")


@when(u'I send a GET request to "/users"')
def step_impl(context):
    logger.info("Sending a GET request to '/users'")
    context.Api_testing.get_users()


@when(u'I send a GET request to /users/user_id with "{user_id}"')
def step_impl(context, user_id):
    logger.info(f"Sending a GET request to '/users/{user_id}'")
    context.get_user_By_id = context.Api_testing.get_user_by_id(user_id)


@then(u'the response status code should be 200')
def step_impl(context):
    try:
        response = context.Api_testing.get_users()
        logger.info(f"Response status code: {response.status_code}")
        if response.status_code == 200:
            logger.info("Response JSON:")
            logger.info(response.json())
        else:
            logger.error(f"Unexpected Status code: {response.status_code}")
            raise AssertionError(f"Unexpected status code: {response.status_code}")
    except NoSuchElementException as e:
        response = context.get_user_By_id
        logger.info(f"Response status code: {response.status_code}")
        if response.status_code == 200:
            logger.info("Response JSON:")
            logger.info(response.json())
        else:
            logger.error(f"Unexpected Status code: {response.status_code}")
            raise AssertionError(f"Unexpected status code: {response.status_code}")


@when(u'I send a POST request to "/users" with "{name}" and "{job}"')
def step_impl(context, name, job):
    logger.info(f"Sending a POST request to '/users' with name='{name}' and job='{job}'")
    context.create_user = context.Api_testing.create_user(name, job)


@then(u'the response status code should be 201')
def step_impl(context):
    response = context.create_user
    logger.info(f"Response status code: {response.status_code}")
    if response.status_code == 201:
        logger.info("Response JSON: ")
    else:
        logger.error(f"Unexpected Status code: {response.status_code}")
        response.raise_for_status()
        raise AssertionError(f"Unexpected status code: {response.status_code}")


@when(u'I send a Delete request to /users/user_id with "{user_id}"')
def step_impl(context, user_id):
    logger.info(f"Sending a DELETE request to '/users/{user_id}'")
    context.Deleted_user = context.Api_testing.Delete_user(user_id)


@then(u'the response status code should be 204')
def step_impl(context):
    response = context.Deleted_user
    logger.info(f"Response status code: {response.status_code}")
    if response.status_code == 204:
        logger.info("Response JSON: ")
    else:
        logger.error(f"Unexpected Status code: {response.status_code}")
        response.raise_for_status()
        raise AssertionError(f"Unexpected status code: {response.status_code}")


@when(u'I send a PUT request to "/users" with "{name}" and "{job}" by "{user_id}"')
def step_impl(context, name, job, user_id):
    logger.info(f"Sending a PUT request to '/users/{user_id}' with name='{name}' and job='{job}'")
    context.data = {"name": name, "job": job}
    context.updated_user_response = context.Api_testing.Update_user(user_id, context.data)
    print(context.updated_user_response)


@then(u'The response body should contain the data')
def step_impl(context):
    response = context.updated_user_response
    expected_data = context.data
    logger.info(f"Response status code: {response.status_code}")

    if response.status_code == 200:
        logger.info("Response JSON:")
        response_data = response.json()[0]
        logger.info(response_data)

        expected_name = expected_data["name"]
        expected_job = expected_data["job"]

        name = response_data.get("name")
        job = response_data.get("job")

        assert name == expected_name, f"Expected name: '{expected_name}', Actual name: {name}"
        assert job == expected_job, f"Expected job: '{expected_job}', Actual job: {job}"

    else:
        logger.error(f"Unexpected Status code: {response.status_code}")
        raise AssertionError(f"Unexpected status code: {response.status_code}")
