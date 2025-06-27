controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (steve.isHittingTile(CollisionDirection.Bottom) && mode == 0) {
        y = -100
        pause(350)
        y = 100
    } else {
        r += -1
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (!(controller.down.isPressed())) {
        if (mode == 1) {
            if (!(tiles.tileAtLocationEquals(mySprite.tilemapLocation(), assets.tile`myTile0`))) {
                if (list[select] == assets.tile`myTile1`) {
                    tiles.setWallAt(mySprite.tilemapLocation(), false)
                    tiles.setTileAt(mySprite.tilemapLocation(), list[select])
                } else if (!(list[select] == assets.tile`myTile1`)) {
                    tiles.setTileAt(mySprite.tilemapLocation(), list[select])
                    tiles.setWallAt(mySprite.tilemapLocation(), true)
                    if (list[select] == no_wall_block[select]) {
                        tiles.setWallAt(mySprite.tilemapLocation(), false)
                    }
                }
            }
        }
    }
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mode == 0) {
        animation.runImageAnimation(
        steve,
        assets.animation`myAnim0`,
        200,
        true
        )
        x = -1 * speed
    } else {
        c += -1
    }
})
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.ImageAnimation, steve)
    steve.setImage(assets.image`myImage1`)
    x = 0
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.ImageAnimation, steve)
    steve.setImage(assets.image`myImage2`)
    x = 0
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mode == 0) {
        animation.runImageAnimation(
        steve,
        assets.animation`myAnim`,
        200,
        true
        )
        x = speed
    } else {
        c += 1
    }
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mode == 0) {
    	
    } else {
        r += 1
    }
})
function start () {
    black = sprites.create(assets.image`block0`, SpriteKind.Player)
    tiles.setCurrentTilemap(tilemap`level1`)
    steve = sprites.create(assets.image`myImage1`, SpriteKind.Player)
    tiles.placeOnRandomTile(steve, assets.tile`myTile3`)
    tiles.setTileAt(steve.tilemapLocation(), assets.tile`myTile1`)
    steve.y += -16
    y = 100
}
let list2: Image[] = []
let black: Sprite = null
let c = 0
let speed = 0
let x = 0
let no_wall_block: Image[] = []
let list: Image[] = []
let r = 0
let y = 0
let steve: Sprite = null
let mode = 0
let select = 0
let mySprite: Sprite = null
music.play(music.createSong(assets.song`minecraft`), music.PlaybackMode.LoopingInBackground)
scene.setBackgroundImage(img`
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
    `)
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
sprites.destroy(mySprite)
game.setDialogCursor(img`
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
    `)
game.setDialogFrame(img`
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
    `)
game.showLongText("start", DialogLayout.Bottom)
select = 0
mode = 0
start()
forever(function () {
    scene.cameraFollowSprite(steve)
    steve.setVelocity(x, y)
    speed = 50
    if (controller.A.isPressed()) {
        if (controller.down.isPressed()) {
            if (mode == 1) {
                mode = 0
                sprites.destroy(mySprite)
                pause(200)
            } else {
                mode = 1
                mySprite = sprites.create(img`
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
                    `, SpriteKind.Player)
                mySprite.setPosition(steve.x, steve.y)
                grid.snap(mySprite)
                c = grid.spriteCol(mySprite)
                r = grid.spriteRow(mySprite)
                pause(200)
            }
        }
    }
    if (controller.B.isPressed()) {
        select += 1
        if (select > list2.length) {
            select = 0
        }
        pause(100)
        black.setImage(list2[select])
    }
    mySprite.setStayInScreen(true)
    black.setStayInScreen(true)
    black.setVelocity(-1000, -1000)
})
forever(function () {
    list = [
    assets.tile`myTile`,
    assets.tile`myTile2`,
    assets.tile`myTile4`,
    assets.tile`myTile0`,
    assets.tile`myTile5`,
    assets.tile`myTile6`,
    assets.tile`myTile7`,
    assets.tile`myTile1`
    ]
    list2 = [
    assets.image`block0`,
    assets.image`block2`,
    assets.image`myImage4`,
    assets.image`block1`,
    assets.image`block3`,
    assets.image`myImage5`,
    assets.image`myImage6`,
    assets.image`pickaxe`
    ]
    no_wall_block = [
    assets.tile`transparency16`,
    assets.tile`transparency16`,
    assets.tile`transparency16`,
    assets.tile`transparency16`,
    assets.tile`transparency16`,
    assets.tile`myTile6`,
    assets.tile`myTile7`,
    assets.tile`myTile1`
    ]
})
forever(function () {
    grid.place(mySprite, tiles.getTileLocation(c, r))
})
