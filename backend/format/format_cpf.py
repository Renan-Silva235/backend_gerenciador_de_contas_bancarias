
def format_cpf_entry(entry):
    get_cpf = entry.get()
    cpf = ''.join(filter(str.isdigit, get_cpf))  # Remove caracteres não numéricos
    formatted_cpf = ''

    if len(cpf) > 0:
        formatted_cpf += cpf[:3]
    if len(cpf) >= 4:
        formatted_cpf += '.' + cpf[3:6]  
    if len(cpf) >= 7:
        formatted_cpf += '.' +cpf[6:9]
    if len(cpf) >= 10:
        formatted_cpf += '-' + cpf[9:11]

    
    if get_cpf != formatted_cpf:
        entry.delete(0, 'end')
        entry.insert(0, formatted_cpf)


