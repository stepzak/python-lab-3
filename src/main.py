from shlex import split
import src.commands as cmds

def main() -> None:
    variables = {}
    while True:
        try:
            prompt = input("> ")
            args = split(prompt)
            if not args:
                continue
            if args[0] == "exit":
                break
            if args[0] == "help":
                print("""
                exit: exit the program
                help: display this help message
                sort {array} {algorithm} {reversed}: sorts {array} with {algorithm}
                benchmark {iter}: run a benchmark of all algorithms with {iter} iterations
                stack {name} create {implementation}: create stack named {name} with {implementation}
                stack {name} push {value}: pushes {value} to stack named {name}
                stack {name} pop: pops from {name}
                stack {name} peek: peeks from {name}
                stack {name} __len__: length of {name}
                stack {name} min: min value in {name}
                stack {name} is_empty: is {name} empty
                stack {name} __str__: prints stack items
                fibonacci {value} {mode}: fibonacci of {value} {recursive|iterative}
                factorial {value} {mode}: factorial of {value} {recursive|iterative}
                
                """)
                continue
            else:
                cmd = args[0]
                cmd_callable = getattr(cmds, cmd+"_command", None)
                if not cmd_callable:
                    print("Command not found")
                    continue
                output = cmd_callable(*args[1:])
                meta = output.meta
                if meta:
                    var = meta["variable"]
                    if meta.get("mode") == "create":
                        variables[var] = output.result
                    else:
                        var_val = variables[var]
                        attr = meta["attr"]
                        call_args = meta.get("args", tuple())
                        callable_val = getattr(var_val, attr)
                        result = callable_val(*call_args)
                        if result is not None:
                            output.result = result
                print(output.result)
        except Exception as e:
            print(e)




                

if __name__ == "__main__":
    main()
