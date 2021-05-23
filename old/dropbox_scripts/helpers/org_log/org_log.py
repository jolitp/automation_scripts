#! /usr/bin/python3
"""
'library' to log variables and logic to a file
"""
import os
import inspect
import tokenize
import contextlib
from varname import nameof
from colorama import Fore
from colorama import Style
from datetime import datetime


DEBUG = False
DEBUG = True        # comment to turn off

LOGIC_PRINTS = Fore.LIGHTBLACK_EX
STRING_TO_PRINT = ""

DEBUG_LOGIC = False
DEBUG_LOGIC = True    # comment to turn off


































# DONE get the name of a variable in a string
#      see if the name changes whether its inside a function or not
#
#      importing: from varname import nameof
#
#      use: nameof(variable)
#
#      if used inside a function on a parameter variable it gets the name of the parameter variable
"""
https://stackoverflow.com/questions/18425225/getting-the-name-of-a-variable-as-a-string
"""


































# DONE get nesting level or indentation level
"""
https://stackoverflow.com/questions/39172306/can-a-line-of-python-code-know-its-indentation-nesting-level
"""
def get_indentation_level():
    """ get indentation level of the place where it is called in the script
        Parameters:
            None
        Returns:
            indentation_level (int): the indentation level
    """
    caller_frame = inspect.currentframe().f_back
    filename, caller_lineno, _, _, _ = inspect.getframeinfo(caller_frame)
    with open(filename) as f_n:
        indentation_level = 0
        for token_record in tokenize.generate_tokens(f_n.readline):
            token_type, _, (token_lineno, _), _, _ = token_record
            if token_lineno > caller_lineno:
                break
            elif token_type == tokenize.INDENT:
                indentation_level += 1
            elif token_type == tokenize.DEDENT:
                indentation_level -= 1
        return indentation_level































# TODO refactor the class to only print to the file once and keep a sting in memory
# printing is taking too long, because of all opening and closing of files


# TODO add line numbers to the functions, and print after the *

