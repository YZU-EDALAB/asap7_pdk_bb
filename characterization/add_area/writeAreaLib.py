# Python Version: 3.4.3
# Lastest Version: 2016/09/28
# How to run this program?
#   python3.4 writeAreaLib.py


import re

def addAreaToLib():
 inputLib_Name = "fin21.lib"			# Input .Lib File Name (Area incorrect)
 outputLib_Name = "fin21_add.lib"	# Output .Lib File Name (Area correct depend on *Map)

 Single_FinalMap = {
'OR5x2_fin21':'0.69984',
'OAI333xp33_fin21':'0.8748',
'AOI32x1_fin21':'0.78732',
'OA21x2_fin21':'0.52488',
'AO32x1_fin21':'0.61236',
'AOI32xp25_fin21':'0.52488',
'AND2x2_fin21':'0.4374',
'NAND2xp33_fin21':'0.26244',
'DECAPx4_fin21':'0.78732',
'HB1xp67_fin21':'0.26244',
'O2A1O1Ixp33_fin21':'0.52488',
'OAI22xp5_fin21':'0.4374',
'MUX2x1_fin21':'0.69984',
'NAND2x2_fin21':'0.61236',
'NOR2xp5_fin21':'0.26244',
'INVx3_fin21':'0.34992',
'NAND4xp75_fin21':'0.96228',
'OA221x2_fin21':'0.78732',
'NOR2x1p5_fin21':'0.61236',
'OA333x2_fin21':'1.04976',
'NOR3x1_fin21':'0.61236',
'BUFx10_fin21':'1.13724',
'BUFx5_fin21':'0.61236',
'OAI322xp25_fin21':'0.69984',
'OAI33x1_fin21':'0.8748',
'BUFx8_fin21':'0.96228',
'SDFLx3_fin21':'2.44944',
'HB4xp67_fin21':'0.52488',
'INVx2_fin21':'0.26244',
'AOI21xp25_fin21':'0.34992',
'AOI321xp25_fin21':'0.61236',
'AO332x1_fin21':'0.8748',
'BUFx24_fin21':'2.53692',
'DFFHQNx2_fin21':'1.48716',
'AO332x2_fin21':'0.96228',
'OA22x2_fin21':'0.69984',
'OR2x6_fin21':'0.78732',
'OAI22xp25_fin21':'0.4374',
'INVx8_fin21':'0.78732',
'BUFx6f_fin21':'0.78732',
'AOI31xp5_fin21':'0.69984',
'OR4x4_fin21':'0.78732',
'AO333x1_fin21':'0.96228',
'AOI22xp5_fin21':'0.4374',
'A2O1A1Ixp25_fin21':'0.4374',
'OR3x4_fin21':'0.69984',
'OA333x1_fin21':'0.96228',
'OAI21xp5_fin21':'0.34992',
'SDFLx1_fin21':'2.27448',
'XOR2x2_fin21':'0.96228',
'AOI32xp33_fin21':'0.52488',
'OAI321xp25_fin21':'0.61236',
'AOI211x1_fin21':'0.69984',
'OAI331xp33_fin21':'0.69984',
'NAND2xp5_fin21':'0.26244',
'NOR4xp25_fin21':'0.4374',
'NOR3xp33_fin21':'0.34992',
'OR4x1_fin21':'0.52488',
'AOI221xp25_fin21':'0.52488',
'BUFx12f_fin21':'1.48716',
'AND3x2_fin21':'0.52488',
'SDFLx2_fin21':'2.36196',
'AND4x1_fin21':'0.52488',
'NAND3xp33_fin21':'0.34992',
'AOI31xp25_fin21':'0.4374',
'BUFx4_fin21':'0.52488',
'INVx6_fin21':'0.61236',
'OA222x2_fin21':'0.8748',
'AO221x1_fin21':'0.69984',
'AND4x4_fin21':'0.78732',
'NOR2xp25_fin21':'0.26244',
'DLLx2_fin21':'1.13724',
'AO333x2_fin21':'1.04976',
'INVx5_fin21':'0.52488',
'OAI33xp33_fin21':'0.61236',
'OAI21xp25_fin21':'0.34992',
'AO222x1_fin21':'0.78732',
'OA211x1_fin21':'0.61236',
'SDFLx4_fin21':'2.53692',
'AO32x2_fin21':'0.69984',
'DFFLQNx2_fin21':'1.48716',
'AOI21xp5_fin21':'0.34992',
'DHLx1_fin21':'1.04976',
'OAI32xp25_fin21':'0.52488',
'XNOR2x2_fin21':'0.78732',
'MAJx2_fin21':'0.69984',
'AOI331xp33_fin21':'0.69984',
'ASYNC_set_DFFHx1_fin21':'2.09952',
'MUX2x2_fin21':'0.78732',
'AO31x2_fin21':'0.61236',
'AO322x2_fin21':'0.96228',
'AND3x1_fin21':'0.4374',
'NAND4x2_fin21':'0.78732',
'OR2x2_fin21':'0.4374',
'AOI33xp33_fin21':'0.61236',
'OA33x2_fin21':'0.78732',
'AO33x1_fin21':'0.69984',
'TIEHIx1_fin21':'0.17496',
'NAND5xp2_fin21':'0.52488',
'MAJIxp5_fin21':'0.52488',
'DFFHQx4_fin21':'1.83708',
'NOR4xp75_fin21':'0.96228',
'OAI222xp25_fin21':'0.69984',
'DHLx3_fin21':'1.22472',
'DECAPx6_fin21':'1.13724',
'OAI32x1_fin21':'0.78732',
'INVx13_fin21':'1.22472',
'NAND4x1_fin21':'0.69984',
'FAx1_fin21':'1.13724',
'DECAPx1_fin21':'0.26244',
'OAI221x1_fin21':'0.78732',
'INVx11_fin21':'1.04976',
'DFFLQx4_fin21':'1.83708',
'AOI311xp33_fin21':'0.52488',
'AO22x1_fin21':'0.61236',
'XOR2xp5_fin21':'0.61236',
'OAI332xp33_fin21':'0.78732',
'ICGx3_fin21':'1.57464',
'O2A1O1Ixp5_fin21':'0.61236',
'DFFLQNx1_fin21':'1.39968',
'AO22x2_fin21':'0.69984',
'AO21x1_fin21':'0.4374',
'INVx1_fin21':'0.17496',
'BUFx3_fin21':'0.4374',
'BUFx1_fin21':'0.26244',
'AND3x6_fin21':'0.8748',
'NOR4x2_fin21':'0.78732',
'NOR2x1_fin21':'0.4374',
'AND5x2_fin21':'0.69984',
'DECAPx2_fin21':'0.4374',
'HB2xp67_fin21':'0.34992',
'NAND4xp25_fin21':'0.4374',
'DHLx2_fin21':'1.13724',
'DFFHQNx1_fin21':'1.39968',
'AND4x2_fin21':'0.61236',
'OAI221xp25_fin21':'0.52488',
'ICGx2_fin21':'1.48716',
'XOR2x1_fin21':'0.8748',
'ASYNC_reset_DFFHx1_fin21':'2.09952',
'AOI332xp33_fin21':'0.78732',
'AOI22x1_fin21':'0.69984',
'OAI311xp33_fin21':'0.52488',
'XNOR2xp5_fin21':'0.61236',
'AO31x1_fin21':'0.52488',
'MAJx3_fin21':'0.78732',
'NAND2x1_fin21':'0.4374',
'SDFHx4_fin21':'2.53692',
'AO211x2_fin21':'0.69984',
'TAPCELL_fin21':'0.08748',
'NOR4x1_fin21':'0.69984',
'AOI211xp25_fin21':'0.4374',
'AOI33x1_fin21':'0.8748',
'HB3xp67_fin21':'0.4374',
'AO331x1_fin21':'0.78732',
'NOR3x2_fin21':'0.69984',
'AND2x6_fin21':'0.78732',
'DLLx3_fin21':'1.22472',
'NAND2x1p5_fin21':'0.61236',
'AND3x4_fin21':'0.69984',
'XNOR2x1_fin21':'0.69984',
'OAI31xp5_fin21':'0.69984',
'OA31x2_fin21':'0.61236',
'AOI333xp33_fin21':'0.8748',
'OAI22x1_fin21':'0.69984',
'SDFHx3_fin21':'2.44944',
'OR2x4_fin21':'0.61236',
'OA332x2_fin21':'0.96228',
'OR5x1_fin21':'0.61236',
'ICGx1_fin21':'1.39968',
'BUFx4f_fin21':'0.61236',
'AO221x2_fin21':'0.78732',
'OR3x2_fin21':'0.52488',
'OA331x2_fin21':'0.8748',
'NAND3x1_fin21':'0.61236',
'HAxp5_fin21':'0.61236',
'OAI211xp25_fin21':'0.4374',
'AOI22xp25_fin21':'0.4374',
'HAx1_fin21':'0.96228',
'AO331x2_fin21':'0.8748',
'NOR2x2_fin21':'0.61236',
'DFFLQNx3_fin21':'1.57464',
'AO222x2_fin21':'0.8748',
'FILLER_fin21':'0.08748',
'A2O1A1O1Ixp25_fin21':'0.61236',
'BUFx12_fin21':'1.3122',
'SDFHx1_fin21':'2.27448',
'OA221x1_fin21':'0.69984',
'OAI211x1_fin21':'0.69984',
'SDFHx2_fin21':'2.36196',
'NOR5xp2_fin21':'0.52488',
'OAI32xp33_fin21':'0.52488',
'OA211x2_fin21':'0.69984',
'AOI322xp25_fin21':'0.69984',
'TIELOx1_fin21':'0.17496',
'AOI222xp25_fin21':'0.69984',
'AND4x6_fin21':'0.96228',
'NOR2xp33_fin21':'0.26244',
'AO33x2_fin21':'0.78732',
'AND2x1_fin21':'0.34992',
'BUFx2_fin21':'0.34992',
'AO21x2_fin21':'0.52488',
'OA222x1_fin21':'0.78732',
'DECAPx10_fin21':'1.83708',
'AND2x4_fin21':'0.61236',
'OA332x1_fin21':'0.8748',
'DLLx1_fin21':'1.04976',
'OAI21x1_fin21':'0.61236',
'OR5x4_fin21':'0.8748',
'INVx4_fin21':'0.4374',
'OAI31xp25_fin21':'0.4374',
'DFFHQNx3_fin21':'1.57464',
'AND5x1_fin21':'0.61236',
'AOI221x1_fin21':'0.78732',
'OR2x1_fin21':'0.34992',
'OR4x2_fin21':'0.61236',
'OA331x1_fin21':'0.78732',
'BUFx16f_fin21':'1.83708',
'OR3x1_fin21':'0.4374',
'AOI21x1_fin21':'0.61236',
'NAND3x2_fin21':'0.69984'
}


 pattern_cell = '  cell \('
 pattern_cellName = '\(\S+\)'
 pattern_area = '    area : '
 wf = open(outputLib_Name, 'w' , newline = "\n")
 cellName = ''
 area = ''
 with open(inputLib_Name, 'r') as rf:
			lines = rf.readlines()

			for line in lines:
				#print(line)
				match1 = re.search(pattern_cell, line)
				match2 = re.search(pattern_area, line)

				if match1 == None and match2 == None:
					wf.write("{}".format(line) )
				elif match1 != None:
					wf.write("{}".format(line) )
					cellName = line
					#print(cellName)
					match3 = re.search(pattern_cellName, cellName)
					if match3 != None:
						cellName = match3.group()
						#print(cellName)
						cellName = cellName.replace('(','').replace(')','')
						print(cellName)

				elif match2 != None:
					area = Single_FinalMap[cellName]		# Get Area Value from oursMap
					#area = nangateMap[cellName]		# Get Area Value from nangateMap

					wf.write("    area : {};\n".format(area) )
					cellName = ''
					area = ''
 rf.close()
 wf.close()


addAreaToLib()
