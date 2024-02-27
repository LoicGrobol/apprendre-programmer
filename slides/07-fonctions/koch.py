import turtle

turtle.speed("fast")


def segment_koch(l, n):
    """Trace un des cotés du flocon à l'ordre `n`, de longueur `l` en partant de la
    position courante et dans la direction courante."""
    if n == 0:
        turtle.forward(l)
    else:
        segment_koch(l / 3.0, n - 1)
        turtle.left(60)
        segment_koch(l / 3.0, n - 1)
        turtle.right(120)
        segment_koch(l / 3.0, n - 1)
        turtle.left(60)
        segment_koch(l / 3.0, n - 1)


def flocon_koch(l, n):
    """Trace le flocon à l'ordre `n` et de côté `l` en partant de la position courant
    et dans la direction courante."""
    for _ in range(3):
        segment_koch(l, n)
        turtle.right(120)


for n in range(6):
    flocon_koch(3**5, n)
