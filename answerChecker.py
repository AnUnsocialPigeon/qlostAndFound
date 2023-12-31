import math

##############################################################
##    PLEASE DO NOT EDIT THIS FILE WITHOUT PERMISSION       ##
##        - WILL SAP THE FUN OUT OF THE ACTIVITY -          ##
##    (unless its broken in which case, please do :) )      ##
##############################################################


def parse_to_dict(input_string):
    result = {}
    for line in input_string:
        components = line.split(',')
        name = components[0]

        # Get the coords
        coordinates = []
        for coord_str in components[1:]:
            coord_tuple = tuple(map(int, coord_str.strip('()').split(':')))
            coordinates.append(coord_tuple)
        result[name] = coordinates
    return result

# The Checker class which will be used for the tests.
class Checker:
    def __init__(self):
        """
        Initialize the Checker object by reading answers from the "answers.txt" file.

        Note: if anything doesn't work, blame Jake :) This was made tooooo late at night NGL... (+ it is untested. Unlike real software)

        Raises:
            IOError: If there is an error reading the "answers.txt" file.
        """
        try: 
            with open("./answers.txt") as file:
                self.__answer_dict = parse_to_dict(file.readlines())
        except IOError as e:
            print(f"Error reading {e}")    

    def get_example_file_name(self):
        """
        Get an example file name from the answers. 
        Imperative that the file_name given to check_answers is formatted the same as this function's return.

        Returns:
            str: An example file name from the answers.
        """
        return next(iter(self.__answer_dict))
    

    def hello(self):
        """
        A hello from the program! :D
        """
        length = len(self.__answer_dict)
        if (length < 1):
            print("There is no data in the checker. Something may have gone wrong, or you forgot to create the data.")
            return 
        print(f"Checker is instantiated correctly! There is {length} members of data loaded")


    def check_answer(self, file_name, x, y):
        """
        Check if the given (x, y) coordinates lie inside a circle with properties specified by the file name.

        Args:
            file_name (str): The file name specifying the challenge attempted. You may only attempt each file once (per run)!
            x (float): The x-coordinate of the point to check.
            y (float): The y-coordinate of the point to check.

        Returns:
            float: An accuracy score. -1 for a wrong answer, 5 for perfect, gradiented out to 0. An incorrect file name will also score -1.

        """
        # Check if file name correct
        if file_name not in self.__answer_dict:
            return -1

        circles = self.__answer_dict[file_name]
        for circle_properties in circles:
            c_x = circle_properties[0]
            c_y = circle_properties[1]
            r = circle_properties[2]
            
            # Return if x and y are in the circle with center c_x, c_y, radius r.
            if (x - c_x)**2 + (y - c_y)**2 <= r**2:
                unit_distance = math.sqrt((x - c_x)**2 + (y - c_y)**2) / r
                return 5 - (unit_distance * 5)
        
        return -1