class OrgLogger:
    """
    Create an Org file with the statements of the script
    """
    # def __init__(self) -> None:
    #     dt_string = datetime.now().strftime("%Y %m %d - %H:%M:%S.%f")
    #     script_name : str = os.path.basename(__file__)
    #     cwd = os.getcwd()
    #     exec_for_folder = '/executions : ' + script_name + '/'
    #     path : str = cwd + exec_for_folder
    #     if not os.path.isdir(path):
    #         os.mkdir(path)
    #         ...
    #     self.org_file_path : str = path + dt_string + '.org'
    #     self.org_file = open(self.org_file_path, 'w+')
    #     self.add_line("#+TODO: IF_BEGIN IF_END | ")
    #     self.add_line("#+TODO: ELSE_BEGIN ELSE_END | ")
    #     self.add_line("#+TODO: FOR_BEGIN FOR_END | ")
    #     self.add_line("#+TODO: WHILE_BEGIN WHILE_END | ")
    #     self.add_line("#+TODO: FUNC_BEGIN FUNC_END | ")
    #     self.add_line("#+TODO: SWITCH_BEGIN SWITCH_END | ")

    #     #+TODO: TODO | DONE
    #     #+TODO: REPORT BUG KNOWNCAUSE | FIXED
    #     #+TODO: | CANCELED

    #     self.org_file.close()

    def __init__(self,
                cwd = os.getcwd(),
                script_name : str = os.path.basename(__file__)) -> None:
        dt_string = datetime.now().strftime("%Y %m %d - %H:%M:%S.%f")
        self.start_time = dt_string
        self.script_name : str = script_name
        self.cwd = cwd
        exec_for_folder = '/executions : ' + script_name + '/'
        path : str = cwd + exec_for_folder
        if not os.path.isdir(path):
            os.mkdir(path)
            ...

        self.lines : str = ""
        self.org_file_path : str = path + dt_string + '.org'
        self.add_line("#+TODO: IF_BEGIN IF_END | ")
        self.add_line("#+TODO: ELSE_BEGIN ELSE_END | ")
        self.add_line("#+TODO: FOR_BEGIN FOR_END | ")
        self.add_line("#+TODO: WHILE_BEGIN WHILE_END | ")
        self.add_line("#+TODO: FUNC_BEGIN FUNC_END | ")
        self.add_line("#+TODO: SWITCH_BEGIN SWITCH_END | ")

        #+TODO: TODO | DONE
        #+TODO: REPORT BUG KNOWNCAUSE | FIXED
        #+TODO: | CANCELED




    def add_line(self,
                line_to_add : str
                ) -> None:
        """
        add line to the org file with a new line character at the end
        """
        self.lines += line_to_add
        # self.org_file = open(self.org_file_path, 'a+')
        # self.org_file.write(line_to_add + '\n')
        # self.org_file.close()



    def print_to_file(self):
        """
        print all lines to
        """


        dt_string = datetime.now().strftime("%Y %m %d - %H:%M:%S.%f")
        end_time = dt_string

        # d1 = datetime.datetime.strptime('2011:10:01:10:30:00', '%Y:%m:%d:%H:%M:%S')
        # d2 = datetime.datetime.strptime('2011:10:01:11:15:00', '%Y:%m:%d:%H:%M:%S')
        # diff = (d2 - d1).total_seconds() / 60

        d1 = datetime.strptime(self.start_time, "%Y %m %d - %H:%M:%S.%f")
        d2 = datetime.strptime(end_time, "%Y %m %d - %H:%M:%S.%f")
        diff = (d2 - d1)

        self.lines += "\n* time to run script: " + str(diff) + "\n"

        org_file = open(self.org_file_path, 'w')
        org_file.write(self.lines)
        org_file.close()
        ...



    def add_blank_line(self) -> None:
        """
        add line to the org file with a new line character at the end
        """
        self.lines += "\n"



    def add_variable(self,
                    variable_value,
                    variable_name : str,
                    indentation : int,
                    comment : str = ''
                    ) -> None:
        """
        add a variable to the org file
        """
        # string of format: * variable_name = variable_value
        # * is indentation level

        header : str = '*'*int(indentation + 1) + " "
        name : str = str(variable_name)
        value_local : str = str(variable_value)
        value_type : str = str(type(variable_value))
        line : str = header + name + ' <- ' + value_local + '\n ( of type ' +  value_type + " )"

        self.add_line(line)

        if comment:
            self.add_line(comment)

        # TODO print a table of members of an array if it is an array

        if type(variable_value) == list:
            table = self.table_of_a_list(variable_value, variable_name)
            self.add_line(table)
            ...
        ...



    def add_if_statement(self,
                        predicate_value,
                        predicate_name : str,
                        indentation : int,
                        comment : str = '',
                        begin_or_end : str = 'begin',
                        inside_or_outside : str = 'outside'
                        ) -> None:
        """add if statement to the org file

            put inside the else clause

        Args:
            predicate_value ([type]):
                the value of the predicate of the IF statement
            predicate_name (str):
                the name of the variable that is the predicate
            indentation (int):
                the indentation level of the calling code
            comment (str, optional):
                a comment to insert after the header. Defaults to ''.
            begin_or_end (str, optional):
                wether it begins or ends the statement. Defaults to 'begin'.
            inside_or_outside (str, optional):
                wether it is inserted (in the calling code) inside or outside the actual statement
        """
        # string of format: * predicate_name = predicate_value
        # * is indentation level

        marker : str = "IF_" + begin_or_end.upper() + " "

        tabs_to_add = 1
        if inside_or_outside == 'outside':
            tabs_to_add = 2

        header : str = '*'*int(indentation + tabs_to_add) + " "
        line : str = header + marker + str(predicate_name) + ' == ' + str(predicate_value)

        if marker == "IF_BEGIN ":
            self.add_blank_line()
            self.add_line(line)
        elif marker == "IF_END ":
            self.add_line(line)
            self.add_blank_line()

        if comment:
            self.add_line(comment)
        ...



    def add_else_statement(self,
                        predicate_value,
                        predicate_name : str,
                        indentation : int,
                        comment : str = '',
                        begin_or_end : str = 'begin',
                        inside_or_outside : str = 'outside'
                        ) -> None:
        """add else statement to the org file

            put inside the else clause

        Args:
            predicate_value ([type]):
                the value of the predicate of the IF statement
            predicate_name (str):
                the name of the variable that is the predicate
            indentation (int):
                the indentation level of the calling code
            comment (str, optional):
                a comment to insert after the header. Defaults to ''.
            begin_or_end (str, optional):
                wether it begins or ends the statement. Defaults to 'begin'.
            inside_or_outside (str, optional):
                wether it is inserted (in the calling code) inside or outside the actual statement
        """

        marker : str = "ELSE_" + begin_or_end.upper() + " "

        tabs_to_add = 1
        if inside_or_outside == 'outside':
            tabs_to_add = 2
        header : str = '*'*int(indentation + tabs_to_add) + " "
        line : str = header + marker + str(predicate_name) + ' == ' + str(predicate_value)

        if marker == "ELSE_BEGIN ":
            self.add_blank_line()
            self.add_line(line)
        elif marker == "ELSE_END ":
            self.add_line(line)
            self.add_blank_line()

        if comment:
            self.add_line(comment)
        ...

        ...


