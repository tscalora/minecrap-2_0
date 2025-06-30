@namespace
class SpriteKind:
    ivtery = SpriteKind.create()
    tree = SpriteKind.create()

def on_up_pressed():
    global y, r
    if steve.is_hitting_tile(CollisionDirection.BOTTOM) and mode == 0:
        y = -100
        pause(350)
        y = 100
    elif mode == 1:
        r += -1
    else:
        pass
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_a_pressed():
    global mySprite2, mode
    if mode == 1:
        if not (controller.down.is_pressed()):
            if not (tiles.tile_at_location_equals(mySprite.tilemap_location(),
                assets.tile("""
                    myTile0
                    """))):
                if list3[select] == assets.tile("""
                    myTile1
                    """):
                    tiles.set_wall_at(mySprite.tilemap_location(), False)
                    tiles.set_tile_at(mySprite.tilemap_location(), list3[select])
                elif not (list3[select] == assets.tile("""
                    myTile1
                    """)):
                    tiles.set_tile_at(mySprite.tilemap_location(), list3[select])
                    tiles.set_wall_at(mySprite.tilemap_location(), True)
                    if list3[select] == no_wall_block[select]:
                        tiles.set_wall_at(mySprite.tilemap_location(), False)
    else:
        if not (controller.down.is_pressed()):
            if not (mode == 2):
                mySprite2 = sprites.create(assets.image("""
                    myImage0
                    """), SpriteKind.ivtery)
                mode = 2
            else:
                mode = 0
                sprites.destroy(mySprite2)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    global x, c
    if mode == 0:
        animation.run_image_animation(steve, assets.animation("""
            myAnim0
            """), 200, True)
        x = -1 * speed
    elif mode == 1:
        c += -1
    else:
        pass
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    global x
    animation.stop_animation(animation.AnimationTypes.IMAGE_ANIMATION, steve)
    steve.set_image(assets.image("""
        myImage1
        """))
    x = 0
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    global x
    animation.stop_animation(animation.AnimationTypes.IMAGE_ANIMATION, steve)
    steve.set_image(assets.image("""
        myImage2
        """))
    x = 0
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_right_pressed():
    global x, c
    if mode == 0:
        animation.run_image_animation(steve, assets.animation("""
            myAnim
            """), 200, True)
        x = speed
    elif mode == 1:
        c += 1
    else:
        pass
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    global r
    if mode == 0:
        pass
    elif mode == 1:
        r += 1
    else:
        pass
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def start():
    global black, steve, mySprite2, y, saved
    black = sprites.create(assets.image("""
        block4
        """), SpriteKind.player)
    tiles.set_current_tilemap(tilemap("""
        level1
        """))
    steve = sprites.create(assets.image("""
        myImage1
        """), SpriteKind.player)
    mySprite2 = sprites.create(assets.image("""
        myImage0
        """), SpriteKind.player)
    sprites.destroy(mySprite2)
    tiles.place_on_random_tile(steve, assets.tile("""
        myTile3
        """))
    tiles.set_tile_at(steve.tilemap_location(),
        assets.tile("""
            myTile1
            """))
    steve.y += -16
    y = 100
    tiles.set_tile_at(tiles.get_tile_location(randint(0, 32), 11),
        assets.tile("""
            myTile12
            """))
    saved = 0
