import csv
import sys


def test_bit_num(num_state):
    bit_num = 1
    while 2 ** bit_num < num_state:
        bit_num += 1
    return bit_num


if len(sys.argv) != 3:
    print('Usage: python3 state_machine_gen.py config_file.csv output.sv')
    exit(1)

# File ops
csv_file = open(sys.argv[1], 'r')
sheet = csv.reader(csv_file)
output_file = open(sys.argv[2], 'w')

next_logic = 'next_logic'
next_state = 'next_state'

# read info from file
state_dict = dict()  # record state info
skip = 1  # skip the header row

for each_row in sheet:
    # skip the header row
    if skip:
        skip = 0
        continue
    if each_row[0] not in state_dict and each_row[0] != '':
        state_dict.update({each_row[0]: []})
        prev_state = each_row[0]
    if each_row[0] == '':
        state_dict[prev_state].append({'next_logic': each_row[1], 'next_state': each_row[2]})
    else:
        state_dict[each_row[0]].append({'next_logic': each_row[1], 'next_state': each_row[2]})

# write sv headers
output_file.write('module !TODO! (\n\tinput logic clk;\n\tinput logic n_rst;\n\n')
output_file.write('\t!TODO!\n\n')
output_file.write(');\n')

# define state enum
output_file.write(f'\ttypedef enum logic [{test_bit_num(len(state_dict)) - 1}:0] {{')
counter = 0
for each_state in state_dict:
    output_file.write(each_state)
    if counter < len(state_dict) - 1:
        output_file.write(', ')
    counter += 1

# always_ff
output_file.write('} state_t;\n\n')
output_file.write('\tstate_t state;\n\tstate_t next_state;\n\n')
output_file.write('\talways_ff @( posedge clk, negedge n_rst ) begin\n')
output_file.write('\t\tif (n_rst == \'0) begin\n')
output_file.write(f'\t\t\tstate <= {next(iter(state_dict))};\n')
output_file.write('\t\tend else begin\n')
output_file.write('\t\t\tstate <= next_state;\n')
output_file.write('\t\tend\n\tend\n\n')

# next state logic
output_file.write('\t// next state logic\n\talways_comb begin\n')
output_file.write('\t\tnext_state = state;\n')
output_file.write('\t\tcase (state)\n')
for each_state in state_dict:
    output_file.write(f'\t\t\t{each_state}: begin\n')
    if len(state_dict[each_state]) == 1 and state_dict[each_state][0][next_logic] != '':
        output_file.write(f'\t\t\t\tif ({state_dict[each_state][0][next_logic]}) begin\n')
        output_file.write(f'\t\t\t\t\tnext_state = {state_dict[each_state][0][next_state]};\n')
        output_file.write(f'\t\t\t\tend\n\t\t\tend\n')
    elif len(state_dict[each_state]) == 1:  # direct transition
        output_file.write(f'\t\t\t\tnext_state = {each_transition[next_state]};\n\t\t\tend\n')
    else:
        counter = 0
        for each_transition in state_dict[each_state]:
            if counter == 0 and each_transition[next_logic] != '':
                output_file.write(f'\t\t\t\tif ({each_transition[next_logic]}) begin\n')
            elif each_transition[next_logic] != '':
                output_file.write(f'\t\t\t\tend else if ({each_transition[next_logic]}) begin\n')
            else:
                output_file.write(f'\t\t\t\tend else begin\n')
            output_file.write(f'\t\t\t\t\tnext_state = {each_transition[next_state]};\n')
            counter += 1
        output_file.write('\t\t\t\tend\n')
output_file.write('\t\tendcase\n')
output_file.write('\tend\n\n')

# output logic
output_file.write('\t// output logic\n')
output_file.write('\talways_comb begin\n')
output_file.write('\t!TODO!\n')
output_file.write('\tend\n\n')

output_file.write('endmodule\n')


# File ops
csv_file.close()
output_file.close()
