import subprocess
from dataclasses import dataclass

@dataclass
class ReturnResult:
    success : bool
    output : str
    error : str
    return_code: int | None

class Executor :
    def validate(self,cmd_list):
        returnCode = 1
        if type(cmd_list) != list:
                    return returnCode
        if len(cmd_list) == 0:
            return returnCode

        if cmd_list is None:
                    return returnCode


        if any(isinstance(item, (int, float)) for item in cmd_list):
                    return returnCode
        if "" in cmd_list:
              return returnCode
        return 0
        

    def execute(self,command_list:list):
        if(self.validate(cmd_list=command_list) != 0):
              return ReturnResult(
    success=False,
    output="Validation Error",
    error="Validation Error",
    return_code=1
) 
        try:
            result = subprocess.run(command_list,capture_output=True,text=True,check=False,timeout=100)
                # print("success")
            return ReturnResult(
    success=(result.returncode == 0),
    output=result.stdout,
    error=result.stderr,
    return_code=result.returncode
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
        except subprocess.TimeoutExpired as timeex:
            return ReturnResult(
    success=False,
    output=timeex.stdout,
    error=timeex.stderr,
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