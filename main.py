from cryptography.fernet import Fernet
from rich.table import Table
from rich.console import Console
from Encryption import encrypt_message
import typer

app = typer.Typer()

console = Console()

@app.command()
def main():

    table = Table("Command", "Description")
    table.add_row("Encrypt", "Encrypt a message\n")
    table.add_row("Decrypt", "Decrypt a message")
    console.print(table)

    while True:
        command = input("Enter a command: ")
        if command.lower() == "encrypt" or command.lower() == "Encrypt":
            message = input("Enter a message to encrypt: ")
            key = Fernet.generate_key()
            encrypted_message = encrypt_message(message, key)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            console.print(f"Encrypted Message: {encrypted_message}")
            console.print(f"Encryption Key: {key}\n")
            print("Please save the encryption key to decrypt the message later.")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("exiting...\n")
            break

        elif command.lower() == "decrypt":
            console.print("Decryption functionality is not implemented yet.")
        else:
            console.print("Invalid command. Please try again.")




if __name__ == "__main__":
    app()