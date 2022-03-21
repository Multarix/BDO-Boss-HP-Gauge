from tkinter import *;

window = Tk();

window.title("Boss HP Gauge");

screenWidth = window.winfo_screenwidth();
screenHeight = window.winfo_screenheight();

windowWidth = 0;
windowHeight = 0;
horizontalOffset = 0;
verticalOffset = 0;
canvasWidth = 400;
canvasHeight = 50;

# "4k" Displays
if(screenWidth == 3840): # "4k" Width
	windowWidth = 410;
	horizontalOffset = 0;
	canvasWidth = 400;

if(screenHeight == 2160): # "4k" Height
	windowHeight = 50;
	verticalOffset = 0;
	canvasHeight = 50;


# 1440p Displays
if(screenWidth == 2560): # 1440p Width
	windowWidth = 403;
	horizontalOffset = 0;
	canvasWidth = 400;

if(screenHeight == 1440): # 1440p Height
	windowHeight = 51;
	verticalOffset = 32;
	canvasHeight = 46;


# 1080 Displays
if(screenWidth == 1920): # 1080p Width
	windowWidth = 410;
	horizontalOffset = 0;
	canvasWidth = 400;

if(screenHeight == 1080): # 1080p Height
	windowHeight = 50;
	verticalOffset = 0;
	canvasHeight = 50;

horizontalLocation = int(((screenWidth / 2) - (windowWidth / 2)) + horizontalOffset);

window.geometry(f"{windowWidth}x{windowHeight}+{horizontalLocation}+{verticalOffset}");
window.resizable(width=False, height=False);
window.overrideredirect(True);
window.attributes("-alpha", 0.5, "-topmost", True, "-transparentcolor", window["bg"]);

canvas = Canvas(window, width=canvasWidth, height=canvasHeight);


horiStart = 5;
horiEnd = 398

vertiStart = 5;
vertiEnd = 46;

gap = horiEnd - horiStart;
interval = gap / 10;
offset = 1;


def rectStart(num):
	return horiStart + ((interval * 2) * num);

def rectEnd(num):
	num += 2;
	return min(horiStart + ((interval * 2) * num), horiEnd);


# Make colored rectangles for the HP zones
canvas.create_rectangle(rectStart(0), vertiStart, rectEnd(0), vertiEnd, fill="#ff0000", width=0); 		# 0%  - 20% Area
canvas.create_rectangle(rectStart(1), vertiStart, rectEnd(1), vertiEnd, fill="#ff7c00", width=0); 		# 21% - 40% Area
canvas.create_rectangle(rectStart(2), vertiStart, rectEnd(2), vertiEnd, fill="#ffd100", width=0); 		# 41% - 60% Area
canvas.create_rectangle(rectStart(3), vertiStart, rectEnd(3), vertiEnd, fill="#b9ff00", width=0); 		# 61% - 80% Area
canvas.create_rectangle(rectStart(4), vertiStart, rectEnd(4), vertiEnd, fill="#1fff00", width=0); 		# 81% - 100% Area


line1Start = 5;
line1End = 19;
line2Start = 32;
line2End = 46;


# Draw lines for every 10%
canvas.create_line(4, 3, 4, 50, width=2);												# add 0% mark
canvas.create_line(399, 3, 399, 60, width=2);											# add 100% mark

canvas.create_line(rectStart(0.5), line1Start, rectStart(0.5), line1End, width=1);		# 10% Top Mark
canvas.create_line(rectStart(0.5), line2Start, rectStart(0.5), line2End, width=1);		# 10% Bottom Mark

canvas.create_line(rectStart(  1), line1Start, rectStart(  1), line1End, width=2);		# 20% Top Mark
canvas.create_line(rectStart(  1), line2Start, rectStart(  1), line2End, width=2);		# 20% Bottom Mark

canvas.create_line(rectStart(1.5), line1Start, rectStart(1.5), line1End, width=1);		# 30% Top Mark
canvas.create_line(rectStart(1.5), line2Start, rectStart(1.5), line2End, width=1);		# 30% Bottom Mark

canvas.create_line(rectStart(  2), line1Start, rectStart(  2), line1End, width=2);		# 40% Top Mark
canvas.create_line(rectStart(  2), line2Start, rectStart(  2), line2End, width=2);		# 40% Bottom Mark

