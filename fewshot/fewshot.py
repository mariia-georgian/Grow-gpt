class FewShot:

    @staticmethod
    def get_examples():
        examples = [
        {
            "question": """We have tabular data about the leads that are most likely to convert into paying customers.
            What is the Converted value here? Output one word.
            Do Not Email: No, Do Not Call: No, Converted: ?, TotalVisits: 0.0, Total Time Spent on Website: 0, Page Views Per Visit: 0.0, Last Activity: Page Visited on Website, Country: nan, Specialization: Select, How did you hear about X Education: Select, What is your current occupation: Unemployed, What matters most to you in choosing a course: Better Career Prospects, I agree to pay the amount through cheque: No, A free copy of Mastering The Interview: No, Last Notable Activity: Modified
            """,
            "answer": "True",
        },
        {
            "question": """We have tabular data about the leads that are most likely to convert into paying customers.
            What is the Converted value here? Output one word.
            Do Not Email: No, Do Not Call: No, Converted: ?, TotalVisits: 5.0, Total Time Spent on Website: 674, Page Views Per Visit: 2.5, Last Activity: Email Opened, Country: India, Specialization: Select, How did you hear about X Education: Select, What is your current occupation: Unemployed, What matters most to you in choosing a course: Better Career Prospects, I agree to pay the amount through cheque: No, A free copy of Mastering The Interview: No, Last Notable Activity: Email Opened
            """,
            "answer": "False",
        },
        {
            "question": """We have tabular data about the leads that are most likely to convert into paying customers.
            What is the Converted value here? Output one word.
            Do Not Email: No, Do Not Call: No, Converted: ?, TotalVisits: 2.0, Total Time Spent on Website: 1532, Page Views Per Visit: 2.0, Last Activity: Email Opened, Country: India, Specialization: Business Administration, How did you hear about X Education: Select, What is your current occupation: Student, What matters most to you in choosing a course: Better Career Prospects, I agree to pay the amount through cheque: No, A free copy of Mastering The Interview: Yes, Last Notable Activity: Email Opened
            """,
            "answer": "True",
        },
        {
            "question": """We have tabular data about the leads that are most likely to convert into paying customers.
            What is the Converted value here? Output one word.
           Do Not Email: No, Do Not Call: No, Converted: ?, TotalVisits: 1.0, Total Time Spent on Website: 305, Page Views Per Visit: 1.0, Last Activity: Unreachable, Country: India, Specialization: Media and Advertising, How did you hear about X Education: Word Of Mouth, What is your current occupation: Unemployed, What matters most to you in choosing a course: Better Career Prospects, I agree to pay the amount through cheque: No, A free copy of Mastering The Interview: No, Last Notable Activity: Modified
            """,
            "answer": "False",
        },
        {
            "question": """We have tabular data about the leads that are most likely to convert into paying customers.
            What is the Converted value here? Output one word.
           Do Not Email: No, Do Not Call: No, Converted: 1, TotalVisits: 2.0, Total Time Spent on Website: 1428, Page Views Per Visit: 1.0, Last Activity: Converted to Lead, Country: India, Specialization: Select, How did you hear about X Education: Other, What is your current occupation: Unemployed, What matters most to you in choosing a course: Better Career Prospects, I agree to pay the amount through cheque: No, A free copy of Mastering The Interview: No, Last Notable Activity: Modified
            """,
            "answer": "True",
        },
        {
            "question": """We have tabular data about the leads that are most likely to convert into paying customers.
            What is the Converted value here? Output one word.
           Do Not Email: No, Do Not Call: No, Converted: 0, TotalVisits: 0.0, Total Time Spent on Website: 0, Page Views Per Visit: 0.0, Last Activity: Olark Chat Conversation, Country: nan, Specialization: nan, How did you hear about X Education: nan, What is your current occupation: nan, What matters most to you in choosing a course: nan, I agree to pay the amount through cheque: No, A free copy of Mastering The Interview: No, Last Notable Activity: Modified
            """,
            "answer": "False",
        }]
        return examples
  
    @staticmethod
    def get_example_template():
        template = """
        Question: {question}

        Answer: {answer}
        """
        example_variables = ["question", "answer"]
        return template, example_variables

    @staticmethod
    def get_prefix():
        return f"""
        I have data for most promising leads, i.e. the leads that are most likely to convert 
        into paying customers. Look at these examples where each value corresponds to the 
        appropriate column that I gave earlier. Try to find a pattern for making decision for
          Converted value. For the Converted values write just True of False.
        """

    @staticmethod
    def get_suffix():
        return """
                Question: {question}

                Answer: 
                """