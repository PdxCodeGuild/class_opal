# PDX Code Guild Fullstack Developer Capstone
### *James Brennan - 2023.01.14*

## Summary of Capstone Plan -- Investor Portal

### Architecture
The Investor Portal project will use Django with a custom user model for the backend. The database will be a SQLite database that stores user info and parameter values for personalized indexes. (Some stock data for the "universe" for portfolio filtering may be obtained from Yahoo Finance and stored in a separate CSV file.)

Django Rest Framework (DRF) will be used to create an API layer for communication between the frontend and backend.

The frontend will be written in HTML5 and CSS with dynamic elements written in Vue.js. If necessary Django templates may also be used for some pages, and a frontend CSS framework like Bootstrap may be used to create certain page elements.

### Features (v1)
Users will be able to sign up, login, and logout of the portal. Unauthenticated users will have access to a basic interface to query metadata and price history for individual stock tickers.

Authenticated users will be able to create, read, update, and delete personalized indexes, which are essentially lists of stocks and quantities of shares owned. In particular, the application will have an interface to view the metadata associated with all stocks in the index in tabluar form. Users can have multiple personalized indexes stored to their profile and can allocate different amounts of cash to different indexes. Finally, users will be able to download a simple "order form" in CSV format containing stock tickers and quantities.

### Features (v2)
Time permitting, v2 of the software will also be released for the capstone. In v2, the universe of stock data will be integrated into the project database, and the universe will be refreshed automatically according to a set end-of-day schedule.


