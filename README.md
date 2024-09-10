# Shortlisted

Shortlisted is a closed circle direct referral network for TV & Film Editors and Assistant Editors. The backend API is written in Python using the Flask server framework. The frontend functionality is built with React and the UI is enhanced with CSS. Shortlisted users can create profiles, connect with their peers, curate lists of references for different job opportunities, and communicate with their peers about the jobs. Each user can list their areas of expertise, and block out days of availability to ensure they appear in shortlists for opportunities that are perfect for them.

## Live Website
https://shortlisted-m7e4.onrender.com

## Table of Contents
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Technical Implementations](#Technical-Implementations)
* [Set Up](#set-up)
* [Screenshots](#screenshots)
* [Wiki Documentation](#wiki-documentation)
* [Contact](#contact)

## Technologies Used

### Frameworks and Libraries
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![BCRYPT](https://img.shields.io/badge/BCRYPT-darkgreen?style=for-the-badge&logo=CryptPad&logoColor=white)

### Database
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

### Hosting
![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)

## Features
 1. Shortlists
 2. Comment Threads

### Future Features
1. Availability Calendar
2. Connections
3. Endorsements
4. Ranked Search
5. Facebook Login
6. Google Maps API Integration

## Technical Implementations

### Filtering Connections by Availability

### Inline Form Fields

### 

## Set Up
To set up and run the project locally, follow these steps:
1. Clone the repository to your local machine:
   
   ```
   git clone https://github.com/dvidale/shortlisted.git
   ```
2. Navigate to the project directory:
```
cd shortlisted
```
3. Install the project dependencies:

   In the frontend directory: `shortlisted/react-vite/`

   ```bash
   npm install
   ```

   In the root directory: `shortlisted/`

   ```bash
   pipenv install -r requirements.txt
   ```

4. Create a .env file from the included example file.

5. Start the development servers:

   Backend directory: `shortlisted/`

   ```bash
   pipenv run flask run
   ```

   Frontend directory: `shortlisted/react-vite/`

   ```bash
   npm run dev
   ```

## Screenshots

### Landing Page
![Landing Page](react-vite/public/assets/screenshots/001_shortlist_landing_page.gif)



##Wiki Documentation

### Find the following additional documentation in our Wiki

- [Database Schema](https://github.com/dvidale/shortlisted/wiki/Database-Schema)
- [Features List](https://github.com/dvidale/shortlisted/wiki/Feature-List)
- [User Stories](https://github.com/dvidale/shortlisted/wiki/User-Stories)
- [API Endpoints](https://github.com/dvidale/shortlisted/wiki/API-Endpoints)
- [Redux Store Tree](https://github.com/dvidale/shortlisted/wiki/Redux-Store-Tree)

## Contact

DeAndré Vidale

- [Github](https://github.com/dvidale)
- [Website](https://deandrevidale.com)
- [Email](mailto:deandre.vidale@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/deandrevidale/)
