from cryptography.fernet import Fernet
from rich.table import Table
from rich.console import Console
import typer

app = typer.Typer()

console = Console()

@app.command()
def main():

    table = Table("Command", "Description")
    table.add_row("Encrypt", "Encrypt a message\n")
    table.add_row("Decrypt", "Decrypt a message")
    console.print(table)


if __name__ == "__main__":
    app()