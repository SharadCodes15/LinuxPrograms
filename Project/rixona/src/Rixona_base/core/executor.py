import subprocess
from dataclasses import dataclass

@dataclass
class ReturnResult:
    success : bool
    output : str
    error : str
    return_code: int | None

class Executor :
    def __init__(self,timeout:int = 100) -> None:
          self.timeout = timeout

    def validate(self,cmd_list:list[str])->None:
        if not isinstance(cmd_list,list):
            raise TypeError("Command must be a list")
        if not cmd_list:
            raise ValueError("Command cant be empty")
        if not all(isinstance(item,str) for item in cmd_list):
            raise TypeError("All command args must be strings")

        if not cmd_list[0].strip():
                    raise ValueError("Executable name cant be empty")

    @staticmethod
    def normalize_output(value)->str:
        '''Convert subprocess output into a string'''
        if value is None:
            return ""
        if isinstance(value,bytes):
            return value.decode(errors="replace")
        return value

    def execute(self,command_list:list):
        try:
            self.validate(command_list)
            result = subprocess.run(command_list,capture_output=True,text=True,check=False,timeout=self.timeout)
                # print("success")
            return ReturnResult(
    success=(result.returncode == 0),
    output=result.stdout,
    error=result.stderr,
    return_code=result.returncode
)

        except (ValueError,TypeError) as e:
            return ReturnResult(
                success=False,
                output="",
                error=str(e),
                return_code=None
            )

        except FileNotFoundError as e:
            # print("file not found")
            return ReturnResult(
    success=False,
    output="",
    error=str(e),
    return_code=None
)
        except PermissionError as p:
            # print("permission error")
            return ReturnResult(
    success=False,
    output="",
    error=str(p),
    return_code=None
)
        except subprocess.TimeoutExpired as e:
            return ReturnResult(
    success=False,
    output=self.normalize_output(e.stdout) or "command timed out",
    error=self.normalize_output(e.stderr),
    return_code=None
)

if __name__ == '__main__':
    executor = Executor()
    tests = [
    ["ls", "-la"],
    ["uname", "-r"],
    ["false"],
    ["invalid_xyz"],
    ["sleep", "10"],
    [],
]

    for command in tests:
        result = executor.execute(command)
        print(result)
