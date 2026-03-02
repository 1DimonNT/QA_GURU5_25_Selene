import os

from selene import browser, command, have


def test_fill_practice_form():
    # 1. Открываем форму
    browser.open("https://demoqa.com/automation-practice-form")

    # 2. Убираем мешающие баннеры
    browser.execute_script('document.getElementById("fixedban")?.remove();')
    browser.execute_script('document.querySelector("footer")?.remove();')

    # 3. Имя, Фамилия, Почта
    browser.element("#firstName").type("Dmitry")
    browser.element("#lastName").type("QA_GURU")
    browser.element("#userEmail").type("test@qaguru.ru")

    # 4. Пол (Клик по Label для Male)
    browser.element('[for="gender-radio-1"]').click()

    # 5. Телефон
    browser.element("#userNumber").type("1234567890")

    # 6. Дата рождения
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").send_keys("June")
    browser.element(".react-datepicker__year-select").send_keys("1995")
    browser.element(
        ".react-datepicker__day--015:not(.react-datepicker__day--outside-month)"
    ).click()

    # 7. Предметы
    browser.element("#subjectsInput").type("Computer Science").press_enter()

    # 8. Хобби
    browser.element('[for="hobbies-checkbox-2"]').should(have.text("Reading")).click()

    # 9. Загрузка файла
    browser.element("#uploadPicture").send_keys(os.path.abspath("tests/photo.jpg"))

    # 10. Адрес
    browser.element("#currentAddress").type("Russia, Nizhny Tagil")

    # 11. Штат и Город
    browser.element("#state").click()
    browser.all('//div[contains(text(), "NCR")]').should(
        have.size_greater_than(0)
    ).first.click()

    browser.element("#city").click()
    browser.all('//div[contains(text(), "Delhi")]').should(
        have.size_greater_than(0)
    ).first.click()

    # 12. Submit
    browser.element("#submit").perform(command.js.click)

    # 13. Проверки
    browser.element(".modal-content").should(
        have.text("Thanks for submitting the form")
    )
    browser.element(".table-responsive").should(have.text("Dmitry QA_GURU"))