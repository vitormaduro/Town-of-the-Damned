# Books!
label d1s3b:
    scene black
    scene bg library with fade

    show marley smile at right
    show ron neutral at center
    show danny neutral at left

    b "Here's the library."
    m "Ooh, I love a good library!"
    b "Then you're going to be disappointed. This library is tiny and seriously underfunded. But we've got a few interesting books! Feel free to flick through some—like that one there."

    call screen bookshelf with fade

screen bookshelf():
    imagemap:
        ground "bg bookshelf"
        hotspot (1078, 468, 77, 405) action Show("local_wildlife")


screen local_wildlife():
    image ("bg book"):
        matrixcolor TintMatrix("#424242")

    text "{b}The Mexican Grey Wolf{/b}\n\nI had an interesting internal debate as to whether to include the Mexican Grey Wolf in this book. Officially, the wolf has not been seen in the area since 1970. However, several more recent reports have claimed sighting these majestic beasts in the Kingston area. None have been confirmed, and no photographic evidence has been found, but these intriguing wolves are a personal interest of mine, so I shall include them.\nThese animals are small for wolves and typically have a narrow skull and dark pelt. If you come across a wolf, any wolf, remember that these are not dogs, despite any outward resemblance. They need to be treated with the utmost respect at all times. They are not your friendly puppy.":
        color "#ffffff"
        xalign 0.5
        yalign 0.4
        textalign 0.5
        maximum (1350, 760)

    imagebutton idle "images/temp/check_solution.png" action Jump("after_reading_book"):
        xalign 0.5
        yalign 0.9

# Returns to the map after reading the book
label after_reading_book:
    hide screen local_wildlife with fade

    b "Come on; can't stay in a musty old library all day."

    call screen map_screen with fade    