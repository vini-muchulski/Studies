def file_size(file_info):
	name,tipo,tamanho= file_info
	return("{:.2f}".format(tamanho / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21



