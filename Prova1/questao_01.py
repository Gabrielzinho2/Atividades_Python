altura = float(input("\nDigite a altura da placa do piso(cm):" ))

base = float(input("\nDigite a base da placa do piso(cm):" ))

area_cobrir = float(input("\nDigite a área a cobrir (m²):" ))

altura_metros = altura / 100

base_metros = base / 100

area_piso = (base_metros * altura_metros) / 2

print(f"\nA área do piso é {area_piso:,.2f}m²")

qtd_pisos = area_cobrir / area_piso

print(f"\nPara cobrir a área de {area_cobrir:,.2f}m², serão necessários {qtd_pisos:,.2f} pisos")
