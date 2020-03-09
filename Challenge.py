# -*- coding: utf-8 -*-

class Challenge:
    
    def __init__(self, questions = [], answer_key = [], code= []):
        """
        Initializes variables
        """
        self.questions = questions
        self.__answer_key = answer_key
        self.code = code
        
    def get_questions(self):
        """
        Returns a list of questions from the text file
        """
        #Create a list of questions from Questions text file
        self.questions = []
        #Open and read the file
        infile = open("Questions.txt", "r")
        
        #add each line to the list
        for question in infile.readlines():
            self.questions.append(question.strip("\n"))
            
        return self.questions
        
    def get_answer_key(self):
        """
        Access the value of the answer key
        """
        #Create a list of answer key
        self.__answer_key = []
        #Open and read the file
        infile = open("Answer_Key.txt", "r")
        
        #add each key to the list
        for key in infile.readlines():
            self.__answer_key.append(key)
            
        #Convert the data type in integer      
        self.__answer_key = [int(x) for x in self.__answer_key]

        return self.__answer_key
    
    def set_answer_key(self):
        """Sets the value of the answer key"""
        self.__answer_key = answer_key
        
    def __get_code(self):
        """Access the keys for the code"""
        #Open and read the file
        self.code = []
        infile = open("Code.txt", "r")
        
        #add each code to the list
        for letter in infile.readlines():
            self.code.append(letter.strip("\n"))
        
        return self.code
    
    def set_code(self, code):
        """ Sets the keys for the code"""
        self.code = code
        
        
    def __repr__(self):
        return ("Welcome to 'CRACK THE CODE' challenge.")
