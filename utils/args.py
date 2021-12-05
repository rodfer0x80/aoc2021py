from sys import argv, stderr, exit


class Args:
    def get_mod_args(self):
        self.argVector = ["day"]
        self.argCount = len(self.argVector) + 1 # progname


    def get_configs(self):
        self.day = int(argv[1])


    def invalid_args_errMsg(self):
        args = ""
        for arg in self.argVector:
            args += " <" + arg + ">"
        self.errMsg = "Usage ./" + argv[0] + args
        self.errMsg += "\n"


    def check_args(self) -> int:
        if len(argv) != self.argCount:
            self.invalid_args_errMsg()
            stderr.write(self.errMsg)
            exit(0)
        else:
            return 0


    def get_args(self):
        self.get_mod_args()
        if self.check_args() == 0:
            self.get_configs()