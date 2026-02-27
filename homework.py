from selene import browser, have, command
import time

def test_student_registration_form():
    # Увеличиваем таймаут до 10 секунд для всех операций
    browser.config.timeout = 10

    base_url = "https://demoqa.com"
    form_path = "/automation-practice-form"

    # 1. ОТКРЫВАЕМ ФОРМУ
    browser.open(base_url + form_path)

    # 2. УДАЛЯЕМ БАННЕРЫ (исправлен JavaScript)
    browser.driver.execute_script('var el = document.querySelector("#fixedban"); if (el) el.remove();')
    browser.driver.execute_script('var el = document.querySelector("footer"); if (el) el.remove();')

    # 3. ЯВНО ЖДЁМ ПОЯВЛЕНИЯ ПОЛЯ ИМЕНИ
    browser.element('#firstName').should(have.exact_text('').or_(have.no.text)).type('Ivan')

    # Далее остальная часть теста...
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('ivan@example.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('1234567890')

    # 4. КАЛЕНДАРЬ
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.all('.react-datepicker__month-select option').element_by(have.text('May')).click()
    browser.element('.react-datepicker__year-select').click()
    browser.all('.react-datepicker__year-select option').element_by(have.text('1995')).click()
    browser.element('.react-datepicker__day--015').click()

    # 5. ПРЕДМЕТЫ
    browser.element('#subjectsInput').type('Computer Science')
    browser.all('.subjects-auto-complete__option').should(have.size_greater_than(0))
    browser.element('#subjectsInput').press_enter()

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#currentAddress').type('Some street 123')

    # 6. ШТАТ И ГОРОД
    browser.element('#state').click()
    browser.all('//div[contains(text(), "NCR")]').should(have.size_greater_than(0)).first.click()

    browser.element('#city').click()
    browser.all('//div[contains(text(), "Delhi")]').should(have.size_greater_than(0)).first.click()

    # 7. SUBMIT
    browser.element('#submit').perform(command.js.click)

    # 8. ПРОВЕРКИ
    browser.element('.modal-content').should(have.text_containing('Thanks for submitting the form'))
    browser.element('.table-responsive').should(have.text_containing('Ivan Ivanov'))