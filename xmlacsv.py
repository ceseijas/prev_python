from lxml import etree
import xlsxwriter

def main():
	#crea el archivo de resultados en formato xlsx, depende de la libreria xlsxwriter
	workbook = xlsxwriter.Workbook('Cuentas_contable_base.xlsx')
	#agrega una nueva hoja
	worksheet = workbook.add_worksheet()
	#lee y asigna a una variable el contenido del archivo xml, depende de la libreria lxml
	doc = etree.parse('../l10n_pe_chart_fmr2.xml')
	#obtiene la estructura del archivo, se tuvo que eliminar el campo DATA del archivo xml original
	raiz=doc.getroot()
	#asigna la cantidad de "registros" a leer que tiene el archivo xml	
	len_xml = len(raiz)
	#Se genera la cabecera del archivo excel, no refleja la cantidad total de columnas
	worksheet.write(0,0,"Registro")
	worksheet.write(0,1,"Cuenta Contable")
	worksheet.write(0,2,"Descripción Cuenta Contable")
	worksheet.write(0,3,"Eval")
	

	for i in range(len_xml): #i es el total de registros desde el valor 0
		j=3; m=5 #los atributos en el archivo xml por cada paquete de registro(record) son de 2x2 tiene que incrementar el valor dentro del for
		#libro obtiene todo el contenido del paquete de registro (record)
		libro=raiz[i]
		#agrega en la fila 1 columna 0, el contador de registro
		worksheet.write(i+1,0,i+1)
		worksheet.write(i+1,1, libro[1].text)  #codigo cuenta contable
		worksheet.write(i+1,2, libro[0].text)  #descripcion cuenta contable
		col_x_attr =""
		col_x_value=""
		#un paquete de registro puede contener atributos con nombre y valor, el for recorre cada atributo (2) 
		for attr,value in libro[2].items():
			col_x_attr=attr
			col_x_value=value
			worksheet.write(i+1,3, col_x_value)  #eval false
		#un paquete de registro puede contener atributos con nombre y valor el for recorre cada atributo (2)
		for attr,value in libro[3].items():
			col_x_attr=attr
			col_x_value=value
			worksheet.write(i+1,j+1, col_x_value) #account.data_account_type_current_assets
			j=j+1 #incrementa una columna a la derecha
		for attr,value in libro[4].items():
			col_x_attr=attr
			col_x_value=value
			worksheet.write(i+1,m+1, col_x_value) #chart_template_id
			m=m+1 #incrementa una columna a la derecha
		print(i)
	workbook.close()

if __name__=="__main__":
	main()
 