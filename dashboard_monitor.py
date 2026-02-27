def check_dashboard_error():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    import os
    from dotenv import load_dotenv
    load_dotenv()

    options = Options()
    options.add_argument('--headless')  # O quita esto para ver el navegador
    driver = webdriver.Chrome(options=options)
    driver.get(os.getenv("DASHBOARD_URL"))

    error = driver.find_element(By.ID, "error-code").text
    driver.quit()
    return int(error)
