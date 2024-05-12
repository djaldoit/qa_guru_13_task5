from selene import have, be, browser
import time


def test_automation_form():
    browser.open('/automation-practice-form')

    # Name, Last name, Email, Gender
    browser.element('#firstName').type('Piter')
    browser.element('#lastName').type('Parker')
    browser.element('#userEmail').type('spiderman@example.com')
    browser.element('#genterWrapper').element('.custom-control-label').click()

    # Phone Number, Date of Birth
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').element('option[value="6"]').click()
    browser.element('.react-datepicker__year-select').element('option[value="1995"]').click()
    browser.element('.react-datepicker__day--028').click()

    # Subjects, Hobbies
    browser.element('#subjectsInput').type('Arts').press_enter()
    browser.element('.//label[@for="hobbies-checkbox-1"]').click()
    browser.element('.//label[@for="hobbies-checkbox-3"]').click()

    # Picture, Address, State and City
    browser.element('#uploadPicture').send_keys('C:/Users/djald/PycharmProjects/qa_guru_13_task5/images/111.jpg')
    browser.element('#currentAddress').type('Vladimir Street 12')
    browser.element('#state').click().element('#react-select-3-option-2').click()
    browser.element('#city').click().element('#react-select-4-option-0').click()

    # Submit
    browser.element('#submit').press_enter()

    # Check
    assert browser.element('.modal-content').should(have.text('Thanks for submitting the form'))
    assert browser.element('.modal-content').should(have.text('Piter Parker'))
    assert browser.element('.modal-content').should(have.text('spiderman@example.com'))
    assert browser.element('.modal-content').should(have.text('Male'))
    assert browser.element('.modal-content').should(have.text('1234567890'))
    assert browser.element('.modal-content').should(have.text('28 June,1995'))
    assert browser.element('.modal-content').should(have.text('Arts'))
    assert browser.element('.modal-content').should(have.text('Sports, Music'))
    assert browser.element('.modal-content').should(have.text('111.jpg'))
    assert browser.element('.modal-content').should(have.text('Vladimir Street 12'))
    assert browser.element('.modal-content').should(have.text('Haryana Karnal'))

    #Close
    browser.element('#closeLargeModal').click()





