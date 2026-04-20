def check_grade(grade):

        if len(grade) > 2:
         return 'Please enter correct grades!!' 
        elif not grade[0].isalpha() :
            return 'You entered a number as a grade'
        else:
            return True


def check_name(name):
       
        if len(name) > 50:
            return 'Really big name lad!!'
        elif len(name) < 5:
            return 'Enter full name nigga!!'
        elif not name.replace(" ","").isalpha() :
            return 'You entered a number in your name field'
        else:
            return True

