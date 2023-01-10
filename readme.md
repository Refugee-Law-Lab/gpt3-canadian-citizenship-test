# Can GPT-3 Pass the Canadian Citizenship Test?

9 January 2022

**Sean Rehaag**\
Director, Centre for Refugee Studies\
Director, Refugee Law Lab\
Associate Professor, Osgoode Hall Law School\
York University

One of the requirements to obtain Canadian citizenship is to pass a multiple-choice test that that involves questions about Canadian history, geography, economy, government, laws, and important symbols.

Details about the test, along with a study guide, are available [here](https://www.canada.ca/en/immigration-refugees-citizenship/services/canadian-citizenship/become-canadian-citizen/citizenship-test.html).

The notebook, *Can_gpt_pass_citizenship_test.ipynb*, examines whether, as of January 2022, OpenAI's GPT-3 can pass the citizenship test without any fine-tuning, using 60 practice questions made available by the [Toronto Public Library](https://www.torontopubliclibrary.ca/new-to-canada/citizenship.jsp).

You can scrape practice questions and answers from the Toronto Public Library's website by running the *ScrapeCitizenshipTest.py* file from a terminal (scraping uses playwright, which does not work well in Jupyter Notebook):

>pip install pandas
>
>pip install playwright
>
>playwright install
>
>python -m ScrapeCitizenshipTest

Alternatively, you can run the notebook using the Excel file with the scraped data in this repo.

Requirements for the notebook:

>pip install pandas
> 
>pip install openai

To run the notebook, you will also need an API key from OpenAI. Details about obtaining an account are [here](https://beta.openai.com/signup), and details about getting an API key are [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key). Once you have an API key, place it in a text file called SECRETS-OPENAI.txt in the project secrets folder using the template in the folder.

At the end of the notebook, a no-code method to produce similar results using ChatGPT is outlined.

To be cited as: Sean Rehaag, "Can GPT-3 Pass the Canadian Citizenship Test?" (9 January 2022), online: \<https://github.com/Refugee-Law-Lab/gpt3-canadian-citizenship-test\>.

License: [CC BY-NC-SA/4.0](https://creativecommons.org/licenses/by-nc-sa/4.0)