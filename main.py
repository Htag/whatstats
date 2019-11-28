import sys
from flask import Flask

app = Flask(__name__)

def analyse(filename):
  """
  Analyses the chat file.

  :param filename: name of the chat
  """
  print(filename)
  pass # Start here


def main():
  """
  Main function that serves as an entrypoint for the program. Reads the chat file name from the command line when the program is run from the terminal and passed it to the `analyse()` method. 

  For example, if the file is called "chat_file.txt", the command that needs to be run is:
  ```
  python3 main.py chat_file.txt
  ```
  """
  chatfile_name = "discuss.txt"
  analyse(chatfile_name)

@app.route("/")
def home():
    main()
    return "Hello, World!"


if __name__ == "__main__":
  app.run(debug=True)