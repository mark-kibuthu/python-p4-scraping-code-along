from bs4 import BeautifulSoup
import requests
from Course import Course  # Assuming Course class is defined in Course.py

class Scraper:
    def __init__(self):
        self.courses = []

    def get_page(self):
        """Fetches the HTML document from the course listing page."""
        doc = BeautifulSoup(
            requests.get(
                "http://learn-co-curriculum.github.io/site-for-scraping/courses"
            ).text,
            'html.parser'
        )
        return doc

    def get_courses(self):
        """Returns a collection of course elements from the HTML document."""
        return self.get_page().select('.post')

    def make_courses(self):
        """Creates Course objects for each course and adds them to the courses list."""
        for course in self.get_courses():
            title = course.select("h2")[0].text if course.select("h2") else ''
            date = course.select(".date")[0].text if course.select(".date") else ''
            description = course.select("p")[0].text if course.select("p") else ''

            new_course = Course(title, date, description)
            self.courses.append(new_course)
        return self.courses

    def print_courses(self):
        """Prints out the details of each course."""
        for course in self.make_courses():
            print(course)  # Assuming the Course class has a __str__ method implemented

# This will execute the print_courses method when the script is run.
if __name__ == "__main__":
    scraper = Scraper()
    scraper.print_courses()
