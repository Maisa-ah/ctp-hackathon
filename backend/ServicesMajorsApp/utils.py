"""
Terrible mapper

* Calculates the total "matching" score
* by comparing users' models values
* (school, major, number of mutual classes)

"""


def mapper(service, user, compareUser):

    # initialize total points to 0. Pretty straightforward, heh?
    total_points = 0

    # if, if, if. If school, if major, blah blah blah
    if user['school'] == compareUser.school.school_code:
        total_points += 2

    if user['major'] == compareUser.major.major_code:
        total_points += 1
            
    # Okay, here is gets worse. We make a call to the database to
    # fetch all services associated with this user. Remember,
    # we are iterating over a queryset and we will do this a lot of times
    compareUserServices = compareUser.services.all()

    # look for the intersection of classes. The more mutual classes - the more points
    total_points += len(set(user['classes']).intersection(set(compareUserServices)))

    return { 
            'score': total_points,
            'user': compareUser
        }