canvas.create_line(rectStart(2.5), line1Start, rectStart(2.5), line1End, width=1);		# 50% Top Mark
canvas.create_line(rectStart(2.5), line2Start, rectStart(2.5), line2End, width=1);		# 50% Bottom Mark

canvas.create_line(rectStart(  3), line1Start, rectStart(  3), line1End, width=2);		# 60% Top Mark
canvas.create_line(rectStart(  3), line2Start, rectStart(  3), line2End, width=2);		# 60% Bottom Mark

canvas.create_line(rectStart(3.5), line1Start, rectStart(3.5), line1End, width=1);		# 70% Top Mark
canvas.create_line(rectStart(3.5), line2Start, rectStart(3.5), line2End, width=1);		# 70% Bottom Mark

canvas.create_line(rectStart(  4), line1Start, rectStart(  4), line1End, width=2);		# 80% Top Mark
canvas.create_line(rectStart(  4), line2Start, rectStart(  4), line2End, width=2);		# 80% Bottom Mark

canvas.create_line(rectStart(4.5), line1Start, rectStart(4.5), line1End, width=1);		# 90% Top Mark
canvas.create_line(rectStart(4.5), line2Start, rectStart(4.5), line2End, width=1);		# 90% Bottom Mark

# Draw the top and bottom lines
canvas.create_line(3,  4, 400,  4, width=2);	# Top Line
canvas.create_line(3, 47, 400, 47, width=2);	# Bottom Line



def textOffset(num):
	return rectStart(num) + 6;

# Create the text for each Zone
canvas.create_text(textOffset(0.5), 26, text="10%", fill="#000000", font="Helvetica 11 bold");
canvas.create_text(textOffset(  1), 26, text="20%", fill="#000000", font="Helvetica 11 bold");
canvas.create_text(textOffset(1.5), 26, text="30%", fill="#000000", font="Helvetica 11 bold");
canvas.create_text(textOffset(  2), 26, text="40%", fill="#000000", font="Helvetica 11 bold");
canvas.create_text(textOffset(2.5), 26, text="50%", fill="#000000", font="Helvetica 11 bold");
canvas.create_text(textOffset(  3), 26, text="60%", fill="#000000", font="Helvetica 11 bold");
canvas.create_text(textOffset(3.5), 26, text="70%", fill="#000000", font="Helvetica 11 bold");
canvas.create_text(textOffset(  4), 26, text="80%", fill="#000000", font="Helvetica 11 bold");
canvas.create_text(textOffset(4.5), 26, text="90%", fill="#000000", font="Helvetica 11 bold");

canvas.pack()

m = Menu(window, tearoff=0, bg="#333333", fg="#FFFFFF", bd=0, title="Opacity");

# Right click menu
def closeProgram():
	window.destroy();

currentOption = 50;

def setOpacity(num):
	global currentOption;
	window.attributes("-alpha", (num / 100));

	cur = m.index(f"• {currentOption}%");
	nxt = m.index(f"  {num}%");

	m.entryconfig(cur, label=f"  {currentOption}%");
	m.entryconfig(nxt, label=f"• {num}%");
	

	currentOption = num;
	return currentOption;

m.add_command(label="  10%", command=lambda: setOpacity(10));
m.add_command(label="  20%", command=lambda: setOpacity(20));
m.add_command(label="  30%", command=lambda: setOpacity(30));
m.add_command(label="  40%", command=lambda: setOpacity(40));
m.add_command(label="• 50%", command=lambda: setOpacity(50));
m.add_command(label="  60%", command=lambda: setOpacity(60));
m.add_command(label="  70%", command=lambda: setOpacity(70));
m.add_command(label="  80%", command=lambda: setOpacity(80));
m.add_command(label="  90%", command=lambda: setOpacity(90));
m.add_separator();
m.add_command(label=" Exit", command=closeProgram);

def openMenu(event):
	try:
		m.tk_popup(event.x_root, event.y_root);
	finally:
		m.grab_release();

window.bind("<Button-3>", openMenu);

# Move the window by middle mouse + move
def moveWindow(event):
	x, y = window.winfo_pointerxy();
	window.geometry(f"+{x - round(windowWidth / 2)}+{y - round(windowHeight / 2)}");


window.bind("<B2-Motion>", moveWindow);

window.mainloop();