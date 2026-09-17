import subprocess


def hello_world() -> str:
    return "Hello World"


def run_command(command: str) -> None:
    subprocess.run(command, shell=True, check=False)


def main() -> None:
    print(hello_world())  # noqa: T201 print only used as placeholder :)


if __name__ == "__main__":
    main()
