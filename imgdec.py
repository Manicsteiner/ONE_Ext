import json, os
from PIL import Image

with open('atlas.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

blocks = data['Block']
isChara = False
charaBase = ""
charaBaseX = charaBaseY = 0

for block in blocks:
    outimg = Image.new(size = (int(block['width']), int(block['height'])), mode= "RGBA", color="#00000000")
    if not isChara:
        if not (block['filename'] == block['filenameOld']):
            isChara = True
            charaBase = str(block['filenameOld'])
            charaBaseX = int(block['offsetX'])
            charaBaseY = int(block['offsetY'])
    
    # 遍历Mesh字段下的每一个区块
    meshes = block['Mesh']
    #for i, mesh in enumerate(meshes):
    for mesh in meshes:
        # print(f"Mesh {i}: srcOffsetX={mesh['srcOffsetX']}, srcOffsetY={mesh['srcOffsetY']}")
        texpic = Image.open("tex" + str(mesh['texNo']) + ".webp")
        meshpiece = texpic.crop((int(mesh['viewX']), int(mesh['viewY']), int(mesh['viewX'] + mesh['width']), int(mesh['viewY'] + mesh['height']))).convert("RGBA")
        outimg.paste(meshpiece, (int(mesh['srcOffsetX']), int(mesh['srcOffsetY'])), mask = meshpiece)
        
    # End of single output
    if isChara:
        if (charaBase == block['filenameOld']):
            outimg.save(block['filenameOld'] + ".png")
        else:
            baseimg = Image.open(charaBase + ".png")
            baseimg.paste(outimg, (int(block['offsetX']) - charaBaseX, int(block['offsetY']) - charaBaseY), mask = outimg)
            baseimg.save(block['filenameOld'] + ".png")
    elif (os.path.isfile(block['filename'] + ".png")):
        outimg.save(block['filename'] + "_" + str(block['priority']) + ".png")
    else:
        outimg.save(block['filename'] + ".png")