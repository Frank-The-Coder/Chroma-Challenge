import re

def file_to_c_array(input_file):
  c_array = []
  num_entries = 0
  with open(input_file, 'r') as file:
    for line in file:
      hex_numbers = re.findall(r'[0-9a-fA-F]{4}', line)
      c_array.extend([f'0x{num}' for num in hex_numbers])
      num_entries += len(hex_numbers)
  return '{' + ', '.join(c_array) + '}', num_entries

def write_c_array_to_file(c_array, output_file):
  with open(output_file, 'w') as file:
    file.write(c_array)

name = "partyhorn"
input_file = f'{name}.txt'  # Replace with the path to your input file
output_file = f'{name}_array.txt'  # Replace with the desired output file path
output_array, num_entries = file_to_c_array(input_file)
write_c_array_to_file(output_array, output_file)

print(f"C array with {num_entries} entries written to {output_file}")
