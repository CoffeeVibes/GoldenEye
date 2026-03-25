from cryptography.fernet import Fernet
from rich.table import Table
from rich.console import Console
from Decryption import decrypt_message
from Encryption import encrypt_message
import typer

app = typer.Typer()

console = Console()

@app.command()
def main():

    console.print("\nWelcome to the GoldenEye Encryption and Decryption Tool!\n", style="bold green")
    table = Table("Command", "Description")
    table.add_row("Encrypt", "Encrypt a message\n")
    table.add_row("Decrypt", "Decrypt a message")
    console.print(table)
    console.print("\n")

    while True:
        command = input("\nEnter a command: ")
        if command.lower() in {"encrypt", "Encrypt"}:
            message = input("\nEnter a message to encrypt: ")
            key = Fernet.generate_key()
            encrypted_message = encrypt_message(message, key)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            console.print(f"Encrypted Message: {encrypted_message}")
            console.print(f"Encryption Key: {key}\n")
            print("Please save the encryption key to decrypt the message later.")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("exiting...\n")
            break

        elif command.lower() in {"exit", "Exit", "quit", "Quit", "q", "Q"}:
            console.print("\nExiting the program. Goodbye!")
            break

        elif command.lower() in {"decrypt", "Decrypt"}:
            messageTwo = input("Enter a message to decrypt: ")
            keyTwo = input("\nEnter the encryption key: ")

            decrypted_message = decrypt_message(messageTwo.encode(), keyTwo.encode())
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            console.print(f"Decrypted Message: {decrypted_message}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("exiting...\n")


        elif command.lower() in {"exit", "Exit", "quit", "Quit", "q", "Q"}:
            console.print("Exiting the program. Goodbye!")
            break

        else:
            console.print("Invalid command. Please try again.")




if __name__ == "__main__":
    app()