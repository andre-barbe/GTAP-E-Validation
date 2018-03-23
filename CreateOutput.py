__author__ = "Andre Barbe"
__project__ = "GTAP-E Validation"
__created__ = "2018-3-15"
__altered__ = "2018-3-23"

import shutil, datetime


class CreateOutput(object):
    """Copies files from the work files directory to the output files directory"""

    __slots__ = ["simulation_list", "list_of_files_to_copy"]

    def __init__(self, simulation_list: list) -> None:
        self.list_of_files_to_copy = []
        for simulation_name in simulation_list:
            self.list_of_files_to_copy.append("Results {0}.csv".format(simulation_name))

    def create(self) -> None:
        # Gets current date and time
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M")

        # loop to copy and rename output files
        for file_name in self.list_of_files_to_copy:
            # copy files with file_name from Input_Files to Work_Files, also appends current_time
            shutil.copy('Work_Files\\GTAP-E\\{0}'.format(file_name),
                        'Output_Files\\{1} {0}'.format(file_name, current_time))
