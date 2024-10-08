"""
Script Name: test_hidden_layers_page.py
Description: This script tests the "Hidden Layers" subpage at http://www.uitestingplayground.com/hiddenlayers.
Challenge: Make sure that the test can not interact with the green button after it has been clicked.
Comment: Not happy with this solution using 'try', but since the green button doesn't actually change state, I see no other way.
"""

import pytest
from playwright.sync_api import expect
from pages.hidden_layers_page import HiddenLayersPage

@pytest.fixture
def hidden_layers_page(page) -> HiddenLayersPage:
    hidden_layers_page = HiddenLayersPage(page)
    hidden_layers_page.navigate()
    return hidden_layers_page    

""" Test Scenario: Verify that he page title is 'Hidden Layers'. """
@pytest.mark.hiddenlayers
def test_hidden_layers_page_title(hidden_layers_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'Hidden Layers' page,
        When the page is loaded,
        Then the page title should be 'Hidden Layers'.
    """
    expect(hidden_layers_page.title).to_have_text("Hidden Layers")

@pytest.mark.hiddenlayers
def test_green_button(hidden_layers_page) -> None:
    """
    Test Scenario: Test Clicking Green Button Twice
        Given the user navigates to the 'Hidden Layers' page,
        When they click the Green Button,
        Then the Greeen Button should not be clickable again.
    """
    hidden_layers_page.click_green_button()
    try:
        hidden_layers_page.click_green_button()
        # Failure
        raise AssertionError("Green button should not be clickable after the initial click.")
    except:
        # Success
        pass