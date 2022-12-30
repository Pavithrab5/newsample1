#public method -- can be accesed from any where , by default everything
class Public_Sample_AccessModifier:
    def __init__(self,course,duration):
        self.course=course
        self.duration=duration
    def display_public_class_method(self):
        print("course: {}".format(self.course,self.duration))

publicObj = Public_Sample_AccessModifier


#private -- within the same class

    def display_details(self):
            # select query
            query = ''' select * from EMPLOYEE where NAME = '{0}' SALARY={1} PROJECT={2}'''
            searchQuery = query.format(self.NAME,self.SALARY,self.PROJECT)
            values = cursor.execute(searchQuery)
            print("displaying deatils")

            for fileInfo in values:
                print("NAME: {}  SALARY: {} PROJECT: {}".format(fileInfo.self.NAME, fileInfo.self.SALARY,fileInfo.self.PROJECT))

obj1



