
import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def colorBlender(rgb_v1, rgb_v2, midpoints, n):
    r_v1 = rgb_v1/1000000
    g_v1 = (rgb_v1%1000000)/1000
    b_v1 = (rgb_v1%1000000)%1000

    r_v2 = rgb_v2/1000000
    g_v2 = (rgb_v2%1000000)/1000
    b_v2 = (rgb_v2%1000000)%1000

    midpoints = float(midpoints+1) 
    rinterval = (r_v1 - r_v2) / midpoints 
    ginterval = (g_v1 - g_v2) / midpoints 
    binterval = (b_v1 - b_v2) / midpoints 
    rn = roundHalfUp(r_v1 - n*rinterval)
    gn = roundHalfUp(g_v1 - n*ginterval)
    bn = roundHalfUp(b_v1 - n*binterval)

    return rn*1000000+gn*1000+bn 

print(colorBlender(220020060, 189252201, 3, 4))