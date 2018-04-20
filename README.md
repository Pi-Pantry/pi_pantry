
# pi_pantry

**Authors**: Brandon Holderman, George Ceja, Steven Starwalt

**Version**: 0.1.0


## Overview
This is a UPC based inventory management application that will allow users to keep thier current inventory and make a shopping list that will be available to them anywhere they have internet access.

## Getting Started
- `python3 -m venv env`
- `pip install -e ".[testing]"`
- `initialize_pi_pantry_db development.ini`
- `pytest`
- `pserve development.ini`

## Architecture
This app is written using Python 3.6, following all best practices and industry standards.

### Stack and packages
- Python 3.6
- Pyramid
- SQLAlchemy
- Cookiecutter
- Heroku

## API
Semantics3 UPC database

## Accredidations:
 * The logo is from APKPure.com
 * This app would not have been possible without the help of Megan Flood.
 * Rebecca Prows is the prime architect of the about me page animation.
 
## Change Log in chronilogical order with onewest first

v.1  April 16 2018 - Repo Created
4/19 2130 Final merge pull request #5 from Pi-Pantry/dev to master, deployed master on Heroku 
4/19 2050 Merge pull request #4 from final_merge to dev
4/19 2000 Merge branch '3randon' into final_merge
4/19 1950 final css commit before merge
4/19 1900 removed corpse code in pantry
4/19 1900 18 passing test at 76% coverage
4/19 1800 fixed the detail page logo issue
4/19 1700 2 tests failing, coverage at 78%
4/19 1645 styled the magange items
4/19 1600 removed the theme css
4/19 1400 added styling to the pantry page view
4/19 1300 first swing at style, added the logo and fonts
4/19 1200 allowed the products to be moved and removed from each list
4/19 1100 have 16 passing tests
4/19 1030 fixed code conflicts on merge to dev from steve_thur
4/19 1000 fixed the delete code, working on the pantry.py page
4/19 0930 11 passing tests one failing. working out the bugs
4/18 2245 Users can now remove from their pantry and cart
4/18 2200 Added Delete funtionality to remove from current users data
4/18 2130 added 4 tests for pantry.py and added a table to the pantry page
4/18 2030 created tests for auth_view, 6 created and passing
4/18 2000 added new conftest.py and test_pantry.py
4/18 1900 added test folder and files
4/18 1800 merged the bnrandon code to dev and debugged
4/18 1700 detail view functioning properly after merge with steve_wed_after
4/18 1600 fixed the manage item route
4/18 1530 pulled to dev from 3randon
4/18 1400 css styling on detail page
4/18 1300 can select to move items to either pantry or cart
4/18 1200 merged dev with george branch
4/18 1100 added a new asso. class to address the pantry and shopping lists
4/18 1000 Added funtionality to append to database from Pantry View. CSS changes.
4/18 0930 added pdb to pantry
4/18 0900 all works after converting to association object
4/17 2200 seperated pantry and cart items
4/17 2100 merged merge to master
4/17 1800 fixed the req.txt
4/17 1700 added the new Procfile and code for Heroku deployment
4/17 1630 deleted the ProcFile because of case issues
4/17 1200 added the code from the notes to production.ini
4/17 1145 added a new req.txt for Heroku deployemnt
4/17 1100 ready to deploy, again
4/17 1000 added the heroku code and rebuilt the ENV
4/17 0930 Authentication up and running
4/17 0900 cleaned up detail.jinja, added travis, removed corpse code in pantry
4/16 2200 detail functioning properly
4/16 2130 Fixed a couple missing imports from semantics3.
4/16 2100 scans attaching to assoc table and add to users pantry
4/16 2030 Handled API Response Errors, fixed semi commented code in templates, scanning properly and adding to database
4/16 1800 added doc strings and added pantry view, see detail view working
4/16 1600 Users can now scan products and add to our database.
4/16 1400 auth functioning properly
4/16 1200 Localhost displaying mock_data
4/16 1000 Update README.md
4/16 0930 cleaned up code on default
4/15 2200 presenting detail information on page
4/15 2100 no errors but not displaying mock data
4/15 1800 fixed typo from copy paste, error pi_pantry has no attribute main, 
4/15 1600 Created functionality To Parse Data from API CALL, Added to view_confid
4/15 1200 setup up scaffold for post and delete requests
4/15 1130 Added semantics3 Lib(API CALLS).
4/15 1000 built models and building views
4/15 0950created readme
4/15 0930 Initial commit
