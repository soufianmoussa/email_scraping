import csv
import re
import requests

def extract_emails_from_websites(urls):
    email_data = []
    email_pattern = re.compile(r'''[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?''', flags=re.IGNORECASE)

    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)
            html = response.text
            emails = set(email_pattern.findall(html))  # Store emails in a set to eliminate duplicates
            email_data.append((url, emails))

        except requests.exceptions.HTTPError as err:
            print(f"Cannot retrieve URL {url}: HTTP Error Code: {err.response.status_code}")
        except requests.exceptions.RequestException as err:
            print(f"Cannot retrieve URL {url}: {err}")

    return email_data

def write_emails_to_csv(email_data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Website', 'Emails'])
        for website, emails in email_data:
            writer.writerow([website, ', '.join(emails)])

# Example usage:
websites = ["https://www.ucd.ac.ma/", 
            "https://www.goandev.net/",
            "https://www.slideshare.net/slideshows/email-test-code-python-ppt-ima-soufiane-test/266456076"
           ]  # Add your list of website URLs here

#return email.csv
output_file = "emails.csv"
email_data = extract_emails_from_websites(websites)
write_emails_to_csv(email_data, output_file)
print(f"Emails extracted and saved to {output_file}")