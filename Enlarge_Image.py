#Program to enlarge image using bilinear interpolation.
# -*- coding: utf-8 -*-

from pillow import Image as im

xx = im.open('zebra.jpg')  # original image
xpix = xx.load()

aa = im.new('L',[xx.size[0]+2,xx.size[1]+2],0) # zero-pad edges
aa.paste(xx,(1,1))

apix = aa.load()

bb = im.new('L',[3*aa.size[0]-2,aa.size[1]],0) # horiz stretch
bpix = bb.load()

cc = im.new('L',[3*aa.size[0]-2,aa.size[1]],0) # horiz interpolated
cpix = cc.load()

dd = im.new('L',[3*aa.size[0]-2,3*aa.size[1]-2],0) # vertical stretch
dpix = dd.load()

yy = im.new('L',[3*aa.size[0]-2,3*aa.size[1]-2],0) # final answer
ypix = yy.load()

for j in range(aa.size[1]):
	for i in range(aa.size[0]): # stretch image horizontally
		bpix[3*i,j] = apix[i,j]

for i in range(2,bb.size[0]-2): # convolve with triangle
	cpix[i,j] = 0.333*bpix[i-2,j]+0.666*bpix[i-1,j]+bpix[i,j]+0.666*bpix[i+1,j]+0.333*bpix[i+2,j]

for i in range(cc.size[0]):
	for j in range(cc.size[1]): # stretch image vertically
		dpix[i,3*j] = cpix[i,j]

for j in range(2,dd.size[1]-2): # convolve with triangle
	ypix[i,j] = 0.333*dpix[i,j-2]+0.666*dpix[i,j-1]+dpix[i,j]+0.666*dpix[i,j+1]+0.333*dpix[i,j+2]

yy.crop([3,3,yy.size[0]-3,yy.size[1]-3]).save('zebraBilinear.jpg')