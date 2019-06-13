import turtle as tu
#https://deptinfo-ensip.univ-poitiers.fr/ENS/doku/doku.php/stu:python:turtle

def polygone(long, nbcotes):
    for i in range(nbcotes):
        tu.fd(long)
        tu.rt(360 / nbcotes)


def frise(ang, long, nbcotes):
    for i in range(720 // ang):
        polygone(long, nbcotes)
        tu.lt(ang)


def main():
    tu.setup(400, 400)  # Facultatif
    tu.reset()
    tu.speed(0)
    tu.tracer(50, 0)
    frise(3, 80, 5)
    tu.update()


if __name__ == '__main__': main()
tu.done()

