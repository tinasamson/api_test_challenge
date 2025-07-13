import pytest

@pytest.mark.parametrize("person_id, status_code, type_test", [
    ("111", 200, "Happy path"),            # happy path
    ("", 400, "Sad path"),           # sad path
])
def test_post_person(person_api, person_id, status_code, type_test):
    try:
        response = person_api.post_request_person_data(person_id)

        # Validate response status
        assert response.status_code == status_code, (
            f"Error: The expected status = {status_code}" + 
            f"but response returned {response.status_code}"
        )

        # Validate response json
        try:
            response_json = response.json()
            # Validate data from the json
            
        except ValueError:
            raise AssertionError(
                "The response JSON does not exist or is not valid"
            )
        
        # Log if the test is executed correctly
        print(f"{type_test}: POST person data executed succesfull")

    except Exception as e:
        print(f"Error with this ID '{person_id}': {e}")
        raise
