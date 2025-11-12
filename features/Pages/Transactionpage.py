from selenium.common import NoSuchElementException

from features.Pages.Basepage import Basepage


class Transactionpage(Basepage):
    def __init__(self, driver):
        super().__init__(driver)

    transaction_xpath = "//span[contains(text(),'Transactions')]"
    transaction_lookup_xpath = "//div[contains(text(),'Transaction Lookup')]"
    tran_pos_lookup_xpath = "//div[contains(text(),'TranPos Lookup')]"
    transaction_lookup_title_xpath = "//h1[contains(text(),'Transaction Lookup')]"
    transaction_start_date_id = "input-534"
    transaction_end_date_id = "input-540"
    transaction_card_number_id = "card_number"
    transaction_merchant_id = "merchant_id"
    more_options_link_xpath = "//a[contains(text(),'More Options')]"
    transaction_device_id = "device_id"
    transaction_authorization_id = "authorization_id"
    transaction_start_time_id = "start_time"
    transaction_end_time_id = "end_time"
    transaction_host_name_id = "host_name"
    transaction_search_button = "//span[contains(text(),'Search')]"
    transaction_masked_checkbox_id = "input-531"
    transaction_pages_number = "//div[contains(@class, 'v-select__selections')]"
    transaction_select_page_number = "//div[@role='option' and normalize-space()='50']"
    details_pos_header = "//h2[text()='Point Of Sale (POS)']"
    details_message_text_field = "//div[normalize-space()='Message Type']/following-sibling::div//div"
    details_pos_entry_mode_field = "//div[normalize-space()='POS Entry Mode']/following-sibling::div//div"
    details_pos_data_field = "//div[normalize-space()='POS Data']/following-sibling::div//div"
    details_pos_condition_field = "//div[normalize-space()='POS Condition Code']/following-sibling::div//div"
    details_general_response_code_field = "//div[normalize-space()='Response Code']/following-sibling::div//div"



    def click_transaction_lookup_page(self):
        self.click_element("xpath", self.transaction_xpath)
        self.wait_method()
        self.click_element("xpath", self.transaction_lookup_xpath)
        self.wait_method()

    def click_transaction_lookup_page_title(self):
        return self.display_element("xpath", self.transaction_lookup_title_xpath)

    def click_masked_checkbox(self):
        self.click_element("id", self.transaction_masked_checkbox_id)

    def enter_transaction_search_fields(self, start_date, end_date, card_number):
        self.wait_method()
        self.send_text("id", self.transaction_start_date_id, start_date)
        self.send_text("id", self.transaction_end_date_id, end_date)
        self.send_text("id", self.transaction_card_number_id, card_number)
        self.send_text("id", self.transaction_end_date_id, end_date)

    def click_search_button(self):
        self.click_element("xpath", self.transaction_search_button)
        self.wait_method()


    def find_transaction_in_lookup_page(self,trn_number):
        transaction_to_be_searched = "//td[contains(text(), '" + trn_number + "')]/parent::tr//a[text()='View']"
        self.wait_until_element("xpath", self.transaction_pages_number)
        self.click_element("xpath", self.transaction_pages_number)
        self.click_element("xpath", self.transaction_select_page_number)
        self.scroll_to_view("xpath", transaction_to_be_searched)
        self.wait_method()
        self.click_element("xpath", transaction_to_be_searched)

    def validate_transaction_details(self, data1, data2, data3,data4):
        assert self.display_element("xpath", self.details_pos_header)
        assert self.getvalue_element("xpath", self.details_pos_entry_mode_field,data1)
        assert self.display_element("xpath", self.details_pos_data_field)
        assert self.getvalue_element("xpath", self.details_pos_data_field, data2)
        assert self.display_element("xpath", self.details_pos_condition_field)
        assert self.getvalue_element("xpath", self.details_pos_condition_field, data3)
        assert self.getvalue_element("xpath", self.details_general_response_code_field, data4)

















