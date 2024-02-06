default visited_library = False
default visited_museum = False

screen map_screen():
    image("images/city_map/city_map.jpg")

    if not visited_library:
        imagebutton:
            idle "images/city_map/book.png"
            hover "images/city_map/book_hover.png"
            xpos 785
            ypos 90
            action Jump("d1s3b")

    if not visited_museum:
        imagebutton:
            idle "images/city_map/museum.png"
            hover "images/city_map/museum_hover.png"
            xpos 1465
            ypos 385
            action Jump("d1s3f")

    if visited_library and visited_museum:
        imagebutton:
            idle "images/city_map/house.png"
            hover "images/city_map/house_hover.png"
            xpos 240
            ypos 515
            action Jump("d1s3h")

label d1s3b:
    "You went to the library. This scene is missing for now"
    $ visited_library = True
    call screen map_screen

label d1s3f:
    "You went to the museum. This scene is missing for now"
    $ visited_museum = True
    call screen map_screen

label d1s3h:
    "You went to Danny's house. This scene is missing for now"