# TODO add different functions to be put inside and outside of the loop
# the outside one should print the collection
# the inside one should print that the loop is beginning
#   and the iteration counter
#   and the variables used inside the loop (passed as an array)
    def add_for_statement(self,
                        collection_value,
                        collection_name : str,
                        indentation : int,
                        comment : str = '',
                        begin_or_end : str ='begin',
                        inside_or_outside : str = 'outside'
                        ) -> None:
        """
        add an if statement to the org file
        """
        # string of format: * predicate_name = predicate_value
        # * is indentation level

        marker : str = "FOR_" + begin_or_end.upper() + " "

        tabs_to_add = 1
        if inside_or_outside == 'outside':
            tabs_to_add = 2

        header : str = '*'*int(indentation + tabs_to_add) + " "
        line : str = header + marker + str(collection_name) + ' <- ' + str(collection_value)

        collection_formatted = ""
        is_list = isinstance(collection_value, list)
        is_dict = isinstance(collection_value, dict)
        if is_list:
            collection_formatted : str = self.table_of_a_list(collection_value,
                                                            collection_name)
            ...
        elif is_dict:
            collection_formatted : str = self.table_of_a_dictionary(collection_value,
                                                                    collection_name)
            ...
        if marker == "FOR_BEGIN ":
            self.add_blank_line()
            self.add_line(line)

            self.add_line(collection_formatted)
        elif marker == "FOR_END ":
            self.add_line(line)
            self.add_line(collection_formatted)
            self.add_blank_line()

        if comment:
            self.add_line(comment)
        ...


    def add_while_statement(self,
                            predicate_value,
                            predicate_name,
                            indentation,
                            comment : str = "",
                            begin_or_end : str = "begin",
                            inside_or_outside : str = 'outside'
                            ) -> None :
        """adds a while statement to the org file

        Args:
            predicate_value (variable):
                the predicate used in the while loop
            predicate_name (str):
                the name of the variable used in the while loop
            indentation (int):
                the indentation level of the calling code
            comment (str, optional):
                a comment to be put inside the header in the org file. Defaults to "".
            begin_or_end (str, optional):
                wether or not it is the begin or end of the loop. Defaults to "begin".
        """

        marker : str = "WHILE_" + begin_or_end.upper() + " "

        tabs_to_add = 1
        if inside_or_outside == 'outside':
            tabs_to_add = 2

        header : str = '*'*int(indentation + tabs_to_add) + " "
        line : str = header + marker + str(predicate_name) + ' <- ' + str(predicate)

        if marker == "FOR_BEGIN ":
            self.add_blank_line()
            self.add_line(line)

        elif marker == "FOR_END ":
            self.add_line(line)
            self.add_blank_line()

        if comment:
            self.add_line(comment)

        ...




    def add_function_delimeter(self,
                                function_value,
                                function_name,
                                list_of_params : list,
                                list_of_param_names : list,
                                indentation : int,
                                comment : str = "",
                                begin_or_end : str = "begin",
                                inside_or_outside : str = 'inside'
                                ) -> None:
        """
        add a function to the org file
        """

        line : str = ""
        for index, _ in enumerate(list_of_params):
            param_value : str = str(list_of_params[index])
            param_name : str = str(list_of_param_names[index])

            line += "| " + param_name + " | " + param_value + " |\n"
            ...

        tabs_to_add : int = 1
        if inside_or_outside == 'inside':
            tabs_to_add = 2
        header : str = '*'*int(indentation + tabs_to_add) + " "
        marker : str = "FUNC_" + begin_or_end.upper() + " "
        header_line : str = header + marker + str(function_name) + ' <- ' + str(function_value)

        self.add_blank_line()
        self.add_line(header_line)
        self.add_line(line)
        self.add_blank_line()

        if comment:
            self.add_line(comment)
        ...



    def table_of_a_list(self,
                    list_value,
                    list_name : str
                    ) -> None:
        """
        returns a list(one item per line) of a list, with the list name at the top
        """

        restult : str = ""
        name : str = self.add_characters_to_both_sides_of_word(list_name, "=")
        restult = name + "\n"

        # TODO put the type of each item

        # TODO pad zeroes
        for index_a, item_a in enumerate(list_value):

            restult += "| " + list_name + "[" + str(index_a) + "] | " + str(item_a) + " |\n"
            ...

        # TODO format the table so each collung align
        return restult
        ...



    def add_characters_to_both_sides_of_word(self,
                                            word : str,
                                            character : str,
                                            max_characters : int = 80,
                                            space_before_and_after : bool = True
                                            ) -> str:
        """
        add characters to both sides of word, until max characters were reached
        """
        result : str = ""

        word_length = len(word)
        n_of_chars_side = int((max_characters - word_length) / 2)
        left, right = n_of_chars_side, n_of_chars_side

        if space_before_and_after:
            result = " " + (left * character) + " " + word + " " + (right * character) + " "
        else:
            result = (left * character) + " " + word + " " + (right * character)

        return result
        ...



    def table_of_a_dictionary(self,
                    dict_value,
                    dict_name : str
                    ) -> None:
        """
        returns a list(one item per line) of a list, with the list name at the top
        """

        restult : str = ""
        name : str = self.add_characters_to_both_sides_of_word(dict_name, "=")
        restult = name + "\n"

        # TODO pad zeroes
        for index_a, item_a in enumerate(dict_value):

            restult += "| " + dict_name + "[" + str(index_a) + "] | " + str(item_a) + " |\n"
            ...

        # TODO format the table so each collung align
        return restult
        ...


