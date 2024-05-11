from selene import have, be, browser
import time

def test_automation_form():
    browser.open('/')
    # Name, Last name, Email, Gender
    browser.element('#firstName').type('Piter')
    browser.element('#lastName').type('Parker')
    browser.element('#userEmail').type('spiderman@example.com')
    browser.element('#genterWrapper').element('.custom-control-label').click()

    # Date of Birth, Phone Number, Subjects, Hobbies
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').element('option[value="6"]').click()
    browser.element('.react-datepicker__year-select').element('option[value="1995"]').click()
    browser.element('.react-datepicker__day--028').click()

    # Subjects, Hobbies
    browser.element('#subjectsInput').type('Arts').press_enter()
    # browser.element('#hobbiesWrapper').element('[value=Sports]').click()
    # browser.element('#hobbiesWrapper').all('type*=checkbox')[2].click()

    # Picture, State and City, Address
    browser.element('#uploadPicture').send_keys('C:/Users/djald/PycharmProjects/qa_guru_13_task5/picture/111.jpg')
    browser.element('#currentAddress').type('Vladimir Street 12')
    browser.element('#state').click().press('PageDown').press('Enter')
    # browser.element('#city').click().element('[value=Karnal]').click()
    time.sleep(10)

    # Submit
    browser.element('#submit').press_enter()