col = 0
row = 0
_get = 0
mySprite3: Sprite = None
tree_type: List[Image] = []
treey: List[number] = []
treex: List[number] = []
list2: List[Image] = []
black: Sprite = None
c = 0
speed = 0
x = 0
mySprite2: Sprite = None
no_wall_block: List[Image] = []
list3: List[Image] = []
r = 0
y = 0
steve: Sprite = None
saved = 0
mode = 0
select = 0
mySprite: Sprite = None
music.play(music.create_song(assets.song("""
        minecraft
        """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
scene.set_background_image(img("""
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    eeeeeeeeeeeeeeeee77777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee7777777777eeeeeeeeeeeeeeeee77777eeeeeeeee
    eeeeeeeeeeeeeeeee77777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee7777777777eeeeeeeeeeeeeeeee77777eeeeeeeee
    eeeeeeeeeeeeeeeee77777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee7777777777eeeeeeeeeeeeeeeee77777eeeeeeeee
    eeeeeeeeeeeeeeeee77777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee7777777777eeeeeeeeeeeeeeeee77777eeeeeeeee
    eeeeeeeeeeeeeeeee77777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee7777777777eeeeeeeeeeeeeeeee77777eeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeee999eeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeee9999eeeeeeeeeeeeeeeeeeeeeeee999bbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeee999eeeeeeeeeeeeeeeeeeeeeee
    eeeeeebbbbbee9999eeeeeeeeee9999eeeeeeeeee999bbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeebbbbbeeeeeeee999999999eeeeeeeeeeeeeeeee
    eeeeeebbbbbee9999eeeeeeeee99999eeeeeeeeee999eeeeeee999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeebbbbbeeeeeee999999999999eeeeeeeeeeeeeee
    eeeeeebbbbbee9999eeeeeeeee99999eeeeeeeeeeeeeeeeeeee999ee9999999eeeeeeebbbbbe99999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeee9999999999999eeeeeeeeeeeeee
    eeeeeebbbbbee9999eeeeeeee999999eeeeeeeeeeeeeeeeeeee9999999999999eeeeeebbbb9999999999eeeeee999999999eeeee999eeeeeeeeeeeeeebbbbbeeeeeee999999ee99999eeeeeeeeeeeeee
    eeeeeebbbbbee99999eeeeee9999999eeeeeeeeeee999eeeeee99999999999999eeeeebbbb9999999999eeeeee999999999eeeee999eeeeeeeeeeeeeebbbbbeeeeeee99999eeee9999eeeeeeeeeeeeee
    eeeeeeeeeeeee9999999eee99999999eeeeeeeeeee999eeeeee99999999e99999eeeeebbb99999ee9999eeeeee999999999eeeee9999999999eeeee999999e999eeeee999eeeeee9999eeeeeeeeeeeee
    eeeeeeeeeeeee99999999e999999999eeeeeeeeeee999eeeeeee999999eeee999eeeeebb99999ee99999eeeee9999eeeeeeeeeee99999999999eee99999999999eeeee999eeeeee9999eeeeeeeeeeeee
    eeeeeeeeeeeee99999999999999e999eeeeeeeeee9999eeeeeee99999eeeee9999eeeeee9999eee9999eeeeee9999eeeeeeeeeee99999999999ee999999999999eeeee999eeeeeee999eeeeeeeeeeeee
    eeeeeeeeeeee9999e999999999ee999eeeeeeeeee9999eeeeeee99999eeeee9999eeeeee9999ee99999eeeeee999eeeeeeeeeeee999999e9999ee999999999999eeeee9999eeeee9999eeeeeeeeeeeee
    eeeeeeeeeeee9999ee9999999eee999eeeeeeeeee9999eeeeeee9999eeeeeee999eeeeee9999999999eeeeeee999eeeeeeeeeeee9999eeeeeeeee9999ee999999eeeee9999eeeee9999eeeeeeeeeeeee
    eeeeeeeeeeee9999eee99999eeee999eeeeeeeeee999eeeeeeee9999eeeeeee999eeee999999999999eeeeeee999eeeeeeeeeeee9999eeeeeeeee9999eee99999eeeee99999eee99999eeeeeeeeeeeee
    eeeeeeeeeeee999eeeeeeeeeeeee999eeeeeeeeee999eeeeeeee9999eeeeeee999eeee9999999999eeeeeeeee999eee99999eeee999eeeeeeeeee9999ee9999999eeee99999e999999eeeeeeeeeeeeee
    eeeeeeeeeeee999eeeeeeeeeeeee999eeeeeeeee9999eeeeeeee9999eeeeeee999eeee9999999eeee9999eeee99999999999eeee999eeeeeeeeee9999999999999eeee999999999999eeeeeeeeeeeeee
    eeeeeeeeeeee999eeeeeeeeeeeee999eeeeeeeee9999eeeeeeee9999eeeeeee999eeeee99999eeee99999eeee99999999999eeee999eeeeeeeeeee999999999999eeee99999999999eeebbbbbeeeeeee
    eeeeeeeeeeee999eeeeeeeeeeeee999eeeeeeeee999eeeeeeeee999eeeeeeee999eeeeee9999999999999eeee99999999eeeeeee999eeeeeeeeeeeee999999e999eeee999999999eeeeebbbbbeeeeeee
    eeeeeeeeeeee999eeeeeeeeeeeee999eeeeeeeee999eeeeeeeee999eeeeeeee999eeeeeee99999999999eeeeeeeeeeeeeeeeeeee999eeeeeeeeeeeeeeeeeeee999eeee999eeeeeeeeeeebbbbbeeeeeee
    eeeeeeeeeeee999eeeeeeeeeeeee999eeeeeeeee999eedddddee999eeeeeeeeeeeeeeeeeee99999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeee999eeeeeeeeeeebbbbbeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeee999eeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeee999eeeeeeeeeeebbbbbeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeee9999eeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeebbbbbeeeeeeeeedddddeeeeeeeeeeeeeee9999eeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeebbbbbeeeeeeeeedddddeeeeeeeeeeeeeee9999eeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeee999eeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeee999eeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeee999eeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeee
    eeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeee
    eeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeee
    eeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeedddddeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    """))
mySprite = sprites.create(img("""
        f f f f f f f f f f f f f f f f
        f . . . . . . . . . . . . . . f
        f . . . . . . . . . . . . . . f
        f . . . . . . . . . . . . . . f
        f . . . . . . . . . . . . . . f
        f . . . . . . . . . . . . . . f
        f . . . . . . . . . . . . . . f
        f . . . . . . . . . . . . . . f
        f . . . . . . . . . . . . . . f
        f . . . . . . . . . . . . . . f
        f . . . . . . . . . . . . . . f
        f . . . . . . . . . . . . . . f
        f . . . . . . . . . . . . . . f
        f . . . . . . . . . . . . . . f
        f . . . . . . . . . . . . . . f
        f f f f f f f f f f f f f f f f
        """),
    SpriteKind.player)
sprites.destroy(mySprite)
game.set_dialog_cursor(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    4 4 4 4 4 4 4 e 4 4 4 4 4 4 4 4
    e e e e e e e e e e e e e e e e
    4 e 4 4 4 4 4 f f 4 4 4 e 4 4 4
    4 e 4 4 4 4 f 4 4 f 4 4 e 4 4 4
    e e e e e e f e e f e e e e e e
    4 4 4 e 4 f 4 e 4 4 f 4 4 4 e 4
    4 4 4 e 4 f f f f f f 4 4 4 e 4
    e e e e e f e e e e f e e e e e
    4 4 4 4 4 f e 4 4 4 f 4 4 e 4 4
    4 4 4 4 4 4 e 4 4 4 4 4 4 e 4 4
    e e e e e e e e e e e e e e e e
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    """))
game.set_dialog_frame(img("""
    bbddddddbdddbbddbbddddddbdddbbddbbddddddbdddbbddbbddddddbddd
    ddbbddbbddbbbdbdddbbddbbddbbbdbdddbbddbbddbbbdbdddbbddbbddbb
    dddbbdbdddbdddbbdddbbdbdddbdddbbdddbbdbdddbdddbbdddbbdbdddbd
    ddddbbdddbbdbbbdddddbbdddbbdbbbdddddbbdddbbdbbbdddddbbdddbbd
    bbbddbdddbddbdddbbbddbdddbddbdddbbbddbdddbddbdddbbbddbdddbdd
    ddbdbbbbbbddbdddddbdbbbbbbddbdddddbdbbbbbbddbdddddbdbbbbbbdd
    ddbbbddbbdddbdbbddbbbddbbdddbdbbddbbbddbbdddbdbbddbbbddbbddd
    ddbbddbdbdddbdbdddbbddbdbdddbdbdddbbddbdbdddbdbdddbbddbdbddd
    dbbbdbddbdddbbdddbbbdbddbdddbbdddbbbdbddbdddbbdddbbbdbddbddd
    dbddbbddbddbbbdddbddbbddbddbbbdddbddbbddbddbbbdddbddbbddbddb
    bbddbdddbbbddbbdbbddbdddbbbddbbdbbddbdddbbbddbbdbbddbdddbbbd
    bdbbbbbbbbddddbdbdbbbbbbbbddddbdbdbbbbbbbbddddbdbdbbbbbbbbdd
    bdddbbbdddbdddbbbdddbbbdddbdddbbbdddbbbdddbdddbbbdddbbbdddbd
    bbddbbdbddbddddbbbddbbdbddbddddbbbddbbdbddbddddbbbddbbdbddbd
    dbbbbddbbbbbbbbbdbbbbddbbbbbbbbbdbbbbddbbbbbbbbbdbbbbddbbbbb
    ddbbddddbbddddddddbbddddbbddddddddbbddddbbddddddddbbddddbbdd
    bbddddddbdddbbddbbddddddbdddbbddbbddddddbdddbbddbbddddddbddd
    ddbbddbbddbbbdbdddbbddbbddbbbdbdddbbddbbddbbbdbdddbbddbbddbb
    dddbbdbdddbdddbbdddbbdbdddbdddbbdddbbdbdddbdddbbdddbbdbdddbd
    ddddbbdddbbdbbbdddddbbdddbbdbbbdddddbbdddbbdbbbdddddbbdddbbd
    bbbddbdddbddbdddbbbddbdddbddbdddbbbddbdddbddbdddbbbddbdddbdd
    ddbdbbbbbbddbdddddbdbbbbbbddbdddddbdbbbbbbddbdddddbdbbbbbbdd
    ddbbbddbbdddbdbbddbbbddbbdddbdbbddbbbddbbdddbdbbddbbbddbbddd
    ddbbddbdbdddbdbdddbbddbdbdddbdbdddbbddbdbdddbdbdddbbddbdbddd
    dbbbdbddbdddbbdddbbbdbddbdddbbdddbbbdbddbdddbbdddbbbdbddbddd
    dbddbbddbddbbbdddbddbbddbddbbbdddbddbbddbddbbbdddbddbbddbddb
    bbddbdddbbbddbbdbbddbdddbbbddbbdbbddbdddbbbddbbdbbddbdddbbbd
    bdbbbbbbbbddddbdbdbbbbbbbbddddbdbdbbbbbbbbddddbdbdbbbbbbbbdd
    bdddbbbdddbdddbbbdddbbbdddbdddbbbdddbbbdddbdddbbbdddbbbdddbd
    bbddbbdbddbddddbbbddbbdbddbddddbbbddbbdbddbddddbbbddbbdbddbd
    dbbbbddbbbbbbbbbdbbbbddbbbbbbbbbdbbbbddbbbbbbbbbdbbbbddbbbbb
    ddbbddddbbddddddddbbddddbbddddddddbbddddbbddddddddbbddddbbdd
    bbddddddbdddbbddbbddddddbdddbbddbbddddddbdddbbddbbddddddbddd
    ddbbddbbddbbbdbdddbbddbbddbbbdbdddbbddbbddbbbdbdddbbddbbddbb
    dddbbdbdddbdddbbdddbbdbdddbdddbbdddbbdbdddbdddbbdddbbdbdddbd
    ddddbbdddbbdbbbdddddbbdddbbdbbbdddddbbdddbbdbbbdddddbbdddbbd
    bbbddbdddbddbdddbbbddbdddbddbdddbbbddbdddbddbdddbbbddbdddbdd
    ddbdbbbbbbddbdddddbdbbbbbbddbdddddbdbbbbbbddbdddddbdbbbbbbdd
    ddbbbddbbdddbdbbddbbbddbbdddbdbbddbbbddbbdddbdbbddbbbddbbddd
    ddbbddbdbdddbdbdddbbddbdbdddbdbdddbbddbdbdddbdbdddbbddbdbddd
    dbbbdbddbdddbbdddbbbdbddbdddbbdddbbbdbddbdddbbdddbbbdbddbddd
    dbddbbddbddbbbdddbddbbddbddbbbdddbddbbddbddbbbdddbddbbddbddb
    bbddbdddbbbddbbdbbddbdddbbbddbbdbbddbdddbbbddbbdbbddbdddbbbd
    bdbbbbbbbbddddbdbdbbbbbbbbddddbdbdbbbbbbbbddddbdbdbbbbbbbbdd
    bdddbbbdddbdddbbbdddbbbdddbdddbbbdddbbbdddbdddbbbdddbbbdddbd
    """))
game.show_long_text("start", DialogLayout.BOTTOM)
select = 0
mode = 0
saved = 1
start()

def on_forever():
    global speed, mode, mySprite, c, r, select
    scene.camera_follow_sprite(steve)
    steve.set_velocity(x, y)
    speed = 50
    if controller.A.is_pressed():
        if controller.down.is_pressed():
            if not (mode == 2):
                if mode == 1:
                    mode = 0
                    sprites.destroy(mySprite)
                    pause(200)
                else:
                    mode = 1
                    mySprite = sprites.create(img("""
                            f f f f f f f f f f f f f f f f
                            f . . . . . . . . . . . . . . f
                            f . . . . . . . . . . . . . . f
                            f . . . . . . . . . . . . . . f
                            f . . . . . . . . . . . . . . f
                            f . . . . . . . . . . . . . . f
                            f . . . . . . . . . . . . . . f
                            f . . . . . . . . . . . . . . f
                            f . . . . . . . . . . . . . . f
                            f . . . . . . . . . . . . . . f
                            f . . . . . . . . . . . . . . f
                            f . . . . . . . . . . . . . . f
                            f . . . . . . . . . . . . . . f
                            f . . . . . . . . . . . . . . f
                            f . . . . . . . . . . . . . . f
                            f f f f f f f f f f f f f f f f
                            """),
                        SpriteKind.player)
                    mySprite.set_position(steve.x, steve.y)
                    grid.snap(mySprite)
                    c = grid.sprite_col(mySprite)
                    r = grid.sprite_row(mySprite)
                    pause(200)
    if mode == 1:
        if controller.B.is_pressed():
            select += 1
            if select > len(list2):
                select = 0
            pause(100)
            black.set_image(list2[select])
    mySprite.set_stay_in_screen(True)
    black.set_stay_in_screen(True)
    black.set_velocity(-1000, -1000)
forever(on_forever)

def on_forever2():
    global treex, treey, tree_type, mySprite3, _get, saved
    treex = [0, 0, 0, 0, -1, -2, 1, 2, -1, 0, 1, -1, 0, 1, 0]
    treey = [0, 1, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6]
    tree_type = [assets.tile("""
            myTile6
            """),
        assets.tile("""
            myTile6
            """),
        assets.tile("""
            myTile6
            """),
        assets.tile("""
            myTile7
            """),
        assets.tile("""
            myTile7
            """),
        assets.tile("""
            myTile7
            """),
        assets.tile("""
            myTile7
            """),
        assets.tile("""
            myTile7
            """),
        assets.tile("""
            myTile7
            """),
        assets.tile("""
            myTile7
            """),
        assets.tile("""
            myTile7
            """),
        assets.tile("""
            myTile7
            """),
        assets.tile("""
            myTile7
            """),
        assets.tile("""
            myTile7
            """),
        assets.tile("""
            myTile7
            """)]
    if saved == 1:
        pause(5000)
    mySprite3 = sprites.create(assets.image("""
        myImage
        """), SpriteKind.tree)
    tiles.place_on_random_tile(mySprite3, assets.tile("""
        myTile12
        """))
    _get = 0
    for index in range(len(tree_type)):
        tiles.set_tile_at(tiles.get_tile_location(mySprite3.tilemap_location().column - treex[_get],
                mySprite3.tilemap_location().row - treey[_get]),
            tree_type[_get])
        _get += 1
    saved = 1
    sprites.destroy(mySprite3)
forever(on_forever2)

def on_forever3():
    global list3, list2, no_wall_block
    list3 = [assets.tile("""
            myTile
            """),
        assets.tile("""
            myTile2
            """),
        assets.tile("""
            myTile4
            """),
        assets.tile("""
            myTile0
            """),
        assets.tile("""
            myTile5
            """),
        assets.tile("""
            myTile6
            """),
        assets.tile("""
            myTile7
            """),
        assets.tile("""
            myTile8
            """),
        assets.tile("""
            myTile12
            """),
        assets.tile("""
            myTile1
            """)]
    list2 = [assets.image("""
            block4
            """),
        assets.image("""
            block2
            """),
        assets.image("""
            myImage4
            """),
        assets.image("""
            block1
            """),
        assets.image("""
            block3
            """),
        assets.image("""
            myImage5
            """),
        assets.image("""
            myImage6
            """),
        assets.image("""
            myImage3
            """),
        assets.image("""
            block0
            """),
        assets.image("""
            pickaxe
            """)]
    no_wall_block = [assets.tile("""
            transparency16
            """),
        assets.tile("""
            transparency16
            """),
        assets.tile("""
            transparency16
            """),
        assets.tile("""
            transparency16
            """),
        assets.tile("""
            transparency16
            """),
        assets.tile("""
            myTile6
            """),
        assets.tile("""
            myTile7
            """),
        assets.tile("""
            myTile8
            """),
        assets.tile("""
            myTile12
            """),
        assets.tile("""
            myTile1
            """)]
forever(on_forever3)

def on_forever4():
    grid.place(mySprite, tiles.get_tile_location(c, r))
forever(on_forever4)

def on_forever5():
    if tiles.tile_at_location_equals(mySprite.tilemap_location(),
        assets.tile("""
            myTile8
            """)):
        if tiles.tile_at_location_equals(tiles.get_tile_location(mySprite.tilemap_location().column,
                1 + mySprite.tilemap_location().row),
            assets.tile("""
                myTile1
                """)):
            tiles.set_tile_at(mySprite.tilemap_location(),
                assets.tile("""
                    myTile10
                    """))
            tiles.set_tile_at(tiles.get_tile_location(mySprite.tilemap_location().column,
                    1 + mySprite.tilemap_location().row),
                assets.tile("""
                    myTile9
                    """))
        elif tiles.tile_at_location_equals(tiles.get_tile_location(mySprite.tilemap_location().column,
                mySprite.tilemap_location().row - 1),
            assets.tile("""
                myTile1
                """)):
            tiles.set_tile_at(mySprite.tilemap_location(),
                assets.tile("""
                    myTile9
                    """))
            tiles.set_tile_at(tiles.get_tile_location(mySprite.tilemap_location().column,
                    mySprite.tilemap_location().row - 1),
                assets.tile("""
                    myTile10
                    """))
forever(on_forever5)

def on_forever6():
    mySprite2.set_position(scene.camera_property(CameraProperty.X),
        scene.camera_property(CameraProperty.Y))
forever(on_forever6)

def on_update_interval():
    global row, col
    row = 0
    col = 0
    for index2 in range(256):
        save: List[Image] = []
        save.append(tiles.tile_image_at_location(tiles.get_tile_location(col, row)))
        col += 1
        if col < 16:
            col = 0
            row += 1
game.on_update_interval(500, on_update_interval)
