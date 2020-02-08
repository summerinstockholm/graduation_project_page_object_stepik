# Основная идея состоит в том, что каждую страницу веб-приложения можно описать в виде объекта класса.
# Способы взаимодействия пользователя со страницей можно описать с помощью методов класса. В идеале тест, который будет использовать Page Object,
# должен описывать бизнес-логику тестового сценария и скрывать Selenium-методы взаимодействия с браузером и страницей.
# При изменениях в верстке страницы не придется исправлять тесты, связанные с этой страницей. Вместо этого нужно будет поправить только класс, описывающий страницу.
from .pages.main_page import MainPage
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()                      # открываем страницу
    page.go_to_login_page()
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()