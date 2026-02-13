libName = "All_finFlex21_NOTAP" 
isFirst = "True"
TRACK = "fin21"
foreach(cellId ddGetObj(libName)->cells
	cv = dbOpenCellViewByType(libName cellId~>name  "layout")
	lppList = cv~>layerPurposePairs 
	foreach(lpp lppList
		lppName = lpp~>layerName 			
		if(lppName== "BOUNDARY" then                   
			lppShapes = lpp~>shapes~>bBox  
			ld_x = car(car(car(lppShapes)))
			ru_x = car(car(cdr(car(lppShapes))))
			if(TRACK=="fin21" then
				area = (ru_x - ld_x)*0.27*6
			)
			if(TRACK=="fin22" then
				area = (ru_x - ld_x)*0.27*7
			)
			if(TRACK=="fin32" then
				area = (ru_x - ld_x)*0.27*8
			)
			if(TRACK=="6T" then
				area = (ru_x - ld_x)*0.27*8
			)
			if(TRACK=="75T" then
				area = (ru_x - ld_x)*0.27*10
			)
			if(TRACK=="9T" then
				area = (ru_x - ld_x)*0.27*12
			)
			if(isFirst=="False" then
				printf(",\n")
			)
			if(isFirst=="True" then
				isFirst = "False"
			)
			printf("\'%s\':\'%L\'" cellId~>name, area)
		)	
	)
)