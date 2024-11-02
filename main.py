import requests
from bs4 import BeautifulSoup
import time

# Base URL and year range for the AIME Answer Keys
base_url = "https://artofproblemsolving.com/wiki/index.php/"
years = range(1983, 2025)  # Change the range as needed

def fetch_answer_numbers(year, exam_type):
    # Correct URL construction based on the year and exam type
    if year < 2000:
        url = f"{base_url}{year}_AIME_Answer_Key"
    else:
        url = f"{base_url}{year}_AIME_{exam_type}_Answer_Key"
        
    print(f"Fetching: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve page for {year} {exam_type}: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the ordered list with the answer keys
    ol = soup.find('ol')

    if not ol:
        print(f"Answer key list not found for {year} {exam_type}")
        return None

    answer_numbers = [li.get_text(strip=True) for li in ol.find_all('li')]

    return answer_numbers

all_answers = []
for year in years:
    if year < 2000:
        answers = fetch_answer_numbers(year, '')  # No exam_type for pre-2000
        if answers is not None:
            all_answers.extend(answers)
    else:
        for exam_type in ['I', 'II']:
            answers = fetch_answer_numbers(year, exam_type)
            if answers is not None:
                all_answers.extend(answers)
    time.sleep(1)  # Add delay to prevent rate limiting

# # Print all answer numbers, each on a new line
# for answer in all_answers:
#     print(answer)

# Additional code to save output to a file
output_file = 'aime_scores.txt'

with open(output_file, 'w') as file:
    for answer in all_answers:
        file.write(f"{answer}\n")

print(f"All scores have been saved to {output_file}.")
