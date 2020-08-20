
# CollabU

CollabU is a web application designed specifically for mobile devices. It is a valuable resourse for students who are willing to reach out to their peers, build their network or ask for advice with no access to their campus! (which is especially useful during the transition to online distance learning)

CollabU's target audience is currently enrolled students, but is not limited to only enrolled ones! Alumnis and high school folks who are considering different university/college options will also find it helpful!

CollabU relies on the matching algorithm which will take user's information (student's school, major and currently enrolled classes), ask for a desired service (Careed Advice, Major Advice, Classes Advice, Club/Activities, Friendly Chat, Collaboration) and will match the user with people who fit the provided criteria the most.


### Tech

CollabU uses a number of open source projects to work operate:

* [Django](https://www.djangoproject.com/) - a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
CollabU uses Django and its [Django-REST-Framework](https://www.django-rest-framework.org/) to handle backend logic, provide an API and manage the [PostgreSQL](https://www.postgresql.org/) database


* [ReactJS](https://reactjs.org/) - a declarative, efficient, and flexible JavaScript library for building user interfaces.
CollabU uses ReactJS as its main frontend tool to deliver the smooth and enjoyable user experience. 



### Installation

CollabU requires [Python 3.6](https://www.python.org/) or above and [yarn](https://yarnpkg.com/) package manager to be installed on the local machine.

Make sure you have Python 3.6 or above installed on your local machine.

1. Clone/Download this repository and name the folder as you wish
2. Navigate to <folder_name>/backend
3. Create a virtual environment `python -m venv venv`
4. Navigate to your environment and activate it
5. Install the requirements `pip install -r requirements.txt`
6. Create a database `python manage.py migrate`
7. Create a superuser `python manage.py createsuperuser`
8. Run the server `python manage.py runserver`
9. Navigate to <folder_name>/frontend
10. Install the project's dependencies `yarn install`
1Run the React script `yarn start` 

Does it work? No? Perfect. It shouldn't.


### Deployment
Backend endpoints can be accessed at [https://crested-talon-233500.uc.r.appspot.com/](https://crested-talon-233500.uc.r.appspot.com/)


### Todos
 - Clean this mess
 - Integrate frontend with backend
 - Think again about the structure
 - Refactor, refactor, refactor
