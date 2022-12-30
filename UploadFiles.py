import pyodbc

server = 'HCL-02-29\SQLEXPRESS01'
database = 'FileSearchResults'
username = 'capstone1'
password = 'capstone@1234'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

class UploadFilesToDB:

#to display the contents of the tables from the database
    def show_file_search_results_fromdb(self):
        values = cursor.execute('select * from FileSearchResults_table')
        for fileInfo in values:
            print("File Name: {}".format(fileInfo.NameOfFile))
            print("File Location: {}".format(fileInfo.File_Location))

    def upload_file_results_todb(self,fileName, fileLocation, searchCount):
        query = '''  
                    INSERT INTO FileSearchResults_table (File_Location, SearchCount, NameOfFile)
                    VALUES
                    ('{0}',{1},'{2}')  '''

        insertQuery = query.format(fileLocation, searchCount, fileName)
        cursor.execute(insertQuery)
        cnxn.commit()
        print("New file search results committed to DB")

    # searches for a file in db
    # Input : Filename (string)
    # output : True or False (Boolean)
    def search_in_db_for_file(self, fileName):
        # select query
        query = ''' select * from FileSearchResults_table where NameOfFile = '{0}' '''
        searchQuery = query.format(fileName)
        values = cursor.execute(searchQuery) #excute
        print("File search results from DB.")
        flag=1

        for fileInfo in values:
            #print("==========================")
            print("File name: {} - File path: {} ".format(fileInfo.NameOfFile, fileInfo.File_Location))
            flag=0
            #print("File path: {}".format(fileInfo.File_Location))
            #print("==========================")
        if flag == 0:
            self.update_file_searchcount(fileName)
            #print("updating search count")
            return False
        else:
            return True



    def update_file_searchcount(self, fileName):
        try:
            query = ''' select * from FileSearchResults_table where NameOfFile = '{0}' '''
            searchQuery = query.format(fileName)
            values = cursor.execute(searchQuery)
            for fileInfo in values:
                fileSearchCount = fileInfo.SearchCount
                fileinfoQuery = '''
                        Update FileSearchResults_table SET SearchCount = {0} WHERE NameOfFile = '{1}'
                        '''
                updateQuery = fileinfoQuery.format((fileSearchCount + 1), fileName)
                cursor.execute(updateQuery)
                cursor.commit()
                print("updated file search count")
        except:
            pass