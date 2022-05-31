def getHeightFromFallTime(fallTime: float, gravity=9.81) -> float:
    """Uses the equation y = 1/2*g*t^2 to calculate drop height,
    in meters, from an object's fall time, in seconds"""
    height = 0.5 * gravity * (fallTime ** 2)
    return height


earthFall = getHeightFromFallTime(0.75)
moonFall = getHeightFromFallTime(2.3, gravity=1.62)
