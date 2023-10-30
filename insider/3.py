import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def scroll_to_element(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.perform()

# 1
def test_home_page(browser):
    url = "https://useinsider.com/"
    url_home = "https://useinsider.com/"
    browser.get(url)
    if url == url_home:
        print(f"Test Passed: Home page 'https://useinsider.com/' was opened.")
    else:
        print(f"Test Failed: Home page 'https://useinsider.com/' wasn't opened.")

# 2
def test_career_page(browser):
    url = "https://useinsider.com/"
    browser.get(url)
    company_menu = browser.find_element(By.XPATH, "//a[contains(text(), 'Company')]")
    company_menu.click()
    careers_option = browser.find_element(By.XPATH, "//a[contains(text(), 'Careers')]")
    careers_option.click()

    url_career = "https://useinsider.com/careers/"
    WebDriverWait(browser, 10).until(EC.url_to_be(url_career))
    current_url = browser.current_url
    assert current_url == url_career, f"Expected URL: {url_career}, Actual URL: {current_url}"
    if current_url == url_career:
        print(f"Test Passed:'https://useinsider.com/careers/' page was opened.")
    else:
        print(f"Test Failed:'https://useinsider.com/careers/' page wasn't opened.")

    accept_cookies = browser.find_element(By.XPATH, "//a[@id='wt-cli-accept-all-btn']")
    accept_cookies.click()

    teams_block = (By.XPATH, "//section[@id='career-find-our-calling']")
    WebDriverWait(browser, 10).until(EC.presence_of_element_located(teams_block))
    first_block = browser.find_element(*teams_block)
    assert first_block.is_displayed() is not None, print(f"teams_block block is not present.")

    location_block = (By.XPATH, "//section[@id='career-our-location']")
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(location_block))
    except TimeoutException as e:
        print(f"TimeoutException: {e}")
    second_block = browser.find_element(*location_block)
    assert second_block.is_displayed() is not None, print(f"teams_block block is not present.")

    life_at_insider_block = (By.XPATH, "/html/body/div[1]/section[4]")
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(life_at_insider_block))
    except TimeoutException as e:
        print(f"TimeoutException: {e}")
    third_block = browser.find_element(*life_at_insider_block)
    assert third_block.is_displayed() is not None, print(f"teams_block block is not present.")

#3
def test_quality_assurance_page(browser):
    quality_assurance_url = "https://useinsider.com/careers/quality-assurance//"
    browser.get(quality_assurance_url)

    accept_cookies = browser.find_element(By.XPATH, "//a[@id='wt-cli-accept-all-btn']")
    accept_cookies.click()

    see_all_qa_jobs_button = browser.find_element(By.XPATH, "//a[contains(text(), 'See all QA jobs')]")
    see_all_qa_jobs_button.click()

    location_filter = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='top-filter-form']/div[1]/span/span[1]/span")))
    location_filter.click()

    location_option = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//li[contains(text(),'Istanbul, Turkey')]")))
    location_option.click()


    # department_filter = WebDriverWait(browser, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//span[@id='select2-filter-by-department-container']")))
    # department_filter.click()
    #
    # department_option = browser.find_element(By.XPATH, "//li[contains(text(), 'Quality Assurance')]")
    # department_option.click()
    #
    # job_listings = browser.find_elements(By.XPATH, "//section[@id='career-position-list']")
    # assert job_listings, "No job listings found for the selected filters."
    #
    # num_job_listings = len(job_listings)
    # print(f"Number of job listings found: {num_job_listings}")









# def test_quality_assurance_page(browser):
#     quality_assurance_url = "https://useinsider.com/careers/quality-assurance//"
#     browser.get(quality_assurance_url)
#
#     accept_cookies = browser.find_element(By.XPATH, "//a[@id='wt-cli-accept-all-btn']")
#     accept_cookies.click()
#
#     see_all_qa_jobs_button = browser.find_element(By.XPATH, "//a[contains(text(), 'See all QA jobs')]")
#     see_all_qa_jobs_button.click()
#
#
#     location_filter = browser.find_element(By.XPATH, "//span[@id='select2-filter-by-location-container']")
#     location_filter.click()
#
#
#     location_option = browser.find_element(By.XPATH, "//span[@id='select2-filter-by-department-container']")
#     location_option.click()







# 4
# 5

