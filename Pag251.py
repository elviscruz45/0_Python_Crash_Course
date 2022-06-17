#Unit Tests and Test Cases
import unittest

from Pag249 import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for 'Pag249'"""
    def test_first_last_name(self):
        """DO names like Hanis Hoplin Work?"""
        formated_name=get_formatted_name("Janis","Joplin")
        self.assertEqual(formated_name,"Janis Joplin")
        
unittest.main()