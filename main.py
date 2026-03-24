from cryptography.fernet import Fernet
import typer

app = typer.Typer()


@app.command()
def encrypt():

    #User type message to encrypt
    plaintext = input("Enter text to encrypt:")

    #Generate encryption key
    key = Fernet.generate_key()
    f = Fernet(key)
    print("Encrypytion key:", key.decode("utf8"))

    #Encrypt the message
    token = f.encrypt(plaintext.encode("utf8"))
    print(token)

@app.command()
def decrypt():

    #User message to decrypt
    token = input("Enter text to decrypt:")
    key = input("Enter encryption key:")
    f = Fernet(key)

    #decrypt the message
    decrypted = f.decrypt(token.encode("utf8"))

    #Print the decrypted message
    print(decrypted.decode("utf8"))


if __name__ == "__main__":
    app()
