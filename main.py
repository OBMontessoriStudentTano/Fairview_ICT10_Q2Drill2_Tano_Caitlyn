from pyscript import document
from html import escape

# Predefined Grade Sets
grade7 = {
    ("Caitlyn", "Tano"),
    ("Enzo", "Navarro"),
    ("Camille", "Dela Cruz")
} 

grade8 = {
    ("Vincent", "Villanueva"),
    ("Scarlett", "Santos"),
    ("Theo", "Marasigan")
}

grade9 = {
    ("Valerie", "Bautista"),
    ("Damian", "Malabanan"),
    ("Vivienne", "Gatdula")
} 

grade10 = {
    ("Isaiah", "Manansala"), 
    ("Anna", "Dimaculangan")
}

# Combines all grade-level sets into one set
master_members = grade7 | grade8 | grade9 | grade10

# Function when the Submit button is clicked
def enter(event):

    # Gets the first name
    first_name = document.querySelector("#text1").value.strip()

    # Gets the last name
    last_name = document.querySelector("#text2").value.strip()

    # Selects the appropriate function depending on whether both names were entered
    actions = {
        True: add_member, 
        False: show_error
    }

    # Checks whether both names are non-empty and passes them to the selected function
    actions[bool(first_name and last_name)](
        first_name, last_name
    )

# Function that adds a new member
def add_member(first_name, last_name):

    # Update the master_members variable outside this function
    global master_members

    # Stores the new member's first and last names together in a tuple
    new_member = (first_name, last_name)
    # Adds the new member and add it to the list of names
    master_members = master_members | {new_member}

    # Clears any previous error message
    document.querySelector("#message").innerText = ""

    # Clears the first name input field after submission
    document.querySelector("#text1").value = ""

    # Clears the last name input field after submission
    document.querySelector("#text2").value = ""

    # Updates and displays member list
    show_members()

# Function that displays an error when either name is missing
def show_error(first_name, last_name):

    # Displays error message
    document.querySelector("#message").innerText = (
        "Please enter both your first and last names."
    )

# Function that sorts and displays all club members
def show_members():

    # Sorts members alphabetically by last name
    sorted_members = sorted(
        master_members,
        key=lambda person: (
            person[1].casefold(), 
            person[0].casefold()
        )
    )

    # Converts each member's name into a HTML list item
    member_items = "".join(
        map(
            lambda person: (
                f"<li>{escape(person[0])} "
                f"{escape(person[1])}</li>"
            ),
            sorted_members
        )
    )

    # Inserts the ordered member list and the total number of members into the webpage
    document.querySelector("#members").innerHTML = (
        f"<ol>{member_items}</ol>"
        f"<p><strong>Total members: "
        f"{len(master_members)}</strong></p>"
    )

    # Makes the previously hidden member list container visible
    document.querySelector("#box").style.display = "block"