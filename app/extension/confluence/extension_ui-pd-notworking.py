from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from util.conf import CONFLUENCE_SETTINGS

TC_TITLE_DISPLAY_TABLE = "Test Case Display Table"
TC_TITLE_TRANSCLUDE_DOCUMENTS = "Test Case Transclude from Documents"


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_pages']:
        app_specific_page_id = datasets['custom_page_id']

# Mergeprobleme ??
#    print(f'Custom page  {datasets['custom_page_id']} form spacekey {datasets['custom_space_key']} OR {datasets['custom_spacekey']}')

    mykeys=','.join(str(e) for e in datasets['custom_pages'])
    print(f"Custom page  {datasets['custom_page_id']} form spacekey {mykeys}")

    # To run action as specific user uncomment code bellow.
    # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
    # just before test_2_selenium_z_log_out
    # @print_timing("selenium_app_specific_user_login")
    # def measure():
    #     def app_specific_user_login(username='admin', password='admin'):
    #         login_page = Login(webdriver)
    #         login_page.delete_all_cookies()
    #         login_page.go_to()
    #         login_page.wait_for_page_loaded()
    #         login_page.set_credentials(username=username, password=password)
    #         login_page.click_login_button()
    #         if login_page.is_first_login():
    #             login_page.first_user_setup()
    #         all_updates_page = AllUpdates(webdriver)
    #         all_updates_page.wait_for_page_loaded()
    #     app_specific_user_login(username='admin', password='admin')
    # measure()

    @print_timing("selenium_app_custom_action")
    def measure():

        @print_timing("selenium_app_custom_action:view_page")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/pages/viewpage.action?pageId={app_specific_page_id}")
            page.wait_until_visible(
                (By.ID, "title-text"))  # Wait for title field visible

            title = page.get_element((By.ID, "title-text")).text
            if (TC_TITLE_DISPLAY_TABLE == title):
                print(f"XXXXX found Display Table")
                # page.wait_until_visible((By.ID, "projectdoc-success"))
                i = 1
            elif (TC_TITLE_TRANSCLUDE_DOCUMENTS == title):
                print(f"XXXXX found Transclusion")
                # page.wait_until_visible((By.ID, "projectdoc-success"))
                i = 2

        sub_measure()

    measure()