from pages.main_page import MainPage

class TestConstructor:

    def test_switch_to_buns_section(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        main_page = MainPage(driver)

        # Для надежности кликнем по соусам, а потом обратно на булки
        main_page.click_sauces_section()
        main_page.click_buns_section()

        active_section = main_page.get_active_section_text()
        assert active_section == "Булки", "Активный раздел не 'Булки'"

    def test_switch_to_sauces_section(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        main_page = MainPage(driver)

        main_page.click_sauces_section()

        active_section = main_page.get_active_section_text()
        assert active_section == "Соусы", "Активный раздел не 'Соусы'"

    def test_switch_to_fillings_section(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        main_page = MainPage(driver)

        main_page.click_fillings_section()

        active_section = main_page.get_active_section_text()
        assert active_section == "Начинки", "Активный раздел не 'Начинки'"