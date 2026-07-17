
from core.command_factory import CommandFactory


class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory

    def start(self):
        while True:
            try:
                input_line = input()
                if input_line.lower() == 'end':
                    break

                result = self._process_command(input_line)
                print(result)
            except ValueError as err:
                print(err.args[0])

    def _process_command(self, input_line):
        cmd_name, *params = input_line.split()
        command = self._command_factory.create(cmd_name, params)
        return command.execute()
