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

master_members = grade7 | grade8 | grade9 | grade10

def enter(event):
    first_name = document.querySelector("#text1").value.strip()
    last_name = document.querySelector("#text2").value.strip()

    actions = {
        True: add_member, 
        False: show_error
    }

    actions[bool(first_name and last_name)](
        first_name, last_name
    )

def add_member(first_name, last_name):
    global master_members

    new_member = (first_name, last_name)
    master_members = master_members | {new_member}

    document.querySelector("#message").innerText = ""
    document.querySelector("#text1").value = ""
    document.querySelector("#text2").value = ""

    show_members()

def show_error(first_name, last_name):
    document.querySelector("#message").innerText = (
        "Please enter both your first and last names."
    )

def show_members():
    sorted_members = sorted(
        master_members,
        key=lambda person: (
            person[1].casefold(), 
            person[0].casefold()
        )
    )

    member_items = "".join(
        map(
            lambda person: (
                f"<li>{escape(person[0])} "
                f"{escape(person[1])}</li>"
            ),
            sorted_members
        )
    )

    document.querySelector("#members").innerHTML = (
        f"<ol>{member_items}</ol>"
        f"<p><strong>Total members: "
        f"{len(master_members)}</strong></p>"
    )

    document.querySelector("#box").style.display = "block"