# TODO add logging of exceptions

# TODO add logging of classes















org_logger = OrgLogger()


# variables
variable_in___main__ = "value of variable_in___main__"

org_logger.add_variable(variable_in___main__,
                        nameof(variable_in___main__),
                        get_indentation_level())


# if statements
predicate : bool = True
org_logger.add_if_statement(predicate,
                            nameof(predicate),
                            get_indentation_level())

if predicate:
    variable_inside_1_indent_if : int = 1
    org_logger.add_variable(variable_inside_1_indent_if,
                            nameof(variable_inside_1_indent_if),
                            get_indentation_level())
    ...

org_logger.add_if_statement(predicate,
                            nameof(predicate),
                            get_indentation_level(),
                            begin_or_end='end')

# this is the actual comment in the script
variable_with_comment = "value variable_with_comment"
org_logger.add_variable(variable_in___main__,
                        nameof(variable_in___main__),
                        get_indentation_level(),
                        comment="this is the comment passed to the function to be printed")



# for statements
list_of_items = [1,2,3]

org_logger.add_for_statement(list_of_items,
                            nameof(list_of_items),
                            get_indentation_level())

for item in list_of_items:
    org_logger.add_variable(item,
                            nameof(item),
                            get_indentation_level())
    ...

org_logger.add_for_statement(list_of_items,
                            nameof(list_of_items),
                            get_indentation_level(),
                            begin_or_end='end')


# dictionary
dictionary_var = {
    "key1": "value1",
    "key2": "value2",
    "k:str,v:list": [1,2,3]
}

org_logger.add_for_statement(dictionary_var,
                            nameof(dictionary_var),
                            get_indentation_level())

for key, value in dictionary_var.items():
    org_logger.add_variable(key,
                            nameof(key),
                            get_indentation_level())
    org_logger.add_variable(value,
                            nameof(value),
                            get_indentation_level())
    ...

org_logger.add_for_statement(dictionary_var,
                            nameof(dictionary_var),
                            get_indentation_level(),
                            begin_or_end='end')



# functions
def global_function(parameter_a):
    org_logger.add_function_delimeter(global_function,
                                        nameof(global_function),
                                        [parameter_a],
                                        [nameof(parameter_a)],
                                        get_indentation_level()
                                        )

    local_variable_inside_global_function = []

    org_logger.add_variable(local_variable_inside_global_function,
                            nameof(local_variable_inside_global_function),
                            get_indentation_level())

    org_logger.add_function_delimeter(global_function,
                                        nameof(global_function),
                                        [parameter_a],
                                        [nameof(parameter_a)],
                                        get_indentation_level(),
                                        begin_or_end="end"
                                        )
    ...

a = 1
global_function(a)


def delimeters_put_outside_of_function():

    ...

org_logger.add_function_delimeter(delimeters_put_outside_of_function,
                                        nameof(delimeters_put_outside_of_function),
                                        [],
                                        [],
                                        get_indentation_level()
                                        )

delimeters_put_outside_of_function()

org_logger.add_function_delimeter(delimeters_put_outside_of_function,
                                    nameof(delimeters_put_outside_of_function),
                                    [],
                                    [],
                                    get_indentation_level(),
                                    begin_or_end="end"
                                    )





def main():
    """ the main function """



    ...

































if __name__ == "__main__":
    main()
    ...
