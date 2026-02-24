import os
from selene import browser, have, be, command

def test_fill_practice_form():
    # 1. Открываем форму
    browser.open('https://demoqa.com/automation-practice-form')

    # 2. Убираем мешающие баннеры
    browser.execute_script('document.getElementById("fixedban")?.remove();')
    browser.execute_script('document.querySelector("footer")?.remove();')

    # 3. Имя, Фамилия, Почта
    browser.element('#firstName').type('Dmitry')
    browser.element('#lastName').type('QA_GURU')
    browser.element('#userEmail').type('test@qaguru.ru')

    # 4. Пол (Клик по Label для Male)
    browser.element('[for="gender-radio-1"]').click()

    # 5. Телефон
    browser.element('#userNumber').type('1234567890')

    # 6. Дата рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys('June')
    browser.element('.react-datepicker__year-select').send_keys('1995')
    browser.element('.react-datepicker__day--015:not(.react-datepicker__day--outside-month)').click()

    # 7. Предметы
    browser.element('#subjectsInput').type('Computer Science').press_enter()

    # 8. Хобби
    browser.element('[for="hobbies-checkbox-2"]').should(have.text('Reading')).click()

    # --- ДОБАВЛЕНО: Загрузка файла ---
    browser.element('#uploadPicture').send_keys(os.path.abspath('photo.jpg'))

    # 9. Адрес
    browser.element('#currentAddress').type('Russia, Nizhny Tagil')

    # 10. Штат и Город
    browser.element('#state').click().element('#react-select-3-option-0').click()
    browser.element('#city').click().element('#react-select-4-option-0').click()

    # 11. Нажимаем Submit
    browser.element('#submit').perform(command.js.click)

    # --- ПРОВЕРКИ (Усиленные) ---
    # Проверяем заголовок модального окна
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    # Проверяем ВСЕ данные в таблице одной командой.
    # Мы берем вторую колонку (значения) и сверяем их со списком.
    browser.all('.table td:nth-child(2)').should(have.texts(
        'Dmitry QA_GURU',
        'test@qaguru.ru',
        'Male',
        '1234567890',
        '15 June,1995',
        'Computer Science',
        'Reading',
        'photo.jpg',
        'Russia, Nizhny Tagil',
        'NCR Delhi'
    ))
