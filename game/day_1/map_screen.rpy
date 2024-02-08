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
            action Jump("library")

    if not visited_museum:
        imagebutton:
            idle "images/city_map/museum.png"
            hover "images/city_map/museum_hover.png"
            xpos 1465
            ypos 385
            action Jump("museum")

    if visited_library and visited_museum:
        imagebutton:
            idle "images/city_map/house.png"
            hover "images/city_map/house_hover.png"
            xpos 240
            ypos 515
            action Jump("house")

label library:
    $ visited_library = True
    jump d1s3b

label museum:
    $ visited_museum = True
    jump d1s3f

label house:
    "You went to Danny's house. This scene is missing for now"
