import re

from bs4 import BeautifulSoup

layout_lines = open("./config/kyria_rev2.keymap", "r").read()
layout_lines = layout_lines.replace("\r", "")

# parsing
layouts = re.findall(r"\tbindings = <([^>]*)>", layout_lines, re.MULTILINE)


layer_colors = [
    "rgba(120,160,255,0.5)",
    "rgba(160,250,160,0.5)",
    "rgba(255,160,160,0.5)",
]

# loop over non whitespace and add as separate divs
layer_divs = []
for il, lout in enumerate(layouts):
    ldiv = "<div class='layer'>"
    for ir, line in enumerate(lout.split("\n")):
        ldiv += "<div class='key_row'>"
        for key in line.split("&"):
            if len(key.strip()) > 0:
                k = re.findall(r"(.*)\s*", key)[0]

                # remove prefix if present
                k = re.sub(r"kp ", "", k)
                k = re.sub(r"mo ", "", k)

                ldiv += f"<div class='key_layer_{il} irow_{ir} key'>{k}</div>"
                # add trailing whitespace to ensure alignment
                # tw = re.findall(r"(\s*)$", key)[0]
                # ldiv += f"<div class='ws_layer_{il}'>{'.'*len(tw)}</div>"
        ldiv += "</div>"
    ldiv += "</div>"

    layer_divs.append(ldiv)


soup = BeautifulSoup(
    "<!DOCTYPE html><html><head><title>My ZMK Layout</title></head><body></body></html>",
    "html.parser",
)
soup.body.append(BeautifulSoup("<br><br><br>".join(layer_divs), "html.parser"))

# add the styling header
soup.head.append(soup.new_tag("style", type="text/css"))
soup.style.append(
    " ".join(
        [
            f".key_layer_{i} {{background-color:{c}}}"
            for i, c in enumerate(layer_colors)
        ]
    )
)
soup.style.append(".key {width: 4rem; max-width: 4rem; padding: 0.5rem;}")
soup.style.append(".key {border: solid 0.05rem black;}")
soup.style.append(".key_row {display: flex;}")
soup.style.append(".layer {font-family: monospace;}")
soup.style.append(".irow_1:nth-child(6) {margin-right: 28.25rem;}")
soup.style.append(".irow_2:nth-child(6) {margin-right: 28.25rem;}")
soup.style.append(".irow_3:nth-child(8) {margin-right: 8rem;}")
soup.style.append(".irow_4:nth-child(5) {margin-right: 8rem;}")
soup.style.append(".irow_4:nth-child(1) {margin-left: 15.2rem;}")

open("layout.html", "w").write(soup.prettify())


import os

os.system("open layout.html")
