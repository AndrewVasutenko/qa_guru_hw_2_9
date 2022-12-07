import allure
from selene.support.shared import browser
from Models import controls
from Models import pages
from selene.support.conditions import have

@allure.title("Successful fill form")
def test_demo_qa_form():

    with allure.step("start demoqa"):
        browser.open("https://demoqa.com/automation-practice-form")

    with allure.step("fill form"):
        pages.fill_fullname("Andrew", "Vasutenko")
        pages.fill_user_email("qqqqq@qqqq.qq")
        controls.select_gender_male()
        pages.fill_user_number_phone("8800555353")
        controls.fill_date_of_birthday("07 December,2022")
        pages.fill_subjects(("Art", "Commerce"))
        controls.select_hobby_music()
        controls.download_picture()
        pages.fill_curent_adress("Russia,Moscow")
        controls.select_state_and_city("Rajasthan", "Jaipur")
        controls.submit()

    with allure.step("check result"):
        pages.table_result.should(have.text("Andrew"))
        pages.table_result.should(have.text("Vasutenko"))
        pages.table_result.should(have.text("qqqqq@qqqq.qq"))
        pages.table_result.should(have.text("Male"))
        pages.table_result.should(have.text("8800555353"))
        pages.table_result.should(have.text("07 December,2022"))
        pages.table_result.should(have.text("Arts, Commerce"))
        pages.table_result.should(have.text("Music"))
        pages.table_result.should(have.text("meme.jpg"))
        pages.table_result.should(have.text("Russia,Moscow"))
        pages.table_result.should(have.text("Rajasthan"))
        pages.table_result.should(have.text("Jaipur"))
        browser.element("#closeLargeModal").double_click()
        browser.close()