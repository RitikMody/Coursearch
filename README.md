
Coursearch 💻 📝 📚
============

[![](https://img.shields.io/badge/Made_with-Python3-blue?style=for-the-badge&logo=python)]()
[![](https://img.shields.io/badge/Made_with-flask-blue?style=for-the-badge&logo=flask)]()
[![](https://img.shields.io/badge/Made_with-pandas-blue?style=for-the-badge&logo=pandas)]()
[![](https://img.shields.io/badge/Made_with-selenium-blue?style=for-the-badge&logo=selenium)]()
[![](https://img.shields.io/badge/Made_with-crochet-blue?style=for-the-badge&logo=crochet)]()
[![](https://img.shields.io/badge/Made_with-scrapy-blue?style=for-the-badge&logo=scrapy)]()
[![](https://img.shields.io/badge/Made_with-material_design-blue?style=for-the-badge&logo=material-design)]()
[![](https://img.shields.io/badge/deployed_on-heroku-blue?style=for-the-badge&logo=heroku)]()

A one stop solution to navigate the endless sea of online courses.

This is our submission for the HackChennai Hackathon 2020. It was made under 36 hours with no prior preparation.

---

## The problem:
- In the past few years, the popularity of MOOC platforms has skyrocketed, prompting many other such platforms to crop up.
- However, not many users are satisfied with all the courses present.
- Sometimes the level of difficulty is too high, or the hands-on labs are outdated, or the instructor hides behind technical jargon, or the videos lack contextual clarity and so on.
- With so many courses coming up, it is essential for the learner to save time and money by choosing only the best course available.

---

## The solution:
- Why not let the user select something they want to learn and leave the choosing courses to us?
- Why not gather data from multiple MOOC platforms?
- Why not use this data of ratings and reviews to rank courses with a unique method? 
- Why not let the user view this combined information in one place where they can easily search, sort and visit these courses?

---

## Features:

- Crawls information from Coursera, Udemy, Pluralsight and Udacity (in progress) to gather MOOC data for any search term.
- Ranks the courses using a weighted average of their number of reviews and the average rating (out of five.)
- Allows the user to further filter the results on any basis they want: difficulty, ratings, intructor, etc.
- Additional search option is provided in the table too.
- Users can find direct links to any MOOC.
- The `/api` endpoint can be used by anyone to query data using parameters defined in the documentation.

---

## Tech stack:

- `flask:` web framework.
- `python:` backend routing and web crawlers.
- `jinja2:` templating and rendering frontend.
- `scrapy`, `selenium` and `beautifulsoup:` data mining.
- `crochet:` running the reactor for consecutive searches.
- `pandas` and `json:` formatting and cleaning the dataframe.
- `Material Design` and `Bootstrap:` styling the frontend.

---

## Deployment:

The live project is deployed on https://coursearch.herokuapp.com/. You may use it to search MOOCS, use the API for your projects or run it locally using the instructions below.

---

## Local installation:

**You must have Python 3.6 or higher to run the file.**

- Create a new virtual environment for running the application. You can follow the instructions [here.](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)
- Navigate to the virtual environment and activate it.
- Install the dependancies using `pip install -r requirements.txt`
- Run the `app.py` file with `python app.py`

**Note:** to run it locally, you must have a version of `chromedriver.exe` that matches the one installed on your device. 

---

## Future scope:

- Convert the website into a PWA.
- Explore and mine data from other platforms too.
- Add a variety of parameters to the `/api` endpoint.

We are open to enhancement and bug fixes: fork and clone this repository, submit a pull request and we'll test your changes before merging them!

---

<p align="center">Made with ❤️ by Team Infinity.</p>
