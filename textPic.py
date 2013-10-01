import ImageDraw, Image, argparse,sys


ARG=argparse.ArgumentParser(\
      description="convert string to picture with repped hex",\
      epilog="")

ARG.add_argument('-m', '--message', help="Message to encode", dest="Message", default="lol")
ARG.add_argument('-p', '--path', help="path to file", dest="path", default="/home/tyler/pic.png")

# -- Parsing passed arguments to variables -- #
args=ARG.parse_args()


Message = args.Message
path = args.path

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


height = 600
width = 800

im = Image.new('RGB',(800,600))

draw = ImageDraw.Draw(im)

val = Message
hexVal = val.encode('hex')
hexVal_len = len(hexVal)
extraLen = hexVal_len % 6

extraVal = hexVal[int(extraLen).__neg__():]
s = hexVal[:len(hexVal)-extraLen]
splitVal = [s[i:i+6] for i in xrange(0, len(s), 6)]

parts = len(splitVal)
if parts > width:
    print "message is too long, less than a pixel per row"
    sys.exit()

drawWidth = width/parts

j = 0
for i in splitVal:
    draw.rectangle([(j,0),(j+drawWidth,height)],fill=hex_to_rgb(i),outline='black')
    j += drawWidth

if extraLen !=0:
    draw.text((300,400),'+'+str(extraVal),fill='white')

im.save(path,'PNG')
