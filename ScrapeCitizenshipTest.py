from playwright.sync_api import sync_playwright
import pandas as pd
import time

url = 'https://www.torontopubliclibrary.ca/new-to-canada/citizenship.jsp'

results = []

with sync_playwright() as pw:
    
    browser = pw.chromium.launch(headless=False,)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    
    page = context.new_page()
    page.goto(url, wait_until="networkidle")
    time.sleep(5)
    
    for x in range(60):
        print("Getting Question ", x)
        
        result = {}
        name_q = x+1

        # Get question
        
        result['question'] = page.locator(".components-CitizenshipTest-___styles__position___2t2vL").text_content()
        result['answerA'] =page.locator("button.components-CitizenshipTest-___styles__question-button___3GI40:nth-child(1)").text_content()
        result['answerB'] = page.locator("button.components-CitizenshipTest-___styles__question-button___3GI40:nth-child(2)").text_content()
        result['answerC'] = page.locator("button.components-CitizenshipTest-___styles__question-button___3GI40:nth-child(3)").text_content()
        result['answerD'] = page.locator("button.components-CitizenshipTest-___styles__question-button___3GI40:nth-child(4)").text_content()
                
        # get correct answer
        page.locator("button.components-CitizenshipTest-___styles__question-button___3GI40:nth-child(1)").click()
        page.wait_for_load_state("networkidle")
        time.sleep(2)
        page.locator("text=Previous").click()
        page.wait_for_load_state("networkidle")
        time.sleep(1)       
        answer = page.locator(".components-CitizenshipTest-___styles__successful___1Hd_c")
        count = answer.count()
        if count > 1:
            result['correct_answer'] = answer.nth(count-1).text_content()
        else:
            result['correct_answer'] = answer.text_content()
        
        # append results
        results.append(result)

        print(result)
        print()
        
        # Go to next question
        page.locator("text=Next").click()
        page.wait_for_load_state("networkidle")
        time.sleep(1)

# results to dataframe
df = pd.DataFrame(results)
df.to_excel('questions.xlsx', index=False)

