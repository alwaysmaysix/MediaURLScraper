# MediaURLScraper

MediaURLScraper is a Python script that allows you to easily scrape media URLs from webpages. Whether you're looking to extract video URLs, audio URLs, or source URLs, this script has got you covered!

## Features

- Scrapes media URLs from webpages
- Supports extraction of video URLs, audio URLs, and source URLs
- Uses Python and the Selenium library for web scraping and automation

## Prerequisites

- Python 3.x installed
- Selenium library installed (use `pip install selenium` to install)
- Validators library installed (use `pip install validators` to install)
- Chrome WebDriver installed

Note: This script utilizes the Selenium library with the Chrome WebDriver to automate web interactions. The Chrome WebDriver is a separate executable that allows Selenium to control the Chrome browser. It is necessary to have the Chrome WebDriver installed on your system.

To install the Chrome WebDriver, follow these steps:

-Check your Chrome browser version by navigating to chrome://settings/help in the address bar.
-Visit the official Chrome WebDriver downloads page: Chrome WebDriver [Download Link](https://sites.google.com/a/chromium.org/chromedriver/downloads)
-Download the appropriate Chrome WebDriver version that matches your Chrome browser version.
-Extract the downloaded file and place the WebDriver executable (chromedriver) in a directory accessible to your Python script.
-Ensure that the Chrome WebDriver is properly installed and available in your system's PATH so that the script can locate and use it during execution.

Please make sure to have the Chrome WebDriver installed and configured correctly before running the script.

## Usage

1. Clone or download the repository to your local machine.

2. Install the required Python packages:

3. Set up the Python environment:
- Create a virtual environment (optional but recommended)
- Activate the virtual environment (refer to your platform-specific instructions)

To further simplify the setup process, I've included a setup.bat file in the repository. This batch file handles the environment setup and activation for you. 
-To automate the environment setup, simply double-click the setup.bat file. It will open a command prompt, navigate to the script directory, and activate the virtual environment for you.

4.To make it work, follow these steps:

-Open the script in your favorite text editor or Python IDE.

5.Modify the following parts of the code to match your setup:

-Set the correct file path to the Chrome WebDriver executable:

Service('your_chromedriver_path/chromedriver.exe')

-Adjust the desired file path for exporting the media URLs:

 'your_desired_file_path/media_urls.txt'

6.Save the modified script.

7. Run the script using the following command:

      python script_name.py

8. Follow the prompts to enter the URLs you want to scrape media URLs from. The script will scrape the URLs and display the results.

9. The extracted media URLs will be saved in a file named `media_urls.txt` in the project directory.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute, open issues, or submit pull requests if you have any suggestions or improvements.

Happy scraping!
