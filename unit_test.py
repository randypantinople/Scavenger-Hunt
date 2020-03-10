# -*- coding: utf-8 -*-

import unittest
from Challenge import Challenge

class Test_Challenge(unittest.TestCase):
    
    def test_questions(self):
        """
        Test the get_questions function from the Challenge class
        """
        
        #List of actual questions
        questions_list = ["Challenge 1: When Steve woke up. His temperature was" 
         " 102-degree Fahrenheit.Two hours later it was 3 degree" 
         " Fahrenheit lower.What was his temperature then?",
         
         "Challenge 2: An elevator is on the twentieth floor. It goes down 11"
         " floors and then up 5 floors. What floor is the elevatoron now?",
         
         "Challenge 3: Some number added to -11 is 37. Divide this number by"
         " -12. Then, multiply by -8. What is the final number?",
         
         "Challenge 4: If it is 5 degree Fahrenheit outside and the temperature"
         " will drop 17 degree Fahrenheit in the next six hours, how cold will it get?",
         
         "Challenge 5: Josie has $47 left on her checking account."
         " If she writes a check for $55, what will Josie’s balance be?",
         
         "Challenge 6: A scuba diver swam 96 feet beneath the surface of the lake."
          " He then climbs up 49 feet. What is his depth now?",
          
          "Challenge 7: The temperature was –3 degree Celsius last night."
          " It is now –4 degree Celsius. What was the change in temperature?",
          
          "Challenge 8: Sonny has $75 to spend. The purchase he wants to make"
          " requires $93. If he borrows the extra money that he needs, how much"
          " does he need to borrow?",
          
          "Challenge 9: Steve has overdrawn his checking account by $27.  His"
          " bank charged him $15 for an overdraft fee.  Then he quickly"
          " deposited $100.  What is his current balance?",
          
          "Challenge 10: The local movie theater reported losses of $475 each"
          " day for three days. What was the loss for the three days?"]
         
         #Test each actual questions with  the  questions from get_questions function
        for i in range(10):
            self.assertEqual(Challenge.get_questions(self)[i], questions_list[i])
    
    def test_answer_key(self):
        """
        Test the get_answer_key function from the Challenge class
        
        """
        #List for an actual keys
        answer_key_list =[99, 14, 32, -12, -8, -47, -1, 18, 58, -1425]
        
        #Test each actual key with  the  keys from get_answer_key function
        for i in range(10):
            self.assertEqual(Challenge.get_answer_key(self)[i], answer_key_list[i])
        
    def test_code(self):
        """
        Test the __get_code function the Challenge class
        """
        #List of actual codes
        code_list = ["R", "H", "O", "G", "T", "S", "L", "M", "I", "A"]
        
        #Check each code from the list with the code from the function
        for i in range(10):
            self.assertEqual(Challenge._Challenge__get_code(self)[i], code_list[i])
        
    
        
if __name__ =="__main__":
    unittest.main()
        
        
