from pyscript import display, document

# List of names
names = ["Caitlyn Tano", "Enzo Navarro", "Camille Dela Cruz", "Vincent Villanueva", "Scarlett Santos", "Theo Marasigan", "Valerie Bautista", "Damian Malabanan", "Vivienne Gatdula", "Isaiah Manansala", "Anna Dimaculangan"]

def enter(event):
    first_name = document.querySelector("#text1").value.strip()
    last_name = document.querySelector("#text2").value.strip()