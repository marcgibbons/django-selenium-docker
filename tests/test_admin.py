from functools import partial

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement

User = get_user_model()


def test_create_new_group(
    base_url: str,
    driver: Remote,
    query_selector: partial[WebElement],
) -> None:
    # Create a superuser
    user = User.objects.create(
        username="george",
        is_staff=True,
        is_superuser=True,
    )
    user.set_password("costanza123")
    user.save()

    # Go to admin login
    driver.get(base_url + "/admin/")

    # Log in user
    query_selector("input[name=username]").send_keys("george")
    query_selector("input[name=password]").send_keys("costanza123")
    query_selector("input[type=submit]").click()

    # Create a new group
    query_selector(".model-group .addlink").click()
    query_selector("input[name=name]").send_keys("Vandelay Industries\n")

    # Assert that the group was created successfully.
    success_element = query_selector(".messagelist .success")
    expected = "The group “Vandelay Industries” was added successfully."
    assert success_element.text == expected

    # Assert that the group was added to the database.
    assert Group.objects.filter(name="Vandelay Industries").exists() is True
